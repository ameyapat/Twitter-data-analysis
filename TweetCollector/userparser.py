with open('mod_tweet.txt', 'r') as f:
    data = f.readlines()
with open("usernames.txt", "w") as fw:
    for line in data:
        words = line.split()
	if (len(words)>0):
		for x in words:
			if x.startswith('@'):
				print fw.write(x[0:x.index('^')].lower()+"\n")

	 
