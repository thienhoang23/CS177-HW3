inputs = open('wordsEn.txt','r')
outputs = open('ModwordsEn.txt','w')

for each_line in inputs:
	if(len(each_line) > 6):
		outputs.write(each_line)