#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>

using namespace std;

const string MOVIE_FILENAME = "movies.txt";
const string SERIES_FILENAME = "series.txt";
const string INTROS_FILENAME = "intros.txt";
const string BETWEEN_FILENAME = "between.txt";

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
        vector<string> series;
        vector<string> intros;
        vector<string> between;

        ReadFileIntoVector(MOVIE_FILENAME, movies);
        ReadFileIntoVector(SERIES_FILENAME, series);
        ReadFileIntoVector(INTROS_FILENAME, intros);
        ReadFileIntoVector(BETWEEN_FILENAME, between);

	srand(time(NULL));
        ShuffleVideos(movies);
        ShuffleVideos(series);
        ShuffleVideos(intros);
        ShuffleVideos(between);

	ofstream videoFileOutput(VIDEO_OUTPUT_FILENAME.c_str());

        OutputVideosToFile(intros, 1, videoFileOutput);
	while(!series.empty() || !movies.empty())
	{
                OutputVideosToFile(series, rand() % 10 + 5, videoFileOutput);
                OutputVideosToFile(between, rand() % 3, videoFileOutput);
                OutputVideosToFile(movies, 1, videoFileOutput);
                OutputVideosToFile(between, rand() % 3, videoFileOutput);
	}

	videoFileOutput.close();
}
