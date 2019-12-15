# imports model and view
import model as m
import view as v


# creates a new class 
class Controller():

    # initializes the model and view
    def __init__(self):
        self.x = m.MapQuest()
        self.y = v.Main_GUI()

    # links the model and view to check if url is correct
    def return_dist(self, h):
        dis = self.x.checking_url(h)
        return dis
    
    # links the model and view to return distance
    def return_distance(self, a):
        dista = self.x.totalDistance(a)
        return dista

    # links the model and view to retun time
    def return_time(self, b):
        timing = self.x.totalTime(b)
        return timing

    # links the model and view to return directions
    def return_direction(self, d):
        direct = self.x.directions(d)
        return direct

    # links the model and view to return latitude and logitude
    def return_LatandLong(self, g):
        L,P = self.x.LatandLong(g)
        return L,P

    # links the model and view to your choices for your interest
    def return_POI(self, q, keyw, rest):
        my_POI = self.x.pointOfInterest(q, keyw, rest)
        return my_POI

    # main method to run the GUI file
    def main_screen(self):
        self.y.run()

# main functionality of the code
if __name__ == '__main__':
    u = Controller()
    u.main_screen()
