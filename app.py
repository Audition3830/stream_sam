import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="데이터 정리 툴", layout="wide")

st.title("📊 지인용 데이터 가공 서비스")
st.info("엑셀 파일을 업로드하면 데이터를 정리해 드립니다.")

# 1. 파일 업로드 섹션
uploaded_file = st.file_uploader("엑셀 파일을 선택하세요 (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    try:
        # 엑셀 읽기
        df = pd.read_excel(uploaded_file)
        
        st.subheader("✅ 원본 데이터 미리보기")
        st.dataframe(df.head()) # 상위 5줄만 출력

        # ---------------------------------------------------------
        # 2. 데이터 가공 로직 (여기에 원하는 로직을 넣으시면 됩니다)
        # 예시: 단순히 모든 숫자의 합계를 구하거나 컬럼명을 정리하는 등
        processed_df = df.copy() 
        # ---------------------------------------------------------

        st.subheader("🔄 가공된 결과")
        st.write(f"총 {len(processed_df)}행의 데이터가 정리되었습니다.")
        st.dataframe(processed_df)

        # 3. 엑셀 다운로드 버튼
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            processed_df.to_excel(writer, index=False, sheet_name='Sheet1')
        
        processed_data = output.getvalue()

        st.download_button(
            label="📥 가공된 엑셀 다운로드",
            data=processed_data,
            file_name="result.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        
        st.success("가공이 완료되었습니다!")

    except Exception as e:
        st.error(f"에러가 발생했습니다: {e}")