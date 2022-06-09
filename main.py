"""Open “main.py”. You’ll find the skeleton of the class Student. Student class should have the following attributes:

 Name: A string, should be initialized when creating an instance of Student
 Age: An integer, should be initialized when creating an instance of Student
Tracks: A list of strings, should be initialized when creating an instance of Student. Feel free to pick any values as tracks.
 Score: A float, should be initialized when creating an instance of Student.    
3.  Create the following methods for class “Student”:

change_name: Change students name, should accept a new name as an argument.
Change_age: Change students' age, should accept a new age as an argument. Should ensure age remains an integer.
Add_track: Add a new item to students tracks, should accept a new track as an argument.
get_score: Return student’s score."""

class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        
    def change_name(self, name) :
        self.name = name
        return self.name
        
    def change_age(self, age):
        if type(int(age)) == int:
            self.age = age
            return self.age
        print("input a number")
        
        
    def get_score (self):
         return self.score
         
         
    def add_track(self, tracks):
        self.tracks = [ ]
        self.tracks = self.tracks.append(tracks)
        
        return self.tracks


Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

