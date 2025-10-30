import streamlit as st

st.image("f1-banner.jpg")

st.title("F1 2025 Random Track Generator")

import random

tracks = ['Australia', 'China', 'Japan', 'Bahrain', 'Saudi Arabia', 'Miami',
          'Imola', 'Monaco', 'Spain', 'Canada', 'Austria', 'Silverstone', 'Spa',
          'Hungary', 'Zandvoort', 'Monza', 'Baku', 'Singapore', 'COTA', 'Mexico',
          'Brazil', 'Las Vegas', 'Qatar', 'Abu Dhabi']

def track_selection(tracks, K):
  selected_track_index = []
  index = 0

  while index < K:
    seed = random.randint(1,24)
    if seed not in selected_track_index:
      selected_track_index.append(seed)
      index += 1

  return selected_track_index

#my_options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
st.subheader("\nSelect how many tracks you want to generate:")
number = st.slider(
    label='Number of Races',
    min_value=1,
    max_value=len(tracks),
    value=1
)
indices = track_selection(tracks, number)
st.subheader("\nHere is your track selection:")
for i in indices:
  st.write(tracks[i])

