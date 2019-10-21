class Solution {
    public int game(int[] guess, int[] answer) {
        int nums[] = {0,1,2};
        int count = 0;
        for (int num : nums) {
            int a = guess[num];
            int b = answer[num];
            if (a == b) {
                count++;
            }
        }    
        return count;
    }
}