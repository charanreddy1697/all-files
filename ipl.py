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



import streamlit as st
import random
import time

st.set_page_config(page_title="IPL Live Match", layout="centered")

st.title("🏏 IPL Live Match Simulator")

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

# Ball outcomes & commentary
outcomes = [
    (0, "Dot ball"),
    (1, "Single run"),
    (2, "Two runs"),
    (3, "Three runs"),
    (4, "FOUR! What a shot!"),
    (6, "SIX! Huge hit!"),
    ("W", "WICKET! Clean bowled!")
]

col1, col2 = st.columns(2)
with col1:
    team1 = st.selectbox("Select Team 1", teams, key="t1")
with col2:
    team2 = st.selectbox("Select Team 2", teams, key="t2")

if team1 == team2:
    st.warning("Please select two different teams!")
else:
    if st.button("Start Match"):
        st.subheader(f"{team1} vs {team2}")
        overs = 2  # For quick demo
        total_score = 0
        wickets = 0

        commentary_placeholder = st.empty()
        score_placeholder = st.empty()

        for over in range(overs):
            for ball in range(6):
                outcome = random.choice(outcomes)
                if outcome[0] == "W":
                    wickets += 1
                    commentary = outcome[1]
                else:
                    total_score += outcome[0]
                    commentary = outcome[1]

                # Update live commentary
                commentary_placeholder.write(f"**Over {over}.{ball+1}** → {commentary}")
                score_placeholder.subheader(f"Score: {total_score}/{wickets} in {over}.{ball+1} overs")

                time.sleep(1)  # Simulate live delay

        st.success(f"Innings Over! Final Score: {total_score}/{wickets} in {overs} overs")

