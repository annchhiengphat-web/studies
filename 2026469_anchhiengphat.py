# average score
def calculate_average():
    score1 = int(input("Enter your first score: "))
    score2 = int(input("Enter your second score: "))
    score3 = int(input("Enter your third score: "))
    score4 = int(input("Enter your fourth score: "))
    score5 = int(input("Enter your fifth score: "))
    score6 = int(input("Enter your sixth score: "))
    return score1 + score2 + score3 + score4 + score5 + score6
x = calculate_average()/6
print("your average score is", x)

# multiplication table
def multiplication_table():
    number = int(input("Enter a number: "))
    for i in range(1,11):
        result = i * number
        if result % 2 == 0:
             print(f"{number} x {i} = {i * number} (even)")
        else:
            print(f"{number} x {i} = {i * number} (odd)")
multiplication_table()



