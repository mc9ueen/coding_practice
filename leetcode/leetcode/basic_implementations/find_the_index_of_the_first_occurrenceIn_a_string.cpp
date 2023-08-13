// Given two strings needle and haystack, return the index of the first occurrence
// of needle in haystack, or -1 if needle is not part of haystack.

#include <string>

int strStr(std::string haystack, std::string needle) {
    if (size(haystack) < size(needle)) return -1;
    int haystack_index = 0;
    int needle_index = 0;
    while (haystack_index < size(haystack)) {
        if (haystack[haystack_index] == needle[needle_index]) {
            needle_index++;
        } else {
            haystack_index -= needle_index;
            needle_index = 0;
        }
        if (needle_index == size(needle)) {
            return haystack_index - needle_index + 1;
        }
        haystack_index++;
    }
    return -1;
}
