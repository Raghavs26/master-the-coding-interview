#include <iostream>
#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> mp;
        for (int i = 0; i < nums.size(); i++)
        {
            int numToFind = target - nums[i];
            if(mp.find(numToFind) != mp.end()){
                return vector<int>{mp[numToFind],i};
            }else{
                mp[nums[i]] = i;
            }
        }
        return vector<int>{-1,-1};
    }
};

int main()
{
    return 0;
}