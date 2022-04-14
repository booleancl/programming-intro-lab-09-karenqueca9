from student import Student
from person import Person

class TestStudent:
    def test_is_a_student(self):
        student = Student('Winston', 'Davis')
        student_two = Student('Alexander','Soto')
        assert isinstance(student, Person)
        assert student.sayhello() == "hola mi nombre es Winston Davis"
        assert student_two.sayhello() == "hola mi nombre es Alexander Soto"