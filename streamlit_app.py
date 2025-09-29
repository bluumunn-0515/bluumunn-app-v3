



import streamlit as st
import pandas as pd
import altair as alt
from datetime import date
import os

# 한글 폰트 경로 설정
FONT_PATH = os.path.join(os.path.dirname(__file__), "fonts", "NanumGothic-Regular.ttf")
FONT_URL = "./fonts/NanumGothic-Regular.ttf"

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

st.set_page_config(page_title="자동차과 자격증 취득 현황 집계", page_icon="🚗", layout="wide")
st.title("🚗 특성화고 자동차과 자격증 취득 현황 집계 프로그램")
st.write("학생들의 자격증 취득 현황을 입력하고, 집계 및 시각화할 수 있습니다.")

# 지역/학교 목록 예시 (실제 환경에 맞게 수정 가능)
region_list = ["서울", "경기", "부산"]
school_dict = {
    "서울": ["A고", "B고"],
    "경기": ["C고", "D고"],
    "부산": ["E고"]
}

# 데이터 초기화
if "cert_df" not in st.session_state:
    st.session_state.cert_df = pd.DataFrame(columns=[
        "이름", "학년", "반", "자격증명", "취득일", "지역", "학교"
    ])

# 입력 폼
with st.form("cert_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("학생 이름")
        grade = st.selectbox("학년", [1, 2, 3])
        class_num = st.selectbox("반", [1, 2, 3, 4])
        region = st.selectbox("지역", region_list)
        school = st.selectbox("학교", school_dict[region])
    with col2:
        cert_name = st.selectbox("자격증명", [
            "자동차정비기능사", "운전면허(1종)", "운전면허(2종)", "전산응용기계제도기능사", "지게차운전기능사", "굴삭기운전기능사", "기타"
        ])
        cert_date = st.date_input("취득일", value=date.today())
    submitted = st.form_submit_button("입력")
    if submitted:
        new_row = {
            "이름": name,
            "학년": grade,
            "반": class_num,
            "자격증명": cert_name,
            "취득일": cert_date,
            "지역": region,
            "학교": school
        }
        st.session_state.cert_df = pd.concat([
            pd.DataFrame([new_row]), st.session_state.cert_df
        ], ignore_index=True)
        st.success(f"{name} 학생의 자격증 취득 정보가 등록되었습니다.")

# 데이터 테이블 표시
st.header("입력된 자격증 취득 현황")
st.dataframe(st.session_state.cert_df, use_container_width=True)

# 집계 및 시각화
st.header("자격증별 취득자 수 집계")
if not st.session_state.cert_df.empty:
    cert_count = st.session_state.cert_df["자격증명"].value_counts().reset_index()
    cert_count.columns = ["자격증명", "취득자 수"]

    chart = alt.Chart(cert_count).mark_bar().encode(
        x=alt.X("자격증명", sort="-y"),
        y="취득자 수",
        color="자격증명"
    ).configure_axis(
        labelFont="NanumGothic",
        titleFont="NanumGothic"
    ).configure_legend(
        labelFont="NanumGothic",
        titleFont="NanumGothic"
    ).configure_title(
        font="NanumGothic"
    )
    st.altair_chart(chart, use_container_width=True)

    st.header("학년별 취득자 수 집계")
    grade_count = st.session_state.cert_df.groupby("학년").size().reset_index(name="취득자 수")

    chart2 = alt.Chart(grade_count).mark_bar().encode(
        x="학년:O",
        y="취득자 수:Q",
        color="학년:O"
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

    st.header("반별 취득자 수 집계")
    class_count = st.session_state.cert_df.groupby(["학년", "반"]).size().reset_index(name="취득자 수")

    chart3 = alt.Chart(class_count).mark_bar().encode(
        x=alt.X("반:O"),
        y="취득자 수:Q",
        color="학년:O",
        column="학년:O"
    ).configure_axis(
        labelFont="NanumGothic",
        titleFont="NanumGothic"
    ).configure_legend(
        labelFont="NanumGothic",
        titleFont="NanumGothic"
    ).configure_title(
        font="NanumGothic"
    )
    st.altair_chart(chart3, use_container_width=True)

    st.header("데이터 다운로드")
    csv = st.session_state.cert_df.to_csv(index=False).encode('utf-8-sig')
    st.download_button(
        label="CSV로 다운로드",
        data=csv,
        file_name="자동차과_자격증_취득현황.csv",
        mime="text/csv"
    )
else:
    st.info("아직 입력된 데이터가 없습니다.")
