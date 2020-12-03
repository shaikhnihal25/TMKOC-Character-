import random

man1 = "Jethalal"
woman1 = "Daya"
man2 = "Iyer"
woman2 = "Babita"
man3 = "Bhide"
woman3 = "Madhvi"
man4 = "Soddhi"
woman4 = "Roshan"
man5 = "Mr.Hathi"
woman5 = "Mrs.Hathi"
man6 = "Tarak"
woman6 = "Anjali"
man7 = "Popatlal"
man8 = "Champak ChaCha"
man9 = "Bagha"
woman7 = "Bavri"
man10 = "Nattu Kaka"
man11 = "Tapu"
woman8 = "Sonu"
man12 = "Goli"
man13 = "Gogi"
man14 = "Pinku"
man15 = "Abdul"
# man

mens = man1, man2, man3, man4, man5, man6, man7, man8, man9, man10, man11, man12, man13, man14, man15

# woman

womens = woman1, woman2, woman3, woman4, woman5, woman6, woman7, woman8

source1m = random.choice(mens)
source2m = random.choice(mens)
source1w = random.choice(womens)
source2w = random.choice(womens)
a = input("Enter Player 1 Name: ")
b = input("Enter Player 2 Name: ")
c = input("Player 1 Gender : ")
d = input("Player 2 Gender : ")

# engine

if c == "male":
    print(a + " is a " + source1m)
elif c == "female":
    print(a + " is a " + source1w)
if d == "male":
    print(b + " is a " + source2m)
elif d == "female":
    print(b + " is a " + source2w)
else:
    print("Wrong Property Entered !")
