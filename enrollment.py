import json      
import os       
import uuid  
import sys    

file_name = "students.json"
def load_data()->list[dict]:
    if not os.path.exists(file_name):
        return []
    
    try:
        with open(file_name, 'r') as f:
            if not f.read().strip():
                return []
            return json.load(f)
        
    except json.JSONDecodeError as e:
        print(f'corrupted JSON in {file_name}')
        print(f'error at line {e.lineno}, column {e.colno}: {e.msg}')
        sys.exit(1)

    except OSError as e:
        print(f'error reading file: {e}')
        sys.exit(1)

def save_data(data: list[dict]):
    try:
        with open(file_name, 'w') as f: 
            json.dump(data, f, indent= 4)
    except OSError as e:
        print(f'error writing file: {e}')
        sys.exit(1)


def add_student(name: str):
    data = load_data()
    student_id = str(uuid.uuid4())[:8]

    new_student = {
        "id": student_id,
        "name": name,
        "courses": []
    }
    data.append(new_student)
    save_data(data)

    print(f"✅ Added successfully: {name} (ID: {student_id})")

