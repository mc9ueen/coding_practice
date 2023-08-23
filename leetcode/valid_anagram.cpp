// Given two strings s and t, return true if t is an anagram of s, and false otherwise.
//
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
// typically using all the original letters exactly once.
//

#include <string>
#include <map>

bool is_anagram(std::string s, std::string t) {
    if (size(s) != size(t)) return false;

    std::map<char, int> s_map;
    std::map<char, int> t_map;

    for (unsigned int i = 0; i < size(s); i++) {
        ++s_map[s[i]];
    }
    for (unsigned int j = 0; j < size(t); j++) {
        ++t_map[t[j]];
    }
    
    return s_map == t_map ? true : false;
}
