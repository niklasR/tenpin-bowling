competitors = []
max_competitors = 6
frames = 10

class Competitor:
	name = ''
	score = 0
	
	def __init__(self, competitor_name):
		self.competitor_name = competitor_name
		
	def print_stats(self):
		print "Name: " + self.competitor_name
		print "Score: " + str(self.score)
	
	def add_points(self, points):
		self.score += points
	

def add_competitor(name):
	competitors.append(Competitor(name))

def add_competitors():
	while len(competitors) < max_competitors:
		next_competitor = raw_input("Enter the next competitor and confirm with <ENTER>. If there are no more competitors, confirm with <ENTER>\n")

		if len(next_competitor) == 0:
			break
		else:
			add_competitor(next_competitor)
			
#	for competitor in competitors:
#		competitor.add_points(2)
#		competitor.print_stats()

def main():
	for x in xrange(frames):
		print x

if __name__ == "__main__":
	add_competitors()
#    main()
