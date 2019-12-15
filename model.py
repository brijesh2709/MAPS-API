# imports json, request and parse
import json
import urllib.parse
import urllib.request


# MapQuest class is created
class MapQuest:

    # initializes the key and required url's
    def __init__(self):
        self._key = 'GlGadupu2LVe5NCPea9MwWJ8U4mTESLw'
        self._baseURL = 'http://open.mapquestapi.com/directions/v2/route'
        self._baseURL2= 'http://www.mapquestapi.com/geocoding/v1/address'
        self._baseURL3= 'http://www.mapquestapi.com/search/v4/place'
 
    # return the total distance
    def totalDistance(self,locations:list)->float:
        distance=0
        # loops through the locations
        for i in range(1,len(locations)):
            # creates url
            query_parameters=[('key', self._key),('from',locations[i-1]),('to',locations[i])]
            search_url = self._baseURL+'?'+urllib.parse.urlencode(query_parameters)
            response = None
            # takes the response
            try:
                response = urllib.request.urlopen(search_url)
                info = json.load(response)
                distance += info['route']['distance']
            except:
                if response!=None:
                    response.close()
        return distance

    # method to return the time between the entered locations
    def totalTime(self,locations:list)->float:
        time=0
        # loops throught the locations
        for i in range(1,len(locations)):
            # creates url
            query_parameters=[('key',self._key),('from',locations[i-1]),('to',locations[i])]
            search_url = self._baseURL+ '?'+urllib.parse.urlencode(query_parameters)
            response = None
            # takes the rquired info
            try:
                response = urllib.request.urlopen(search_url)
                info = json.load(response)
                time += info['route']['time']
            finally:
                if response!=None:
                    response.close()
        return time

    # new method to return directions
    def directions(self,locations:list)->str:
        directions=''
        # loops throgh locations
        for i in range(1,len(locations)):
            # creates url
            query_parameters = [('key', self._key),('from',locations[i - 1]),('to',locations[i])]
            search_url=self._baseURL+'?'+urllib.parse.urlencode(query_parameters)
            response=None
            # gets the required info
            try:
                response = urllib.request.urlopen(search_url)
                info = json.load(response)
                for j in info['route']['legs'][0]['maneuvers']:
                    directions += j['narrative']+'\n'
            finally:
                if response!=None:
                    response.close()
        self.v = directions
        return directions

    # returns the latitude and logitude of the starting locations 
    def LatandLong(self,locations:list)->list:
        response1= None
        # loops through the locations
        for i in range(1,len(locations)):
            try:
                # creates the url
                query_parameters=[('key',self._key),('location',locations),]
                search_url = self._baseURL2+'?'+urllib.parse.urlencode(query_parameters)
                response1 = urllib.request.urlopen(search_url)
                # retrieves the required info
                info = json.load(response1)
                self.la = info['results'][0]['locations'][0]['latLng']['lat']
                lat = self.decdeg2dms(self.la)
                self.ln = info['results'][0]['locations'][0]['latLng']['lng']
                lng = self.decdeg2dms(self.ln)
                
            finally:
                if response1 != None:
                    response1.close()
        return lat, lng

    # returns the choices for your interest
    def pointOfInterest(self,locations:str,keyword:str,result:int)->dict:
        try:
            response1= None
            response2= None
            # creates a url
            query_parameters=[('key',self._key),('location',locations),]
            search_url = self._baseURL2+'?'+urllib.parse.urlencode(query_parameters)
            response1 = urllib.request.urlopen(search_url)
            # retives the required information
            info = json.load(response1)
            lat = info['results'][0]['locations'][0]['latLng']['lat']
            lng = info['results'][0]['locations'][0]['latLng']['lng']
            mylist=[]
            # creates a url
            query_parameters=[('key',self._key),('location',str(lng)+','+str(lat)),('sort','distance'),('limit', result),('q',keyword)]
            search_url=self._baseURL3+'?'+urllib.parse.urlencode(query_parameters)
            response2=urllib.request.urlopen(search_url)
            # retrieves the required details
            info = json.load(response2)
            for i in info['results']:
                mylist.append(i['displayString'])
            return mylist
        finally:
            if response1 != None:
                response1.close()
            if response2 != None:
                response2.close()

    # method converts the decimal degree of latitude and longitude
    # to degree minute second
    def decdeg2dms(self, dd):
       mnt,sec = divmod(dd*3600,60)
       deg,mnt = divmod(mnt,60)
       return deg,mnt,sec

    # method to check if the entered locations are right                    
    def checking_url(self, locations):
        ret_dit = self.totalDistance(locations)
        return ret_dit
