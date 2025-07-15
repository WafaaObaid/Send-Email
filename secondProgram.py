
#t,w,r=8,3.2,7
#print(t,w,r)


#x = input("Enter first number: ")

'''
#set 
x={2,3,4,5}
x.add(9)
x.pop()
print(x)

y={"w","e","r","t"}
y.add("n")
print(y)

#list
arr=[1,2,3,4]
arr[0]=2
print(arr)

#dict --> key and value
dic={"Wafaa":90, "Ali":60, "Asmaa":85}
print(dic)
'''

'''
x= 2.5
y=int(x)
print(y)
'''

'''
x=2+3
print("x= ",x)

y=5-2
print("y= ",y)

w=3*2
print("w= ",w)

r=6/2
print("r= ",r)

a=7%2
print("a= ",a)

t=2**3
print("t= ",t)
'''
'''
x=7
y=x/2
print(y)

first="100" #string
second="150"
print(first+second)
'''

'''
str="Hello World"
print(str) # it will print the whole word
print(str[0]) # it will print the first letter
print(str[2:5]) # it will print the letters from letter 2 to letter 5
print(str[2:]) # it will print the letters from 2 to the end of the word
print(str*2) # it will repet the word tiwce
print(str+"TEST") # it prints concatendated string
'''


# x is y --> x is the same as y
# x is not y --> x is not the same as y
# x==y --> is x equal y
# x != y --> is x not equal y

'''
import math
#رح يجيبلي اللوق العاشر لرقم 
signal_power = 9.
noise_power = 10.
ratio = signal_power/noise_power
decibels = 10*math.log10(ratio)
print(decibels)
'''


# Full example for week 2
import smtplib #مكتوب فيها كيفية التعامل مع الايميل و ارسال بريد 
sender = "ali@psut.edu.jo"
receivers = ["ahmad@pust.edu.jo"]
message = "I would like to invite you to python course"
try:
  smtpObj = smtplib.SMTP('www.psut.edu.jo') #رح ياخد اسم السيرفر يلي رح يبعت عليه الرسالة
  smtpObj.sendmail(sender, receivers, message) #ياخد اقواس المرسل و المستقبل و الرسالة رح تاخد السيرفر و ترسل الرسالة
  print("Succefully sent email")
except:
  print("Error: Unable to send email")   