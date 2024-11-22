#------------------------------------------------------------------------------------------#
# a dict to repr. det. of a stud.(name,rollno.,reg.no., dep., sem., )                       |
# add new element total mark                                                                |
# based on total mark find grade of student                                                 |
# total mark >= 90 -A                                                                       |
# total mark >= 82 -B                                                                       |
# total mark >= 75 -C                                                                       |
# total mark >= 60 -D                                                                       |
# total mark >= 50 -P                                                                       |
# Delete Roll NO.                                                                           |
#-------------------------------------------------------------------------------------------#
Bibi = {
    "name" : input('Enter the name '),
    "roll.no" : input('Enter your roll number '),
    "reg.no" : input('Enter your register number '),
    "Department" : input('Enter your Department '),
    "Semester" : input('Enter your Current Semester '),   
}
print(f'Before Updating Marks\n{Bibi}')
print()
Bibi.update({"total_mark" : int(input("Enter your mark out of 100 "))})
print(f'After updating Marks\n{Bibi}')
print()
def calculateGrade(total_mark):
    if total_mark >= 90:
        return 'A'
    elif total_mark >= 82:
        return 'B'
    elif total_mark >= 75:
        return 'C'
    elif total_mark >= 60:
        return 'D' 
    elif total_mark >= 50:
        return 'P'
    
Bibi['grade'] = calculateGrade(Bibi['total_mark'])
print(f'After adding Grade\n{Bibi}\n')
print('After Deleting')
del Bibi["roll.no"]
print(f'\n{Bibi}')
