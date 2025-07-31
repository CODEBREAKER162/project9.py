students = {
    "Charith": {"Math": 90, "Science": 80, "English": 85},
    "Krishna": {"Math": 40, "Science": 55, "English": 70},
    "Ravi": {"Math": 30, "Science": 20, "English": 35}
}

for name, subjects in students.items():
    print("\n📘", name)
    total = 0

    for sub, mark in subjects.items():
        print(f"{sub} → {mark}")
        total += mark

    avg = total / len(subjects)
    grade = "A+" if avg >= 90 else "A" if avg >= 75 else "B" if avg >= 60 else "C" if avg >= 40 else "Fail"
    print(f"Total: {total} | Average: {avg:.2f} | Grade: {grade}")
 