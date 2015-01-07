from time import time

topMovies = """1,Toy Story (1995)
780,Independence Day (a.k.a. ID4) (1996)
590,Dances with Wolves (1990)
1210,Star Wars: Episode VI - Return of the Jedi (1983)
648,Mission: Impossible (1996)
344,Ace Ventura: Pet Detective (1994)
165,Die Hard: With a Vengeance (1995)
153,Batman Forever (1995)
597,Pretty Woman (1990)
1580,Men in Black (1997)"""

file = open("ratingFile.txt", "w")
now = int(time())

print "Please rate the following movie (1-5 (best), or 0 if not seen)"
for line in topMovies.split("\n"):
    line_strip = line.strip().split(",")
    score_str = raw_input(line_strip[1] + ": ")
    file.write("0::%s::%d::%d\n" % (line_strip[0], int(score_str), now))

file.close()
