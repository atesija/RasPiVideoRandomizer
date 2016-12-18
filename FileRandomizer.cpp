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

const string CONFIG_FILENAME = "FileRandomizer.config";

struct config
{
        bool playMovies;
        bool playShows;
        bool playIntro;
        bool playBumps;
        int minBumps;
        int maxBumps;
        int minShows;
        int maxShows;
};

void ReadConfigFile(config& configuration)
{
        ifstream configFile(CONFIG_FILENAME.c_str());
	string configOption;
	while (getline(configFile, configOption)) 
	{
                if(configOption == "PlayMovies")
                {
                        configFile >> configuration.playMovies;
                }
                else if(configOption == "PlayShows")
                {
                        configFile >> configuration.playShows;
                }
                else if(configOption == "PlayIntro")
                {
                        configFile >> configuration.playIntro;
                }
                else if(configOption == "PlayBumps")
                {
                        configFile >> configuration.playBumps;
                }
                else if(configOption == "MinBumps")
                {
                        configFile >> configuration.minBumps;
                }
                else if(configOption == "MaxBumps")
                {
                        configFile >> configuration.maxBumps;
                        configuration.maxBumps++;
                }
                else if(configOption == "MinShows")
                {
                        configFile >> configuration.minShows;
                }
                else if(configOption == "MaxShows")
                {
                        configFile >> configuration.maxShows;
                        configuration.maxShows++;
                }
	}
        configFile.close();
}

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

int GetRandomNumberBetween(int min, int max)
{
        return (rand() % (max - min)) + min;
}

int main()
{
        config configuration;
        ReadConfigFile(configuration);

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

        if(configuration.playIntro)
        {
             OutputVideosToFile(intros, 1, videoFileOutput);
        }
	while((!shows.empty() && configuration.playShows) || (!movies.empty() && configuration.playMovies))
	{
                if(configuration.playShows)
                {
                        int numberOfShows = GetRandomNumberBetween(configuration.minShows, configuration.maxShows);
                        for(int i = 0; i < numberOfShows; ++i)
                        {
                                OutputVideosToFile(shows, 1, videoFileOutput);
                                if(configuration.playBumps)
                                {
                                        OutputVideosToFile(bumps, GetRandomNumberBetween(configuration.minBumps, configuration.maxBumps), videoFileOutput);
                                }
                        }
                }

                if(configuration.playMovies)
               {
                        OutputVideosToFile(movies, 1, videoFileOutput);
                        if(configuration.playBumps)
                        {
                                OutputVideosToFile(bumps, GetRandomNumberBetween(configuration.minBumps, configuration.maxBumps), videoFileOutput);
                        }
               }
	}

	videoFileOutput.close();
}
