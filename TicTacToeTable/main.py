def print_board(board):

	for row in board:
		print("|".join(cell if cell != '' else ' ' for cell in row))
		print("-" * 9)

def check_winner(board, player):

	for row in board:
		if all([cell == player for cell in row]):  # Satır kontrolü
			return True

	for col in range(3):
		if all(board[row][col] == player for row in range(3)):  # Sütun kontrolü
			return True

	if all([board[i][i] == player for i in range(3)]) or all(board[i][2 - i] == player for i in range(3)):
		return True

	return False

def is_full(board):

	return all([cell != '' for row in board for cell in row])

def play_game():

	board = [['' for _ in range(3)] for _ in range(3)]
	current_player = 'X'

	while True:
		print_board(board)
		row = int(input(f"Player {current_player}, satır numarasını girin (0, 1 veya 2): "))
		col = int(input(f"Player {current_player}, sütun numarasını girin (0, 1 veya 2): "))

		if row not in range(3) or col not in range(3):
			print("Geçersiz giriş! Lütfen 0, 1 veya 2 girin.")
			continue

		if board[row][col] == '':
			board[row][col] = current_player
		else:
			print("Bu hücre dolu! Başka bir hücre seçin.")
			continue
        
		if check_winner(board, current_player):
			print_board(board)
			print(f"Player {current_player} kazandı!")
			break
        
		if is_full(board):
			print_board(board)
			print("Berabere!")
			break

			current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
	play_game()
