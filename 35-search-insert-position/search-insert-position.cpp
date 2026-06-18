#include <algorithm>

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == target){
                return i;
            }
        }

        if (nums[nums.size() - 1] < target) {
            return nums.size();
        } 

        for (int j = 0; j < nums.size(); j++) {
            if (nums[j] > target) {
                return j;
            }
            
        }
        return 0;

        

    }
};