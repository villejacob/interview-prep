def print_paths(board):
    current_path = []
    final_paths = []

    def dfs(row, col, board, current_path, final_paths):
        rows = len(board)
        cols = len(board[0])
        if row > rows - 1 or col > cols - 1:
            return
        current_path.append(board[row][col])
        if row == rows - 1 and col == cols - 1:
            final_paths.append("".join(current_path))
            current_path.pop()
            return

        dfs(row + 1, col, board, current_path, final_paths)
        dfs(row, col + 1, board, current_path, final_paths)
        current_path.pop()

    dfs(0, 0, board, current_path, final_paths)
    return final_paths

board = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'J', 'K', 'L']]
print print_paths(board)
