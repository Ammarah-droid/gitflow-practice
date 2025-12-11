
def calculate_age(birth_date, current_year):
    age=current_year-birth_date
    return age
    
birth_date=int(input("enter your year of birth: "))
current_year=int(input("enter current year: "))
calculated_age=calculate_age(birth_date, current_year)
age=calculated_age
if age>=0 and age<13:
    print("you are a child")
elif age>12 and age<20:
    print("you are a teenager")
elif age >19 and age<61:
    print("you are an adult")
elif age>60 and age<120:
    print("you are a senior")
else:
    print("age category undefined")



