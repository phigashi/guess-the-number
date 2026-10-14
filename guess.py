import random

number = random.randint(1, 100)

userInput = None

count = 0

while number != userInput:
    userInput = int(input("1 ~ 100 の間で数字を選んでください： "))
    count += 1

    if userInput > number:
        print("もっと小さい数字です")
    elif userInput < number:
        print("もっと大きい数字です")
    else:
        print("正解 ", count, " 回で当てました")