import pandas as pd
import altair as alt
import streamlit as st

brush = alt.selection_single(on='mouseover')

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

disable = pd.DataFrame({
    'reason': ['In past year, needed to see doctor but did not because of cost', 'Women current with mammogram', 'Women current with Pap test', 'Adults who engage in no leisure-time physical activity', 'Children and adolescents considered obese (aged 2–17 y)', 'Adults who are obese', 'Adults who smoke (100 cigarettes in lifetime and currently smoke)', 'Annual no. of new cases of diagnosed diabetes (per 1000 persons)', 'Adults with cardiovascular disease (18-44)', 'Adults with cardiovascular disease (45-64)', 'Victim of violent crime (per 1000 persons)', 'Adults reporting sufficient social and emotional support', 'Adults reporting sufficient social and emotional support (Adult (> 16 y) unemployment)', 'Social determinants of health (Adult (> 16 y) employment)', 'Social determinants of health (Adults with < high school education)', 'Social determinants of health (Internet access)', 'Social determinants of health (Household income < $15 000)', 'Social determinants of health (Inadequate transportation)'],
    'value': [12.1, 76.6, 82.3, 32.2, 15.2, 34.2, 18.0, 6.8, 3.4, 9.7, 21.3, 83.1, 8.7, 63.6, 9.5, 85, 15, 16]
})

disable_chart = alt.Chart(disable).mark_bar().encode(
    x=alt.X('reason', title=None),
    y=alt.Y('value', title=None),
    color=alt.value('pink'),
    opacity=alt.condition(brush, alt.OpacityValue(1), alt.OpacityValue(0.4))
)

able = pd.DataFrame({
    'reason': ['In past year, needed to see doctor but did not because of cost', 'Women current with mammogram', 'Women current with Pap test', 'Adults who engage in no leisure-time physical activity', 'Children and adolescents considered obese (aged 2–17 y)', 'Adults who are obese', 'Adults who smoke (100 cigarettes in lifetime and currently smoke)', 'Annual no. of new cases of diagnosed diabetes (per 1000 persons)', 'Adults with cardiovascular disease (18-44)', 'Adults with cardiovascular disease (45-64)', 'Victim of violent crime (per 1000 persons)', 'Adults reporting sufficient social and emotional support', 'Adults reporting sufficient social and emotional support (Adult (> 16 y) unemployment)', 'Social determinants of health (Adult (> 16 y) employment)', 'Social determinants of health (Adults with < high school education)', 'Social determinants of health (Internet access)', 'Social determinants of health (Household income < $15 000)', 'Social determinants of health (Inadequate transportation)'],
    'value': [27.0, 70.7, 78.3, 54.2, 21.1, 44.6, 28.8, 19.1, 12.4, 27.7, 32.4, 70.0, 15.0, 17.8, 13, 54, 34, 34]
})

able_chart = alt.Chart(able).mark_bar().encode(
    x=alt.X('reason', title=None),
    y=alt.Y('value', title=None),
    color=alt.value('red'),
    opacity=alt.condition(brush, alt.OpacityValue(1), alt.OpacityValue(0.4))
)
chart_2 = (able_chart + disable_chart).add_selection(
    brush
).properties(
    width=500,
    height=400,
    title = 'Percent of disabled people get care compared with the people without disablity'
).interactive()


st.altair_chart(chart_2, theme=None, use_container_width=True)