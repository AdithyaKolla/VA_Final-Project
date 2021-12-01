import altair as alt
import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
from vega_datasets import data
source = alt.topo_feature(data.world_110m.url, "countries")
mapc=alt.Chart(source).mark_geoshape(
        fill='lightgray',
        stroke='white'
        ).project(
        "equirectangular"
        ).properties(
        width=500,
        height=300
        )
st.altair_chart(mapc)