# Programming Language Lexer

This project is a compiler design tool aimed at recognizing different programming languages using lexical analysis. It utilizes the Python Lex-Yacc (PLY) library to build a lexer capable of identifying tokens in Python, C++, and Java code.

Features

1. Multi-Language Support: The lexer can identify tokens in Python, C++, and Java code.
2. Token Recognition: Recognizes various language constructs such as function definitions, variable declarations, assignments, control structures, and more.

Installation

1. Install the required dependencies: ```pip install -r requirements.txt```
2. Install Streamlit: ```pip install streamlit```

Usage

1. The Programming_Language.py file is a front-end developed using streamlit.
2. The ne.py file contains the code for tokenisation. The functions can be altered and are extensible for further more programming languages.
3. To execute the application, run the following command: ```streamlit run Programming_Language.py```
4. This command will launch a Streamlit web application where you can enter code snippets in Python, C++, or Java and see the lexer output.
