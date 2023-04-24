import pandas as pd
import plotly.express as px 
import streamlit as st


def rd1_question_9(df):
    df_grouped = df[['id', 'seller_type']].groupby('seller_type')

    df_grouped = df_grouped.count().reset_index()

    df_grouped = df_grouped.rename(columns={'id': 'count'})
    ax = px.bar(
        data = df_grouped,
        x = 'seller_type',
        y = 'count',
        labels = {'seller_type': 'Seller type',
                  'count': 'Quantity',
                  },
        color = 'seller_type'
        )

    ax.bar_label(ax.containers[0])

    ax.set(
        title = 'Quantidade de Tipos de Vendendores',
        xlabel = 'Tipos de Vendedores',
        ylabel = 'Quantidade'
    )
    
    st.plotly_chart(ax, use_container_width= True)
    return None

def rd1_question_13(df):
    df_grouped = df.groupby('owner').agg(
    qty = pd.NamedAgg('id', 'count')
    ).sort_values('qty').reset_index()

    ax = px.bar(
        data=df_grouped,
        x = 'owner',
        y = 'qty',
        label = {
            'owner':'Owner Types',
            'qty': 'Quantity'
        }
    )

    ax.bar_label(ax.containers[0])

    ax.set(
        title = 'Quantidade de Motos por tipo de dono',
        xlabel = 'Tipo de Dono',
        ylabel = 'Quantidade de donos'
    )
    st.plotly_chart(ax, use_container_width= True)
    return None

def rd1_question_14(df):
    df_grouped = df[['km_class', 'selling_price']].groupby('km_class')

    df_grouped = df_grouped.mean().sort_values('selling_price', ascending=False).reset_index()
    
    ax = px.scatter(
        data = df_grouped,
        x = 'km_class',
        y = 'selling_price',
        labels= {
                'km_class': 'Kilometers', 
                'selling_price': 'Selling Price'
        }
    )
    st.plotly_chart(ax, use_container_width= 'True')
    return None


def create_answers_section(df):
    st.title("Main Questions Answers")

    st.header("First Round")
    st.subheader("How many bikes are being sold by their owners and how many bikes are being sold by distributors?")

    st.subheader("How many bikes are being sold are bikes from a unique owner?")

    st.subheader("Are high kilometer bikes more expensive than bikes with lower kilometer?")

    st.subheader("Are the bikes with a unique owner more expense on avarege than the other bikes?")

    st.subheader("Are the bikes that have more owners also the bikes with more kilometers traveled on avarege?")

    st.subheader("Which company has the most bikes registered?")

    st.subheader("Which company has the most expensive bikes on avarege?")

    st.subheader("Are the company that has the most expensive bikes registered also the company with the most bikes registered?")

    st.subheader("Which bikes are good for buying?")
    
    return None
