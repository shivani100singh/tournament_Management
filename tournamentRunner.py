import fontstyle 
class Tournament:
    def __init__(self, num: int, team: list):
        self.numberOfTeams = num
        self.numberOfMatches = num-1
        self.matches = []
        self.currentRound =1
        self.teams= team

    def generateMacthes(self):
        self.currentRound += 1
        for i in range(0, self.numberOfTeams):
            if( self.teams[i].winner == True ):
                for j in range( i+1, self.numberOfTeams):
                    if(self.teams[j].winner == True ):
                        self.numberOfMatches = self.numberOfMatches-1
                        m= Match(team[i],  team[j])
                        m.decideWinner()
                        self.matches.append(m)

                        matchBetween = (f"MATCH BETWEEN: Team {self.teams[i].teamName} and Team {self.teams[j].teamName} ")
                        matchBetween = fontstyle.apply(matchBetween, 'bold/black/white_bg')
                        print( matchBetween )
                        
                        
                        result= (f"WINNER IS:   {self.teams[i].teamName}" )
                        result = fontstyle.apply(result, 'bold/black/white_bg')
                        print(result + "\n")
                        i=j
                        break
 

class Match:
    def __init__(self, team1, team2 ):
        self.team1 = team1
        self.team2 = team2
        
    def decideWinner(self):
        self.team2.winner = False


class Team:
    def __init__(self, name):
        self.teamName = name
        self.winner = True

print("\n")
text = fontstyle.apply('Tournament Begins', 'bold/red/WHITE_BG')
print(text)

noOfTeam = int(input("\nEnter number of teams: "))
team =[ Team(i+1) for i in range(0,noOfTeam)]

game = Tournament(noOfTeam, team)
totalTeams = game.numberOfTeams
numberOfMatches = game.numberOfMatches
print("\n")
while game.numberOfMatches:
    text = (f"ROUND : {game.currentRound}")
    text = fontstyle.apply(text, 'bold/red/white_BG')
    print(text)
    print("\n")
    game.generateMacthes()
    if( game.numberOfMatches ):
        takeInput = input("Press enter to continue for next round")
    print("\n")




