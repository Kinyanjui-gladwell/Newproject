# This file contains exercises in chapter 2
#2.1
message = 'Hello there'
print(message)
#2.2
message = 'Hello there'
print(message.title())
message = 'Hello'
print(message)
#2.3
name = 'Eric'
print("Hello there %s" % (name,))
#2.4
name = 'Mr Kaplan'
print(name.lower())
print(name.upper())
#2.5 & 2.6
famous_person = 'Albert Einstein'
quote = 'A person who never made a mistake never tried anything new'
print("%s once said '%s'" % (famous_person, quote))
quote = famous_person + " " + "once said" + " " + quote
print(quote)
#2.7
name = ' Mr Kaplan '
print("'%s'" %(name.rstrip()))
print("'%s'" %(name.lstrip()))
print("'%s'" %(name.strip()))
#2.8
print(4+4)
print(18-8)
print(int(64/8))
print(4*2)
#2.9
number = 7
print('my favourite number is %d'%(number))