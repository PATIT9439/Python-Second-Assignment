# part 2

text =["1.txt","2.txt","3.txt","4.txt","5.txt","6.txt","7.txt","8.txt","9.txt","10.txt"]


numbers = int(input("enter a number between 1 to 10 :"))

if (numbers>10):
    print("Incorrect Output")
elif(numbers<10):
    print(f"Here are contents for {numbers}.txt")