class Solution {
public:
    bool isHappy(int n) {
        while (n != 1 && n != 4) {
            int sum = 0;
            int x = 0;
            while (n > 0) {
                x = n % 10;
                sum += x * x;
                n /= 10;
            }
            n = sum;
        }
        return n == 1;
    }
};