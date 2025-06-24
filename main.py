# from selectors import SelectSelector
#
# x=5 #theto integer
# print("x") #prosoxi etsi to diavazei san x sketo kai oxi 5
# print(str(x)) #str(x) -> 5 ->"5"


# askisi1
# y=4
# x=5
# athroisma = x + y
# print(str(athroisma))

def athroisma(ar1, ar2):
    print(ar1 + ar2)

# athroisma(4 , 5)



#askisi2


# print("geia sou kosma")

def leksi(grapse_th_leksi):
    print(grapse_th_leksi)

# leksi("γεια σου κοσμα")




#askisi3

# a = 5
# b = 3
# sunolo = a + b
# print(sunolo)

def sunolo(ar1, ar2):
    print(ar1 + ar2)

# sunolo(5, 3)


# askisi4

# a = 10
# b = 2
# afairesi = 10-2
# print(afairesi)
#
def afairesi(ar1, ar2):
    print(ar1 - ar2)

# afairesi(4, 6)


#askisi5
# a = 4
# b = 6
# pollaplasiase = a * b
# print(pollaplasiase)
#

def pollaplasiase(ar1, ar2):
    print(ar1 * ar2)

# pollaplasiase(4, 6)


#askisi6

# a = 20
# b = 4
# diairesh = 20/4
# print(diairesh)
#
def dieraish(ar1, ar2):
    print(ar1 / ar2)

# dieraish(20, 4)

#askisi7

# print("Καλημέρα Κόσμε!")

def leksi(ektupwse):
    print(ektupwse)

# leksi("καλημέρα κόσμε!")

#askisi8

# print("Η Python είναι διασκεδαστική!")


def leksi(ektupwse):
    print(ektupwse)

# leksi("Η Python είναι διασκεδαστική!")

# 23/6/2025 πρωτες ασκησεις επαναληψης απο εδω και πανω ^


# 24/6/25 επαναληψη

# exercise 1

# onoma = "Μαρία"
# hlikia = 25
# stoixeia = "Η Μαρία είναι 25 ετών"
# print(stoixeia)





#  exercise 2

# α = 15
# b = 4
# διαιρεση = α / b
# print(διαιρεση)
#

def diairesh(ar1, ar2):
    print(ar1/ar2)

# diairesh(15, 4)



#  exercise 3

# χ = 3
#
# χ5 = χ ** 5
# print(χ5)



# exercise 4

# p = 7
#
# if p == 7:
#     print("Ο Αριθμός είναι Περιττός")
# elif p == 6:
#     print("Ο αριθμός είναι Άρτιος")


# exercise 5
# ar1 = 105
# ar2 = 96

# if ar1 > ar2:
#     print(ar1)
# elif ar1 < ar2:
#     print(ar2)


# exercise 6
#
# for number in range(10):
#     print("αριθμός",number)


# exercise 7
#
# x = 5
#
# while x <=50:
#     print(x)
#
#     x +=5


# exercise 8


# list = [2, 4, 6, 8, 10]
# print(sum(list))


# exercise 9


#
# x = float(input("δωσε εναν αριθμο"))
# if x % 2 == 0:            #γιατι χρησιμοποιω στην ευκλειδια διαιρεση το 2 επι κάτι σύν κατι
#     print("ο αριθμος ειναι αρτιος")
# elif x % 2 == 1:
#     print("ο αριθμος ειναι περιττος")



# x = float(input("αριμος 1"))
# y = float(input("αριθμος 2"))
# if x > y:
#     print(str(x))
# elif x < y:
#     print(str(y))




# a = str(input("δωσε ενα ονομα"))
# print(a)
# arithmos_gramaton = len(a)
# print(str(arithmos_gramaton))
# if len(a) > 8:
#     print("Γεια σου")




# # 8/6/2025

#exercise 1


# ar = int(input("δωσε εναν ακεραιο αριθμο"))
# if ar >= 1:
#     print(str("ο αριθμος είναι θετικος"))
# elif ar == 0:
#     print(str("ο αριθμός ειναι μηδεν "))
# elif ar <= -1:
#     print(str("ο αριθμος ειναι αρνητικος"))


# exercise 2


# ar1 = float(input("εισαγετε τον αριθμο 1"))
# ar2 = float(input("εισαγετε τον αριθμο 2"))
# if ar1 == ar2:
#     print(str("οι αριθμοι είναι ισοι"))
# elif ar1 < ar2:
#     print(str("ο αριθμός 2 είναι μεγαλυτερος απο τον αριθμο 1 "))
# elif ar1 > ar2:
#     print(str("ο αριθμος 1 ειναι μεγαλυτερος απο τον αριθμο 2"))
#
# exercise 3

# vathmos = 95

# vathmos = int(input("εισάγετε τον βαθμό σας"))

# if vathmos >= 95:
#     print(str("ο βαθμός σας ειναι Αριστος"))

# elif vathmos >= 85 and vathmos < 95:
#     print(str("o βαθμός σας ειναι Πολύ καλος"))

# elif vathmos >= 60 and vathmos < 85:
#     print(str("ο βαθμός σας ειναι Καλος"))

# elif vathmos <= 60:
#     print(str("ο βαθμος σας ειναι Ανεπαρκής"))


# exercise 4

# hlikia = int(input("εισάγετε την ηλικία σας"))
# if hlikia >= 18:
#     print(str("ο χρηστης ειναι ενηλικας"))
# elif hlikia <= 18:
#     print(str("ο χρηστης ειναι ανηλικος"))


 # exercise 5
# arithmos = float(input("γραψε εναν αριθμο "))
# if arithmos % 3 == 0 and arithmos % 5 == 0:
#     print(str("lucky number"))
# else:
#     print(str("ακυρος αριθμος"))

# exercise 6

# etos = int(input("γραψε ενα ετος "))
# if etos % 4 == 0:
#     if etos % 100 != 0:
#         print(str("ειναι δισεκτο ετος"))
#     elif etos % 100 == 0:
#         print(str("το ετος δεν ειναι δισεκτο"))
# elif etos % 4 != 0:
#     print(str("το ετος δεν ειναι δισεκτο"))








# exercise 7
# kodikos =str(input("δωσε κωδικο"))
# if kodikos == "python123":
#     print("σωστος κωδικος")
# elif kodikos !="python123":
#     print("λαθος κωδικος")




# exercise 8

# ar1 = float(input("δωσε τον πρωτο αριθμο"))
# ar2 = float(input("δωσε τον δευτερο αριθμο"))
# ar3 = float(input("δωσε τον τριτο αριθμο"))
# if ar1 > ar2:
#     if ar1 > ar3:
#         print(str("ο αριθμος 1 ειναι ο μεγαλυτερος"))
#     elif ar3 > ar1:
#         print(str("ο αριθμος 3 ειναι ο μεγαλυτερος"))
# elif ar2 > ar1:
#     if ar2 > ar3:
#         print(str("ο αρθιμος 2 ειναι ο μεγαλυτερος"))
#     elif ar3 > ar2:
#         print(str("ο αριθμος 3 ειναι μεγαλυτερος"))


# hard exercises 9/6/25

# exercise 1

# arithmos = float(input("γραψε εναν αριθμο"))






# exercise 3



# exercise 4

# protasi = str(input("γραψε την προταση"))

# for protasi in range ( 4 ):
#     print(protasi)



# exercise 5
# code = str(input("γραψε τον κωδικο"))
# if code == "admin2024":
#     print("ο κωδικος ειναι σωστος")

# if code != "admin2024":
#     print("εχετε αλλες 2 προσπάθειες")

# code = str(input("ξανα γραψε τον κωδικο"))
# elif code != "admin2024":
#     print("τελευταια προσπαθεια")


# exercise 6
# varos = float(input("γραψε το βαρος σου"))
# ipsos = float(input("γραψε το υψος σου"))
# bmi = varos / (ipsos * 2)
#
# if bmi > ipsos:
#     print(str(f"ο δεικτης μαζας σωματος σου ειναι {bmi} και είσαι παχυσαρκος "))



# exercise 7




# exercise 8



# loops exercises 11/6/25

# exercise 1

# for i in range ( 1, 11):
#     print(i)

# exercise 2

# for i in range (2, 21): # γιατι οταν αντι για 2 βαζω 1 μεσα στη παρενθεση τρεχει και παλι σωστα το προγραμμα ?
#     if i % 2 == 0:
#         print(i)

# for i in range (55, 1001):
#     if i % 7 == 0:
#         print(i)



# exercise 3
# for i in range (1, 6):
#     print("καλημέρα")

# exercise 4
#
# sum = 0
# for i in range (1, 101):
#     sum = sum + i
# print(sum)


# prod = 1
# for i in range (1, 101):
#     prod = prod * i
# print(prod)

# exercise 5
# for letter in "python":
#     print(letter)

# count = 0 #πριν ξεκινησω την αναζητηση δεν εχω καποιο "ταφ" ακομα
# for letter in "The if condition is considered the simplest of the three and makes a decision based on whether the condition is true or not. If the condition is true, it prints out the indented expression. If the condition is false, it skips printing the indented expression.":
#     if letter == 't' or  letter == 'T':
#         count = count + 1
# print(count)


# count = 0 #πριν ξεκινησω την αναζητηση δεν εχω καποιο κεφαλαιο γραμμα
# for letter in "The if condition is considered the simplest of the three and makes a decision based on whether the condition is true or not. If the condition is true, it prints out the indented expression. If the condition is false, it skips printing the indented expression.":
#     if letter.islower():
#         count = count + 1
# print(count)



# exercise 6

# exercise 7

# exercise 8


# for i in range ( 1, 51):
#     ipoloipo = i % 2
#     if ipoloipo == 1:
#         print(i)



def leksi():
    print("γεια σου!")

# leksi()

def apotelesma(arithmos1, arithmos2, arithmos3, arithmos4 , arithoms5):
    print((arithmos1 + arithmos2 + arithmos3 + arithmos4 + arithoms5)/5)

# apotelesma(5, 3 ,123 , 45, 32 )


def protasi(protasi1):
    count = 0
    for letter in protasi1:
        if letter == "ε":
            count = count + 1
    print(count)

# protasi("γεια σου φιλε")


def sinartisi(arithmos1):
    if arithmos1 % 2 == 0:
        print("ειναι αρτιος")
    elif arithmos1 % 2 == 1:
        print("ειναι περιττος")

# sinartisi(11)


def apotelesma(arithmos):
    for i in range (1, arithmos + 1):
        print(i)

# apotelesma(49)