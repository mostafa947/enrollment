import argparse  # مكتبه جهزة عشان فكرة ال CLi argument
import json      # مكتبة ال json 
import os        #  عشان نسال النظام عن الملفات

file_name = "students.json"

def load_data ():
    if not os.path.exists(file_name):
        return [] # بيعمل check لو الفايل مش موجود بيبدا ب ليست 
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []# بيشوف لو الملف موجود بيجيب الداتا الي فيه لو فاضي او فيه eror بيرجع ليست فاضية 
def save_data (data):
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)#بيحول الداتا ل json و يكتبه جوا الملف و يحفظه
        
def add_student ():
    data = load_data
    