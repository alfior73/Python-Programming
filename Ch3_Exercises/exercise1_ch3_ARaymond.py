######################################
# Creator: Alfio Raymond
# Date: 18 Jan 2023
#
# Exercise 1 in Chapter 3
# Rewrite your pay computation to give the employee 1.5 times
# the hourly rate for hours worked above 40 hours.
#
# N/A
######################################

hours = input("Enter your hours: ")
rate = input("Enter your rate: ")


if hours <= '40':
    pay = float(hours) * float(rate)
    totalPay = pay
else:
    overtime = float(hours) - float(40)
    regularPay = float(rate) * 40
    overtimePay = (float(overtime) * (float(rate) * 1.5))
    totalPay = float(regularPay) + float(overtimePay)

print("\nPay:", totalPay)
