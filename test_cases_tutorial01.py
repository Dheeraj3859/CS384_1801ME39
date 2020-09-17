import tutorial01 as A1

actual_answers = [9, 12,2,28,16,[2,6,18,54,162],[1,4,7,10,13]]
student_answers = []

test_case_1 = A1.add(4, 5)
student_answers.append(test_case_1)

test_case_2 = A1.subtract(14, 2)
student_answers.append(test_case_2)

test_case_3 = A1.divide(8, 4)
student_answers.append(test_case_3)

test_case_4 = A1.multiply(14, 2)
student_answers.append(test_case_4)

test_case_5 = A1.power(2,4)
student_answers.append(test_case_5)

a=2
r=3
n=5
gp = A1.printGP(a,r,n)
gp = list(gp)
student_answers.append(gp)

a1=1
d=3
n1=5
ap=A1.printAP(a1,d,n1)
ap=list(ap)
student_answers.append(ap)

print(actual_answers)
print(student_answers)

total_test_cases = len(actual_answers)
count_of_correct_test_cases = 0

for x, y in zip(actual_answers, student_answers):
    if x == y:
        count_of_correct_test_cases += 1

print(f"Test Cases Passed = '{count_of_correct_test_cases}'  / '{total_test_cases}'")
