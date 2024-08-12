a =[[1,2,3] ,['Kaushik'] ] # This is the list which contains the multiple value in the ordered way . Here each [] is the single objects .
print ("Your rooll number is " ,a)    # Here we are printing the value of the list .
print (a[-2])     # This is for getting the value from the end of the list  .
print (len(a))    # This is for getting the length of the list.
del a[0]
print (a)
b = ['a','d','g','f'] + [1,2,3,4,5]   # The list can perform the concatation too .
print (b)

# Working with the list  here we have created the complex programm to ease the data processing 
catNames = []
while True :
    print ("Enter the name of the cat " + str (len(catNames)+1)+ '(Or Just press the Enter nothing to stop.):')
    name = input()
    if name == '':
        break 
    catNames = catNames + [name]   # We used the concept of the list concation 
    print ('The cat names are :')
    for name in catNames:
       print (''+name)