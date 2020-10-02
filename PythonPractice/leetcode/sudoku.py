def getThreebyThree(board):
    newlist = []
    newFirstlist=[]
    newSecondlist=[]
    newThirdlist=[]
    for l in range(len(board)):
        for i in range(0, 3):
            newFirstlist.append(board[l][i])
        for i in range(3, 6):
            newSecondlist.append(board[l][i])
        for i in range(6, 9):
            newThirdlist.append(board[l][i])
        if l % 3 == 2:
            newlist.append(newFirstlist)
            newlist.append(newSecondlist)
            newlist.append(newThirdlist)
    return newlist

input = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

output = getThreebyThree(input)
print(output)