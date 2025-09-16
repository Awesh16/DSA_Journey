// Provided API: bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1, right = n, ans = n;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)) {
                ans = mid;          // mid might be the first bad version
                right = mid - 1;    // check earlier versions
            } else {
                left = mid + 1;     // check later versions
            }
        }
        return ans;
    }
};
