
"""Override the play method in each derived class """

#Define the base class Player
class Player:
  def play(self):
    print("The player is playing cricket.")

#Define the derived class1 Batsman
class Batsman(Player):
  def play(self):
    print("The batsman is batting.")

#Define the derived class2 Bowler
class Bowler(Player):
  def play(self):
    print("The bowler is bowling.")

#Crete a object of each class
batsman = Batsman()
bowler  = Bowler()

#Run the play method of Batsman and Bowler
batsman.play()
bowler.play()
  
  