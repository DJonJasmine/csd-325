import sys

def countdown_song(count):
    """
    Manages the countdown and displays the reverse counting song lyrics.
    
    Args:
        count (int): The starting number of bottles.
    """
    current_bottles = count
    
    # Loop continues as long as there is at least one bottle to sing about
    while current_bottles > 0:
        
        # Determine current bottle phrase (e.g., "1 bottle" vs. "3 bottles")
        if current_bottles == 1:
            current_phrase = "1 bottle of beer"
        else:
            current_phrase = f"{current_bottles} bottles of beer"
            
        # Calculate the next number of bottles after taking one down
        next_bottles = current_bottles - 1
        
        # Determine next bottle phrase (e.g., "1 bottle(s)" vs. "0 bottle(s)")
        # Note: The problem output specifies "(s)" for singular/plural handling
        if next_bottles == 1:
            next_phrase = "1 bottle of beer on the wall."
        elif next_bottles == 0:
            next_phrase = "0 bottle(s) of beer on the wall."
        else:
            next_phrase = f"{next_bottles} bottle(s) of beer on the wall."

        # Display the full verse
        print(f"{current_phrase} on the wall, {current_phrase[0:current_phrase.find(' on the wall')]}.")
        print(f"Take one down and pass it around, {next_phrase}")
        
        # Decrement the count for the next iteration
        current_bottles -= 1

# --- Main Program ---

def main():
    try:
        # Prompt user for input
        bottles_input = input("Enter number of bottles: ")
        
        # Validate input is a non-negative integer
        if not bottles_input.isdigit():
            print("Invalid input. Please enter a whole number.")
            return

        start_count = int(bottles_input)
        
        if start_count < 0:
            print("The number of bottles must be zero or positive.")
            return

        # Pass input to the function
        countdown_song(start_count)

        # Reminder after the countdown completes
        print("Time to buy more bottles of beer.")

    except EOFError:
        # Handles case where input is terminated (e.g., Ctrl+D)
        print("\nInput terminated.")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()