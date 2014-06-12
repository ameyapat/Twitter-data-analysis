with open('mod_tweet.txt', 'r') as f:
    data = f.readlines()
with open("usernames_graph.txt", "w") as fw:
    for line in data:
        words = line.split('^')
	if(len(words)>2):
		print fw.write(words[0]+" "+words[1]+"\n")
	 
