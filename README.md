# Driverless_Taskphase

# # This is a python project for Student Marksheet

# # Libraries used - NumPy, Pandas

# # The student details are stored in a csv file called 'rc.csv'

1. It has a main page (task3.py) which has the options to add student details, update student details, computing ranks, displaying marksheet, finding merit students. Ech option invokes a different function to perform the request.

2. On choosing 'add new student detail' a function (detail.py) is called which takes name, admission number, roll number, class and marks as input and stores the information as a row in the csv file.

3. The 'update stored detail' option calls a function (update.py) which takes row and column number as input to find the cell to be changed and then replaces it with the new information entered.

4. On choosing 'compute ranks' a function (rank.py) calculates the percentage of each student based on marks and display them in descending order.

5. In the 'display marksheet' option the (marksheet.py) function displays marksheet of the required student.

6. The 'merit students' option uses a function (merit.py) to display student records who scored more that 90 in all subjects
