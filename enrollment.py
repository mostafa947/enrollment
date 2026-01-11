import json      # مكتبة ال json 
import os        # عشان نسال النظام عن الملفات
import uuid      # (جديد) مكتبة عشان نعمل ID عشوائي مبيتكررش

file_name = "students.json"

def load_data():
    if not os.path.exists(file_name):
        return [] # بيعمل check لو الفايل مش موجود بيبدا ب ليست فاضية
    try:
        with open(file_name, 'r') as f:
            return json.load(f) # Deserialization
    except json.JSONDecodeError:
        return [] # لو الملف موجود بس فاضي او فيه error بيرجع ليست فاضية 

def save_data(data):
    with open(file_name, 'w') as f: # بيحول الداتا ل json و يكتبه جوا الملف و يحفظه
        json.dump(data, f, indent=4) # Serialization

# the logic ;)
def add_student(args):
    data = load_data()
    
    # بنعمل id عشاوئي و بناخد اول 8 حروف بس
    student_id = str(uuid.uuid4())[:8]
    
    # الاسم الي جايلنا من البارس جاهز
    name = args.name

    # 3. نكون شكل الطالب (Dictionary)
    new_student = {
        "id": student_id,
        "name": name,
        "courses": [] # لسه مسجلش مواد، فبنخليها فاضية
    }
    
    # 4. نضيف الطالب ونحفظ
    data.append(new_student) # بنزوده علي الليست
    save_data(data)          # بنحفظ التعديل في الملف
    
   
    print(f"✅ Added successfully: {name} (ID: {student_id})")

