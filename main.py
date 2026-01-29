from parse import parser
import enrollment
import sys

def main():
    try:
        
        args = parser()
        
        if args.command == 'add':
            
            enrollment.add_student(args.name, args.courses)
            
        elif args.command == 'enroll':
            enrollment.enroll_student(args.id, args.courses)
            
        elif args.command == 'display':
            
            print("Display functionality coming soon...")
        else:
            print("Please specify a command: add, enroll, or display")

    except SystemExit:
        pass
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()