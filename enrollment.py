from database import session, Student, Course, init_db


init_db()

def add_student(name: str, course_names: list[str]):
    
    
    course_names = [c.upper() for c in course_names]
    
    
    courses_to_enroll = []
    for c_name in course_names:
        course = session.query(Course).filter_by(name=c_name).first()
        if course:
            courses_to_enroll.append(course)
        else:
            print(f" Warning: Course '{c_name}' not found.")

    
    new_student = Student(name=name, courses=courses_to_enroll)
    session.add(new_student)
    session.commit()
    
    print(f" Added successfully: {name} (ID: {new_student.id})")
    if courses_to_enroll:
        print(f"   Enrolled in: {', '.join([c.name for c in courses_to_enroll])}")


def enroll_student(student_id: int, course_names: list[str]):
    
    student = session.query(Student).filter_by(id=student_id).first()
    
    if not student:
        print(f" Error: Student with ID {student_id} not found.")
        return

    count = 0
    for c_name in course_names:
        c_name = c_name.upper()
        course = session.query(Course).filter_by(name=c_name).first()
        
        if not course:
            print(f" Course '{c_name}' does not exist.")
            continue
            
        if course in student.courses:
            print(f" Already enrolled in {c_name}.")
        else:
            student.courses.append(course)
            count += 1
            print(f" Enrolled in {c_name}.")

    if count > 0:
        session.commit()
        print(f" Successfully enrolled in {count} new course(s).")