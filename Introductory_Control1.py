#to get input
print("For T-20 match press 1 and 2 for test match")
A = int(input("enter 1 or 2: "))
if A == 1:
    print(" Welcome to T-20 worldcup ")
    print("Newzealand")
h = int(input("Enter total runs made by team:"))
rr = h / 20
    print("Newzeland run rate", rr)
    print("Pakistan")
H = int(input("enter Total runs made by team:"))
RR = H / 20
     print("Pakistan run rate", RR)
if A == 2:
    print(" Welcome to test match ")
    print("newzealand")
h = int(input("Enter total runs made by team:"))
rr = h / 50
    print("newzeland run rate", rr)
    print("Pakistan")
H = int(input("Enter Total runs made by team:"))
RR = H / 50
    print("pakistan run rate", RR)
Net_Run_Rate = rr - RR
    print("Net run rate", abs(Net_Run_Rate))
#For getting result
if h < H:
    print("\033[1;31;42m Pakistan has won the match \n")
if h > H:
    print("\033[1;31;40m Newzealand has won the match \n")
if h == H:
    print("\033[1;49;34m Match has tied \n")