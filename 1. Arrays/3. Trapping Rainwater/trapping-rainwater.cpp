#include <bits/stdc++.h>
#include <iostream>

using namespace std;

class Solution {
public:
  int trap(vector<int> &height) {
    int n = height.size(), totalWater = 0;
    int left = 0, right = n - 1;
    int maxLeft = 0, maxRight = 0;
    while (left <= right) {
      if (height[left] <= height[right]) {
        if (height[left] > maxLeft) {
          maxLeft = height[left];
        } else {
          totalWater += (maxLeft - height[left]);
        }
        left += 1;
      } else {
        if (height[right] > maxRight) {
          maxRight = height[right];
        } else {
          totalWater += (maxRight - height[right]);
        }
        right -= 1;
      }
    }
    return totalWater;
  }
};

int main() { return 0; }