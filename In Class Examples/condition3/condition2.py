#In class
#Conditions 2
# MPenta

print("Enter pay rate")
rate = float(input())

print("Enter hours worked")
hours = int(input())

overtime_hours = 0

if hours > 40:
    #overtime
    print("you have overtime")
    overtime_hours = hours - 40
    hours = 40

otpay = overtime_hours * (rate * 1.5)
print(f"OT Pay {otpay}")
regpay = rate * hours
print(f"reg Pay {regpay}")
totalPay = regpay + otpay

roundedPay = round(totalPay, 2)
print("your pay is: $" + str(roundedPay))


