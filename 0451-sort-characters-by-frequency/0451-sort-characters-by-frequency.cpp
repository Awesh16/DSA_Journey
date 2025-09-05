class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }

        // Max heap to sort by frequency
        priority_queue<pair<int, char>> pq;
        for (auto& p : freq) {
            pq.push({p.second, p.first});
        }

        string result;
        while (!pq.empty()) {
            auto [count, ch] = pq.top();
            pq.pop();
            result.append(count, ch);  // Append character count times
        }
        return result;
    }
};
