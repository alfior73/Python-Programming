######################################
# Creator: Alfio Raymond
# Date: 18 Jan 2023
#
# Exercise 6 in Chapter 4
# Rewrite your pay computation with time-and-a-half for over- time 
# and create a function called computepay which takes two parameters (hours and rate).
#
# N/A
######################################
def computePay(hours, rate):
    pay = float(hours) * float(rate)
    totalPay = pay
    
hours = input("Enter your hours: ")
rate = input("Enter your rate: ")


try:
    
    if hours <= '40':
           totalPay = computePay(hours, rate) 
            
    elif hours > '40':
            overtime = float(hours) - float(40)
            regularPay = float(rate) * 40
            overtimePay = (float(overtime) * (float(rate) * 1.5))
            totalPay = float(regularPay) + float(overtimePay)

    print("\nPay:", totalPay)
    
except:
    print('Error! Please enter a numeric value!')

   
    
