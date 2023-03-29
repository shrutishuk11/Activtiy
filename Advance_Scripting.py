def Bulk_message():
A = int(input("How many messages do you want to send(write in numbers): "))
x = 1
S1 = []
Admission_ID1 = []
Rank1 = []
I1 = 0
while I1 < A:
S = (input(f"Enter the student Name {x}:"))
ID = (input(f"Enter the student ID {x}:"))
Rank = (input(f"Rank of Student {x}:"))
S1.append(S)
Admission_ID1.append(ID)
Rank1.append(Rank)
x = x+1
A -= 1
print("\n")
for index in range(x-1):
message = f'Hi {S1[index]} Congratulations.....! {S1[index]} , You got
selected for the next round of requirement process'\
f'submit your academic credential including primary and secondary
'\
f'certificates. Your admission ID is : {Admission_ID1[index]} and
will be eligible '\
f'for the next round of interview with a CAP rank of :
{Rank1[index]}, If you submit all the documents on time and process '\
f'university might offer you a scholarship.'
print(message)
Bulk_message()