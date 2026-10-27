

print("=====TASK1======")
#Task 1
movies = [
    (1, "MovieA", "Action", 8.2),
    (2, "MovieB", "Drama", 7.5),
    (3, "MovieC", "Action", 9.1),
    (4, "MovieD", "Comedy", 6.8),
    (5, "MovieE", "Drama", 8.9)
]

columns = [
    "movie_id",
    "movie_name",
    "genre",
    "rating"
]
#Practice Questions ,Highest-rated movie in each genre ,Average rating by genre ,Rank movies within genre ,Top 2 movies per genre
print("=====TASK2======")
#Task 2
print("=====TASK1======")
data = [
    (
        101,
        "Green Valley School",
        2005,
        {"city": "Hyderabad", "state": "Telangana"},
        {
            "principal_id": 9001,
            "principal_name": "Ramesh Kumar",
            "email": "ramesh@school.com"
        },
        [
            {
                "teacher_id": 501,
                "teacher_name": "Anitha",
                "experience": 8,
                "salary": 65000.0,
                "subjects": ["Maths", "Physics"]
            },
            {
                "teacher_id": 502,
                "teacher_name": "Suresh",
                "experience": 5,
                "salary": 52000.0,
                "subjects": ["Chemistry", "Biology"]
            },
            {
                "teacher_id": 503,
                "teacher_name": "Priya",
                "experience": 10,
                "salary": 72000.0,
                "subjects": ["English", "Social"]
            }
        ],
        [
            {
                "student_id": 1001,
                "student_name": "Arjun",
                "age": 15,
                "class_name": "10A",
                "subjects": ["Maths", "Physics", "English"],
                "attendance": [
                    {
                        "month": "January",
                        "total_days": 22,
                        "present_days": 20
                    },
                    {
                        "month": "February",
                        "total_days": 20,
                        "present_days": 18
                    }
                ],
                "exam_results": [
                    {
                        "subject": "Maths",
                        "marks": 92,
                        "grade": "A"
                    },
                    {
                        "subject": "Physics",
                        "marks": 85,
                        "grade": "A"
                    },
                    {
                        "subject": "English",
                        "marks": 78,
                        "grade": "B"
                    }
                ]
            },
            {
                "student_id": 1002,
                "student_name": "Sneha",
                "age": 14,
                "class_name": "9A",
                "subjects": ["Maths", "Chemistry", "English"],
                "attendance": [
                    {
                        "month": "January",
                        "total_days": 22,
                        "present_days": 16
                    },
                    {
                        "month": "February",
                        "total_days": 20,
                        "present_days": 19
                    }
                ],
                "exam_results": [
                    {
                        "subject": "Maths",
                        "marks": 88,
                        "grade": "A"
                    },
                    {
                        "subject": "Chemistry",
                        "marks": 91,
                        "grade": "A"
                    },
                    {
                        "subject": "English",
                        "marks": 82,
                        "grade": "A"
                    }
                ]
            },
            {
                "student_id": 1003,
                "student_name": "Rahul",
                "age": 15,
                "class_name": "10A",
                "subjects": ["Maths", "Physics", "Social"],
                "attendance": [
                    {
                        "month": "January",
                        "total_days": 22,
                        "present_days": 21
                    },
                    {
                        "month": "February",
                        "total_days": 20,
                        "present_days": 20
                    }
                ],
                "exam_results": [
                    {
                        "subject": "Maths",
                        "marks": 76,
                        "grade": "B"
                    },
                    {
                        "subject": "Physics",
                        "marks": 89,
                        "grade": "A"
                    },
                    {
                        "subject": "Social",
                        "marks": 95,
                        "grade": "A"
                    }
                ]
            }
        ]
    ),
    (
        102,
        "Sunrise Public School",
        2010,
        {"city": "Bengaluru", "state": "Karnataka"},
        {
            "principal_id": 9002,
            "principal_name": "Lakshmi Devi",
            "email": "lakshmi@school.com"
        },
        [
            {
                "teacher_id": 601,
                "teacher_name": "Kiran",
                "experience": 7,
                "salary": 60000.0,
                "subjects": ["Maths", "Statistics"]
            },
            {
                "teacher_id": 602,
                "teacher_name": "Meena",
                "experience": 4,
                "salary": 48000.0,
                "subjects": ["Biology", "Chemistry"]
            }
        ],
        [
            {
                "student_id": 2001,
                "student_name": "Divya",
                "age": 16,
                "class_name": "11A",
                "subjects": ["Maths", "Statistics", "Physics"],
                "attendance": [
                    {
                        "month": "January",
                        "total_days": 22,
                        "present_days": 22
                    },
                    {
                        "month": "February",
                        "total_days": 20,
                        "present_days": 17
                    }
                ],
                "exam_results": [
                    {
                        "subject": "Maths",
                        "marks": 96,
                        "grade": "A"
                    },
                    {
                        "subject": "Statistics",
                        "marks": 93,
                        "grade": "A"
                    },
                    {
                        "subject": "Physics",
                        "marks": 87,
                        "grade": "A"
                    }
                ]
            },
            {
                "student_id": 2002,
                "student_name": "Vikram",
                "age": 16,
                "class_name": "11A",
                "subjects": ["Maths", "Chemistry", "Biology"],
                "attendance": [
                    {
                        "month": "January",
                        "total_days": 22,
                        "present_days": 19
                    },
                    {
                        "month": "February",
                        "total_days": 20,
                        "present_days": 20
                    }
                ],
                "exam_results": [
                    {
                        "subject": "Maths",
                        "marks": 81,
                        "grade": "A"
                    },
                    {
                        "subject": "Chemistry",
                        "marks": 74,
                        "grade": "B"
                    },
                    {
                        "subject": "Biology",
                        "marks": 90,
                        "grade": "A"
                    }
                ]
            }
        ]
    ) 
# Flaten this data
