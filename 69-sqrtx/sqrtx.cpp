class Solution {
public:
    int mySqrt(int x) {

        int left = 1;
        int right = x;
        int n = 0;

        if (x==0 || x==1) {
            return x;
        }

        while (left <= right) {
            long long mid = left + (right - left) / 2;

            if (mid * mid <= x) {
                n = mid;
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }

        return n;

    }
};