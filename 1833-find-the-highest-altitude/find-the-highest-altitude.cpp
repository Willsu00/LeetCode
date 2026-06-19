class Solution {
public:
    int largestAltitude(vector<int>& gain) {

        int x = 0;
        
        vector<int> alt(gain.size() + 1);
        alt[0] = 0;

        for (int i = 1; i < alt.size(); i++) {
            alt[i] = gain[i-1] + alt[i-1];
        }

        for (int k = 0; k < alt.size(); k++) {
            if (x < alt[k]) {
                x = alt[k];
            }
        }

        return x;

    }
};