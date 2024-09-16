
#here we will create a list funcitons

lucky_numbers = [98,8,54,15]
friends = ["ashu", "noshu", "podu", "podu", "ghochu"] #here we have to use third bracket
friends.sort() #it will short list the value as their alphabet
lucky_numbers.sort()
lucky_numbers.reverse()

friends.extend(lucky_numbers) #it will help to extend the friends with lucky_numbers
friends.append("Creed") #append will help to add a single value on it at the last position
friends.insert(1,"kelly") #er mane hocche 1 numebr index e kelly hobe 0 index
#thik thakbe ebong 2 number theke baki index er value o thik thakbe.
friends.remove("noshu") #remove kore dibe ei value k, don't matter what is the index
friends.pop() #last value k delete kore dibe. ekhane actually creed k delete kore diyeche

print(friends.index("podu")) #it will show the index number of the value
print(friends.count("podu")) #it will count how many time the value is in there

#friends.clear() #it will just clear all the value

print(friends)

friends2= friends.copy()
print(friends)

