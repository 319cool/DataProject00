import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="국가별 MBTI 분포 시각화", page_icon="🌍", layout="wide")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# 제목
st.title("🌍 국가별 MBTI 분포 시각화")
st.markdown("각 나라의 MBTI 유형 비율을 인터랙티브하게 확인해보세요!")

# 국가 선택
country_list = sorted(df["Country"].unique())
selected_country = st.selectbox("국가를 선택하세요", country_list)

# 선택한 국가의 데이터 필터링
country_data = df[df["Country"] == selected_country].iloc[0, 1:]
country_df = pd.DataFrame({
    "MBTI": country_data.index,
    "비율": country_data.values
}).sort_values(by="비율", ascending=False)

# 색상 설정 (1등 빨간색, 나머지는 그라데이션)
colors = ["red"] + [f"rgba(255, 150, 150, {0.9 - i * 0.04})" for i in range(1, len(country_df))]

# Plotly 그래프 생성
fig = px.bar(
    country_df,
    x="MBTI",
    y="비율",
    text=country_df["비율"].apply(lambda x: f"{x*100:.1f}%"),
    color_discrete_sequence=colors
)

# 그래프 디자인
fig.update_traces(textposition="outside")
fig.update_layout(
    title=f"🇨🇮 {selected_country}의 MBTI 유형 분포",
    xaxis_title="MBTI 유형",
    yaxis_title="비율 (0~1)",
    template="simple_white",
    showlegend=False,
    title_font_size=22,
    xaxis_tickangle=-45,
)

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)

# 데이터 보기 옵션
with st.expander("🔍 원본 데이터 보기"):
    st.dataframe(country_df.reset_index(drop=True))


st.set_page_config(page_title="국가별 MBTI 비교 시각화", page_icon="🌎", layout="wide")

# 데이터 불러오기 (캐싱으로 속도 향상)
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

# 제목
st.title("🌎 여러 나라의 MBTI 유형 비교 시각화")
st.markdown("국가를 여러 개 선택해 MBTI 비율을 비교해보세요!")

# 국가 다중 선택
country_list = sorted(df["Country"].unique())
selected_countries = st.multiselect(
    "비교할 국가를 선택하세요 (최대 5개 권장)",
    country_list,
    default=["South Korea"] if "South Korea" in country_list else [country_list[0]]
)

if not selected_countries:
    st.warning("⬆️ 국가를 하나 이상 선택해주세요!")
    st.stop()

# 선택한 국가의 데이터 필터링
filtered_df = df[df["Country"].isin(selected_countries)]

# 긴 형식으로 변환 (Plotly용)
melted_df = filtered_df.melt(id_vars="Country", var_name="MBTI", value_name="비율")

# 평균값 계산 (국가별 MBTI 평균 비교 시 참고)
avg_df = melted_df.groupby("MBTI")["비율"].mean().reset_index().sort_values("비율", ascending=False)

# 그래프 색상 팔레트
colors = px.colors.qualitative.Bold

# Plotly 그래프
fig = px.bar(
    melted_df,
    x="MBTI",
    y="비율",
    color="Country",
    barmode="group",
    text=melted_df["비율"].apply(lambda x: f"{x*100:.1f}%"),
    color_discrete_sequence=colors,
)

# 그래프 꾸미기
fig.update_traces(textposition="outside", marker_line_width=0.5)
fig.update_layout(
    title="🌐 국가별 MBTI 유형 비율 비교",
    xaxis_title="MBTI 유형",
    yaxis_title="비율 (0~1)",
    template="simple_white",
    title_font_size=22,
    xaxis_tickangle=-45,
    legend_title="국가",
    bargap=0.15,
)

# 표시
st.plotly_chart(fig, use_container_width=True)

# 평균 순위 테이블 (참고용)
with st.expander("📊 전 세계 평균 MBTI 순위 보기"):
    st.dataframe(avg_df.reset_index(drop=True))
