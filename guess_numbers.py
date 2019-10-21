class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        count = 0;
        for num in range(0,3):
            if guess[num] == answer[num]:
                count+=1
        return count