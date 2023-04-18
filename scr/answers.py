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

