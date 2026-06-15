#include <iostream>

class Solution {
public:
    bool isPalindrome(string s) {
        string str = "";
        for (int i = 0; i < s.size(); i++){
            if (isalnum(s[i])){
                str += tolower(s[i]);
            }
        }
        string st = str;
        reverse(str.begin(), str.end());
        if (str == st){
            return true;
        }
       return 0;
    }
};