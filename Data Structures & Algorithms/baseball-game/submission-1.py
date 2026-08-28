class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoreStack = []
        finalScore = 0

        for ele in operations:
            score = 0
            
            if (ele == "+"):
                score = scoreStack[-1] + scoreStack[-2]
                scoreStack.append(score)

            elif (ele == "C"):
                scoreStack.pop()
            

            elif (ele == "D"):
                score = scoreStack[-1]*2
                scoreStack.append(score)

            else:
                score = int(ele)
                scoreStack.append(score)
            print(scoreStack)
        
        for score in scoreStack:
            finalScore = score + finalScore
        
        return finalScore