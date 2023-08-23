// You are given two strings word1 and word2.
// Merge the strings by adding letters in alternating order, starting with word1.
// If a string is longer than the other, append the additional letters onto the end of the merged string.
// Return the merged

#include <string>

using namespace std;


void addRest(int &pointer, std::string &word, std::string &result) {
    while (pointer < size(word)) {
        result.push_back(word[pointer]);
        pointer++;
    }
}

std::string mergeAlternately(std::string word1, std::string word2) {
    std::string result = "";
    int first_pointer = 0;
    int second_pointer = 0;
    while (first_pointer < size(word1) && second_pointer < size(word2)) {
        result.push_back(word1[first_pointer]);
        result.push_back(word2[second_pointer]);
        first_pointer++;
        second_pointer++;
    }
    if (first_pointer == size(word1)) {
        addRest(second_pointer, word2, result);
    }
    if (second_pointer == size(word2)) {
        addRest(first_pointer, word1, result);
    }
    return result;
}
