# D'Jon Harrison
# Module 4.2 Assignment

import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys  # NEW: added to allow clean program exit

filename = 'sitka_weather_2018_simple.csv'

# NEW: Function to plot either highs or lows
def plot_temperatures(temp_type):
    """Plots highs or lows depending on temp_type ('high' or 'low')."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # NEW: separate list for the selected temperature type
        dates, temps = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            # NEW: choose which temperature to append
            if temp_type == 'high':
                temps.append(int(row[5]))
            else:
                temps.append(int(row[6]))

    # Plot the selected temperature type
    fig, ax = plt.subplots()
    color = 'red' if temp_type == 'high' else 'blue'  # NEW: red for highs, blue for lows
    ax.plot(dates, temps, c=color)

    # NEW: set title depending on selection
    title = "Daily High Temperatures - 2018" if temp_type == 'high' else "Daily Low Temperatures - 2018"
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()


# NEW: Main program loop with user menu
def main():
    print("Welcome to the Sitka Weather Program!")
    while True:  # NEW: loop until user chooses exit
        print("\nMenu Options:")
        print("1 - High Temperatures")  # NEW: menu option for highs
        print("2 - Low Temperatures")   # NEW: menu option for lows
        print("3 - Exit")               # NEW: menu option to exit
        choice = input("Enter your choice (1/2/3): ").strip()

        # NEW: check user choice and call function accordingly
        if choice == '1':
            plot_temperatures('high')  # call plot function for highs
        elif choice == '2':
            plot_temperatures('low')   # call plot function for lows
        elif choice == '3':
            print("Exiting program. Goodbye!")  # NEW: exit message
            sys.exit()  # clean exit
        else:
            print("Invalid input. Please select 1, 2, or 3.")  # NEW: invalid input handling


# NEW: run main loop if program is executed directly
if __name__ == "__main__":
    main()
