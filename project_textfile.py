def title() :
print('\n' "------------------WELCOME TO CRYSTAL SUPERMARKET-----
---------"'\n')
title()
import pickle as pk
import os
def login():
a = input("ENTER PASSWORD : ")
if a == 'icsk' :
print('OPENING MAIN MENU...' '\n' 'MAIN MENU')
else :
print("INCORRECT PASSWORD. PLEASE TRY AGAIN.")
return
#MAIN MENU
#CHOOSE OFFICE STAFF
if a == 'icsk' :
print("THE WORKING STAFF")
print("1.MANAGER")
print("2. SUPERVISOR")
print("3. ANALYST")
print("4. CASHIER")
print("5. ADMINISTRATOR")
#INTRODUCTION To ANALYZE DATA
e = input("CHOOSE FROM 1-5 : ")
if e == '3':
h = input("ENTER ANALYST PASSWORD : ")
if h == 'hanabi' :
rep = True
while (rep) :
print("WELCOME TO SALES ANALYSIS")
print("1. Inserting Data")
print("2. Deletion of Data")
print("3. Updation of Data")
print("4. Searching for Data")
print("5. Report of the Data")
print("Analyze sales performance of market over the aspects : ")
print("6. General Sale Performance")
print("7. Category-wise sale Performance")
print("8. Customer-wise sale Performance")
print("9. Item-wise sale Performance")
print("10. Computing the number of items which were sold in the
category")
print("11. Computing the number of customers who puchased in the
category")
print("12. Exit")
ch = int(input("ENTER YOUR CHOICE(1-12) : " ))
if ch >= 12 or ch < 0 :
print ( "PROGRAM TERMINATED" )
break
else :
if ch == 1 :
insert()
if ch == 2 :
delete()
if ch == 3:
update()
if ch == 4 :
print('1. FOR SEARCHING ACCORDING TO THE CUSTOMER NAME')
print('2. FOR SEARCHING ACCORDING TO THE ITEM NAME')
print('3. FOR SEARCHING ACCORDING TO THE CATEGORY')
print('4. EXIT')
ch = int(input("ENTER YOUR CHOICE(1-4) : "))
if ch > 3 or ch < 0 :
print("PROGRAM TERMINATED")
break
c = input("DO YOU WISH TO CONTINUE(YES/NO) : ")
if c == 'NO' :
print("PROGRAM TERMINATED")
rep = False
break
if ch == 1 :
search1()
if ch == 2 :
search2()
if ch == 3 :
search3()
if ch == 5 :
access()
if ch == 6 :
analysis()
if ch == 7 :
catg()
if ch == 8 :
cust()
if ch == 9 :
item()
if ch == 10 :
cnt_cust1()
if ch == 11 :
cnt_items1()
c = input("DO YOU WISH TO CONTINUE(YES/NO) : ")
if c == 'NO':
print("PROGRAM TERMINATED")
rep = False
break
else :
print("INCORRECT ANALYST PASSWORD. PLEASE TRY AGAIN."
else :
print("INVALID")
login()
#TO INSERT USER FRIENDLY DATA
def insert() :
bf = open('proj.dat', 'wb')
n = int(input('ENTER NUMBER OF SALES DATA ENTRIES : '))
for i in range(n) :
ITEM_CATEGORY = (input('ENTER ITEM CATEGORY :'))
ITEMNAME = input('ENTER ITEM NAME : ')
PRICE = int(input("ENTER PRICE :"))
CUSTOMER = input("ENTER CUSTOMER NAME : ")
CARD_TYPE = input("ENTER CARD TYPE : ")
sales = [ITEM_CATEGORY, ITEMNAME, PRICE, CUSTOMER, CARD_TYPE]
pk.dump(sales,bf)
bf.close()
#TO DELETE OR EXCHANGE AN ITEM BOUGHT BY THE CUSTOMER
def deleting() :
found = 0
nf = open("proj.dat", 'rb')
ra = open("newproj.dat", 'wb')
try :
n = input("ENTER THE ITEMNAME TO BE DELETED :")
found = 0
while True :
sale = pk.load(nf)
if sale[1] == n :
found = 1
pass
else :
pk.dump(sale, ra)
except :
ra.close()
nf.close()
os.remove('proj.dat')
os.rename('newproj.dat', 'proj.dat')
if found == 0 :
print("record not found")
else :
print('record found')
#INSERTING A NEW ITEM INTO THE RECORD
def update() :
s = input("ENTER THE FILE NAME : ")
r = open(s,'ab')
n = int(input("ENTER NUMBER OF SALES DATA ENTRIES :"))
for i in range(n) :
ITEM_CATEGORY = input('ENTER ITEM CATEGORY :')
ITEMNAME = input('ENTER ITEM NAME : ')
PRICE = int(input("ENTER PRICE : "))
CUSTOMER = input("ENTER CUSTOMER NAME : ")
CARD_TYPE = input( "ENTER CARD TYPE : ")
sales = [ITEM_CATEGORY, ITEMNAME, PRICE, CUSTOMER, CARD_TYPE]
pk.dump(sales, r)
r.close()
#TO SEARCH FOR A CUSTOMER, AN ITEM, AN ITEM_CATEGORY
def search1() :
bf = open ('proj.dat', 'rb')
try :
a = input("ENTER CUSTOMER'S NAME : ")
print('ITEM_CATEGORY ITEMNAME PRICE CUSTOMER CARD_TYPE')
while True :
sale = pk.load(bf)
if sale[3] == a :
print(sale[0], sale[1], sale[2], sale[3], sale[4], sep = '\t')
except :
bf.close()
def search2() :
bf = open("proj.dat", 'rb')
try :
a = input("ENTER ITEM NAME : ")
print('ITEM_CATEGORY ITEMNAME PRICE CUSTOMER CARD_TYPE')
while True :
sale = pk.load(bf)
if sale[1] == a :
print(sale[0], sale[1], sale[2], sale[3], sale[4], sep = '\t')
except :
bf.close()
def search3() :
bf = open("proj.dat", 'rb')
try :
a = input("ENTER CATEGORY : ")
print('ITEM_CATEGORY ITEMNAME PRICE CUSTOMER CARD_TYPE')
while True :
sale = pk.load(bf)
if sale[0] == a :
print(sale [0], sale [1], sale [2], sale [3], sale [4], sep='\t')
except :
bf.close()
#TO ACCESS DATA
def access() :
bf = open('proj.dat', 'rb')
try :
print('ITEM_CATEGORY ITEMNAME PRICE CUSTOMER CARD_TYPE')
while True :
sales = pk.load(bf)
print(sales[0], sales[1], sales[2], sales[3], sales[4], sep = '\t')
except :
bf.close()
#SECTION-WISE ANALYSIS
#COMPUTING GENERAL ANALYSIS
def analysis() :
total_price = 0
bf = open("proj.dat", 'rb')
substring = input("ENTER THE CATEGORY ACCORDING TO WHICH YOU'D LIKE TO COMPUTE
THE PRICE : ")
try :
while True :
sale = pk.load(bf)
if sale[0] == substring :
total_price += sale[2]
except :
bf.close()
print("TOTAL PRICE = ", total_price)
n = int(input("ENTER THE NO OF ITEMS : " ))
avg = total_price/n
print("AGGREGATE OF SALES IS : ", avg)
#PROFIT AND LOSS FOR A MONTH
if avg <= 1000000 :
print("EXPERIENCING LOSS")
print("RESULT : REQUIRES AN EXTENSION IN SALES")
elif avg > 2000000 :
print("EXPERIENCING PROFIT")
else :
print("BALANCED CONDITION")
#COMPUTING CATEGORY WISE SALES PERFORMANCE
def catg() :
i = 0
bf = open("proj.dat", 'rb')
substring = input("ENTER THE CATEGORY ACCORDING TO WHICH YOU'D LIKE TO COMPUTE
THE PRICE : ")
try :
while True :
sale = pk.load(bf)
if sale [0] == substring : # this statement checks if the required
substring is in the file.
i += sale[2]
except :
bf.close()
print('THE CATEGORY OF', substring, 'HAD', i, 'SALE')

17

#COMPUTING CUSTOMER WISE SALES PERFORMANCE
def cust() :
i = 0
bf = open("proj.dat", 'rb')
substring = input("ENTER THE CUSTOMER NAME ACCORDING TO WHICH YOU'D LIKE TO
COMPUTE THE PRICE")
try :
while True :
sale = pk.load(bf)
if sale[3] == substring :
i += sale[2]
except :
bf.close()
print('THE CUSTOMER', substring, 'DID PURCHASE OF', i,)
#COMPUTING ITEM WISE SALES PERFORMANCE
def item() :
i = 0
bf = open("proj.dat", 'rb')
substring = input("ENTER THE ITEM NAME ACCORDING TO WHICH YOU'D LIKE TO COMPUTE
THE PRICE")
try :
while True :
sale = pk.load(bf)
if sale[1] == substring :
i += sale[2]
except :
bf.close()
print('THE ITEM', substring, 'HAD A TOTAL SALE OF', i,)
#BASIC ANALYSIS
#COMPUTING THE NUMBER OF CUSTOMERS WHO PURCHASED IN THE CATEGORY
def cnt_cust1() :
count = 0
bf = open("proj.dat", 'rb')
substring = input("ENTER THE CATEGORY ACCORDING TO WHICH YOU'D LIKE CHECK : ")
try :
while True :
sale = pk.load(bf)
if sale [0] == substring :
count += 1
except :
bf.close()
print('THE CATEGORY OF', substring, 'HAD', count, 'NUMBER OF CUSTOMERS')
#COMPUTING THE NUMBER OF ITEMS WHICH WERE SOLD IN THE CATEGORY
def cnt_items1() :
count = 0
bf = open("proj.dat", 'rb')
substring = input("ENTER THE ITEM NAME ACCORDING TO WHICH YOU'D LIKE TO CHECK :
")
try :
while True :
sale = pk.load(bf)
if sale[1] == substring :
count += 1
except :
bf.close()
print('THE ITEM', substring, 'WAS SOLD', count, 'TIMES')
