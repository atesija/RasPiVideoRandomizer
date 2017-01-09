//Written by Anthony Tesija www.AnthonyTesija.com 

#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>

#include "RandomizerConfiguration.h"

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

int GetRandomNumberBetween(int min, int max)
{
    return (rand() % (max - min)) + min;
}

void WhitelistVideos(vector<string>& whitelist, vector<string>& videos)
{
    if(whitelist.empty() || videos.empty())
    {
        return;
    }
    
    vector<string> prunedVideos;
    for(int videoIndex = 0; videoIndex < videos.size(); ++videoIndex)
    {
        for(int i = 0; i < whitelist.size(); ++i)
        {
            if (videos[videoIndex].find(whitelist[i]) != std::string::npos)
            {
                prunedVideos.push_back(videos[videoIndex]);
                break;
            }
        }
    }
    
    videos = prunedVideos;
}

void BlacklistVideos(vector<string>& blacklist, vector<string>& videos)
{
    if(blacklist.empty() || videos.empty())
    {
        return;
    }
    
    vector<string> prunedVideos;
    for(int videoIndex = 0; videoIndex < videos.size(); ++videoIndex)
    {
        bool videoBlacklisted = false;
        for(int i = 0; i < blacklist.size(); ++i)
        {
            if (videos[videoIndex].find(blacklist[i]) != std::string::npos)
            {
                videoBlacklisted = true;
                break;
            }
        }
        if(!videoBlacklisted)
        {
            prunedVideos.push_back(videos[videoIndex]);
        }
    }
    
    videos = prunedVideos;
}

string GetVideoSeries(string fullVideoPath, string seriesLocation)
{
    string videoSeries = fullVideoPath;
    videoSeries.erase(0, seriesLocation.size());
    //videoSeries.erase(videoSeries.rend(), std::find_if(videoSeries.rend(), videoSeries.rbegin(), std::bind1st(std::not_equal_to<char>(), '/')));
    return videoSeries;
}

void ShuffleVideosInSeries(vector<string>& videoContainer, string seriesLocation)
{
    vector< vector<string> > allVideoSeries;
    string lastSeries;
    int videoIndex = 0;
    while(videoIndex < videoContainer.size())
    {
        vector<string> videoSeries;

        cout << GetVideoSeries(videoContainer[videoIndex], seriesLocation);

        if(!videoSeries.empty())
        {
            allVideoSeries.push_back(videoSeries);
        }
        ++videoIndex;
    }
}

int main()
{        
    RandomizerConfiguration configuration;
    
    vector<string> movies;
    vector<string> shows;
    vector<string> intros;
    vector<string> bumps;

    ReadFileIntoVector(MOVIE_FILENAME, movies);
    ReadFileIntoVector(SHOWS_FILENAME, shows);
    ReadFileIntoVector(INTROS_FILENAME, intros);
    ReadFileIntoVector(BUMPS_FILENAME, bumps);
    
    WhitelistVideos(configuration.whitelist, shows);
    WhitelistVideos(configuration.whitelist, movies);
    BlacklistVideos(configuration.blacklist, shows);
    BlacklistVideos(configuration.blacklist, movies);

	srand(time(NULL));

    if(configuration.seriesMode)
    {
        ShuffleVideosInSeries(movies, configuration.moviesFolder);
        ShuffleVideosInSeries(shows, configuration.showsFolder);
    }
    else
    {
        ShuffleVideos(movies);
        ShuffleVideos(shows);
    }
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