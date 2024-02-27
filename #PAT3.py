#PAT3
#ques 1 create 2 list which is having all even number and one is having all odd numbers
list1=[10,501,22,100,999,87,351]
list2=[] #new list to store even numbers
list3=[] #new list to store odd numbers
for i in list1:
    if i%2==0:
        list2.append(i)

    else:
        list3.append(i)


print("list of even no.:", list2)
print("list of odd no:", list3)


# Pat3 ques no2 to count primer number and create a new list of prime numbers
list=[10,501,22,37,100,999,87,351]
list_prime=[] #new list which will contain prime number
for i in list:
  list_prime.append(i)
  for j in range(2,i):
    
     if i%j==0:
       list_prime.remove(i)
       break
print("list of Prime number:",list_prime ,"\ncount of prime number in list:",len(list_prime))

#Pat 3 ques3 fine happy number from list given
def numSquareSum(n): #function to calculate square root of digits
    square_sum = 0
    while n:
        digit = n % 10
        square_sum += digit * digit
        n //= 10
    return square_sum

def isHappyNumber(num):        #function to check happy number is or not                                                                                                                        
    seen_numbers = set()
    while True:
        num = numSquareSum(num)
        if num == 1:
            return True
        if num in seen_numbers:
            return False
        seen_numbers.add(num)


list1=[10,501,22,100,999,87,351] #check for given list
hapynumberlist=[]
for i in list1:
    if isHappyNumber(i):
       hapynumberlist.append(i)
print("list of happy number:",hapynumberlist)
     

#pat3 ques 4 write  a program to fin sum of the first and last digit of an integer

int_n=input("enter any integer") #take a input  from user
number=str(int_n)  #convert it to string
first_digit=int(number[1])  #first index value of string and convert it to integer
last_digit=int(number[-1])   # last index value of string and cnvert it to integer
sum_of_digit=first_digit + last_digit #addition
print("sum of first and last digit:",sum_of_digit)

#pat 3 ques 5 find no of ways to ditribute managoes to each student in gyi class

def binomial_coefficient(m, n):
    res = 1
 
    if n > m - n:
        n = m - n
 
    for i in range(0, n):
        res *= (m - i)
        res /= (i + 1) 
 
    return res
 
# helper function for generating no of ways
# to distribute m mangoes amongst n people
def calculate_ways(n, m):
 
    # not enough mangoes to be distributed    
    if n<m:
        return 0
 
    # ways  -> (m + n-1)C(m-1)
    ways = binomial_coefficient(m + n-1, m-1)
    return int(ways)
 




#Pat3 ques 6 write a program to find duplicates in 3 list
L1=[3,5,6,9,1] #List 1
L2=[9,5,2] #list 2
L3=[5,2,4] # List 3
L5=[] #new blank list
L5= L1 + L2 + L3 #contantate 3 list to make one list
print(L5)
duplicateList=[] #to show duplicate list

for i in L5:
    if L5.count(i)>1 and i not in duplicateList: # condition to find duplicates
        duplicateList.append(i)


print("duplicate list :",duplicateList)




#pat3 ques7 python program to find the first non-repeating elements in a given list of integers
list1=[2,2,4,5,7,8,4,7,0]
set2=set(list1) #convert list into set
list2=list(set2) #then convert set to list
list2  #new list will be without non repeating integers.

# pat3 ques 8 write a python program to find the minium element rated in sorted list
List1=[24,67,89,23,45]
List1.sort() #apply sort function on list1
print("minmium rated element:", List1[0])


#Pat3 ques 9 :writea python program to find the triplets in list whose sum equal to 59

list1=[10,20,30,9] #given list
n=len(list1) #find the length of list
list_trplts=[] #blank list for result


for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if list1[i]+list1[j]+list1[k]==59: #condition
                list_trplts.append(list1[i]) #appending digits in new list
                list_trplts.append(list1[j])
                list_trplts.append(list1[k])
print("sum of triplets equal to 59:",list_trplts)


#Pat3 ques 10 sublist whose sum should be zero
list=[4,2,-3,1,6]
n=len(list)  #calculate length of List
sublist=[]  # new list to store result
for i in range(n):
    for j in range(i+1,n):
        for K in range(j+1,n):
            if (list[i]+list[j]+list[K]==0): # condition applied
                sublist.append(list[i])
                sublist.append(list[j])
                sublist.append(list[k])
print("sum of syublist whose sume equal to zero:",sublist)
       