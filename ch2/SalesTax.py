
# 保留小数点后两位的营业税
# prompt the user for input

purchaseAmount = eval(input("enter purchase amount: "))

tax =  purchaseAmount * 0.06

print("sales tax is", int(tax * 100) / 100.0)



