#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to t
#hat person. Your message should b
#e simple, such as, “Hello Eric, would you like to learn some Python today?”
name: str= "Mario"
message: str= f"ciao {name}, ti va di imparare un pò di Python insieme?"
print(message)


#2-4. Name Cases: Use a variable to represent a person’s name, and 
#then print that person’s name in lowercase, uppercase, and title case.
name: str="Mati"
print(name.lower())
print(name.upper())
print(name.title())


#2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote
# and the name of its author. Your output should look something like the following,
# including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”
name: str="Albert Einstein"
quote: str="once said, “A person who never made a mistake never tried anything new.\""
print(f"{name} {quote}")


#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called 
#famous_person. Then compose your message and represent it with a new variable
# called message. Print your message. 
famous_person: str="Maria"
message: str="once said, “A person who never made a mistake never tried anything new.\""
print(f"{famous_person} {message}")


#2-8. File Extensions: Python has a removesuffix() method that works exactly
# like removeprefix(). Assign the value 'python_notes.txt' to 
# a variable called filename. Then use the removesuffix() method to display 
#the filename without the file extension, like some file browsers do.
filename: str="python_notes.txt"
filename = filename.removesuffix(".txt")
print(filename)


#3-1. Names: Store the names of a few of your friends
#in a list called names. Print each person’s name by accessing each element in the list, one at a time.
names: list=["Simone", "Luca", "Mattia"]
print(names[0])
print(names[1])
print(names[2])


#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, 
#print a message to them. 
#The text of each message should be the same, but each message should be personalized with the person’s name.
names: list=["Simone", "Luca", "Mattia"]
message1: str="Roma"
message2: str="Lazio"
message3: str="disinteressato"
print(f"{names[0]} {message1}")
print(f"{names[1]} {message2}")
print(f"{names[2]} {message3}")


#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, 
#and make a list that stores several examples. 
#Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
example: list=["car", "bike", "motorcycle"]
statements1: str="Ferrari is the better"
statements2: str="Mountain bike is the better"
statements3: str="I would like to own a Honda motorcycle"
print(f"{example[0]} {statements1}")
print(f"{example[1]} {statements2}")
print(f"{example[2]} {statements3}")


#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
#Make a list that includes at least 
#three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
GuestList: list=["Matilde", "Giulia", "Chiara", "Fabiana"]
for people in GuestList:
    print(f"{people} come tonight")


#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set
# of invitations. You’ll have to think of someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end of your program, 
#stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still in your list.
GuestList2: list=["Matilde", "Giulia", "Chiara", "Francesca"]
for people in GuestList2:
    print(f"{people} are you come tonighit?")


#3-6. More Guests: You just found a bigger dinner table, so now more space is available.
#Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, 
#informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.
GuestList2: list=["Matilde", "Giulia", "Chiara", "Francesca"]
GuestList2.insert(0,"Ronaldo")
GuestList2.insert(1,"Messi")
GuestList2.append("Immobile")
for people in GuestList2:
    print(f"{people} When coming?")


#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive
# in time for the dinner, and now you have space for only two guests.
#• Start with your program from Exercise 3-6. Add a new line that prints a message
# saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only two names remain 
#in your list. Each time you pop a name from your list, print a message to that person 
#letting them know you’re sorry you can’t invite them to dinner.
#• Print a message to each of the two people still on your list, letting them know they’re still invited.
#• Use del to remove the last two names from your list, so you have an empty list. 
#Print your list to make sure you actually have an empty list at the end of your program.
GuestList2: list=["Matilde", "Giulia", "Chiara", "Francesca"]
GuestList2.insert(0,"Ronaldo")
GuestList2.insert(1,"Messi")
GuestList2.append("Immobile")
for people in GuestList2:
    print(f"{people} When coming?")
print("i can invite only two people")
GuestList2.pop(4)
GuestList2.pop(5)
GuestList2.pop(3)
GuestList2.pop(3)
GuestList2.pop(2)
for people in GuestList2:
    print(f"{people} you are teh guest")
del(GuestList2[:])
print(GuestList2)


#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse-alphabetical order.
#Print the list to show that its order has changed.
places: list=["Italy", "Greece", "USA", "France"]
print(places)
print(sorted(places))
print(sorted(places)[::-1])
places.sort()


#3-9. Dinner Guests: Working with one of the programs from Exercises 3, 
#use len() to print a message indicating the number of people you’re inviting to dinner.
GuestList2: list=["Matilde", "Giulia", "Chiara", "Francesca"]
favoriteGuest=len(GuestList2)
print(favoriteGuest)


#3-10. Every Function: Think of things you could store in a list. 
#For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
#Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
cities: list=["Roma", "Milano", "Genova"]
mycities=len(cities)
print(mycities)
for(città) in(cities):
    print(f"{città} i'm visited")
del(cities[:])
print(cities)