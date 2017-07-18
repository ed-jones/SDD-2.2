"Multi-dimensional Array"
# year -> class -> student -> task

MARKS = [#
    [#year 0
        [#students in class 0
            # class 0: task mark for each student
            [0, 20, 50, 99], [23, 45, 97, 20], [18, 18, 18, 18]
        ],

        [#students in class 1
            # class 1: task mark for each student
            [30, 48, 78, 92], [55, 21, 64, 100], [65, 72, 76, 82]
        ]
    ],

    [#year 1
        [# students in class 0
            # class 0: task mark for each student
            [22, 13, 15, 17], [77, 74, 85, 81], [-1, 44, 52, 32]
        ],

        [#students in class 1
            # class 1: task mark for each student
            [77, 45, 32, 1], [57, 67, 45, 89], [54, 67, 45, 32]
        ]
    ]
]
"""
[ # year
  [ # class
    [ # student
      [ # task ]
    ]
  ]
]
"""
"""twoD = [
  ["first", "second"],
  ["third"]
]
print(twoD[0])
print(twoD[1])
print(twoD[0][1])"""

#print(MARKS[0])        #print MARKS for whole year 0
#print (MARKS[0][0])    #print MARKS for class 0
#print (MARKS[1])       #print MARKS for whole year 1
#print (MARKS[1][1][0]) #print MARKS for year 1, class 1, student 0


def assess_results(year, class_num, student, task):  #parameters
    "Assess Results"
    if not all([x >= 0 for x in (year, class_num, student, task)]):  #checks all elements are >=0
        return -1  #if not, returns -1
    return MARKS[year][class_num][student][task]


def class_task_average(year, class_num, task):  #Pass year, class_num, task parameters
    "Find class task average"
    student = 1  #set student variable to 1.
    total = 0  #current total set to 0.
    num_students = 0  #variable to keep track of student no. of elements
    while student <= 2:  # 0 1 2 len(MARKS_0[year][class_num]) -> gets number of students
        result = assess_results(year, class_num, student, task)  #stores arguments as variables
        if result >= 0:
            num_students += 1  #increment num_students
            total = total + result  #adds each total
        student += 1  #increments through student in list
    if num_students:
        return total / num_students  #return average


def class_task_max(year, class_num, task):
    "Finds class task maximum"
    student = 0
    max_val = 0
    while student <= 2:  #0 1 2
        #print (year, class_num, student, task)
        result = assess_results(year, class_num, student, task)
        if result > max_val:
            max_val = result
        student += 1
    return max_val


#print(class_task_max(0,0,1))
print(class_task_average(0, 0, 1))

# class_task_average ignores array elements that contain -1.
# This is done via the line "if result >= 0".
# If the value of result is less than 0, we simply skip to the next student
# and don't add anything to our total.
# We also disregard incrementing "num_students" as this is the value we
# divide by to get the average.

# It is possible for more than one class to have the same class number.
# This is reasonable as for each year, we can still
# have the same class numbers.
# The problem states that each combination of indexes must be unique.
# This means that we cannot have two identical arrays,
# but as long as one value is different we are safe.
# [9,4,1,2] [9,5,1,2] are both okay. As are:
# [10,4,1,2] [11,4,1,2]; [8,5,3,2] [8,5,4,2]; [3,3,3,3] [3,3,3,4]
# [10,3,5,4] [10,3,5,4] are not okay as they are identical.
