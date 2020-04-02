# Author:
# Date:
# Description:

# Single string containing CSV formatted song data
#  "artist,album,title,duration"
#  Note: Duration is specified in seconds
#
single_song = "Jimmy Buffett,Songs You Know by Heart,Cheeseburger in Paradise,172"

#
# List of strings containing CSV formatted song data
#
songs = ['Jimmy Buffett,Songs You Know by Heart,Cheeseburger in Paradise,172', 
            'Jimmy Buffett,Songs You Know by Heart,He Went to Paris,209',
            'Jimmy Buffett,Songs You Know by Heart,Fins,205',
            'Jimmy Buffett,Songs You Know by Heart,Son of a Son of a Sailor,205',
            'Jimmy Buffett,Songs You Know by Heart,A Pirate Looks at Forty,232',
            'Jimmy Buffett,Songs You Know by Heart,Margaritaville,251',
            'Jimmy Buffett,Songs You Know by Heart,Come Monday,189',
            'Jimmy Buffett,Songs You Know by Heart,Changes in Latitudes Changes in Attitudes,195',
            "Jimmy Buffett,Songs You Know by Heart,Why Don't We Get Drunk,162",
            'Jimmy Buffett,Songs You Know by Heart,Pencil Thin Mustache,170',
            'Jimmy Buffett,Songs You Know by Heart,Grapefruit-Juicy Fruit,176',
            'Jimmy Buffett,Songs You Know by Heart,Boat Drinks,157',
            'Jimmy Buffett,Songs You Know by Heart,Volcano,218']

def print_song(song):
    """Displays a nicely formatted song details for a string provided in the following format: Artist,Album,Title,Duration"""
    pass

def print_songs(song_list):
    pass

def read_songs(data_file):
    return ""

print_song(single_song)
print_songs(songs)
file_songs = read_songs('music_collection.csv')
print_songs(file_songs)