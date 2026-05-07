class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (int a : nums){
            if (seen.count(a)) return true;
            seen.insert(a);
        }       
        return false;
    }
};