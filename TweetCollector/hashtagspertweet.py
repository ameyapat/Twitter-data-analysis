with open('mod_tweet.txt', 'r') as f:
    data = f.readlines()
with open("hashtags_bytweet.txt", "w") as fw:
    for line in data:
	#fw.write("\n")
	words = line.split('^')
	if(len(words)>2):
		if "#" not in words[2]:
			continue
		else:
			y= words[2].split()
			#print y
			for k in y:
				if(k.startswith('#') and k[len(k)-1]!="|"):
					fw.write(k)
				if(k[len(k)-1]=="|"):
					if(k.startswith("#")):
						fw.write(k[0:len(k)-1]+"\n")
					else:
						fw.write("\n")

with open('hashtags_bytweet.txt', 'r') as f:
    data = f.readlines()
with open("hashtags_bytweet.txt", "w") as fw:
    for line in data:
	fw.write(line.strip()+"\n")

 
