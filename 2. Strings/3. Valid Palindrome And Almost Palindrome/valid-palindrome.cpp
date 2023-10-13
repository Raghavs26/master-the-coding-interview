#include <bits/stdc++.h>
#include <iostream>

using namespace std;

class Solution {
public:
  bool isPalindrome(string s) {
    int i = 0;
    int j = s.length() - 1;

    while (i <= j) {
      if (!isalnum(s[i]) || s[i] == ' ') {
        i++;
      } else if (!isalnum(s[j]) || s[j] == ' ') {
        j--;
      } else if (tolower(s[i]) != tolower(s[j])) {
        return false;
      } else {
        i++;
        j--;
      }
    }

    return true;
  }
};

int main() { return 0; }