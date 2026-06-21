class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size() - 1;
        // 9 9 
        digits[n]++;

        // 9,10
        for (int i = n; i >= 0; i--) {
            if (digits[i] == 10 && i-1 < 0) {
                digits[i] = 0;
                digits.insert(digits.begin(), 1);
            }

            if (digits[i] == 10) {
                digits[i-1]++;
                digits[i] = 0;
            }

        }
        return digits;
    }
};