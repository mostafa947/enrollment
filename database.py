from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


Base = declarative_base()


enrollment_table = Table('enrollments', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
   
    students = relationship("Student", secondary=enrollment_table, back_populates="courses")

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)  
    name = Column(String, nullable=False)
    
    courses = relationship("Course", secondary=enrollment_table, back_populates="students")


engine = create_engine('sqlite:///enrollment.db')
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    
    Base.metadata.create_all(engine)
    
    fixed_courses = ['ML', 'CV', 'CA', 'CN', 'OOP']
    for code in fixed_courses:
        exists = session.query(Course).filter_by(name=code).first()
        if not exists:
            session.add(Course(name=code))
    session.commit()