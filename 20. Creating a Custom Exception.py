class invalid_age_Error(Exception):
    pass

def check_age(age):
    if age < 18:
        raise invalid_age_Error("Age must be atleast 18.")
    
try:
    check_age(16)
except Exception as e:
    print(e)