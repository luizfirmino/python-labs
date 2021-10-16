#
# Luiz Filho
# 3/14/2021
# Module 5 Assignment
# 8. The Doubling Time formula below is used in Finance to calculate the length of time required to double an investment or money in an interest bearing account.  
#
# If one wishes to calculate the amount of time to double their money in a money market account that is compounded monthly, then r needs to express the monthly rate and not the annual rate. The monthly rate can be found by dividing the annual rate by 12. With this situation, the doubling time formula will give the number of months that it takes to double money and not years  (Please use monthly rate for 8a - 8c)
#
# a. Marc wants to determine how long it would take to double the money in his money market 
# account in BMO Harris Bank in 2020. BMO offers a 1.85% APR, which is compounded monthly.  How long would it take Marc to double his money by investing with BMO? Please round to 1 decimal place. (You can use the figure above to check your answer). 
#
# b. Write a lambda function (doubling_time_yrs) that returns the time it will take to 
# double his money in years. Use math.log10(a) to get the base-10 logarithm of a number in the formula.
#
# c. According to your ACME broker The 10-year average annual return on the S&P 500, ending 
# in 2018 and including dividends, is around 10%. However your ACME broker is recommending 
# that you open a money market account since stock market volatility is high 
# (understanding you will experience down years as well as up years - no guarantees). 
# How long would it take Marc to double his money (in years) if he invests in a money 
# market account that will compound monthly and earn him 3% per year ? You can use the 
# figure above to check your answer (round to 1 decimal place)
# 

def doubleMoneyTime(amount, rate):
    year = 0
    total = amount

    while total <= amount * 2 :
        total = total + total * (rate)/100
        year = year + 1
    return year

print(doubleMoneyTime(1000, 14))


doubling_time_yrs = lambda amount, rate: doubleMoneyTime(amount, rate)
print(doubling_time_yrs(15000, 2.5))


doubling_time_yrs = lambda amount, rate: doubleMoneyTime(amount, rate)
print(doubling_time_yrs(5000, 3))

