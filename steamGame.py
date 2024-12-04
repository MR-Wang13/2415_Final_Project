import pandas as pd

# Load the dataset
df = pd.read_csv("/kaggle/input/steam-games-dataset/games_may2024_cleaned.csv")

# Display the first few rows of the dataset
df.head()

# Display basic information about the dataset
df.info()

# Display summary statistics for numeric columns
df.describe()

# Check for missing values
df.isnull().sum()

# Convert release_date to datetime format
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Fill missing values in reviews with an empty string
df['reviews'] = df['reviews'].fillna('')

# Convert release_date to datetime format
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Fill missing values in reviews with an empty string
df['reviews'] = df['reviews'].fillna('')

top_developers = df['developers'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_developers.index, y=top_developers.values)
plt.title('Top 10 Developers by Number of Games')
plt.xlabel('Developer')
plt.ylabel('Number of Games')
plt.xticks(rotation=90)
plt.show()

# Split genres into separate rows
df_genres = df.assign(genres=df['genres'].str.split(',')).explode('genres')

avg_price_by_genre = df_genres.groupby('genres')['price'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(14, 7))
sns.barplot(x=avg_price_by_genre.index, y=avg_price_by_genre.values)
plt.title('Average Price of Games by Genre')
plt.xlabel('Genre')
plt.ylabel('Average Price')
plt.xticks(rotation=90)
plt.show()

top_recommended_games = df.nlargest(10, 'recommendations')[['name', 'recommendations']]
plt.figure(figsize=(14, 7))
sns.barplot(x='recommendations', y='name', data=top_recommended_games)
plt.title('Top 10 Games with the Highest Number of Recommendations')
plt.xlabel('Number of Recommendations')
plt.ylabel('Game')
plt.show()

platforms = ['windows', 'mac', 'linux']
platform_counts = df[platforms].sum().sort_values()

plt.figure(figsize=(10, 6))
platform_counts.plot(kind='bar')
plt.title('Proportion of Games Available on Different Platforms')
plt.xlabel('Platform')
plt.ylabel('Number of Games')
plt.show()

top_peak_ccu_games = df.nlargest(10, 'peak_ccu')[['name', 'peak_ccu']]
plt.figure(figsize=(14, 7))
sns.barplot(x='peak_ccu', y='name', data=top_peak_ccu_games)
plt.title('Top 10 Games by Peak Concurrent Users')
plt.xlabel('Peak Concurrent Users')
plt.ylabel('Game')
plt.show()
