import os

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def clear_screen():
    """Terminal ekranını temizler (Windows için cls, macOS/Linux için clear)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_table():
    """
    Oyun tahtasının güncel durumunu ekrana yazdırır.
    Listeyi 3x3'lük bir ızgara (grid) şeklinde formatlar.
    """
    for i in range(0, 9, 3):
        print(board[i], board[i + 1], board[i + 2])


def choose(current_player):
    """
    Sırası gelen oyuncudan (X veya O) pozisyon seçmesini ister.
    Girilen değerin geçerliliğini (1-9 arası) ve seçilen konumun boş olup olmadığını kontrol eder.
    Harf girilmesi gibi hataları (ValueError) yakalar.
    """
    while True:
        try:
            position = int(input(f"Player {current_player}, enter position (1-9): "))

            if position not in range(1, 10):
                print("Invalid position, choose between 1 and 9.")
                continue

            if board[position - 1] in ('X', 'O'):
                print("This position is already taken, try another one.")
                continue

            board[position - 1] = current_player
            clear_screen()
            show_table()
            break
        except ValueError:
            print("Invalid input! Please enter a number.")


def play():
    """
    Ana oyun döngüsünü yönetir.
    Kazanma koşullarını ve beraberlik durumunu kontrol eder.
    Oyun bitiminde tekrar oynama seçeneği sunar.
    """
    global board
    playlist = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']

    while True:
        count = 0
        win_condition = False
        clear_screen()
        show_table()

        for current_player in playlist:
            choose(current_player)
            print('\n')

            # Kazanma durumu kontrolü
            if (board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8]
                    or board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] ==
                    board[8]
                    or board[0] == board[4] == board[8] or board[2] == board[4] == board[6]):
                print(f"Player {current_player} won!")
                win_condition = True
                break

            count += 1

        # Beraberlik durumu kontrolü (9 hamle dolduysa ve kazanan yoksa)
        if count == 9 and not win_condition:
            print("It's a draw!")

        play_choose = input('Do you want to play again? (Y or N): ').upper()
        if play_choose == 'Y':
            board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        else:
            print("Thanks for playing!")
            break

# Bu dosya doğrudan çalıştırıldığında oyunu başlatır.
# Başka bir dosyaya modül olarak aktarıldığında (import) otomatik çalışmasını engeller.
# Sadece 'play()' yazsaydık bu dosyayı başka bir yere import ettiğimizde otomatik olarak çalışırdı.
if __name__ == "__main__":
    play()