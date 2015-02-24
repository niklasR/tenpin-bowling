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
	
	def play_frame(self, frame):
		print "== COMPETITOR: " + self.competitor_name +" == FRAME: " + str(frame) + " =="
		print "Please enter the pins knocked over with the first ball"
		first_ball = self.enter_score()
		if first_ball 
	
	def enter_score(self):
		int_invalid = True # initialise to this as no int entered yet
		
		while int_invalid:
			try:
				score = int(raw_input("Please only enter a number and confirm with <ENTER>\n"))
				if (score <= 10 && score >=0): # not in ranfe
					int_invalid = True
				else:
					int_invalid = False 
			except ValueError: # entered value not int
				int_invalid = True
		return score
		
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
	add_competitors()
	
	for frame in xrange(frames):
		for competitor in competitors:
			competitor.play_frame(frame)
		

if __name__ == "__main__":
#	add_competitors()
    main()
