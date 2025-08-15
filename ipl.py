import streamlit as st 
st.set_page_config(layout="wide")

ipl_winners = {
    2008: "Rajasthan Royals",
    2009: "Deccan Chargers",
    2010: "Chennai Super Kings",
    2011: "Chennai Super Kings",
    2012: "Kolkata Knight Riders",
    2013: "Mumbai Indians",
    2014: "Kolkata Knight Riders",
    2015: "Mumbai Indians",
    2016: "Sunrisers Hyderabad",
    2017: "Mumbai Indians",
    2018: "Chennai Super Kings",
    2019: "Mumbai Indians",
    2020: "Mumbai Indians",
    2021: "Chennai Super Kings",
    2022: "Gujarat Titans",
    2023: "Chennai Super Kings",
    2024: "Kolkata Knight Riders",
    2025: "Royal Challengers Bengaluru"
}

ipl_runner_ups = {
    2008: "Chennai Super Kings",
    2009: "Royal Challengers Bangalore",
    2010: "Mumbai Indians",
    2011: "Royal Challengers Bangalore",
    2012: "Chennai Super Kings",
    2013: "Chennai Super Kings",
    2014: "Kings XI Punjab",
    2015: "Chennai Super Kings",
    2016: "Royal Challengers Bangalore",
    2017: "Rising Pune Supergiant",
    2018: "Sunrisers Hyderabad",
    2019: "Chennai Super Kings",
    2020: "Delhi Capitals",
    2021: "Kolkata Knight Riders",
    2022: "Rajasthan Royals",
    2023: "Gujarat Titans",
    2024: "Sunrisers Hyderabad",
    2025: "Punjab Kings"}

years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 
 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]

import random as rm

import random as rm




teams = ['Rajasthan Royals', 'Deccan Chargers', 'Chennai Super Kings',
 'Kolkata Knight Riders', 'Mumbai Indians', 'Sunrisers Hyderabad',
 'Gujarat Titans', 'Royal Challengers Bengaluru', 'Royal Challengers Bangalore',
 'Kings XI Punjab', 'Rising Pune Supergiant', 'Delhi Capitals', 'Punjab Kings']

if "year" not in st.session_state:
    st.session_state.year = rm.choice(years)

c1,c2,c3 = st.columns([1,3,1])
c2.write(st.session_state.year)

a1,a2 = st.columns(2)
a1.selectbox('winner team',teams)
a2.selectbox('runner up team',teams)


if st.button("🔄 Next Year"):
    st.session_state.year = rm.choice(years)
    st.rerun()

