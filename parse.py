import argparse
import enrollment 

courses = ('ml', 'cv', 'ca', 'cn', 'oop')

def parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers(dest='command')

    add_parser = sub_parsers.add_parser('add')
    add_parser.add_argument(
        'name', 
        type=name, 
        help='the name of the student (Letters only)'
    )
    add_parser.add_argument(
        '-c', '--courses', 
        type=course,
        default=[], 
        nargs='+', 
        help=f'the courses to enroll the student in from {courses}'
    )

    enroll_parser = sub_parsers.add_parser('enroll')
    enroll_parser.add_argument(
        'id', 
        type=sid, 
        help='the id of the student'
    )
    enroll_parser.add_argument(
        'courses', 
        type=course,
        nargs='+',  
        help=f'the courses to enroll the student in from {courses}'
    )
    
    display_parser = sub_parsers.add_parser('display')
    display_parser.add_argument(
        '-c', '--course', 
        type=course, 
        help='filter by course'
    )
    display_parser.add_argument(
        '-s', '--search', 
        type=student, 
        help='search by student id or name'
    )

    edit_parser = sub_parsers.add_parser('edit')
    edit_parser.add_argument(
        'id', 
        type=sid, 
        help='student id to edit'
    )
    edit_parser.add_argument(
        'new_name', 
        type=name, 
        help='new name for the student'
    )

    return parser.parse_args() 


def name(n: str) -> str:
    shortest_name_len = 2
    n = n.strip()
    if not n:
        raise argparse.ArgumentTypeError('the name of the student must be provided')
    
    if len(n) < shortest_name_len:
        raise argparse.ArgumentTypeError(f'Name must be at least {shortest_name_len} characters.')
    
    for c in n:
        if not c.isalpha() and c != '-' and c != ' ':
            raise argparse.ArgumentTypeError(f"'{c}' is invalid. Use letters only.")

    return ' '.join([_n.capitalize() for _n in n.split()])
def sid(_id: str) -> int:
    try:
        v = int(_id)
    except ValueError:
        raise argparse.ArgumentTypeError('ID must be a number')
    
    if v <= 0:
        raise argparse.ArgumentTypeError('ID must be greater than 0')
    
    return v

def course(c: str) -> str:
    c = c.lower()
    if c not in courses:
        raise argparse.ArgumentTypeError(f'Unknown course: {c}. Expected: {courses}')
    return c


def student(s: str) -> str:
    try:
        s = name(s)
    except argparse.ArgumentTypeError:
        try:
             int(s) 
        except ValueError:
             raise argparse.ArgumentTypeError('Value must be a valid Name or ID')
    return s