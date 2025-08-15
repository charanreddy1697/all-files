import streamlit as st
import random

st.set_page_config(page_title="IPL Match Simulator", layout="centered")

st.title("🏏 IPL Match Simulator")

teams = [
    "Chennai Super Kings",
    "Mumbai Indians",
    "Royal Challengers Bangalore",
    "Kolkata Knight Riders",
    "Sunrisers Hyderabad",
    "Rajasthan Royals",
    "Delhi Capitals",
    "Punjab Kings"
]

# Select Teams
col1, col2 = st.columns(2)
with col1:
    team1 = st.selectbox("Select Team 1", teams, key="team1")
with col2:
    team2 = st.selectbox("Select Team 2", teams, key="team2")

if team1 == team2:
    st.warning("Please select two different teams!")
else:
    if st.button("Simulate Match"):
        score1 = random.randint(120, 220)
        score2 = random.randint(120, 220)

        st.subheader(f"{team1} scored: {score1} runs")
        st.subheader(f"{team2} scored: {score2} runs")

        if score1 > score2:
            st.success(f"🏆 {team1} wins by {score1 - score2} runs!")
        elif score2 > score1:
            st.success(f"🏆 {team2} wins by {score2 - score1} runs!")
        else:
            st.info("It's a Tie! Super Over needed 🔥")
