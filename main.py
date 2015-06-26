class latLonDMS:
    def __init__(self,degLat,minLat,secLat,degLon,minLon,secLon):
        self._degLat = degLat
        self._minLat = minLat    
        self._secLat = secLat
        self._degLon = degLon
        self._minLon = minLon
        self._secLon = secLon
        return
    def getCoordinatesDecDeg(self):
        lat = self._degLat + self._minLat/60 + self._secLat/3600
        lon = self._degLon + self._minLon/60 + self._secLon/3600
        return '-%.12f, %.12f'%(lon,lat)
    
class cave:
    def __init__(self, name, latlon, elevation,length,status,caveType):
        self._name = name
        self._latLonDms = latlon
        self._elevation = elevation
        self._length = length
        self._status = status
        self._type = caveType        
    def getName(self):
        return self._name
    def getCoordinatesDecDeg(self):
        return self._latLonDms.getCoordinatesDecDeg()
    def getStatus(self):
        if self._status == 'O':
            return 'Open'
        elif self._status == 'CN':
            return 'Close: natural causes'
        elif self._status == 'CO':
            return 'Closed: by owner'
        elif self._status == 'R':
            return 'Restricted: no caving'
        elif self._status == 'P':
            return 'Entry with special permission only'
        elif self._status == 'G':
            return 'Gated entry by contacting Nittany Grotto'
        elif self._status == 'C':
            return 'Commercial'
        else:
            raise        
    def getType(self):
        return self._type
    def getElevation(self):
        return self._elevation
        

def createCaveList():
    caveList = []
    
    # 1-5
    caveList.append(cave('alters',     latLonDMS(40,52,47,77,30,49),1210,200,'CO','F'))       
    caveList.append(cave('barr',       latLonDMS(40,48,27,77,59,55),1415,40,'O','H'))
    caveList.append(cave('boalsburg',  latLonDMS(40,47,9,77,48,3),1060,343,'CO','F'))
    caveList.append(cave('burckerhoff',latLonDMS(40,51,6,77,38,11),1290,290,'P','W'))
    caveList.append(cave('buffalo run',latLonDMS(40,49,41,77,57,57),1340,200,'O','H'))
    
    # 6-10
    caveList.append(cave('chisel',     latLonDMS(40,42,29,77,57,24),1200,115,'O','F'))
    caveList.append(cave('coleville',  latLonDMS(40,54,17,77,48,45),900,100,'O','QF'))
    caveList.append(cave('coonscat',   latLonDMS(40,52,2,77,32,58),1140,2505,'O','H'))
    caveList.append(cave('copenhaver', latLonDMS(40,50,13,77,37,2),1120,300,'CN','H'))
    caveList.append(cave('cow',        latLonDMS(40,53,45,77,35,20),1240,20,'O','H'))
    
    # 11-15
    caveList.append(cave('decker',      latLonDMS(40,51,5,77,38,50),1300,70,'O','F(R)'))
    caveList.append(cave('deerbone',    latLonDMS(40,53,0,77,37,20),1230,350,'O','L'))
    caveList.append(cave('dung',        latLonDMS(40,53,6,77,51,27),1050,240,'O','QR(F)'))
    caveList.append(cave('earl whites', latLonDMS(40,52,40,77,36,15),1270,200,'O','H'))
    caveList.append(cave('egg hill',    latLonDMS(40,50,8,77,36,44),1120,140,'O','H'))
    
    # 16-20
    caveList.append(cave('elk creek',    latLonDMS(40,56,58,77,24,27),1250,260,'CO','F'))
        
    return caveList

def makeKml(caveList):
    outputFn = 'centreCountyCaves.kml'
    
    # Open file
    f = open(outputFn,'w')
    
    # Make header
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
    f.write('<Document>\n')
    
    for cave in caveList:
        #write cave data to kml file
        f.write('  <Placemark>\n')
        f.write('    <name>'); f.write(cave.getName().capitalize()); f.write('</name>\n');        
        f.write('    <description>'); f.write('<b>Status:</b> %s<br/><b>Elevation [ft]:</b> %d<br/><b>Type:</b> %s'%(cave.getStatus(),cave.getElevation(),cave.getType())); f.write('</description>\n')
        f.write('    <Point>\n');
        f.write('      <coordinates>'); f.write(cave.getCoordinatesDecDeg()); f.write('</coordinates>\n');
        f.write('    </Point>\n');        
        f.write('  </Placemark>\n')
    # Make footer
    f.write('</Document>\n')
    f.write('</kml>\n')
    f.close()
    
    return

if __name__ == "__main__":
    caveList = createCaveList()
    makeKml(caveList)
    print('Done.')
