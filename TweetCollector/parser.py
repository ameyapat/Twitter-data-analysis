with open('mod_tweet_data.txt', 'r') as f:
    data = f.readlines()
with open("hash_tags.txt", "w") as fw:
    for line in data:
        words = line.split()
	if (len(words)>0):
		for x in words:
			if x.startswith('HashTags'):
				fw.write(words[len(words)-1].lower()+"\n")

	 
