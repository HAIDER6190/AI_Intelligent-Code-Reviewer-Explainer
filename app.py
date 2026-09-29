import streamlit as st

from parser import read_code, get_language
from ai_reviewer import review_code


st.set_page_config(
    page_title="Intelligent Code Reviewer",
    page_icon=":robot:",
    layout="wide",
)

st.title("Intelligent Code Reviewer")

st.write(
    "Upload a Python, JavaScript, or Java file "
    "to analyze the code using Generative AI."
)

uploaded_file = st.file_uploader(
    "Upload your source code file",
    type=["py", "js", "java"],
)


if uploaded_file is not None:
    try:
        code = read_code(uploaded_file)
        language = get_language(uploaded_file.name)

        st.success(f"File uploaded successfully: {uploaded_file.name}")

        st.subheader("Detected Language")
        st.write(language)

        st.subheader("Source Code")
        st.code(
            code,
            language=language.lower(),
        )

        if st.button("🔍 Review Code"):
            try:
                with st.spinner("Analyzing your code..."):
                    review = review_code(code, language)

                st.success("Code analysis completed!")

                st.subheader("1. Code Explanation")
                st.write(review["code_explanation"])

                st.subheader("2. Bugs and Issues")

                if review["bugs_and_issues"]:
                    for bug in review["bugs_and_issues"]:
                        st.markdown(f"**{bug['title']}**")
                        st.write(bug["description"])
                        st.write(
                            f"**Why it matters:** "
                            f"{bug['why_it_matters']}"
                        )
                        st.write(
                            f"**Suggested fix:** "
                            f"{bug['suggested_fix']}"
                        )
                else:
                    st.write(
                        "No significant bugs or issues were identified."
                    )

                st.subheader("3. Suggested Improvements")

                for improvement in review["suggested_improvements"]:
                    st.markdown(f"**{improvement['title']}**")
                    st.write(improvement["description"])

                st.subheader("4. Optimized Code")

                st.code(
                    review["optimized_code"],
                    language=language.lower(),
                )

            except Exception as error:
                st.error(
                    f"Unable to analyze the code: {error}"
                )

    except ValueError as error:
        st.error(str(error))