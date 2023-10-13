#include <bits/stdc++.h>
#include <iostream>

using namespace std;

class Solution {
public:
  bool backspaceCompare(string s, string t) {
    int p1 = s.size() - 1;
    int p2 = t.size() - 1;

    while (p1 >= 0 or p2 >= 0) {
      int back_count;
      if ((p1 >= 0 and s[p1] == '#') or (p2 >= 0 and t[p2] == '#')) {
        if (p1 >= 0 and s[p1] == '#') {
          back_count = 2;
          while (back_count > 0 and p1 >= 0) {
            p1 -= 1;
            back_count -= 1;
            if (p1 >= 0 and s[p1] == '#') {
              back_count += 2;
            }
          }
        }
        if (p2 >= 0 and t[p2] == '#') {
          back_count = 2;
          while (back_count > 0 and p2 >= 0) {
            p2 -= 1;
            back_count -= 1;
            if (p2 >= 0 and t[p2] == '#') {
              back_count += 2;
            }
          }
        }
      } else {
        if (p1 >= 0 and p2 >= 0 and s[p1] == t[p2]) {
          p1--;
          p2--;
        } else if (p1 < 0 and p2 < 0) {
          return true;
        } else {
          return false;
        }
      }
    }
    return true;
  }
};

int main() { return 0; }