import webbrowser
import time

#For Loop because we want it to repeat the block of code within three times
#The range is from 1 -> 4 because 4 - 1 is 3 hence the code will run three times we could also have written 0,3 
for index in range(1,4): 
	#we have imported time on the top
	time.sleep(10)
	webbrowser.open('https://www.youtube.com/watch?v=izGwDsrQ1eQ')

print 'Done'	