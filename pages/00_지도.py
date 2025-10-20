# FILE: app.py
# Streamlit app that shows Top 10 popular Korean tourist spots (for foreign visitors) with Folium
# To deploy on Streamlit Cloud: push this file and requirements.txt to a GitHub repo and connect the repo in Streamlit Cloud.

import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster

st.set_page_config(page_title="Korea Top 10 (Folium)", layout="wide")

st.title("🇰🇷 한국 인기 관광지 Top 10 — 지도 표시 (Folium)")
st.markdown("간단한 인터랙티브 지도: 마커를 클릭하면 설명이 나옵니다.")

# Top 10 장소 (이름, 위도, 경도, 간단설명)
PLACES = [
    {"name": "Gyeongbokgung Palace (경복궁)", "lat": 37.579617, "lon": 126.977041, "info": "Joseon 왕조의 대표 궁궐. 교대식 관람 추천."},
    {"name": "Changdeokgung Palace & Secret Garden (창덕궁)", "lat": 37.5743306, "lon": 126.9883306, "info": "유네스코 세계유산에 등재된 궁궐과 비밀의 정원."},
    {"name": "Bukchon Hanok Village (북촌한옥마을)", "lat": 37.582178, "lon": 126.983256, "info": "전통 한옥이 모여있는 서울의 고즈넉한 골목."},
    {"name": "N Seoul Tower (남산타워)", "lat": 37.55117, "lon": 126.988228, "info": "서울을 한눈에 볼 수 있는 전망대. 야경 추천."},
    {"name": "Myeongdong (명동)", "lat": 37.56000, "lon": 126.98600, "info": "쇼핑과 길거리음식의 중심지."},
    {"name": "Insadong (인사동)", "lat": 37.572962, "lon": 126.987332, "info": "전통 공예품과 찻집이 많은 문화거리."},
    {"name": "Hongdae (홍대)", "lat": 37.550355, "lon": 126.925443, "info": "젊음의 거리, 클럽·카페·스트리트 퍼포먼스."},
    {"name": "Jeju Island (제주도, 중심부)", "lat": 33.38, "lon": 126.53, "info": "자연, 폭포, 한라산 등 한국의 대표 섬 관광지."},
    {"name": "Haeundae Beach, Busan (해운대)", "lat": 35.15926, "lon": 129.16035, "info": "부산의 대표 해변. 여름 성수기 인기."},
    {"name": "Imjingak / DMZ (임진각, DMZ 투어 출발지)", "lat": 37.886258, "lon": 126.741581, "info": "비무장지대(DMZ) 관람을 위한 주요 관람지 중 하나."},
]

# Create Folium map centered roughly on Korea
m = folium.Map(location=[36.0, 127.5], zoom_start=7, control_scale=True)

# Use a clustered marker layer for nicer display
marker_cluster = MarkerCluster().add_to(m)

for p in PLACES:
    html = f"<b>{p['name']}</b><br>{p['info']}<br><small>위도: {p['lat']}, 경도: {p['lon']}</small>"
    folium.Marker(
        location=[p['lat'], p['lon']],
        popup=folium.Popup(html, max_width=300),
        tooltip=p['name']
    ).add_to(marker_cluster)

# Add a fullscreen button
folium.plugins.Fullscreen().add_to(m)

# Streamlit layout: map on the left, place list on the right
col1, col2 = st.columns((3,1))
with col1:
    st_folium(m, width="100%", height=700)

with col2:
    st.subheader("장소 목록")
    for p in PLACES:
        if st.button(p['name']):
            # recenters the map by creating a tiny map focused on the place and showing it
            focused = folium.Map(location=[p['lat'], p['lon']], zoom_start=15, control_scale=True)
            folium.Marker([p['lat'], p['lon']], popup=p['name'], tooltip=p['name']).add_to(focused)
            st_folium(focused, width=350, height=350)
            st.write(p['info'])

st.caption("데이터 출처: VisitKorea, TripAdvisor, 여행 가이드 목록 등을 종합했습니다.")

# EOF


# FILE: requirements.txt
# (When deploying to Streamlit Cloud include this file in the repo root)
# content below (not part of the Python module):

# --- requirements.txt START ---
# streamlit app requirements
# streamlit>=1.20
# folium>=0.14
# streamlit-folium>=0.11
# branca>=0.6
# --- requirements.txt END ---
