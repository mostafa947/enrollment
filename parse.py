import argparse
import enrollment 

courses = () # رجعتها فاضية زي ما هي كاتبة بالظبط

def parser()->argparse.Namespace:
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers()

    add_parser = sub_parsers.add_parser('add')
    add_parser.add_argument(
        'name', 
        type= name, 
        help= 'the name of the student')
    
   
    
    add_parser.set_defaults(func=enrollment.add_student)

    enroll_parser = sub_parsers.add_parser('enroll')
    enroll_parser.add_argument(
        'id', 
        type= sid, 
        help= 'the id of the student')
    enroll_parser.add_argument(
        'courses', 
        type= course, 
        nargs= '+', 
        help= f'the courses to enroll the student in from {courses}')   
    #enroll_parser.set_defaults(func= enroll_student)
    
    display_parser = sub_parsers.add_parser('display', help= 'display all student')
    display_parser.add_argument(
        '-c', '--course',
        type= course,
        help= f'display the students that are enrolled in a specific course'
    )
    display_parser.add_argument(
        '-s', '--student',
        type= student,
        help= 'select a student by id'
    )

    #display_parser.set_defaults(func= display)
    return parser.parse_args() 


def name(n: str)->str:
    n = n.strip()
    if not n:
        raise argparse.ArgumentTypeError('the name of the student must be provided')
    
    non_alpha_chars = filter(lambda c: not c.isalpha(), (c for c in n))
    for c in non_alpha_chars:
        if c != '-' and c != ' ':
            raise argparse.ArgumentTypeError(f'\'{c}\' is an invalid character in name')

    return ' '.join([_n.capitalize() for _n in n.split()])


def sid(_id: str)->str:
    
    return _id


def course(c: str)->str:
    if c.lower() not in courses:
        raise argparse.ArgumentTypeError(f'unknown course {c}: expected {courses}')
    
    return c.lower()


def student(s: str)->str:
    try:
        s = name(s)
    except argparse.ArgumentTypeError:
        s = sid(s)
    return s

if __name__ == '__main__':
    try:
        args = parser()
        if hasattr(args, 'func'):
            args.func(args)
    except SystemExit:
        pass