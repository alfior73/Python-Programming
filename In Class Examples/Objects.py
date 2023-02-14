class Student:
    def __init__(self, sname, sid, gpa):
        self.name = sname
        self.id = sid
        self.gpa = gpa
        
    def printStudent(self):
        print(f"{self.name}, {self.id}, {self.gpa}")


class Course:
    def __init__(self, cnum, cname, desc, cred=3):
        self.name = cname
        self.number = cnum
        self.description = desc
        self.credits = cred
        self.studentList=[]
        self.maxseats = 20
        
    def printCourse(self):
        print(f" Course: {self.number}-{self.name}, {self.credits}")
    
    def printStudentList(self):
        for s in self.studentList:
            s.printStudent()
        
    def addStudentToCourse(self, s):
        if len(self.studentList) < self.maxseats:
            self.studentList.append(s)



c1 = Course("CIS 140", "Intro to CS", "Learn some CS", 4)
c2 = Course("CIS 153", "Programming for IT", "practical programming for IT", 4)
c3 = Course("CTN 110", "intro to IT", "IT stuff")

s1 = Student("bob smith", 1, 4.0)
s2 = Student("alice wonderland", 4, 2.0)
s3 = Student("susan storm", 2, 3.0)

c1.addStudentToCourse(s1)
c1.addStudentToCourse(s2)
c1.addStudentToCourse(s3)

c1.printCourse()
c1.printStudentList()
