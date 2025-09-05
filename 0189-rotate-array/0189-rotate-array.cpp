class Solution {
public:
    void rotate(vector<int>& vec, int k) {
        int n = vec.size();
        k = k % n;
        reverse(vec.begin(), vec.end() - k);
        reverse(vec.end() - k, vec.end());
        reverse(vec.begin(), vec.end());
    }
};
