
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="Streamlit 요소 데모", page_icon="✨", layout="wide")
st.title("Streamlit에서 활용할 수 있는 다양한 요소 데모")
st.write("Streamlit의 다양한 위젯, 레이아웃, 미디어, 차트, 입력 요소를 한 페이지에서 모두 체험해보세요.")

# 1. 텍스트 요소
st.header("1. 텍스트 요소")
st.subheader("서브헤더 예시")
st.markdown("**마크다운** _스타일링_ :sparkles:")
st.code("print('Hello Streamlit!')", language="python")
st.latex(r"E = mc^2")

# 2. 입력 위젯
st.header("2. 입력 위젯")
name = st.text_input("이름을 입력하세요")
age = st.number_input("나이", min_value=0, max_value=120, value=25)
agree = st.checkbox("개인정보 수집에 동의합니다")
color = st.radio("좋아하는 색상은?", ["빨강", "파랑", "초록"])
option = st.selectbox("선호하는 동물", ["강아지", "고양이", "토끼"])
multi = st.multiselect("좋아하는 과일", ["사과", "바나나", "포도", "오렌지"])
date = st.date_input("날짜 선택")
time = st.time_input("시간 선택")
file = st.file_uploader("파일 업로드")
slider = st.slider("점수", 0, 100, 50)
st.button("버튼")

# 3. 폼(Form)
st.header("3. 폼(Form)")
with st.form("my_form"):
    st.write("폼 내부의 입력 요소")
    form_text = st.text_input("폼 텍스트 입력")
    form_submit = st.form_submit_button("폼 제출")
    if form_submit:
        st.success(f"폼 제출됨: {form_text}")

# 4. 레이아웃
st.header("4. 레이아웃")
col1, col2 = st.columns(2)
with col1:
    st.write("왼쪽 컬럼")
    st.metric("온도", "23°C", "+2")
with col2:
    st.write("오른쪽 컬럼")
    st.metric("습도", "60%", "-5%")

tab1, tab2, tab3 = st.tabs(["탭1: 차트", "탭2: 이미지", "탭3: 지도"])
with tab1:
    st.write("여러 차트 예시")
    df = pd.DataFrame(np.random.randn(100, 3), columns=["a", "b", "c"])
    st.line_chart(df)
    st.bar_chart(df)
    st.area_chart(df)
    chart = alt.Chart(df).mark_circle().encode(x="a", y="b", size="c", color="c")
    st.altair_chart(chart, use_container_width=True)
with tab2:
    st.write("이미지 표시")
    st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb", caption="샘플 이미지", use_column_width=True)
    st.video("https://www.youtube.com/watch?v=5qap5aO4i9A")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
with tab3:
    st.write("지도 표시")
    map_data = pd.DataFrame({
        'lat': np.random.uniform(37.5, 37.6, 100),
        'lon': np.random.uniform(126.9, 127.0, 100)
    })
    st.map(map_data)

# 5. 데이터 표시
st.header("5. 데이터 표시")
st.write("데이터프레임")
st.dataframe(df)
st.write("테이블")
st.table(df.head())

# 6. 상태 및 알림
st.header("6. 상태 및 알림")
st.success("성공 메시지")
st.info("정보 메시지")
st.warning("경고 메시지")
st.error("에러 메시지")
st.exception(Exception("예외 메시지 예시"))

# 7. 진행률 및 스피너
st.header("7. 진행률 및 스피너")
import time
progress = st.progress(0)
for i in range(1, 101):
    time.sleep(0.01)
    progress.progress(i)
with st.spinner("로딩 중..."):
    time.sleep(1)
st.success("로딩 완료!")

# 8. 사이드바
st.sidebar.title("사이드바")
st.sidebar.write("여기서도 다양한 요소를 넣을 수 있습니다.")
sidebar_option = st.sidebar.selectbox("사이드바 옵션", ["A", "B", "C"])
st.sidebar.button("사이드바 버튼")

# 9. 기타 요소
st.header("8. 기타 요소")
st.caption("캡션 예시")
st.divider()
st.write("마지막으로 Streamlit의 다양한 요소를 모두 활용해보세요!")
