def calculate_grade(scores):
    """Calculate average and letter grade from a list of scores."""
    if not scores:
        return 0, "N/A"
    
    average = sum(scores) / len(scores)
    
    # Determine letter grade
    if average >= 90:
        letter_grade = "A"
    elif average >= 80:
        letter_grade = "B"
    elif average >= 70:
        letter_grade = "C"
    elif average >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    
    return average, letter_grade


def main():
    print("=" * 40)
    print("    SIMPLE GRADE CALCULATOR")
    print("=" * 40)
    
    # Get student name
    name = input("\nEnter student name: ").strip()
    
    # Get scores
    scores = []
    print("\nEnter grades (type 'done' when finished):")
    
    while True:
        try:
            score_input = input(f"Grade {len(scores) + 1}: ").strip()
            
            if score_input.lower() == "done":
                if scores:
                    break
                else:
                    print("Please enter at least one grade.")
                    continue
            
            score = float(score_input)
            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("Please enter a valid grade (0-100).")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    
    # Calculate and display results
    average, letter_grade = calculate_grade(scores)
    
    print("\n" + "=" * 40)
    print(f"Student: {name}")
    print(f"Grades: {', '.join(str(s) for s in scores)}")
    print(f"Average: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print("=" * 40)


if __name__ == "__main__":
    main()

