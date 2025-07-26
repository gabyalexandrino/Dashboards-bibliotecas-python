import streamlit as st
import pandas as pd
import plotly.express as px

df = px.data.gapminder()

#st.set_page_config(layout="wide", page_title="Dashboard Gapminder")


st.title("🌍 Dashboard Gapminder – Streamlit + Plotly")


st.sidebar.header("Filtros")
anos = sorted(df["year"].unique())
ano_selecionado = st.sidebar.slider("Ano", min_value=min(anos), 
                                    max_value=max(anos), 
                                    value=2007, step=5)

continentes = df["continent"].unique().tolist()
continente_selecionado = st.sidebar.multiselect("Continente", continentes, default=continentes)

df_filtrado = df[(df["year"] == ano_selecionado) & (df["continent"].isin(continente_selecionado))]

col1, col2 = st.columns(2)

with col1:
    st.subheader("PIB per capita vs Expectativa de Vida")
    fig_disp = px.scatter(
        df_filtrado,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        hover_name="country",
        log_x=True,
        size_max=60,
        labels={"gdpPercap": "PIB per Capita", "lifeExp": "Expectativa de Vida"},
        title=f"Dispersão por país – {ano_selecionado}"
    )
    st.plotly_chart(fig_disp, use_container_width=True)


with col2:
    st.subheader("🗺️ Mapa: Expectativa de Vida")
    fig_mapa = px.choropleth(
        df_filtrado,
        locations="iso_alpha",
        color="lifeExp",
        hover_name="country",
        color_continuous_scale="Viridis",
        labels={"lifeExp": "Expectativa de Vida"},
        title=f"Expectativa de Vida por País – {ano_selecionado}"
    )
    st.plotly_chart(fig_mapa, use_container_width=True)

# Tabela com os dados
st.markdown("### 📋 Tabela de Dados Filtrados")
st.dataframe(df_filtrado.reset_index(drop=True))