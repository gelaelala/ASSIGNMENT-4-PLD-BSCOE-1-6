def getMoneyPriceofapple():
    Money = int(input("Enter the amount of money: "))
    PriceofApple = int(input("Enter the price of the apple: "))
    numberofapples = int(Money/PriceofApple)
    return Money, PriceofApple, numberofapples

def totalandchange(numberofapples_, money_, priceofapple_):
    total = int(numberofapples_*priceofapple_)
    change = int(money_ - total)
    return change

def display(Numberofapples, change_):
    print (f'You can buy {Numberofapples} apples and your change is {change_} pesos.')

money, priceofapple, numberofapples = getMoneyPriceofapple()

totalandchange_ = totalandchange(numberofapples, money, priceofapple)

display(numberofapples, totalandchange_)