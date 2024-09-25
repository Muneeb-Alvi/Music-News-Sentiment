import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import pandas as pd
import pylast
from dotenv import load_dotenv
import os

spotify_client_id = os.getenv('SPOTIFY_CLIENT_ID')
spotify_client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
genius_client_id = os.getenv('GENIUS_CLIENT_ID')
genius_client_secret = os.getenv('GENIUS_CLIENT_SECRET')
lastfm_api_key = os.getenv('LASTFM_API_KEY')
lastfm_api_secret = os.getenv('LASTFM_API_SECRET')
lastfm_username = os.getenv('LASTFM_USERNAME')
lastfm_password_hash = os.getenv('LASTFM_PASSWORD_HASH')

def get_access_token_spotify(client_id, client_secret): #function to get Spotify access token
    try:
        url = "https://accounts.spotify.com/api/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = {"grant_type": "client_credentials"}
        response = requests.post(url, headers=headers, data=payload, auth=(client_id, client_secret))
        response.raise_for_status()  # Raise HTTPError for bad responses
        token = response.json().get('access_token')
        return token
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving Spotify access token: {e}")
        return None


def find_country_top_50_playlists(access_token): #function to find playlists for top charts in different countries
    countries = ["Argentina", "Australia", "Austria", "Belarus", "Belgium", "Bolivia", "Brazil", "Bulgaria", "Canada", "Chile", "Colombia", "Costa Rica", "Cyprus", "Czech Republic", "Denmark", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Estonia", "Finland", "France", "Germany", "Greece", "Guatemala", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Ireland", "Israel", "Italy", "Japan", "Kazakhstan", "Latvia", "Lithuania", "Luxembourg", "Malaysia", "Mexico", "Morocco", "Netherlands", "New Zealand", "Nicaragua", "Nigeria", "Norway", "Pakistan", "Panama", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Romania", "Saudi Arabia", "Singapore", "Slovakia", "South Africa", "South Korea", "Spain", "Sweden", "Switzerland", "Taiwan", "Thailand", "Turkey", "United Arab Emirates", "USA", "Ukraine", "UK", "Uruguay", "Venezuela", "Vietnam"]
    playlist_ids = {}
    
    if not access_token:
        print("No access token provided for Spotify.")
        return playlist_ids

    for country in countries:
        try:
            url = "https://api.spotify.com/v1/search"
            query = f"Top Songs - {country}"
            params = {"q": query, "type": "playlist", "limit": 1}
            headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            results = response.json()
            playlist_ids[country] = results['playlists']['items'][0]['id'] if results['playlists']['items'] else None
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving playlist for {country}: {e}")
        except (KeyError, IndexError) as e:
            print(f"Error processing playlist data for {country}: {e}")
    
    return playlist_ids

def get_top_song_and_artist_in_country(access_token, playlist_id): #function to get the top song and artist in a country
    try:
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        top_track = response.json()['items'][0]['track']
        top_song_name = top_track['name']
        primary_artist_name = top_track['artists'][0]['name']
        song_popularity = top_track['popularity']
        return top_song_name, primary_artist_name, song_popularity
    except (requests.exceptions.RequestException, KeyError, IndexError) as e:
        print(f"Error retrieving top song for playlist {playlist_id}: {e}")
        return None, None, None

def get_access_token_genius(client_id, client_secret): #function to get access token for Genius API
    try:
        token_url = 'https://api.genius.com/oauth/token'
        data = {'grant_type': 'client_credentials', 'client_id': client_id, 'client_secret': client_secret}
        response = requests.post(token_url, data=data)
        response.raise_for_status()
        access_token = response.json().get('access_token')
        return access_token
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving Genius access token: {e}")
        return None

def get_lyrics_url(song_title, artist_name, access_token): #function to get lyrics URL from Genius API
    try:
        base_url = "https://api.genius.com"
        headers = {'Authorization': 'Bearer ' + access_token}
        search_url = base_url + "/search"
        params = {'q': song_title}
        response = requests.get(search_url, params=params, headers=headers)
        response.raise_for_status()
        json = response.json()
        for hit in json['response']['hits']:
            if artist_name.lower() in hit["result"]['primary_artist']['name'].lower():
                return hit['result']['url']
    except (requests.exceptions.RequestException, KeyError, IndexError) as e:
        print(f"Error retrieving lyrics for {song_title} by {artist_name}: {e}")
    return None

def get_lastfm_data(song_name, artist_name, network): #function to get Last.fm data (genre and play count)
    try:
        track = network.get_track(artist_name, song_name)
        genre = ', '.join(tag.item.get_name() for tag in track.get_top_tags())
        playcount = track.get_playcount()
        return genre, playcount
    except pylast.WSError as e:
        print(f"Error retrieving data from Last.fm for {song_name} by {artist_name}: {e}")
        return None, None

def get_sentiment_from_title_and_genre(song_name, genres): #function to perform sentiment analysis on song title and genre
    combined_text = f"{song_name}, {genres}"
    analysis = TextBlob(combined_text)
    return round(analysis.sentiment.polarity, 2)

def get_sentiment_news(text): #function to perform sentiment analysis on news summaries
    analysis = TextBlob(text)
    return round(analysis.sentiment.polarity, 2)

def scrape_news_for_country(country): #function to scrape news from ABC News for a country
    try:
        url = "https://abcnews.go.com/International"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all('div', class_='ContentRoll__Headline')

        news_list = []
        for article in articles:
            headline = article.get_text(strip=True)
            if country.lower() in headline.lower():
                news_list.append(headline)
        return news_list
    except requests.exceptions.RequestException as e:
        print(f"Error scraping news for {country}: {e}")
        return []

def user_interaction(df): #main user interaction function
    while True:
        user_input = input("Enter a country name to search for news, 'view' to see the DataFrame, or 'exit' to quit: ").strip()

        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        if user_input.lower() == 'view':
            print(df)
        else:
            if user_input in df['Country'].values:
                print(f"\nSearching for news related to {user_input}...\n")

                news = scrape_news_for_country(user_input)
                
                if news:
                    print(f"Found {len(news)} news articles about {user_input}:\n")
                    for i, news_item in enumerate(news, 1):
                        sentiment = get_sentiment_news(news_item)
                        print(f"News {i}: {news_item}")
                        print(f"Sentiment Score: {sentiment}\n")
                else:
                    print(f"No news found related to {user_input}.\n")
                
                country_row = df[df['Country'] == user_input]
                print("\nHere are the music stats for the country:\n")
                print(country_row.to_string(index=False))
            else:
                print(f"{user_input} is not available in the music data.\n")

access_token_spotify = get_access_token_spotify(spotify_client_id, spotify_client_secret)

playlist_ids = find_country_top_50_playlists(access_token_spotify)

top_songs_and_artists = []
for country, playlist_id in playlist_ids.items():
    if playlist_id:
        top_song, primary_artist, song_popularity = get_top_song_and_artist_in_country(access_token_spotify, playlist_id)
        if top_song and primary_artist:
            top_songs_and_artists.append({
                'Country': country,
                'Song': top_song,
                'Artist': primary_artist,
                'Popularity': song_popularity
            })

df = pd.DataFrame(top_songs_and_artists)

access_token_genius = get_access_token_genius(genius_client_id, genius_client_secret)


df['Lyrics'] = df.apply(lambda row: get_lyrics_url(row['Song'], row['Artist'], access_token_genius), axis=1) #add lyrics URL to the DataFrame

network = pylast.LastFMNetwork(api_key=lastfm_api_key, api_secret=lastfm_api_secret, username=lastfm_username, password_hash=pylast.md5(lastfm_password_hash))

# Add genre and play count to the DataFrame
df[['Genre', 'Play Count']] = df.apply(lambda row: pd.Series(get_lastfm_data(row['Song'], row['Artist'], network)), axis=1)


df['Music Sentiment Score'] = df.apply(lambda row: get_sentiment_from_title_and_genre(row['Song'], row['Genre']), axis=1) #add sentiment score for music

df.to_csv("music_data.csv", index=False) #save the final DataFrame to a CSV

user_interaction(df) #start user interaction
