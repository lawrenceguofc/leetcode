class Solution:
    def isValidSudoku(self, board):
        rows = [{} for i in range(9)]
        cols = [{} for i in range(9)]
        boxes = [{} for i in range(9)]
        # rowwise
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i][board[i][j]] = rows[i].get(board[i][j],0) + 1
                    cols[j][board[i][j]] = cols[j].get(board[i][j],0) + 1
                    box_index = 3 * (i//3) + (j//3)
                    boxes[box_index][board[i][j]] = boxes[box_index].get(board[i][j],0) + 1
                    if rows[i][board[i][j]] > 1 or cols[j][board[i][j]] > 1 or boxes[box_index][board[i][j]] > 1:
                        return False
        return True

def main():
    b = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]
    s= Solution()
    print(s.isValidSudoku(b))

if __name__ == "__main__":
    main()
