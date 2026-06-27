class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++) {
            // if nums[i] is found in map AND iterator is NOT .end()
            // .end() is special iterator type that declares the end of the map (not last element but past the last element)
            if(map.find(nums[i]) != map.end()) {
                if(i - map[nums[i]] <= k) {
                    return true;
                }
            }

            map[nums[i]] = i;
        }
        return false;

    }
};