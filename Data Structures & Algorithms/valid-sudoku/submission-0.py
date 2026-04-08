class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        boxes = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                box = (i // 3) * 3 + (j // 3)

                if num and num != ".":
                    if j in col and num in col[j]:
                        return False
                    if i in row and num in row[i]:
                        return False
                    if box in boxes and num in boxes[box]:
                        return False                       

                    if i in row: 
                        row[i].append(num)
                    else:
                        row[i] = [num]
                    if j in col: 
                        col[j].append(num)
                    else:
                        col[j] = [num]
                    if box in boxes: 
                       boxes[box].append(num)
                    else:
                        boxes[box] = [num]
                    

        
        return True