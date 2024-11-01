def main():  
    counts = {      # Initialize counts for each range
        "1-10": 0,
        "11-20": 0,
        "21-30": 0,
        "31-40": 0,
        "41-50": 0
    }

    while True:   # Start a loop for user input
        try:   # To catch the potential errors
            number = int(input("Enter a number between 1 and 50 (or a number outside the range to quit): "))

            # Increment the value by 1 if the number is within that range
            if 1 <= number <= 10:
                counts["1-10"] += 1
            elif 11 <= number <= 20:
                counts["11-20"] += 1
            elif 21 <= number <= 30:
                counts["21-30"] += 1
            elif 31 <= number <= 40:
                counts["31-40"] += 1
            elif 41 <= number <= 50:
                counts["41-50"] += 1
            else:
                break  # Exit loop if the input number is invalid or outside the range
        except ValueError:
            print("Error! Please enter a valid integer (number)")
            continue   # Prompt again on error

    # Display the results
    print("\nInput Summary:")
    for range_label in counts: 
        print(f"{range_label} = {counts[range_label]}") # Label = value 

if __name__ == "__main__":  # To check if the script is running directly
    main()




