# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

investment = int(input("what is your investment amount?: "))
interest_rate = int(input("what interest rate do you need?: "))
time = int(input("how many years do you want to invest for?: "))
future_value = (investment*(interest_rate/100)*time)+investment
#cant use f string for complex calculations 
print(future_value )