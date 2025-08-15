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
    2009: "Royal Challengers Bengaluru",
    2010: "Mumbai Indians",
    2011: "Royal Challengers Bengaluru",
    2012: "Chennai Super Kings",
    2013: "Chennai Super Kings",
    2014: "Kings XI Punjab",
    2015: "Chennai Super Kings",
    2016: "Royal Challengers Bengaluru",
    2017: "Rising Pune Supergiant",
    2018: "Sunrisers Hyderabad",
    2019: "Chennai Super Kings",
    2020: "Delhi Capitals",
    2021: "Kolkata Knight Riders",
    2022: "Rajasthan Royals",
    2023: "Gujarat Titans",
    2024: "Sunrisers Hyderabad",
    2025: "Kings XI Punjab"}

years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 
 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]

import random as rm

import time




teams = ['Rajasthan Royals', 'Deccan Chargers', 'Chennai Super Kings',
 'Kolkata Knight Riders', 'Mumbai Indians', 'Sunrisers Hyderabad',
 'Gujarat Titans', 'Royal Challengers Bengaluru','Gujarat Titans',
 'Kings XI Punjab', 'Rising Pune Supergiant', 'Delhi Capitals']

if "year" not in st.session_state:
    st.session_state.year = rm.choice(years)


if 'score' not in st.session_state:
    st.session_state.score = 0
c1,c2,c3 = st.columns([1,3,1])    
with c2:
    st.title(f"IPL QUIZ GAME")

c11,c22 = st.columns(2)
c11.title(f"Year : {st.session_state.year}")

    
a1,a2 = st.columns(2)
w = a1.selectbox('Winner team',teams)
r = a2.selectbox('Runner Up team',teams)

b1,b2 = st.columns(2)

c1,c2,c3 = st.columns([1,3,1])
if c1.button('submit'):
    with b1:        
        if ipl_winners[st.session_state.year] == w :
            st.write('correct')
            st.session_state.score += 1
        else:
            st.write(f"sorry, winners are : {ipl_winners[st.session_state.year]}")
            st.session_state.score -= 1
    with b2:
        if ipl_runner_ups[st.session_state.year] == r :
            st.write('correct')
            st.session_state.score += 1 
        else:
            st.write(f"sorry, runner ups are : {ipl_runner_ups[st.session_state.year]}")
            st.session_state.score -= 1



c22.title(f"Score {st.session_state.score}")

if c3.button('Next'):
    st.session_state.year = rm.choice(years)
    time.sleep(1)
    st.rerun()
