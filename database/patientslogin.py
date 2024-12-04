#Ashraf-check if Name is valid in table database
def checkname(name):
    for i in name: 
        if not (i.isalpha() or i.isspace()):
            return False
    return True 
# Anas Mohamed - check if the age is valid integer not a string 
## first way ##
# def input_age(age):
#     if not age.isdigit():  
#         print("Invalid input")  
#         return None  
#     else:
#         return int(age)  
## second way ##
def input_age(age):
    try:
        age = int(age)  
        if 0 <= age <= 120: 
              return age
        else:
            print("Invalid input: Age must be between 0 and 120.")
            return None
    except ValueError:  
        print("Invalid input: Must be a numeric value.")
        return None

def check_gender (gender):
    if gender.lower() == "male" or "female" :
        return gender
    else :
        print("enter valid gender Male or Female")
        return None
    


    # testing 