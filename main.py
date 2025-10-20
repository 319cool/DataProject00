# streamlit_app.py
import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천기 🎯", layout="centered")

st.title("🎓 MBTI로 보는 나의 진로!")
st.write("안녕하세요! 😄 당신의 MBTI를 선택하면 어울리는 **진로와 학과, 성격 설명**을 알려드릴게요!")

# MBTI 목록
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 선택 박스
selected_mbti = st.selectbox("👇 당신의 MBTI를 선택해보세요!", mbti_types)

# MBTI별 진로, 학과, 성격 데이터
careers = {
    "ISTJ": [
        {
            "name": "회계사 💼",
            "major": "경영학, 회계학",
            "fit": "꼼꼼하고 책임감이 강한 사람에게 딱이에요! 숫자나 규칙을 잘 다루는 성격이면 최고 👍"
        },
        {
            "name": "관리직 🗂️",
            "major": "행정학, 산업공학",
            "fit": "체계적이고 계획 세우는 걸 좋아하는 사람에게 잘 어울려요 🧠"
        }
    ],
    "INFP": [
        {
            "name": "작가 ✍️",
            "major": "문예창작학, 국어국문학",
            "fit": "감수성이 풍부하고 자신만의 세계를 표현하는 걸 좋아하는 사람에게 좋아요 💫"
        },
        {
            "name": "사회복지사 🤝",
            "major": "사회복지학, 심리학",
            "fit": "다른 사람의 감정을 잘 공감하고 돕는 걸 좋아하는 성격에게 찰떡이에요 💗"
        }
    ],
    "ENTJ": [
        {
            "name": "CEO 💼",
            "major": "경영학, 경제학",
            "fit": "리더십 있고 목표를 향해 밀고 나가는 추진력 있는 사람에게 완전 잘 맞아요 🔥"
        },
        {
            "name": "전략 컨설턴트 🧠",
            "major": "산업공학, 경영정보학",
            "fit": "분석적이고 효율적인 해결책을 찾는 걸 좋아하는 사람에게 어울려요 🚀"
        }
    ],
    "ISFP": [
        {
            "name": "디자이너 🎨",
            "major": "시각디자인, 패션디자인",
            "fit": "감각이 뛰어나고 미적인 걸 좋아하는 사람에게 딱 맞아요 ✨"
        },
        {
            "name": "요리사 🍳",
            "major": "조리학, 호텔외식경영",
            "fit": "감성적이고 손재주 좋은 사람에게 어울려요 😋"
        }
    ],
    "ENFP": [
        {
            "name": "마케팅 전문가 📣",
            "major": "광고홍보학, 경영학",
            "fit": "사람들과 소통 잘하고 창의력 넘치는 사람이라면 최고예요 💥"
        },
        {
            "name": "창업가 🚀",
            "major": "경영학, IT 관련 전공",
            "fit": "새로운 아이디어를 실현하고 싶어하는 열정적인 사람에게 어울려요 💡"
        }
    ]
}

# 결과 출력
if selected_mbti:
    st.subheader(f"🌟 {selected_mbti} 유형에게 어울리는 진로는?")
    if selected_mbti in careers:
        for c in careers[selected_mbti]:
            st.markdown(f"""
            ### {c['name']}
            **📚 관련 학과:** {c['major']}  
            **💬 이런 사람에게 어울려요:** {c['fit']}
            """)
    else:
        st.info("아직 이 MBTI에 대한 데이터가 준비 중이에요 😅 곧 업데이트될 예정이에요!")
