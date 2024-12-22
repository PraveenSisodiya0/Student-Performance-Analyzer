class StudentData:
    def __init__(self):
        self.data = {}

    def add_data(self, student_id, subjects):
        if student_id in self.data:
            print("Student already exists")
        else:
            self.data[student_id] = subjects
            print("Added student")

    def update_data(self, student_id, subjects):
        if student_id in self.data:
            self.data[student_id] = subjects
            print("Updated student")
        else:
            print("Student not found")

    def delete_data(self, student_id):
        if student_id in self.data:
            del self.data[student_id]
            print("Deleted student")
        else:
            print("Student not found")

    def calculate_total_marks(self, student_id):
        if student_id in self.data:
            return sum(self.data[student_id].values())
        else:
            print("Student not found")
            return None

    def calculate_percentage(self, student_id):
        if student_id in self.data:
            total = self.calculate_total_marks(student_id)
            return (total / (len(self.data[student_id]) * 100)) * 100
        else:
            print("Student not found")
            return None

    def calculate_rank(self, student_id):
        if student_id in self.data:
            perc = self.calculate_percentage(student_id)
            rank = 1
            for sid in self.data:
                if sid != student_id:
                    if self.calculate_percentage(sid) > perc:
                        rank += 1
            return rank
        else:
            print("Student not found")
            return None

s = StudentData()

while True:
    print("\n1. Add data")
    print("2. Update data")
    print("3. Delete data")
    print("4. View data")
    print("5. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        sid = input("ID: ")
        n = int(input("Number of subjects: "))
        sub = {}
        for i in range(n):
            name = input("Subject: ")
            marks = int(input("Marks: "))
            sub[name] = marks
        s.add_data(sid, sub)

    elif ch == "2":
        sid = input("ID: ")
        n = int(input("Number of subjects: "))
        sub = {}
        for i in range(n):
            name = input("Subject: ")
            marks = int(input("Marks: "))
            sub[name] = marks
        s.update_data(sid, sub)

    elif ch == "3":
        sid = input("ID: ")
        s.delete_data(sid)

    elif ch == "4":
        for sid, subs in s.data.items():
            total = s.calculate_total_marks(sid)
            perc = s.calculate_percentage(sid)
            rank = s.calculate_rank(sid)
            print(sid, "Total:", total, "Perc:", perc, "Rank:", rank)

    elif ch == "5":
        break

    else:
        print("Invalid choice")
