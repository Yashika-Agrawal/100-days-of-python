# import my_module
# print(my_module)
import random
random_integer= random.randint(1,10)
print(random_integer) #between 1 to 10 inclusive whole no.s

random_float= random.random()
print(random_float) #between 0 to 0.9999... in float value
print(random_float*5) #between 0 to 4.999... in float value

#Lists
states=["gwalior", "indore", "bhopal", "delhi", "mumbai"]
print(states[0])
print(states[-1]) #last item from the list
states[0]="bangalore"
states.append("nagpur") #add an item to the end of the list
states.extend(["kolkata", "chennai"]) #add a bunch of items
print(states)

words= "hello how are you?"
print(words.split(" ")) #split the string into a list, " " is the separator 

#to select random name from a list
names_string= input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
random_idx= random.randint(0, len(names)-1)
print(names[random_idx] + " is going to buy the meal today!")




