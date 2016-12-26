//Written by Anthony Tesija www.AnthonyTesija.com 

#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
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
        vector<string> whitelist;
        vector<string> blacklist;
};

void SplitStringIntoVector(string stringToSplit, char separator, vector<string>& outputStringList)
{
        stringstream stream(stringToSplit);
        string split;
        while(getline(stream, split, separator))
        {
                if(!split.empty())
                {
                        //Remove leading whitespace
                        split.erase(split.begin(), std::find_if(split.begin(), split.end(), std::bind1st(std::not_equal_to<char>(), ' ')));
                        outputStringList.push_back(split);
                }
        }
}

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
                else if(configOption == "Whitelist")
                {
                        string whitelistNames;
                        getline(configFile, whitelistNames);
                        if(whitelistNames.find("//") == string::npos)
                        {
                                SplitStringIntoVector(whitelistNames, ',', configuration.whitelist);
                        }
                }
                else if(configOption == "Blacklist")
                {
                        string blacklistNames;
                        getline(configFile, blacklistNames);
                        if(blacklistNames.find("//") == string::npos)
                        {
                                SplitStringIntoVector(blacklistNames, ',', configuration.blacklist);
                        }
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
        
        WhitelistVideos(configuration.whitelist, shows);
        WhitelistVideos(configuration.whitelist, movies);
        BlacklistVideos(configuration.blacklist, shows);
        BlacklistVideos(configuration.blacklist, movies);

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
