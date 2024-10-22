#PROBLEM STATEMENT-1: Analyzing Spotify Dataset

import pandas as pd

#1 Load the dataset
df = pd.read_csv("top50spotify.csv")
df

#2 save its as "top50.csv"
df.to_csv('top50.csv', index=False)
df

#3 Calculate the average Energy and Length for the first 10 songs
avg_energy = df['Energy'].head(10).mean()
avg_length = df['Length.'].head(10).mean()
print("Average Energy:", avg_energy)
print("Average Length:", avg_length)

#4 Calculate total length of songs grouped by genre from top to bottom

total_length_by_genre = df.groupby('Genre')['Length.'].sum().sort_values(ascending=False)

print("Total Length by Genre:\n", total_length_by_genre)

#5 Find the artist with the most tracks in one genre
most_tracks_artist = df.groupby(['Artist.Name', 'Genre']).size().idxmax()
print("Artist with most tracks in one genre:", most_tracks_artist[0])

#6 print the data of the tracks from the previous question
artist_df = df[df['Artist.Name'] == most_tracks_artist[0]]
print(artist_df)
