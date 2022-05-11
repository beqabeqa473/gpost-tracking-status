from bs4 import BeautifulSoup
import requests

class GPost():

    BASE_URL = "https://gpost.ge/tracking/track-code?trackingCode="

    def __init__(self, trackingCode):
        self.items = []
        res = requests.get(f"{self.BASE_URL}{trackingCode}")
        self.soup = BeautifulSoup(res.content, "html.parser")

    def parseStructure(self):
        pacTracks = self.soup.find(class_="com-packtracks")
        elems = pacTracks.find_all(class_="com-packtrack")
        for elem in elems:
            iDate = elem.find(class_="com-packtrack-date").text
            iStatus = elem.find(class_="com-packtrack-status").text
            iLocation = elem.find(class_="com-packtrack-location").text
            item = {"date": iDate, "status": iStatus, "location": iLocation}
            self.items.append(item)
        return self.items
