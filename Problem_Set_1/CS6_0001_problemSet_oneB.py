#  Problem Set 1b

def calc_savings_time(annual_salary, portion_saved, total_cost, semi_annual_raise):
    current_savings = 0
    months = 0

    while current_savings < total_cost * 0.25:
        current_savings += ((annual_salary / 12) * portion_saved) + (current_savings * (0.04 / 12))
        months += 1

        if months % 6 == 0:
            annual_salary += (annual_salary * semi_annual_raise)

    print()
    print("Needed down-payment: {0:.2f} Rubles".format(
        round(total_cost * 0.25, 2)))
    print("Total savings: {0:.2f} rubles".format(round(current_savings, 2)))
    print("Number of months: {} months".format(months))


class house_hunt:
    #  # Commented out for test cases
    # try:
    #    annual_salary = float(input("Enter your annual salary: "))
    #    portion_saved = float(
    #        input("Enter the percent of your salary to save, as a decimal: "))
    #    total_cost = float(input("Enter the cost of your dream home: "))
    #    semi_annual_raise = float(
    #             input("Enter you semi-annual salary raise: "))

    # except ValueError:
    #    print("Please type float or integers only.")

    calc_savings_time(120000, 0.05, 500000, 0.03)
    # Test Case 1
    # Number of months: 142
    # >>>
    calc_savings_time(80000, 0.1, 800000, 0.03)
    # Test Case 2
    # Number of months: 159
    calc_savings_time(75000, 0.05, 1500000, 0.05)
    # Test Case 3
    # Number of months: 261