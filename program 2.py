
def getApplesOranges():
    AmntofApples = int(input("Enter the amount of apples: "))
    AmntofOranges = int(input("Enter the amount of oranges: "))
    return AmntofApples, AmntofOranges

def totalApplesOranges(apples_, oranges_):
    total_apples = int(apples*20)
    total_oranges = int(apples*25)
    return (total_apples, total_oranges)

def totalamount(Apples_, Oranges_):
    total_amount = int(Apples_ + Oranges_)
    return (total_amount)


apples, oranges = getApplesOranges()
Total_ApplesOranges = totalApplesOranges(apples, oranges)