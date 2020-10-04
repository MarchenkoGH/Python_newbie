import json
import datetime


def duration_tracks():
    with open('acdc.json') as file:
        songs = json.load(file)
        duration_dict = [int(track['duration']) for track in songs['album']['tracks']['track']]
        all_songs_duration_in_sec = sum(duration_dict)
        total_time = datetime.timedelta(seconds=all_songs_duration_in_sec)
        return total_time


print(duration_tracks())
