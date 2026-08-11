x= int (input("Welcome to the 👾 𝙽𝚄𝙼𝙱𝙴𝚁 0𝚁𝙰𝙲𝙻𝙴. Type any number (no decimal points) from any negative integer to 20, and I will tell you some facts about it."))

if x>20:
    print("ERROR! Your number is >20")

elif x==2:
    print(str(x)+" is an even number which is positive, it is a natural number which is the only even prime no.")

elif x%2==0 and x>0:
    print(str(x)+" is an even number which is positive, it is a natural number.")

elif x%2==1 and x>0 and x==3 or x==5 or x==7 or x==11 or x==13 or x==17 or x==19: 
    print(str(x)+" is an odd number which is positive, it is a natural number which is prime.")

elif x%2==1 and x>0: 
    print(str(x)+" is an odd number which is positive,it is a natural number.")

elif x%2==0 and x<0: 
    print(str(x)+" is an even number which is negative, it is not a natural number. Negative integers are not prime.")

elif x%2==1 and x<0: 
    print(str(x)+" is an odd number which is negative, it is not a natural number. Negative integers are not prime.")

elif x==0: 
    print("your number is 0 which is an even number, is neither positive nor negative and is not prime.")

else:
    print("Invalid")

input("What is your feedback on the 👾 𝙽𝚄𝙼𝙱𝙴𝚁 0𝚁𝙰𝙲𝙻𝙴?")
print("Thank you, your feedback will help us improve.")