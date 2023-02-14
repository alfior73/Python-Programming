######################################
# Creator: Alfio Raymond
# Date: 5 Feb 2023
#
# Problem Set 3 Part 1
# 
# Fix the code so it is correct.
# test with the following input
# total = 9, days = 30, result = 0.3
# tatal = 0,  days = 31, results = 0
# total = 3.1, days = 0, result = "Failure, something is wrong with the calculation"
# total = 3.1, days = 30, result = .10333333
#
#########################################

def get_total():
    count = input("Enter the total number of inches it has rained in the month: ")
    rain_total = float(count)
    return rain_total


def get_count():
    days = input("Enter the number of days for the month: ")
    days = float(days)
    return days


def calc_avg_daily_rain(total, days):
    daily_rain = total/days
    return daily_rain


def main():
    print("\nLet's calculate average rainfail!")
    
    total_rain = get_total()
    day_count = get_count()
    try:
        result = calc_avg_daily_rain(float(total_rain), day_count)
        print("The avg daily rainfall for the month is ", result)
        print("\n")
    except:
         
        print("Failure, something is wrong with the calculation\n")

    
main()