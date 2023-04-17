import streamlit as st
from scr import load_data

def main():
    df_raw = load_data()
    
    st.dataframe(df_raw)
    
if __name__ == '__main__':
    main()