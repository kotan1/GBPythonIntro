revenue = float(input("Enter revenue: "))
expenses = float(input("Enter expenses: "))
profit = revenue - expenses

if(profit > 0):
    print("profit")
    print("profitability is %f" % (profit / revenue))
    emp = int(input("Enter number of employees: "))
    print("profit per employee is %f" % (profit / emp))
elif(profit < 0):
    print("loss")