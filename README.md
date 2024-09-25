# Music and Sentiment Analysis Project

## Overview

This project is designed to gather data from Spotify, Genius, Last.fm, and ABC News by leveraging APIs and web scraping techniques. The goal is to extract the top songs from various countries, along with their popularity, lyrics, and genres, and analyze the sentiment of both the song metadata and relevant news articles for each country. This project demonstrates the integration of multiple data sources and performs sentiment analysis to provide valuable insights.

## Table of Contents

- [Purpose of Data Collection](#purpose-of-data-collection)
- [Data Source Selection](#data-source-selection)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Collection Practices](#collection-practices)
- [Data Handling and Privacy](#data-handling-and-privacy)
- [Data Usage](#data-usage)
- [Ethical Considerations](#ethical-considerations)

## Purpose of Data Collection

The primary purpose of this project is to extract and analyze data related to top songs across countries by integrating data from multiple APIs (Spotify, Genius, Last.fm) and scraping news data for each country from ABC News. The collected data is used to:

- Provide users with detailed insights into the most popular songs by country, including lyrics, genre, and play count.
- Perform sentiment analysis on both song metadata (name, genre) and country-specific news headlines.
- Combine music statistics and news data to offer a comprehensive view of cultural and media trends across different countries.

## Data Source Selection

- **Spotify API**: Used to gather the top tracks by country, including the song title, artist name, and popularity score.
- **Genius API**: Provides lyrics URLs for each song.
- **Last.fm API**: Supplies genre and play count data for the songs.
- **ABC News (scraping)**: News articles are scraped to extract headlines and perform sentiment analysis based on country-specific content.

These APIs were selected because they provide detailed song metadata, while ABC News was chosen for its global news coverage.

## Project Structure

Music-Sentiment-Analysis/ ├── main.py ├── requirements.txt ├── README.md ├── ETHICS.md ├── .env ├── .gitignore ├── music_data.csv

- **`main.py`**: The main Python script that gathers the data, performs sentiment analysis, and manages user interactions.
- **`requirements.txt`**: Lists the required Python packages.
- **`README.md`**: Project documentation (this file).
- **`ETHICS.md`**: Discussion of ethical considerations.
- **`.env`**: Stores API credentials (not included in version control).
- **`.gitignore`**: Ensures sensitive or unnecessary files are excluded from the repository.
- **`music_data.csv`**: Final dataset with all collected data.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/YourUsername/Music-Sentiment-Analysis.git

   ```

2. **Navigate to the Project Directory**:
   cd Music-Sentiment-Analysis

3. **Set Up a Virtual Environment**:
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`

4. **Install Required Libraries**:
   pip install -r requirements.txt

5. **Create a .env File with your API credentials.**

## Usage

1. **Run the Script**:
   python main.py

2. **Interact with the Program**:
   Enter a country name to search for news and get corresponding music stats.
   Type view to see the entire dataset.
   Type exit to quit the program.

## Features

- Spotify Integration: Fetches top songs by country, including the artist name and popularity.
- Genius Integration: Retrieves the lyrics URLs for the songs.
- Last.fm Integration: Provides genre and play count data.
- Sentiment Analysis: Analyzes sentiment for both song metadata and country-specific news.
- ABC News Scraping: Scrapes and analyzes country-specific news articles.

## Collection Practices

- Respect for Website Policies: Data scraping is performed in compliance with the robots.txt file of ABC News.
- Rate Limiting: The script is designed to be efficient and minimize server load.
- API Usage: All data gathered through APIs is retrieved within their rate limits and policies.

## Data Handling and Privacy

- No Personal Data Collection: The project does not gather or store any personal information from users.
- API Key Protection: API credentials are securely stored in a .env file, and the file is excluded from version control.

## Data Usage

- Educational Purposes: This project is intended for educational use, demonstrating how to gather and analyze data from various sources.
- Non-Commercial: The data will not be used for any commercial purposes or redistribution.

## Ethical Considerations

- Please refer to the ETHICS.md file for detailed information on how ethical considerations were addressed.
