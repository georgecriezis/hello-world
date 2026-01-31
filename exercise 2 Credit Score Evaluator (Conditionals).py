<<<<<<< HEAD
# Prompt for credit score and convert to integer
try:
    score = int(input("What's your credit score? "))

    # Check for invalid range first 
    if not (300 <= score <= 850):
        print("Invalid score.")
    else:
        
        if score >= 750:
            print("Excellent - Loan Approved.")
            print("Interest rate: Low")
            
        elif 700 <= score < 750:
            print("Good - Loan Approved with Review.")
            print("Interest rate: Low")
            
        elif 600 <= score < 700:
            print("Fair - Loan Conditional.")
            print("Seek credit improvement.")
            
        else: # Score is between 300 and 599
            print("Poor - Loan Denied.")
            print("Seek credit improvement.")

except ValueError:
=======
# Prompt for credit score and convert to integer
try:
    score = int(input("What's your credit score? "))

    # Check for invalid range first (Chained Comparison)
    if not (300 <= score <= 850):
        print("Invalid score.")
    else:
        # Categorize the score
        if score >= 750:
            print("Excellent - Loan Approved.")
            print("Interest rate: Low")
            
        elif 700 <= score < 750: # Chained Comparison
            print("Good - Loan Approved with Review.")
            print("Interest rate: Low")
            
        elif 600 <= score < 700:
            print("Fair - Loan Conditional.")
            print("Seek credit improvement.")
            
        else: # Score is between 300 and 599
            print("Poor - Loan Denied.")
            print("Seek credit improvement.")

except ValueError:
>>>>>>> 34e59adb728f2c7050926ae677a1288c615345cc
    print("Please enter a valid whole number.")