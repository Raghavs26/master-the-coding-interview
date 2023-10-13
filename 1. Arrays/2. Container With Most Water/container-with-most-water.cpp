#include <iostream>
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int p1=0, p2=n-1;
        int area = 0;
        while(p1 <= p2){
            int width = p2 - p1;
            int currentArea = min(height[p1],height[p2]) * width;
            if(height[p1] > height[p2]){
                p2 -= 1;
            }else{
                p1 += 1;
            }
            area = max(area,currentArea);
        }      
        return area;
    }
};

int main()
{
    return 0;
}