#include <bits/stdc++.h>
#include <iostream>

using namespace std;

// "abcabcbb"
class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    if (s.size() == 1)
      return 1;
    unordered_map<int, int> mp;
    int res = 0;
    int windowStart = 0;
    for (int windowEnd = 0; windowEnd < s.size(); windowEnd++) {
      char ch = s[windowEnd];
      if (mp.find(ch) != mp.end()) {
        windowStart = max(windowStart, mp[ch] + 1);
      }
      res = max(res, windowEnd - windowStart + 1);
      mp[ch] = windowEnd;
    }
    return res;
  }
};

int main() { return 0; }