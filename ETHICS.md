# Ethical Considerations in Music and Sentiment Analysis Project

## Overview

This document outlines the ethical considerations related to the data collection and analysis in the Music and Sentiment Analysis project. The project uses APIs and web scraping techniques to gather publicly available data. This document addresses how these activities comply with ethical guidelines.

## Table of Contents

- [Purpose of Data Collection](#purpose-of-data-collection)
- [Compliance with Website Policies](#compliance-with-website-policies)
- [Respecting Robots.txt](#respecting-robotstxt)
- [Rate Limiting](#rate-limiting)
- [Data Handling and Privacy](#data-handling-and-privacy)
- [Data Usage](#data-usage)
- [Conclusion](#conclusion)

## Purpose of Data Collection

- **Educational Purpose**: The project is intended for educational purposes, demonstrating how to use APIs and web scraping techniques to gather and analyze data.
- **Value Addition**: The goal is to provide users with insights into music trends and media coverage across various countries, combining sentiment analysis of songs and news articles.

## Compliance with Website Policies

- **API Usage**: The project uses publicly available APIs from Spotify, Genius, and Last.fm within their respective usage limits and policies.
- **ABC News**: Scraping activities for news articles are done in compliance with ABC News’ `robots.txt` file, which defines the allowed paths for scraping.

## Respecting Robots.txt

- **Robots.txt Compliance**: The scraper checks and adheres to ABC News’ `robots.txt` file to ensure it only accesses pages permitted for scraping.

## Rate Limiting

- **API Rate Limits**: The project ensures compliance with the rate limits of Spotify, Genius, and Last.fm APIs to avoid overloading their services.
- **Minimizing Server Load**: The script is designed to send minimal requests and avoid overloading the server during scraping.

## Data Handling and Privacy

- **No Personal Data**: The project does not collect any personal or sensitive data.
- **Secure Data Storage**: API keys and other sensitive data are stored securely in a `.env` file and not shared publicly.

## Data Usage

- **Non-Commercial**: All collected data is used solely for educational purposes. The project will not use the data for any commercial activities or redistribute it.
- **Fair Use**: The data collected is used under fair use principles for research and educational purposes, and any proprietary data remains the property of the original source.

## Conclusion

This project aims to conduct all data gathering and analysis in an ethical and responsible manner. By respecting the terms of service, complying with `robots.txt` guidelines, and handling data securely, I ensure that this project adheres to the best ethical practices in web scraping and data usage.
