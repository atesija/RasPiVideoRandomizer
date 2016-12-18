#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>

using namespace std;

const string MOVIE_FILENAME = "movies.txt";
const string SHOWS_FILENAME = "shows.txt";
const string INTROS_FILENAME = "intros.txt";
const string BUMPS_FILENAME = "bumps.txt";

const string VIDEO_OUTPUT_FILENAME = "videos.txt";

void ReadFileIntoVector(string filename, vector<string>& fileHolder)
{
	ifstream videoFileInput;
 	videoFileInput.open(filename.c_str());

	string videoFile;
	while (getline(videoFileInput, videoFile)) 
	{
		fileHolder.insert(fileHolder.begin(), videoFile);
	}

	videoFileInput.close();
}

void ShuffleVideos(vector<string>& videoContainer)
{
	random_shuffle(videoContainer.begin(), videoContainer.end());
}

void OutputVideosToFile(vector<string>& videosFrom, int numberOfVideos, ofstream& outputFile)
{
        for(int i = 0; i < numberOfVideos; ++i)
        {
                if(!videosFrom.empty())
                {
		        outputFile << videosFrom.back() << endl;
		        videosFrom.pop_back();
                }
        }
}

int main()
{
        vector<string> movies;
        vector<string> shows;
        vector<string> intros;
        vector<string> bumps;

        ReadFileIntoVector(MOVIE_FILENAME, movies);
        ReadFileIntoVector(SHOWS_FILENAME, shows);
        ReadFileIntoVector(INTROS_FILENAME, intros);
        ReadFileIntoVector(BUMPS_FILENAME, bumps);

	srand(time(NULL));
        ShuffleVideos(movies);
        ShuffleVideos(shows);
        ShuffleVideos(intros);
        ShuffleVideos(bumps);

	ofstream videoFileOutput(VIDEO_OUTPUT_FILENAME.c_str());

        OutputVideosToFile(intros, 1, videoFileOutput);
	while(!shows.empty() || !movies.empty())
	{
                int numberOfShows= rand() % 10 + 5;
                for(int i = 0; i < numberOfShows; ++i)
                {
                        OutputVideosToFile(shows, 1, videoFileOutput);
                        OutputVideosToFile(bumps, rand() % 3, videoFileOutput);
                }
                OutputVideosToFile(movies, 1, videoFileOutput);
                OutputVideosToFile(bumps, rand() % 3, videoFileOutput);
	}

	videoFileOutput.close();
}
