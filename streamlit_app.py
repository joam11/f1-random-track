import streamlit as st

st.image("f1-banner.jpg")

st.title("F1 2025 Random Track Generator")

import random

tracks = ['Australia', 'China', 'Japan', 'Bahrain', 'Saudi Arabia', 'Miami',
          'Imola', 'Monaco', 'Spain', 'Canada', 'Austria', 'Silverstone', 'Spa',
          'Hungary', 'Zandvoort', 'Monza', 'Baku', 'Singapore', 'COTA', 'Mexico',
          'Brazil', 'Las Vegas', 'Qatar', 'Abu Dhabi']

st.subheader("\nSelect how many tracks you want to generate:")
number = st.slider(
    label='Number of Races',
    min_value=1,
    max_value=len(tracks),
    value=1
)

selected_tracks = random.sample(tracks, number)


st.subheader("Here is your track selection:")
for t in selected_tracks:
    st.write(f"🏁 {t}")

