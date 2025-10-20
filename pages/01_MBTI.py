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
