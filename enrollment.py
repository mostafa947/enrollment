import argparse

courses = ()
def parser()->argparse.Namespace:
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers()

    add_parser = sub_parsers.add_parser('add')
    add_parser.add_argument('name', nargs= '+', type= name, help= 'the name of the student')
    add_parser.add_argument('id', nargs= 1, type= id, help= 'the id of the student')
    #add_parser.set_defaults(func= add_student)

    enroll_parser = sub_parsers.add_parser('enroll')
    enroll_parser.add_argument('id', type= id, help= 'the id of the student')
    enroll_parser.add_argument('courses', nargs= '+', choices= courses)
    #enroll_parser.set_defaults(func= enroll_student)
    
    display_parser = sub_parsers.add_parser('display')
    #display_parser.set_defaults(func= display)

    return parser.parse_args() 


def name(n: str)->str:
    if not n.isalpha():
        raise argparse.ArgumentTypeError('name can\'t have non-alphabetical characters')
    
    return n.capitalize()


def id(_id: str)->int:
    try:
        v = int(_id)
    except ValueError:
        raise argparse.ArgumentTypeError('id must be a number')
    
    if v <= 0:
        raise argparse.ArgumentTypeError('id must be a number greater than 0')
    
    return v