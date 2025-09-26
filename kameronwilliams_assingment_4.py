student_name='Kameron Williams'
current_gpa=3.2
study_hours=25
social_points=45
stress_level=30
print(f'Welcome, {student_name}, to College Life Sim')
print(f'Here are your starting stats:')
print(f'GPA: {current_gpa}')
print(f'Study Hours:{study_hours}')
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")
print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")
choice=input("Your choice:")
if choice=="A":
    if current_gpa<=2.5:
        study_hours= study_hours+5
        stress_level= stress_level-5
        print('You chose a light. More Study time, less stressing!')
    else:
        study_hours=study_hours+3
        stress_level=stress_level-2
        print('You chose a light load. Easy semester for you.')
elif choice=='B':
    if current_gpa>=3.0:
        study_hours=study_hours+8
        stress_level=stress_level+5
        print('You chose a more standard load. You found a balance')
    else:
        study_hours=study_hours+10
        stress_level=stress_level+10
        print('You chose a standard load, It might be a bit challenging.')
elif choice=='C':
    if current_gpa>=3.5:
        study_hours=study_hours+15
        stress_level=stress_level+15
        print('You chose a heavy load, but you can handle it.')
    else:
        study_hours=study_hours+20
        stress_level=stress_level+20
        print('You chose heavy load, but can hurt you GPA.')
else:
    print('Invalid input. You lose study time for the week,')
    study_hours=study_hours-7
study_options=['Programming','Math','English','History']
print('\nChoose a subject to focus on this semester:')
print(study_options)
subject_choice=input('Your study choice:')
if subject_choice in study_options:
    if subject_choice =='Programming' and current_gpa <3.0:
        current_gpa=current_gpa+0.3
        social_points=social_points-5
        print('Programming practice increases your GPA but lowers your social time')
    elif subject_choice=='Math' or  subject_choice=='History':
        current_gpa=current_gpa+0.2
        social_points=social_points+3
        print(f'{subject_choice} increased GPA and still allowed you to be social')
    elif subject_choice=='English' and (study_hours>20 and stress_level<60):
        current_gpa=current_gpa+0.2
        social_points=social_points+7
        print('English essayss improved your GPA slightly and allows you to be social')
    else:
        print('Your choice had a little effect this time')
if subject_choice not in study_options:
    print('Invalid subject choice. No academic progress made.')
    stress_level=stress_level+10


