#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> map;
        vector<int> intersect;

        for (int j = 0; j < nums1.size(); j++) {
            map[nums1[j]] = 1;
        }

        for (int i = 0; i < nums2.size(); i++) {
            if (map.find(nums2[i]) != map.end()) {
                intersect.push_back(nums2[i]);
                map.erase(nums2[i]);
            }
        }

        return intersect;
    }
};