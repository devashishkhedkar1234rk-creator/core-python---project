name="Devashish"

#1 Positive index slicing
print(name[0:5])        #Devas
print(name[2:7])        #vashi

#2 Negative index slicing
print(name[-5:-1])      #shis

#3 Negative index + Positive index
print(name[5:-1])        #his

#4 Positive index + Negative index
print(name[-7:5])        #vas

#5 Combination of Positive and Negative
print(name[2:-1])         #vashis

#6 Start from beginning
print(name[:5])          #Devas

#7 End at last
print(name[3:])         #ashish

#8 Negative slicing from end
print(name[:-3])         #Devash

#9 Reverse string using slicing
print(name[::-1])        #hshisaveD

#10 Starting from index 1 , every 3rd character
print(name[1::3])         #ess