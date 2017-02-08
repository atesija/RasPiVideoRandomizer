//Written by Anthony Tesija www.AnthonyTesija.com 

#include <sstream>
#include <fstream>
#include <algorithm>

#include "RandomizerConfiguration.h"

using std::stringstream;
using std::ifstream;

RandomizerConfiguration::RandomizerConfiguration(char* configurationFilepath)
{
    ifstream configFile(configurationFilepath);
	string configOption;
	while (getline(configFile, configOption)) 
	{
        if(configOption == "MoviesFolder")
        {
            configFile >> moviesFolder;
        }
        else if(configOption == "ShowsFolder")
        {
            configFile >> showsFolder;
        }
        else if(configOption == "IntrosFolder")
        {
            configFile >> introsFolder;
        }
        else if(configOption == "BumpsFolder")
        {
            configFile >> bumpsFolder;
        }
        else if(configOption == "PlayMovies")
        {
            configFile >> playMovies;
        }
        else if(configOption == "PlayShows")
        {
            configFile >> playShows;
        }
        else if(configOption == "PlayIntro")
        {
            configFile >> playIntro;
        }
        else if(configOption == "PlayBumps")
        {
            configFile >> playBumps;
        }
        else if(configOption == "MinBumps")
        {
            configFile >> minBumps;
        }
        else if(configOption == "MaxBumps")
        {
            configFile >> maxBumps;
        }
        else if(configOption == "MinShows")
        {
            configFile >> minShows;
        }
        else if(configOption == "MaxShows")
        {
            configFile >> maxShows;
        }
        else if(configOption == "Whitelist")
        {
            string whitelistNames;
            getline(configFile, whitelistNames);
            if(whitelistNames.find("//") == string::npos)
            {
                    SplitStringIntoVector(whitelistNames, ',', whitelist);
            }
        }
        else if(configOption == "Blacklist")
        {
            string blacklistNames;
            getline(configFile, blacklistNames);
            if(blacklistNames.find("//") == string::npos)
            {
                    SplitStringIntoVector(blacklistNames, ',', blacklist);
            }
        }
        else if(configOption == "Series")
        {
            configFile >> seriesMode;
        }
        else if(configOption == "CustomBumpsPercent")
        {
            configFile >> customBumpsPercent;
        }
	}
    configFile.close();
}

void RandomizerConfiguration::SplitStringIntoVector(string stringToSplit, char separator, vector<string>& outputStringList)
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
