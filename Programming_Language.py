import streamlit as st
import pandas as pd
from ne import lexer

# Function to test the lexer
def test_lexer(data):
    lexer.input(data)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    return tokens

import base64

def get_table_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="lexer_output.csv">Download CSV file</a>'
    return href

def main():
    st.set_page_config(
        page_title="Programming Language Lexer",
        page_icon=":computer:",
        layout="centered",
    )

    st.title("Programming Language Lexer")

    data = st.text_area("Enter code:", default_code, height=300)

    if st.button("Run Lexer"):
        st.subheader("Lexer Output:")

        tokens = test_lexer(data)
        token_data = [(tok.type, tok.value) for tok in tokens]
        df = pd.DataFrame(token_data, columns=["Token Type", "Token Value"])

        col_width = {'Token Type': 150, 'Token Value': 300}
        st.table(df.style.set_properties(**{'max-width': '150px', 'font-size': '10px'}))
        st.markdown(get_table_download_link(df), unsafe_allow_html=True)

        common_tokens = ['FUNCTION_DEF', 'FUNCTION_CALL', 'VAR_DECL', 'ASSIGN', 'RETURN', 'CALCULATION_OR_IDENTIFIER','BRANCH','FOR_LOOP','WHILE_LOOP','ACCESS_SPECIFIERS','FUNCTION_DECL','CLASS']
        both_detected = all(tok.type in common_tokens for tok in tokens)
 
        class_token = 'CLASS'
        class_detected = any(tok.type == class_token for tok in tokens)

        cpp_tokens = ['CPP', 'CPP_INCLUDE','CPP_PRINT'] + common_tokens
        cpp_detected = all(tok.type in cpp_tokens for tok in tokens)

        py_tokens = ['PYTHON', 'PYTHON_DEF','PYTHON_CLASS'] + common_tokens
        py_detected = all(tok.type in py_tokens for tok in tokens)

        java_tokens = ['JAVA'] + common_tokens
        java_detected = all(tok.type in java_tokens for tok in tokens)

        print(both_detected)
        print(class_detected)
        if both_detected and class_detected:
            st.success("Detected languages: C++ and Java")
        elif both_detected:
            st.success("Dected languages: C++, Java and Python")
        elif cpp_detected:
            st.success("Detected language: C++")
        elif py_detected:
            st.success("Detected language: Python")
        elif java_detected:
            st.success("Detected language: Java")
        else:
            st.warning("Unable to detect the language.")

if __name__ == "__main__":
    default_code = '''
    def abc():
        a = b + c
        return a
    '''
    main()