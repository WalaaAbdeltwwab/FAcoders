grade_one={'Sami':[19,18,19.5,30,10],
'Ahmad':[15,14,16,21,7],
'Faris':[18,19,17,26,9],
'Salem':[20,20,19,30,10],
'Mahmoud':[7,18,11,13,12]}

grade_two={'Lana':[17,19,20,28,9],
'Dina':[10,29,20,19.5,18.5],
'Maha':[20,20,18,26,9],
'Abeer':[16,18,19.5,25,8]}

grade_three={'Rima':[18,19,18,26,9],
'Tala':[10,29,19,20,20],
'Lamar':[19,20,18,26,9],
'Rola':[15,14,16,19,7],
'Naya':[9,6,11,14,7],
'Dalal':[1,5,2,6,7],
'Ola':[19.5,20,20,29.5,10]}
def students_names(grade_name):
    students_names_list=list(grade_name.keys())
    return students_names_list

def students_count(x):
    students_names_list=list(x.keys())
    count=len(students_names_list)
    return count

def students_score(x,y):
   student_marks_list=x[y]
   total=sum(student_marks_list)
   return total
while True :
    teacher_choice=input('Choose one: students_names , students_count , students_score : ')
    if teacher_choice=='students_names' :
        grade_name=input('Enter grade\'s name: ')
        a=students_names(grade_name)
        teacher_response=input('Enter done to close the program or more to re-choose: ')
        if teacher_response=='done' :
            print('Thank you for using our program')
            break
    elif teacher_choice=='students_count' :
        grade=input('Enter grade\'s name: ')
        b=students_count(grade)
        teacher_response=input('Enter done to close the program or more to re-choose: ')
        if teacher_response=='done' :
            print('Thank you for using our program')
            break
    elif teacher_choice=='students_score' :
        grade=input('Enter grade\'s name: ')
        name=input('Enter student\'s name: ')
        c=students_score(grade,name)
        teacher_response=input('Enter done to close the program or more to re-choose: ')
        if teacher_response=='done' :
            print('Thank you for using our program')
            break
    else :
        print('Please, Enter a matching choice for the following three choices')
    print(a,b,c)
