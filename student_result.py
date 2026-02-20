import random

PASS_MARK = 35
TOTAL_PASSING = PASS_MARK * 6  # 210

# ---------------- Grade Function ----------------
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 35:
        return "Pass"
    else:
        return "Fail"

# ---------------- Rank Function ----------------
def calculate_rank(percentage):
    if 98 <= percentage <= 100:
        return "1st Rank"
    elif 95 <= percentage < 98:
        return "2nd Rank"
    elif 90 <= percentage < 95:
        return "3rd Rank"
    else:
        return "-"

# ---------------- Generate Students ----------------
students = []

first_names = ["Ram", "Shiva", "Amit", "Rohit", "Suresh", "Ganesh",
               "Vijay", "Rahul", "Akash", "Deepak", "Santosh"]

last_names = ["Mishra", "Patil", "Yadav", "Sharma", "Gupta",
              "Jadhav", "Pawar", "Kadam", "More", "Chavan"]

for i in range(1, 101):
    name = random.choice(first_names) + " " + random.choice(last_names)

    marks = {
        "hindi": random.randint(20, 100),
        "marathi": random.randint(20, 100),
        "english": random.randint(20, 100),
        "maths": random.randint(20, 100),
        "science": random.randint(20, 100),
        "social": random.randint(20, 100)
    }

    total = sum(marks.values())
    percentage = round((total / 600) * 100, 2)

    subject_status = {
        sub: "PASS" if marks[sub] >= PASS_MARK else "FAIL"
        for sub in marks
    }

    overall_status = "PASS" if all(m >= PASS_MARK for m in marks.values()) and total >= TOTAL_PASSING else "FAIL"

    students.append({
        "roll_no": i,
        "seat_no": f"SSC{i:03}",
        "name": name,
        **marks,
        "total": total,
        "percentage": percentage,
        "grade": calculate_grade(percentage),
        "rank": calculate_rank(percentage),
        "subject_status": subject_status,
        "result": overall_status
    })

# ---------------- Search System ----------------
while True:
    print("\n===== SSC RESULT SEARCH SYSTEM =====")
    print("1. Search by Roll No")
    print("2. Search by Seat No")
    print("3. Search by Name")
    print("4. Exit")

    choice = input("Enter choice: ")
    result = None

    if choice == "1":
        roll = int(input("Enter Roll No (1-100): "))
        result = next((s for s in students if s["roll_no"] == roll), None)

    elif choice == "2":
        seat = input("Enter Seat No (SSC001): ").upper()
        result = next((s for s in students if s["seat_no"] == seat), None)

    elif choice == "3":
        name = input("Enter Student Name: ").lower()
        result = next((s for s in students if name in s["name"].lower()), None)

    elif choice == "4":
        print("Thank You ✅")
        break

    else:
        print("Invalid Choice ❌")
        continue

    if result:
        print("\n==============================================")
        print("      MAHARASHTRA BOARD SSC EXAM RESULT      ")
        print("==============================================")
        print(f"Seat No : {result['seat_no']}")
        print(f"Roll No : {result['roll_no']}")
        print(f"Name    : {result['name']}")
        print("----------------------------------------------")
        print("Subject        Marks  Out Of  Pass  Status")
        print("----------------------------------------------")

        for sub in ["hindi","marathi","english","maths","science","social"]:
            print(f"{sub.capitalize():<13}{result[sub]:>5}    100    35    {result['subject_status'][sub]}")

        print("----------------------------------------------")
        print(f"TOTAL                {result['total']:>5}    600")
        print(f"Minimum Passing      {TOTAL_PASSING} /600")
        print(f"PERCENTAGE           {result['percentage']} %")
        print(f"GRADE                {result['grade']}")
        print(f"RANK                 {result['rank']}")
        print(f"FINAL RESULT         {result['result']}")
        print("==============================================")

    else:
        print("Record Not Found ❌")