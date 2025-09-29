

import streamlit as st
import pandas as pd
import altair as alt
import os

# 한글 폰트 경로 설정
FONT_URL = "../fonts/NanumGothic-Regular.ttf"

# Streamlit에 한글 폰트 적용 (CSS)
st.markdown(f"""
    <style>
    @font-face {{
        font-family: 'NanumGothic';
        src: url('{FONT_URL}') format('truetype');
        font-weight: normal;
        font-style: normal;
    }}
    html, body, [class^='css'] {{
        font-family: 'NanumGothic', sans-serif !important;
    }}
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="지역/학교별 자격증 취득 현황", page_icon="🏫", layout="wide")
st.title("🏫 지역별·학교별 자격증 취득 현황 집계")
st.write("지역과 학교별로 학생들의 자격증 취득 현황을 집계하고 시각화합니다.")

# streamlit_app.py에서 입력된 데이터 연동
if "cert_df" in st.session_state and not st.session_state.cert_df.empty:
    df = st.session_state.cert_df.copy()
else:
    st.info("입력된 자격증 데이터가 없습니다. 메인 페이지에서 데이터를 먼저 입력하세요.")
    st.stop()

# 지역 선택
regions = df["지역"].unique().tolist()
selected_region = st.selectbox("지역 선택", ["전체"] + regions)
if selected_region != "전체":
    df = df[df["지역"] == selected_region]

# 학교 선택
schools = df["학교"].unique().tolist()
selected_school = st.selectbox("학교 선택", ["전체"] + schools)
if selected_school != "전체":
    df = df[df["학교"] == selected_school]

# 자격증별 취득자 수 (학교별)
st.header("자격증별 취득자 수 (학교별)")
school_cert_count = df.groupby(["학교", "자격증명"]).size().reset_index(name="취득자 수")

chart1 = alt.Chart(school_cert_count).mark_bar().encode(
    x=alt.X("자격증명", sort="-y"),
    y="취득자 수",
    color="자격증명",
    column="학교"
).configure_axis(
    labelFont="NanumGothic",
    titleFont="NanumGothic"
).configure_legend(
    labelFont="NanumGothic",
    titleFont="NanumGothic"
).configure_title(
    font="NanumGothic"
)
st.altair_chart(chart1, use_container_width=True)

# 지역별 자격증 취득자 수 집계
st.header("지역별 자격증 취득자 수 집계")
region_cert_count = df.groupby(["지역", "자격증명"]).size().reset_index(name="취득자 수")

chart2 = alt.Chart(region_cert_count).mark_bar().encode(
    x=alt.X("자격증명", sort="-y"),
    y="취득자 수",
    color="지역",
    column="지역"
).configure_axis(
    labelFont="NanumGothic",
    titleFont="NanumGothic"
).configure_legend(
    labelFont="NanumGothic",
    titleFont="NanumGothic"
).configure_title(
    font="NanumGothic"
)
st.altair_chart(chart2, use_container_width=True)

st.header("데이터 테이블")
st.dataframe(df, use_container_width=True)
