
#Anna S Antony,Batch no:-1,Total percentage

# Asks the user to enter the marks and stores each of them in a variable 
sub1 = int(input("Marks scored in Maths: "))
sub2 = int(input("Marks scored in Physics:"))
sub3 = int(input("Marks scored in Chemistry:"))
sub4 = int(input("Marks scored in Biology:"))
sub5 = int(input("Marks scored in Social:"))
percentage = int(((sub1 + sub2 + sub3 + sub4 + sub5)/5))
 #Calculates the total percentage 
print(f"Total percentage is: {percentage}")
#Following conditions checks the percentages and gives the grade
if percentage>=90:
  print("Grade A")
elif percentage>=80&percentage<90:
  print("Grade B")
elif percentage>=70&percentage<80:
  print("Grade C")
elif percentage>=60&percentage<70:
  print("Grade D")
else:
  print("Grade F")

