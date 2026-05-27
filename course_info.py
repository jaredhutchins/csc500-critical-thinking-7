"""Display course information using dictionaries."""


def main():
    """Get a course number from the user and display course details."""

    # Dictionary containing course numbers and room numbers.
    room_numbers = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411",
    }

    # Dictionary containing course numbers and instructor names.
    instructors = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee",
    }

    # Dictionary containing course numbers and meeting times.
    meeting_times = {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m.",
    }

    # Keep asking until the user enters a valid course number.
    while True:
        # Ask the user for a course number.
        # The strip() method removes extra spaces before or after the input.
        # The upper() method changes the input to uppercase so csc101 and CSC101 both work.
        course_number = input("Enter a course number: ").strip().upper()

        # If the course number is valid, display the course information.
        if course_number in room_numbers:
            print()
            print("Course Information")
            print("------------------")
            print(f"Course Number: {course_number}")
            print(f"Room Number:   {room_numbers[course_number]}")
            print(f"Instructor:    {instructors[course_number]}")
            print(f"Meeting Time:  {meeting_times[course_number]}")

            # Stop the loop because the user entered a valid course number.
            break
        else:
            # If the course number is not valid, display an error message.
            print("Course number not found. Please enter a valid course number.")


# Run the program.
if __name__ == "__main__":
    main()
