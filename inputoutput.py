#File I/O


# write a file
file_handler = open('text.txt', 'w')
file_handler.write('Oh my gosh I\'m writing new things to my file, let\'s see how it works!')
file_handler.close()

#this overwrote the file I had initially, if you don't want to do that, you can append to a file!

#append a file
file_handler = open('text.txt', 'a')
file_handler.write(' Let\'s see if we got appended! Oh my gosh, we did!')
file_handler.close()



#read a file
file_handler = open('text.txt', 'r') #this opens the file
contents = file_handler.read() #this reads the file and puts them in the contents variable
file_handler.close() #always close your files!

print(contents)






#any time you need to do this, you'll google it! Don't worry about memorizing it!

