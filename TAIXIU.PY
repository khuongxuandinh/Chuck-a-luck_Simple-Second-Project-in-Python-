from random import randint 
total = 500
def generate_dices():
    x1 = randint(1,6)
    x2 = randint(1,6)
    x3 = randint(1,6)
    return (x1,x2,x3)
def intro():
    print('Ở Tài Xỉu online, bạn sẽ nhận được 500k khởi đầu! \n ----------')
    print('Sẽ có 3 xúc sắc mỗi xúc sắc có giá trị từ 1-->6 và có tổng 3 viên từ 3 đến 18. \n ---------')
    print('Xỉu sẽ nằm trong khoảng từ 3-10 \nTài nằm trong khoảng từ 11-->18\n----------')
    print('Nếu bạn chọn đúng Tài hoặc Xỉu theo như kết quả, số tiền bạn cược sẽ nhận được gấp đôi')
    print('Nếu không bạn sẽ mất TRẮNG số tiền cược!')
    print('Nếu bạn chọn Xỉu và kết quả ra (1,1,1) bạn nhận được gấp 10 số tiền cược')
    print('Nếu bạn chọn Tài và kết quả ra (6,6,6) bạn nhận được gấp 10 số tiền cược\n-----------')
def init():
    global total
    bet = input('Đặt số tiền bạn cược(nhập số vào bàn phím nhé): ')
    while bet.isalpha() or (bet.isnumeric() and int(bet) > total):
        bet = input('Vui lòng nhập một số tiền hợp lệ nhỏ hơn số tiền hiện tại: ')
    bet = int(bet)
    choice = input('Chọn Tài(t) hoặc Xỉu(x): ').lower()
    while choice not in ('tài','t','x','xỉu'):
        choice = input('Vui lòng chỉ nhập "tài(t)" hoặc "xỉu(x)": ').lower()
    return bet, choice
def start():
    global total
    print('Chào mừng mọi người đến với trò chơi tài xỉu online code bởi khuongxuandinh and alphazero-wd \n --------')
    intro()
    while total > 0:
        begin = input('Bạn đã sẵn sàng chơi chưa? Chọn rồi(r) hoặc chưa(c): ').lower()
        while begin not in ['rồi', 'r', 'chưa', 'c']:
            begin = input('Vui lòng nhập "rồi (r)" hay "chưa (c)": ').lower()
        if begin in ('rồi', 'r'):
            bet, choice = init()
            sum_money(choice, bet)
            print('----------')
        elif begin in ('chưa', 'c'):
            print('Tiếc quá!! Vậy thì gặp bạn lần sau nhé!')
            exit() 
def sum_money(choice, bet):
    global total
    dices = generate_dices()
    dices_sum = sum(dices)
    print(f'Hũ nổ được: {dices} với tổng là: {dices_sum}')
    if choice[0] == 'x':
        if dices_sum == 3:
            total += bet * 10
            print(f'Bạn đã thắng gấp 10 lần rồi: {bet * 10}')
        elif dices_sum in range(4, 11): 
            total += bet
            print(f'Bạn đã thắng được: {bet * 2}')
        elif dices_sum > 10:
            total -= bet
            print('Tiếc quá. Bạn thua rồi')
    if choice[0] == 't':
        if dices_sum == 18:
            total += bet * 10
            print(f'Bạn đã thắng gấp 10 lần rồi: {bet * 10}')
        elif dices_sum in range(11, 18): 
            total += bet
            print(f'Bạn đã thắng được: {bet}')
        elif dices_sum <= 10:
            total -= bet
            print('Tiếc quá. Bạn thua rồi')
    print(f'Số tiền hiện tại của bạn là: {total}')
start()