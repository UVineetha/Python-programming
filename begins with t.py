n = input("enter a string: ")
l = "t"
res = len([str for str in n.split() if l in str])
print("Words begins with t : " + str(res))


#sample process 


#n = "there is a man called tata"
#print("The original string is : " + str(n))
#letter = "t"
#res = len([ele for ele in n.split() if letter in ele])
#print("Words count : " + str(res))

#n = input("enter a string: ")
#l = input("enter the letter: ") 
#res = len([str for str in n.split() if l in str])
#print("Words count : " + str(res))

'''
a=input("enter the string")
def words(string):
    
   count=0
   
   for word in string:
       
       if word[0]=='T':
           
          count=count+1
          
          print(count)
words(a)
'''
