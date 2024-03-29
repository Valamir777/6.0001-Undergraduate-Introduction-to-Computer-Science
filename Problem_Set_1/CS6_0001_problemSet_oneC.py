def calc_savings_time(base_annual_salary, total_cost, down_payment_percentage, semi_annual_raise):
    # import data
    base_annual_salary = base_annual_salary
    total_cost = total_cost
    down_payment_percentage = down_payment_percentage
    semi_annual_raise = semi_annual_raise

    #  fixed data
    down_payment = total_cost * down_payment_percentage
    months = 36  # minimum months to pay for down payment
    epsilon = 0.001 * down_payment  # within 10000 Rubles of Desired down payment or 0.01 of down payment

    #  bounds for bisection search
    initial_high = 100
    high = initial_high  # high boundary for the formula (High + Low)/2
    low = 0  # lower boundary

    #  initial values for the while loop
    current_savings = 0
    step = 0  # step in bisection search
    # floor division to get the integer quotient
    portion_saved = (high + low) // 2

    #  start of bisection search
    while abs(current_savings - down_payment) > epsilon:

        step += 1
        current_savings = 0
        annual_salary = base_annual_salary
        monthly_salary = annual_salary / 12
        monthly_deposit = monthly_salary * (portion_saved / 100)

        for month in range(1, months + 1):

            current_savings += (current_savings * (0.04 / 12)) + monthly_deposit

            if month % 6 == 0:
                annual_salary += (annual_salary * semi_annual_raise)
                monthly_salary = annual_salary / 12
                monthly_deposit = monthly_salary * (portion_saved / 100)

        prev_portion_saved = portion_saved
        if current_savings < down_payment:
            low = portion_saved
        else:
            high = portion_saved

        portion_saved = float(((high + low) / 2))

        if prev_portion_saved == portion_saved:
            break

    print()
    if portion_saved == initial_high:
        print("Not possible to acquire the house within 36 months.")
    else:
        print("Best savings rate: {}".format(round(portion_saved / 100, 2)))
        print("Steps in Bisection search: {}".format(step))


class house_hunt:
    #  # Commented out for test cases
    # try:
    #    base_annual_salary = float(input("Enter your annual salary: "))
    #    total_cost = float(input("Enter the cost of your dream home: "))
    #    down_payment_percentage = float(
    #        input("Enter the percent of your down payment: "))
    #    semi_annual_raise = float(
    #             input("Enter you semi-annual salary raise: "))

    # except ValueError:
    #    print("Please type float or integers only.")

    calc_savings_time(150000, 1000000, 0.25, 0.07)
    # Test Case 1
    # Best savings rate: 0.4411
    # Steps in bisection search: 12

    calc_savings_time(300000, 1000000, 0.25, 0.07)
    # Test Case 2
    # Best savings rate: 0.2206
    # Steps in bisection search: 9

    calc_savings_time(10000, 1000000, 0.25, 0.07)
    # Test Case 3
    # It is not possible to pay the down payment in three years.
    # Desired error_rate = 0.01