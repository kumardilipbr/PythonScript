'''
import pyjokes
import speech_recognition as sr
a = pyjokes.get_joke()
print(a)
'''
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="1a3924998ce945939c497e3c3b8fd720",
                                                           client_secret="228466d2b6bd4b0180bc4ebaa6879fe1"))
#results = sp.search(q='weezer', limit=20)
#for idx, track in enumerate(results['tracks']['items']):
#    print(idx, track['name'])
'''
# This shows the Top 10 tracks
birdy_uri1 = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
results = spotify.artist_albums(birdy_uri1, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
'''
'''
# shows top 10 Tracks, their Audio URL, The Cover Art URL
birdy_uri2 = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

results = spotify.artist_top_tracks(birdy_uri2)
#print(results)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
'''
#birdy_uri3 = 'spotify:track:6VaWHjTTcKiPjWEkejHkMR'
#   https://open.spotify.com/album/63qOqv2FOkfpIUs2SKEuH6?si=BInNsiFVTaWJrBzhotVlRw

# Prints the songs in the album
birdy_uri4 = 'spotify:album:63qOqv2FOkfpIUs2SKEuH6'
#results = spotify.artist_top_tracks(birdy_uri2)
#results = spotify.artist_top_tracks(birdy_uri4)
#results = spotify.album_tracks(birdy_uri4)
results = spotify.start_playback(birdy_uri4)
#print(results)
for track in results['items'][:10]:
    #start_playback(track)
    print('track_Name     : ' + track['name'])
    print('track_URL     : ' + track['preview_url'])

'''
# Prints the songs in the playlist
birdy_uri5 = 'spotify:playlist:37i9dQZF1DXcEKFjZJYZcc'

results = spotify.playlist_items(birdy_uri5)
print(results)
#for track in results['name'][:10]:
#    print('track_Name     : ' + track['name'])
#   # print('track_URL     : ' + track['external_urls'])
'''