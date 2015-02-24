competitors = []
max_competitors = 6
frames = 10

class Competitor:
	name = ''
	score = 0
	double_for_next_x_balls = 0 # set to 2 if strike, 1 if spare. reduce by 1 after next score recorder if > 0.
	
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
		
		if self.double_for_next_x_balls > 0: # Competitor scored a strike/spare before
			self.score = first_ball*2
			self.double_for_next_x_balls -= 1
		else:
			self.score = first_ball
			
		if first_ball == 10: # STRIKE
			double_for_next_x_balls = 2
			return
		
		print "Please enter the pins knocked over with the second ball"
				
		second_ball = self.enter_score()
		if self.double_for_next_x_balls > 0: # Competitor scored a strike/spare before
			self.score = second_ball*2
			self.double_for_next_x_balls -= 1
		else:
			self.score = second_ball
			
		if first_ball + second_ball == 10: # SPARE
			double_for_next_x_balls = 1
		
	
	def enter_score(self):
		int_invalid = True # initialise to this as no int entered yet
		
		while int_invalid:
			try:
				score = int(raw_input("Please only enter a number and confirm with <ENTER>\n"))
				if (score <= 10 and score >=0): # possible range
					int_invalid = False
				else:
					int_invalid = True 
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
