"""
Name : Michael Blanco Chavez
interest.py

a simple Python program that asks for input, does arithmetic, and provides output.

Certification of authenticity:

"""
import math

def main() :
    annual_rate = eval(input("what is the the annual interest rate? : ")) #adquired annual interest rate
    days = eval(input("how many days are in the billing month")) # number od fays in billing cycle
    previous_net_balance = eval(input("what is the current net balance? :" )) # net balance
    pay_amount = eval(input("amount of payment? :")) # payment amount
    date_of_month = eval(input("what day of the month was the payment made? : "))# day of the billing cycle in which payment was made


    average_monthly_balance = (previous_net_balance * days) - (pay_amount * (days - date_of_month))
    #print (average_monthly_balance, "this the average daily balance")
    monthly_interest_rate = (annual_rate / 12) * .01
    monthly_interest_charge = average_monthly_balance
    #print(monthly_interest_rate)
    average_daily_balance = average_monthly_balance / days
    monthly_interest = average_daily_balance * monthly_interest_rate
    print("your monthly interest charge is : $", monthly_interest)







if __name__ == '__main__':
    main()