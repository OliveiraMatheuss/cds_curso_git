import streamlit as st
from scr import load_data
from scr import create_dataframe_section
def main():
    df_raw = load_data()
    create_dataframe_section(df_raw)
    st.dataframe(df_raw)
    
if __name__ == '__main__':
    main()
    
    