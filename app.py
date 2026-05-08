import streamlit as st
import pandas as pd

# 웹 페이지 제목
st.title("🚀 데이터 가공 툴 작동 테스트")

# 화면에 텍스트 출력
st.write("Streamlit이 정상적으로 배포되었습니다!")

# 성공 메시지 박스
st.success("접속에 성공했습니다. 이제 엑셀 업로드 기능을 추가할 준비가 되었네요!")

# 사이드바에 간단한 정보 출력
st.sidebar.header("설정")
st.sidebar.write("제작자: hongy")

# 정상 동작 확인용 데이터프레임 샘플
st.subheader("샘플 데이터 표")
sample_data = pd.DataFrame({
    '항목': ['A', 'B', 'C'],
    '수치': [10, 20, 30]
})
st.table(sample_data)