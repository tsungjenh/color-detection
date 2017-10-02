import os

count = 0
colors = ['red','blue','white','black','yellow','green']

for color in colors:
	count = 0
	path = os.path.join('.', color)
	for f in os.listdir(path):
		os.rename(os.path.join(path,f),os.path.join(path,str(count)) + '.jpg')
		count += 1
