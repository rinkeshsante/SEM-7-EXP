import nltk

# random text from wikipedia
ip1 = '''The siege of Osaka was a series of battles 
undertaken by the Japanese Tokugawa shogunate against 
the Toyotomi clan, and ending in the clan's dissolution. 
Divided into two stages (the winter campaign and the summer 
campaign), and lasting from 1614 to 1615, the siege put an
end to the last major armed opposition to the shogunate's 
establishment. This eight-metre-long (26 ft) painting, 
titled The Summer Battle of Osaka Castle and executed on 
a Japanese folding screen, illustrates Osaka Castle under 
siege, and was commissioned by the daimyo Kuroda Nagamasa, 
who took a team of painters with him to the battlefield to record 
the event. The painting depicts 5071 people and 21 generals, and is 
held in the collection of Osaka Castle. '''


# print(nltk.upppercase(ip1))

print(nltk.word_tokenize(ip1))
