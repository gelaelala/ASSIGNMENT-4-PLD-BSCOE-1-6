
def getApplesOranges():
    AmntofApples = int(input("Enter the amount of apples: "))
    AmntofOranges = int(input("Enter the amount of oranges: "))
    return AmntofApples, AmntofOranges

def totalApplesOranges(apples_, oranges_):
    total_apples = int(apples*20)
    total_oranges = int(oranges*25)
    total_amount = int(total_apples + total_oranges)
    return (total_amount)

def display(total_):
    print(f'The total amount is {total_}.')

apples, oranges = getApplesOranges()

Total = totalApplesOranges(apples, oranges)

display(Total)