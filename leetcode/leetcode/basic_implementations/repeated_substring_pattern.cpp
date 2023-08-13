// Given a string s, check if it can be constructed by taking a substring of it
// and appending multiple copies of the substring together.

#include <stdio.h>
#include <string>
#include <iostream>

bool repeated_substring_pattern(std::string s) {
    int s_length = s.length();
    for (unsigned int i = 1; i <= s_length / 2; i++) {
        if (s_length % i == 0) {
            std::string pattern = "";
            for (unsigned int j = 0; j < s_length / 2; j) {
                pattern += s.substr(0, i);
            }
            if (s == pattern) return true;
        }
    }
    return false;
}
int main() {
    std::cout << (repeated_substring_pattern("abaa") ? "true" : "false") << std::endl;
    return 0;
}
