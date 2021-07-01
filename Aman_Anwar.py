ans = {"1": '1', "2": '1', "3": '60', "4": '25', "5": '217'}
n = 1
a = 0
print("Cos 60 = ?")
print("Tan 45 = ?")
print("360/6 = ?")
print("5 * 5 = ?")
print("210 + 7")
while n < 6:
    k = input()
    if k == ans[str(n)]:
        a += 1
    n += 1
if a == 5:
    print("YOU WIN")
else:
    print("YOU LOSE")
