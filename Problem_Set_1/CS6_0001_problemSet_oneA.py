# Problem Set 1A ps1a.py
# Name: Taylor jackson
# Time spent: 1 Hour

def calc_savings_time(annual_salary, portion_saved, total_cost):
    current_savings = 0
    months = 0

    while current_savings < total_cost * 0.25:
        current_savings += ((annual_salary / 12) * portion_saved) + (current_savings * (0.04 / 12))
        months += 1

    print()
    print("Needed down-payment: {0:.2f} Rubles".format(
        round(total_cost * 0.25, 2)))
    print("Total savings: {0:.2f} rubles".format(round(current_savings, 2)))
    print("Number of months: {} months".format(months))


class house_hunt:
    #  # Commented out
    # try:
    #    annual_salary = float(input("Enter your annual salary: "))
    #    portion_saved = float(
    #        input("Enter the percent of your salary to save, as a decimal: "))
    #    total_cost = float(input("Enter the cost of your dream home: "))

    # except ValueError:
    #    print("Please type float or integers only.")

    calc_savings_time(120000, 0.10, 1000000)
    # Test Case 1
    # Number of months: 183

    calc_savings_time(80000, 0.15, 500000)
    # Test Case 2
    # Number of months: 105