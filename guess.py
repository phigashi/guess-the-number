import random

number = random.randint(1, 100)

userInput = None
maxAttempt = 10

for count in range(1, maxAttempt + 1):
    try:
        userInput = int(input(f"{count}/10 : 1 ~ 100 の間で数字を選んでください： "))
    except ValueError:
        print("整数のみ入力してください。一回分消費しました。")
        continue

    if userInput > number:
        print("もっと小さい数字です")
    elif userInput < number:
        print("もっと大きい数字です")
    else:
        print(f"正解 {count} 回で当てました")
        break
else:
    print (f"ゲームオーバー！正解は {number} でした")