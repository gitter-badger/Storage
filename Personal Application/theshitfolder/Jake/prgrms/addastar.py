import string
# file for making file
strtosplit = '''
put shit here
http://cs.berry.edu/~nhamid/p2p/filer-python.html
https://pythonhosted.org/pyobjc/
We should probably catch more of this shit in the middle of the loop
 a requirements.txt doesn't seem like a bad idea
we shouldn't keep copying and pasting logging to every new file
WE SHOULD MAKE AN API THAT LET'S OTHER APPLICATIONS ACCESS AND UTILIZE DATA FROM OUR SQLITE3 TABLES
 WHEN YOU UPDATE THIS CODE UPDATE FROM THE BULLETIN BOARD DOWN
blacklist these usernames https://gist.github.com/jakesyl/c1c1f24c38d6042bb04e
Alex you need to improve performance on that time function
WE HAVE TO IGNORE GOOGLE DRIVE AND DROPBOX AND SIMILIAR SERVICES, I already did but idk if they're right no time to test anything
To remove .dirs make the return value an array, the first term being the int of the filecount, and the second being any .dotfiles
Look at dependencies folder for the install order
Alex if it's still in here remove your method for getting rid of . directories
Percentage will not work with ignoring files, we need to figure out a way to do percentage
Okay so the thing doesn't actually work (the script to remove, but it doesn't throw an error either so just leave it)
note to self make the dir where the files are actually stored now called files
Make sure that ubuntu counts memory usage frequently too
figure out a way to get rid opf ssh
'''
splitter = strtosplit.split('\n')
newstr = ""
for line in splitter:
	line = '*' + line
	newstr = "\n" + line + newstr
print newstr

