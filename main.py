##
#  Manage student grades.
#
# Use a dictionary named 'grades' to track student grades.
# code here
grades = []

  # Loop until the user chooses to quit.
  # Check user input for the following "(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? "
  # Prevent unexected inputs by converting input to upper-case
  # code here
loop = True
while loop == True:
    get_choice = input("(A)dd, (R)emove, (M)odify, (P)rint All, or (Q)uit? ")
    choice = get_choice.upper()
   # Use a condition to handle adding a new student.
   # Convert grade into integer
   # Gather user input for "Enter the name of the student: "
   # Check if student name already exists "Sorry, that student is already present."
   # Gather user input for student grade "Enter the student's grade: "
   # Validate input is in correct format or range, if not notify "Please enter grade as number 0-100"
   # code here
    if choice == 'A':
        get_name = input("Enter the name of the student: ")
        found = False
        for student in grades:
            if student["Name"] == get_name:
                found = True
        if found == True:
            print("Sorry, that student is already present.")

        else:
            valid_int = False
            while valid_int == False:
                get_grade = int(input("Enter the student's grade: "))
                if get_grade <= 100 and get_grade >= 0 and str(get_grade).isdigit() == True:
                    grades.append({"Name": get_name, "Grade": get_grade})
                    valid_int = True
                else:
                    print("Please enter grade as number 0-100")
                

   # Handle removing a student if user inputs 'R'
   # Check input for "What student do you want to remove? "
   # use pop to remove key/value form grades
   # see notes https://www.programiz.com/python-programming/methods/dictionary/pop
   # Check if student doesn't exist - "Sorry, that student doesn't exist and couldn't be removed."
   # code here
    elif choice == 'R':
        popped = False
        remove_student = input("What student do you want to remove? ")
        index = 0
        for student in grades:
            if student["Name"] == remove_student:
                grades.pop(index)
                popped = True
                break
            index+=1
        if popped == False:
            print("Sorry, that student doesn't exist and couldn't be removed.")

   # Handle modifying a student grade if user inputs 'M'
   # "Enter the name of the student to modify: "
   # Convert grade into integer
   # If student is in grades dictionary, show existing grade "The old grade is"
   # Gather input for new grade "Enter the new grade: "
   # If student doesn't exist "Sorry, that student doesn't exist and couldn't be modified."
   # code here
    elif choice == 'M':
        found = False
        mod_student = input("Enter the name of student to modify: ")
        for student in grades:
            if student["Name"] == mod_student:
                print("The old grade is", student["Grade"])
                new_grade = int(input("Enter the new grade: "))
                student["Grade"] = new_grade
                found = True
                break
        if found == False:
            print("Sorry, that student doesn't exist and couldn't be modified.")

   # Handle printing grade average as a string if user input is 'P'
   # Use "The average grade is "
   # Handle printing all of the student names with associated grade
   # Display explictly as strings
   # code here
    elif choice == 'P':
        total_grade = 0
        count = 0
        for student in grades:
            total_grade += student["Grade"]
            count += 1
        average = total_grade / count
        print("The average grade is ", average)

        for student in grades:
            print(student["Name"] + ": " + str(student["Grade"]))
      

   # Handle the case for quiting if user inputs 'Q' "Goodbye!"
   # code here
    elif choice == 'Q':
        print("Goodbye!")
        loop = False

   # Handle the case of invalid input. "Sorry, that wasn't a valid choice."
   # code here
    else:
        print("Sorry, that wasn't a valid choice.")