import pandas as pd
import altair as alt
import streamlit as st

brush = alt.selection_single()

source = pd.DataFrame({"category": ['Doctors strongly welcome PWD', 'Others'], "value": [44, 56], "text": ['43.2%', '56.8%']})

base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), 
)

pie = base.mark_arc(outerRadius=120).encode(color=alt.Color("category:N", legend=alt.Legend(
        orient='none',
        title = None,
        legendX=200, legendY=310,
        direction='horizontal',
        titleAnchor='middle')),
                                            opacity=alt.condition(brush, alt.OpacityValue(1), alt.OpacityValue(0.4))
).add_selection(
    brush
).properties(
    title='Percent of doctors welcoming disabled patients'
)
text = base.mark_text(radius=60, size=20).encode(text="text:N")


source_2 = pd.DataFrame({"category": ['Doctors very confident of providing same quality of care for PWD', 'Others'], "value": [41, 59], "text": ['40.7%', '59.3%']})

base_2 = alt.Chart(source_2).encode(
    theta=alt.Theta("value:Q", stack=True), 
)

pie_2 = base_2.mark_arc(outerRadius=120).encode(color=alt.Color("category:N"),
        opacity=alt.condition(brush, alt.OpacityValue(1), alt.OpacityValue(0.4))
).add_selection(
    brush
).properties(
    title='Percent of doctors very confident of providing same quality of care'
)
text_2 = base_2.mark_text(radius=60, size=20).encode(text="text:N")

chart_1 = ((pie + text) | (pie_2 + text_2))

st.altair_chart(chart_1, theme=None, use_container_width=True)
