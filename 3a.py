#concatenation
first_name= "poorvi"
last_name= "CS"
full_name= first_name +" " + last_name
print(full_name)
# repeatition
message = "this is a Warning! "
print(message*10)

print(message.upper())
print(message.lower())
#strip
print(message.strip()*2)
a=message.replace("Warning! ", "Error")
print(a)

name='''poorvi said 'hello'' 
 ammu said "hii"
'''
#lenght
print(name)
print(len(message))

name_1="poorvika"
print(name_1[3])   #index=position-1      position=index+1

#slicing
print(name_1[2:6]) #need from starting orto end donot specify the value beginging or end
print(name_1[:6])
print(name_1[3:])
print(name_1[-3])
print(name_1[ : :2])
#escape sequence
s="poorvi \n is\ta good girl"
print(s)