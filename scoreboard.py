# Global Variables and Constants
MAX_COMPETITORS = 6
FRAMES = 10
competitors = []

class Competitor:
    def __init__(self, competitor_name):
        """Constructor: Set Name and empty scorecard."""
        self.competitor_name = competitor_name
        self.frames = []
        self.scores = []
        self.score = 0

    def compute_score(self):
        """Compute the scores for each frame and the total."""
        for i in xrange(FRAMES):
            # STRIKE
            if self.frames[i][0] == 10:
                # CONSECUTIVE STRIKE
                if self.frames[i + 1][0] == 10:
                    self.scores.append(self.frames[i][0] +
                                       self.frames[i + 1][0] +
                                       self.frames[i + 2][0])
                else:
                    self.scores.append(self.frames[i][0] +
                                       self.frames[i + 1][0] +
                                       self.frames[i + 1][1])
            # SPARE
            elif (self.frames[i][0] + self.frames[i][1] == 10):
                self.scores.append(self.frames[i][0] + self.frames[i][1] +
                                   self.frames[i + 1][0])
            # NEITHER
            else:
                self.scores.append(self.frames[i][0] + self.frames[i][1])
        # Total Score
        for score in self.scores:
            self.score += score

    def play_frame(self, frame, single_ball=False):
        """Ask user to enter data of a played frame and record it."""
        self.frames.append([])
        print "== COMPETITOR: " + self.competitor_name + " =="
        ## FIRST BALL ##
        print "Please enter the pins knocked over with the first ball"
        first_ball = self.enter_score()
        self.frames[frame].append(first_ball)

        ## SECOND BALL##
        if not first_ball == 10 and not single_ball:
            print "Please enter the pins knocked over with the second ball"
            # Check if total pins knocked <?= 10
            invalidSecond = True
            while invalidSecond:
                second_ball = self.enter_score()
                if first_ball + second_ball <= 10:
                    invalidSecond = False
            self.frames[frame].append(second_ball)


    def enter_score(self):
        """Asks user to enter score and checks for validity."""
        int_invalid = True # Initialise to this as no int entered yet
        # To ensure that an 0<=integer>=10, and an integer only, is enetered
        while int_invalid:
            try:
                score = int(raw_input("Please only enter a number and " +
                                      "confirm with <ENTER>\n"))
                if (score <= 10 and score >=0): # possible range
                    int_invalid = False
                else:
                    int_invalid = True
            except ValueError: # entered value not int
                int_invalid = True
        return score

    def print_scorecard(self):
        """Print the competitors' scoreboard."""
        self.compute_score()
        frameline = "|"
        scoreline = "|"

        # Assemble frameline (pins knocked over)
        # All but final frame
        for i in xrange(FRAMES - 1):
            if self.frames[i][0] == 10:
                frameline += "X| |"
            elif self.frames[i][0] + self.frames[i][1] == 10:
                frameline += str(self.frames[i][0]) + "|\\|"
            else:
                frameline += (str(self.frames[i][0]) + "|" +
                                            str(self.frames[i][1]) + "|")

        # Final Frame1
        # If Strike in last frame
        if self.frames[FRAMES - 1][0] == 10:
            frameline += ("X|" + str(self.frames[FRAMES][0]) + "|" +
                          str(self.frames[FRAMES + 1][0]))
        # If Spare in last frame
        elif self.frames[FRAMES - 1][0] + self.frames[FRAMES - 1][1] == 10:
            frameline += (str(self.frames[FRAMES - 1][0]) + "\\|" +
                          str(self.frames[FRAMES][0]))
        else:
            frameline += (str(self.frames[FRAMES - 1][0]) + "|" +
                          str(self.frames[FRAMES - 1][1]))

        # Assemble Scoreline (total points scored for each frame)
        for score in self.scores:
            scoreline += str(score).ljust(3) + "|"

        # Print Scorecard
        print self.competitor_name.center(43, "=")
        print frameline
        print scoreline
        print "Total Score: " + str(self.score)
        print "=" * 43


def add_competitor(name):
    """Create a new competitor instance and add it to the list."""
    competitors.append(Competitor(name))

def add_competitors():
    """Ask user for names of competitors."""
    while len(competitors) < MAX_COMPETITORS:
        next_competitor = raw_input("Enter the next competitor and confirm " +
                                    "with <ENTER>. If there are no more " +
                                    "competitors, confirm with <ENTER>\n")
        if len(next_competitor) == 0:
            break
        else:
            add_competitor(next_competitor)

def main():
    """Record a whole game"""
    # Add competitors to game
    add_competitors()

    # Record scores for each competitor
    for frame in xrange(FRAMES):

        for competitor in competitors:
            # Record a frame of scores for a competitor
            competitor.play_frame(frame)

            # If last frame is strike
            if frame == (FRAMES - 1) and competitor.frames[FRAMES - 1][0] == 10:
                # Play two more balls
                print ("Playing 2 more balls for " +
                       competitor.competitor_name)
                for frame_new in xrange(FRAMES, FRAMES + 1):
                    competitor.play_frame(frame_new)
                # If 2nd ball is strike, play one more ball
                if competitor.frames[FRAMES][0] == 10:
                    for frame_new in xrange(FRAMES + 1, FRAMES + 2):
                        competitor.play_frame(frame_new, single_ball = True)

            # If last frame is spare
            elif frame == (FRAMES - 1) and (competitor.frames[FRAMES - 1][0] +
                                            competitor.frames[FRAMES - 1][1]) == 10:
                # Play one more ball
                print "Play 1 more ball for " + competitor.competitor_name
                for frame_new in xrange(FRAMES, FRAMES + 1):
                    competitor.play_frame(frame_new, single_ball = True)

    # Print Scoreboard for each competitor
    for competitor in competitors:
        competitor.print_scorecard()

if __name__ == "__main__":
        main()
