import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


try:
    df = pd.read_csv("C:/Users/heart/OneDrive/Desktop/Stalin DS/Project 1/imdb_cleaned_data.csv")
except FileNotFoundError:
    print("Error: 'imdb_cleaned_data' not found.")
    exit()
st.title("2024 Movie Analysis")
# 1 Top 10 movies
st.subheader("1.Top 10 Movies by Rating and Voting Count")
top_movies = df.sort_values(['Rating', 'Voting'], ascending=[False, False]).head(10)
fig1 = px.bar(top_movies, x='Title', y='Rating', color='Voting', title='Top 10 Movies')
st.plotly_chart(fig1, use_container_width=True)

# 2. Genre Distribution
st.subheader("2. Genre Distribution")
genre_order = df['Genre'].value_counts()
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.countplot(x='Genre', data=df, order=genre_order.index, palette='viridis', ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)

# 3. Average Duration by Genre
st.subheader("3.Average Duration by Genre")
avg_duration = df.groupby('Genre')['Duration'].mean().sort_values()
fig3 = px.bar(avg_duration, orientation='h', title='Average Duration by Genre')
st.plotly_chart(fig3, use_container_width=True)


# 4. Voting Trends by Genre
st.subheader("4.Average Voting Counts by Genre")
avg_votes = df.groupby('Genre')['Voting'].mean().sort_values(ascending=False)
fig4 = px.bar(avg_votes, title='Average Votes by Genre')
st.plotly_chart(fig4, use_container_width=True)

# 5. Rating Distribution 
st.subheader("5.Rating Distribution")
fig5, ax5 = plt.subplots(1, 2, figsize=(14, 5))
sns.histplot(df['Rating'], bins=20, ax=ax5[0], kde=True, color='skyblue')
ax5[0].set_title("Histogram of Ratings")
sns.boxplot(x=df['Rating'], ax=ax5[1], color='lightgreen')
ax5[1].set_title("Boxplot of Ratings")
st.pyplot(fig5)

# 6. Genre-Based Rating Leaders
st.subheader("6.Top-Rated Movie by Genre")
top_genre_movies = df.sort_values('Rating', ascending=False).drop_duplicates('Genre')
st.dataframe(top_genre_movies[['Genre', 'Title', 'Rating', 'Voting']].reset_index(drop=True))

# 7. Most Popular Genres by Voting 
st.subheader("7.Most Popular Genres by Total Votes")
votes_by_genre = df.groupby('Genre')['Voting'].sum().sort_values(ascending=False)
fig7 = px.pie(values=votes_by_genre, names=votes_by_genre.index, title="Votes by Genre")
st.plotly_chart(fig7)

# 8. Duration Extremes
st.subheader("8.Duration Extremes")
shortest = df.sort_values('Duration').iloc[0]
longest = df.sort_values('Duration').iloc[-1]
col1, col2 = st.columns(2)
with col1:
    st.metric("Shortest Movie", f"{shortest['Title']} ({shortest['Duration']} mins)")
with col2:
    st.metric("Longest Movie", f"{longest['Title']} ({longest['Duration']} mins)")

# 9. Ratings by Genre Heatmap
st.subheader("9.Average Ratings by Genre (Heatmap)")
heat_data = df.groupby('Genre')['Rating'].mean().to_frame().T
fig9, ax9 = plt.subplots(figsize=(10, 2))
sns.heatmap(heat_data, annot=True, cmap="coolwarm", cbar=False)
st.pyplot(fig9)

st.subheader("10.Correlation: Ratings vs. Voting Counts")
fig10 = px.scatter(df, x='Voting', y='Rating', size='Duration', hover_name='Title',
                   title='Rating vs Voting', color='Genre')
st.plotly_chart(fig10, use_container_width=True)































































































