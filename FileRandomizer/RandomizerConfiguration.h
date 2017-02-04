//Written by Anthony Tesija www.AnthonyTesija.com 

#include <string>
#include <vector>

using std::string;
using std::vector;

class RandomizerConfiguration
{
public:
    string moviesFolder;
    string showsFolder;
    string introsFolder;
    string bumpsFolder;
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
    bool seriesMode;

    RandomizerConfiguration(char* configurationFilepath);

private:
	void SplitStringIntoVector(string stringToSplit, char separator, vector<string>& outputStringList);
};
