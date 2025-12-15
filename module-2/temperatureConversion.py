# CSD-325 Module 2 Assignment
# Program: Fahrenheit to Celsius Converter (for debugging practice)

import pdb

def fahrenheit_to_celsius(f_temp):
    """Converts Fahrenheit to Celsius."""
    # Formula: (F - 32) * 5/9
    c_temp = (f_temp - 32) * (5/9)
    return round(c_temp, 2)

# Main program execution
if __name__ == "__main__":
    current_temp_f = 68
    
    # FOR ASSIGNMENT: This line pauses the program for debugging.
    pdb.set_trace() 
    
    converted_temp_c = fahrenheit_to_celsius(current_temp_f)
    
    print(f"Fahrenheit: {current_temp_f}")
    
    if converted_temp_c > 20:
        print("It's a warm day.")
    else:
        print("It's a cool day.")
    print("Program finished.")