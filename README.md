# Steam Games Dataset Analysis

## Overview
This project provides an analysis of the **Steam Games Dataset**. The dataset contains detailed information about various games available on the Steam platform, including developers, genres, prices, reviews, and player metrics like recommendations and peak concurrent users.

Using this dataset, the project explores key insights into developers, genres, game pricing, and platform availability. Visualizations are provided to enhance understanding and highlight notable trends.

---

## Files
### `games_may2024_cleaned.csv`
This is the cleaned dataset containing information on Steam games with the following columns:
- `name`: Name of the game
- `release_date`: Release date of the game
- `developers`: Developers of the game
- `price`: Price of the game
- `genres`: Genres associated with the game
- `reviews`: User reviews
- `recommendations`: Number of recommendations the game received
- `peak_ccu`: Peak concurrent users for the game
- `windows`, `mac`, `linux`: Boolean flags indicating platform availability

### `analysis.ipynb`
This Jupyter Notebook contains the code for:
- Data loading and cleaning
- Exploratory data analysis (EDA)
- Generating insights and visualizations

---

## Steps in the Analysis

1. **Loading and Cleaning Data**:
   - Converted `release_date` to datetime format for consistency.
   - Filled missing values in the `reviews` column with an empty string.
   - Checked for missing values and ensured the dataset was ready for analysis.

2. **Top Developers**:
   - Identified the top 10 developers based on the number of games they developed.
   - Visualized using a bar chart.

3. **Average Price by Genre**:
   - Split genres into separate rows for accurate grouping.
   - Calculated the average price of games by genre.
   - Displayed the top 10 genres with the highest average prices using a bar chart.

4. **Top Recommended Games**:
   - Extracted the 10 games with the highest number of recommendations.
   - Visualized the data using a horizontal bar chart.

5. **Platform Availability**:
   - Analyzed the availability of games across platforms (Windows, Mac, Linux).
   - Presented the results as a bar chart.

6. **Peak Concurrent Users**:
   - Identified the 10 games with the highest peak concurrent users.
   - Displayed results in a horizontal bar chart.

---

## Visualizations
The following visualizations were created:
1. **Top Developers by Number of Games**:
   A bar chart displaying the top 10 developers with the most games published on Steam.

2. **Average Price of Games by Genre**:
   A bar chart showcasing the genres with the highest average game prices.

3. **Top 10 Games with the Highest Number of Recommendations**:
   A horizontal bar chart highlighting games most recommended by users.

4. **Proportion of Games Available on Different Platforms**:
   A bar chart showing the number of games available on Windows, Mac, and Linux.

5. **Top 10 Games by Peak Concurrent Users**:
   A horizontal bar chart visualizing the games with the highest peak concurrent users.

---

## How to Run the Project
1. Clone the repository and ensure the dataset `games_may2024_cleaned.csv` is available in the same directory.
2. Open the Jupyter Notebook (`analysis.ipynb`) and run all cells sequentially.
3. Install the required libraries:
   - `pandas`
   - `matplotlib`
   - `seaborn`
4. The visualizations and outputs will be displayed inline.

---

## Insights
- **Developers**: Certain developers dominate the platform by publishing a large number of games.
- **Genres**: Premium genres tend to have higher average prices.
- **Player Recommendations**: Popular games often receive significantly higher recommendations.
- **Platform Availability**: Windows is the most popular platform, with fewer games supporting Mac and Linux.
- **Player Engagement**: Some games achieve exceptionally high concurrent player counts, indicating their popularity.

---

## Requirements
- Python 3.7+
- Libraries:
  - `pandas`
  - `matplotlib`
  - `seaborn`

---

## Future Work
- Analyze user reviews for sentiment analysis.
- Explore trends in release dates and how they affect game success.
- Perform a deeper analysis of pricing strategies across developers and genres.

---

## License
This project is for educational purposes and does not hold any rights to the dataset. Use at your discretion.
