#This file contains exercises in chapter 3
#3.1
names = ['Eric', 'Kaplan', 'Dave', 'Mary', 'Nelly']
for i in names:
    print(i)
#3.2
for i in names:
    print('%s, Welcome home!' %(i))
#3.4 and 3.5
guest_list = ['Kai', 'Kenobi', 'Kaplan']
for i in guest_list:
    print("Dear %s, you're invited to dinner" %(i))
#3.6
for i in guest_list:
    print("Hey %s, we have found a bigger table!" %(i))
print ("Here's the new guest list")
guest_list.insert(0, "Tom")
print(guest_list)
guest_list.append("Grennan")
print(guest_list)
for i in guest_list:
    print("Hello %s, you're invited to dinner at The Delia" %(i))
print("unfortunately, our table will not be available in time, here's the revised list of attendance")
guest_one=guest_list.pop(0)
print("unfortunately %s, we are unable to seat you." %(guest_one))
guest_two=guest_list.pop(3)
print("unfortunately %s, we are unable to seat you." %(guest_two))
guest_three=guest_list.pop(2)
print("unfortunately %s, we are unable to seat you." %(guest_three))
print(guest_list)
guest_list.remove('Kai')
print(guest_list)
del guest_list[0]
print(guest_list)