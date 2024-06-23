# spotify_program.py
# [Your Name], ENDG 233 F23
# A terminal-based application to process and plot data based on given user input and provided data values.
# You may only import numpy, matplotlib, and math. 
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.

import numpy as np
import matplotlib.pyplot as plt

# ******************************************************************************************************
# Data is imported from the included csv file. You may not modify the content, order, or location of the csv file.
# Do not modify the code in this section.
# You may not hardcode (manually enter in the code) any other data.
column_names = ['title', 'artist(s)', 'release', 'num_of_streams', 'bpm', 'key', 'mode', 'danceability', 'valence', 'energy', 'acousticness', 'instrumentalness', 'liveness', 'speechiness']
data = np.genfromtxt('spotify_data.csv', delimiter=',', skip_header=True, dtype=str)
# ******************************************************************************************************

# ******************************************************************************************************
# DEFINE BONUS CLASS HERE (optional)
class Song:
    """
    A class to represent a song with various attributes from the dataset.
    """
    def __init__(self, data_row):
        self.title = data_row[0]
        self.artist = data_row[1]
        self.release = int(data_row[2])
        self.num_of_streams = float(data_row[3])
        self.bpm = float(data_row[4])
        self.key = data_row[5]
        self.mode = data_row[6]
        self.danceability = float(data_row[7])
        self.valence = float(data_row[8])
        self.energy = float(data_row[9])
        self.acousticness = float(data_row[10])
        self.instrumentalness = float(data_row[11])
        self.liveness = float(data_row[12])
        self.speechiness = float(data_row[13])
        self.percentages = [
            self.danceability, self.valence, self.energy, self.acousticness, 
            self.instrumentalness, self.liveness, self.speechiness
        ]

# ******************************************************************************************************
# DEFINE FUNCTIONS HERE

def feature_stats(input_value):
    """
    Calculate and print the highest value, lowest value, and mean value of the desired song feature.
    """
    feature_data = np.array([float(row[input_value]) for row in data], dtype='float')
    highest_value = np.max(feature_data)
    lowest_value = np.min(feature_data)
    mean_value = np.mean(feature_data)
    index_of_highest = np.argmax(feature_data)
    title_of_highest = data[index_of_highest][0]
    
    print(f"Highest value: {highest_value}")
    print(f"Lowest value: {lowest_value}")
    print(f"Mean value: {mean_value:.0f}")
    print(f"Top song in selected feature: {title_of_highest}")

def age_stats(input_value):
    """
    Calculate the total span of release years and print the artist, key, and mode of the oldest song.
    """
    release_years = np.array([int(row[input_value]) for row in data], dtype='int')
    span_of_years = np.max(release_years) - np.min(release_years)
    index_of_oldest = np.argmin(release_years)
    artist_of_oldest = data[index_of_oldest][1]
    key_of_oldest = data[index_of_oldest][5]
    mode_of_oldest = data[index_of_oldest][6]

    print(f"Span of years: {span_of_years}")
    print(f"Artist of oldest song: {artist_of_oldest}")
    print(f"Key and mode of oldest song: {key_of_oldest} {mode_of_oldest}")

# ******************************************************************************************************
# DEFINE MAIN CODE
# Add your code within the main function. A docstring is not required for this function.

def main():
    """
    The main function for the Spotify Statistics program.
    """
    print("ENDG 233 Spotify Statistics\n")
    print("Song analysis options: ")
    for menu, option in enumerate(column_names):
        print(menu, option)

    print("Choose -1 to end the program.")

    # Continue main code below
    while True:
        try:
            user_input = int(input("Please enter a song feature to analyze: "))
        except ValueError:
            print("You must enter a valid menu option")
            continue

        if user_input == -1:
            break
        elif user_input in [0, 1, 5, 6]:
            continue
        elif user_input == 2:
            age_stats(user_input)
        elif user_input in [3, 4, 7, 8, 9, 10, 11, 12, 13]:
            feature_stats(user_input)
        else:
            print("You must enter a valid menu option")

    # Create and print danceability vs. bpm plot
    danceability = np.array([float(row[7]) for row in data], dtype='float')
    bpm = np.array([float(row[4]) for row in data], dtype='float')
    plt.scatter(bpm, danceability)
    plt.title('Danceability vs. BPM')
    plt.xlabel('Beats Per Minute (BPM)')
    plt.ylabel('Danceability')
    plt.grid(True)
    plt.savefig('danceability_vs_bpm.png')
    plt.show()

    # Bonus - Enter any row number
    try:
        bonus_input = int(input("Bonus - Enter any row number: "))
        bonus_song = Song(data[bonus_input])
        plt.bar(range(1, 8), bonus_song.percentages, tick_label=['Danceability', 'Valence', 'Energy', 'Acousticness', 'Instrumentalness', 'Liveness', 'Speechiness'])
        plt.title(f'Bonus Plot - {bonus_song.title} by {bonus_song.artist}')
        plt.xlabel('Song Features')
        plt.ylabel('Percentage')
        plt.show()
    except IndexError:
        print("Invalid row number. Please enter a valid row.")
    except ValueError:
        print("Invalid input. Please enter a valid row number.")

if __name__ == '__main__':
    main()
