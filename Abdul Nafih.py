import random
#Abdul Nafih-Batch 1-Password Generator
def password(q):
  k=''
  s=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  for n in range(q):
    k=k+random.choice(s) 
  print("Generated Password: ",k) 
password(int(input("enter the length: ")))     
