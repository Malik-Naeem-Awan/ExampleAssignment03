#!/usr/bin/env python
# coding: utf-8

# # Assignment 3

# In[1]:


#Task 1 
#Python Program to Add a Key-Value Pair to the Dictionary 
#Problem Solution: 
#1. Take a key-value pair from the user and store it in separate variables. 
#2. Declare a dictionary and initialize it to an empty dictionary. 
#3. Use the update() function to add the key-value pair to the dictionary. 
#4. Print the final dictionary. 
#5. Exit. 


# In[17]:


key=int(input("Enter the (int) Key of the value: "))
value=int(input("Enter(int) value of key: "))
assignment=dict()
pair_dict={}
assignment.update([(key,value)])
print(assignment)


# In[18]:


#Task 2 
#Python Program to Concatenate Two Dictionaries Into One 
#Problem Solution 
#1. Declare and initialize two dictionaries with some key-value pairs 
#2. Use the update() function to add the key-value pair from the second dictionary to the first dictionary. 
#3. Print the final dictionary. 
#4. Exit. 


# In[20]:


d1={'A':1, 'B':2}
d2={'c':3}
d1.update(d2)
print("The Updated dictionary or Concatenated DICTIONARY : ",d1)


# In[1]:


#Task 3 
#Python Program to Check if a Given Key Exists in a Dictionary or Not 
#Problem Solution 
#1. Declare and initialize a dictionary to have some key-value pairs. 
##2. Take a key from the user and store it in a variable. 
#3. Using an if statement and the in operator, check if the key is present in the dictionary using the dictionary.keys() method. 
#4. If it is present, print the value of the key. 
#5. If it isn’t present, display that the key isn’t present in the dictionary. 
#6. Exit. 


# In[5]:


dict1={'A':1, 'B':2,'C':3}
key=input("Enter the Key you want to display the value for: ")
if key in dict1.keys():
    print("The Key is Present in the Dictionary. ")
    print(dict1[key])
else:
    print("The Key is not present in dictionary")


# In[6]:


#Task 4 
#Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x). 
#Problem Solution 
#1. Take a number from the user and store it in a separate variable. 
#2. Declare a dictionary and using dictionary comprehension initialize it to values keeping the number 
#between 1 to n as the key and the square of the number as their values. 
#3. Print the final dictionary. 
#4. Exit. 


# In[9]:


n=int(input("Input a number "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d)


# In[10]:


#Task 5 
#Python Program to Sum All the Items in a Dictionary 
#Problem Solution 
#1. Declare and initialize a dictionary to have some key-value pairs. 
#2. Find the sum of all the values in the dictionary. 
#3. Print the total sum. 
#4. Exit. 


# In[14]:


d = dict()
sum=0
for x in range(1,3):
    d[x]=x
for c in range(1,3):
    sum=sum+d[x]
print("The Total Sum is: " , sum)


# In[15]:


#Task 6 
#Python Program to Multiply All the Items in a Dictionary 
#Problem Solution 
#1. Declare and initialize a dictionary to have some key-value pairs. 
#2. Initialize a variable that should contain the total multiplied value to 1. 
#3. Use the for loop to traverse through the values of the dictionary. 
#4. Then multiply all the values in the dictionary against each other. 
#5. Print the total multiplied value. 
#6. Exit. 


# In[17]:


d = dict()
product=1
for x in range(1,5):
    d[x]=x
for c in range(1,5):
    product=product*d[x]
print("The Total Sum is: " , product)


# In[18]:


#Task 7 
#Python Program to Remove the Given Key from a Dictionary 
#Problem Solution 
#1. Declare and initialize a dictionary to have some key-value pairs. 
#2. Take a key from the user and store it in a variable. 
#3. Using an if statement and the in operator, check if the key is present in the dictionary. 
#4. If it is present, delete the key-value pair. 
#5. If it isn’t present, print that the key isn’t found and exit the program. 
#6. Exit. 


# In[30]:





# In[ ]:





# In[29]:


d = {'a':1,'b':2,'c':3,'d':4}
print("Initial dictionary")
print(d)
key=input("Enter the key to delete(a-d):")
if key in d: 
    del d[key]
else:
    print("Key not found!")
    exit(0)
print("Updated dictionary")
print(d)


# In[31]:


#Task 8 
#Python Program to Map Two Lists into a Dictionary 
#Problem Solution 
#1. Declare two empty lists and initialize them to an empty list. 
#3. Consider a for loop to accept values for the two lists. 
#4. Take the number of elements in the list and store it in a variable. 
#5. Accept the values into the list using another for loop and insert into the list. 
#6. Repeat 4 and 5 for the values list also. 
#7. Zip the two lists and use dict() to convert it into a dictionary. 
#8. Print the dictionary. 
#9. Exit. 


# In[36]:


keys=[]
values=[]
n=int(input("Input Number of elements of list you want to enter: "))
for x in range(1,n+1):
    value=int(input("Enter the value for 1st list:"))
    keys.append(value)
for x in range(1,n+1):
    value=int(input("Enter the value for 2nd list:"))
    values.append(value)
dict_maped=dict(zip(keys,values))
print(dict_maped)

    
    


# In[37]:


#Task 9 
#Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary 
#Problem Solution 
#1. Enter a string and store it in a variable. 
#2. Declare a list variable and initialize it to an empty list. 
#3. Split the string into words and store it in the list. 
#4. Count the frequency of each word and store it in another list. 
#5. Using the zip() function, merge the lists containing the words and the word counts into a dictionary. 
#3. Print the final dictionary. 
#4. Exit. 


# In[41]:


test_string=input("Enter string:")
l=[]
l=test_string.split()
wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))


# In[42]:


#Task 10 
#Python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character 
#Problem Solution 
#1. Enter a string and store it in a variable. 
#2. Declare an empty dictionary. 
#3. Split the string into words and store it in a list. 
#4. Using a for loop and if statement check if the word already present as a key in the dictionary. 
#5. If it is not present, initialize the letter of the word as the key and the word as the value and append 
#it to a sublist created in the list. 
#6. If it is present, add the word as the value to the corresponding sublist. 
#7. Print the final dictionary. 
#8. Exit.


# In[44]:


test_string=input("Enter string:")
l=test_string.split()
d={}
for word in l:
    if(word[0] not in d.keys()):
        d[word[0]]=[]
        d[word[0]].append(word)
    else:
        if(word not in d[word[0]]):
          d[word[0]].append(word)
for k,v in d.items():
        print(k,":",v)


# In[ ]:





# In[ ]:




