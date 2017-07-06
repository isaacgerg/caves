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
    caveList.append(cave('fishing creek',latLonDMS(41,00,2877,32,52),840,40,'O','H'))
    caveList.append(cave('footbridge',   latLonDMS(40,53,16,77,28,26),1070,50,'O','H'))
    caveList.append(cave('fox'           latLongDMS(40,51,04,7735,08),1100,60,'O','H'))
    caveList.append(cave('fry'           latLongDMS(40,42,20,77,58,04),1180,60,'R','H'))
    
    #21-25
    caveList.append(cave('genzel farm', latLongDMS(40,53,37,77,42,02),1040,50,'O',H'))
    caveList.append(cave('hennign',      latLongDMS(40,51,20,77,37,04),1280,700,'O','F(L)'))
    caveList.append(cave('hol-bruck',   latLongDMS(40,51,10,77,37,57),1240,280,'P','F(L)'))
    caveList.append(cave('holter pit',  latLongDMS(40,51,09, 77,37,49),1240, 100, 'P', 'L(VE)'))
    caveList.append(cave('hostermans pit'), latLongDMS(40,53,36,77,26,23),1250,6630,'G','VE'))
    
    # 26-30
    caveList.append(cave('hostermans fiss', latLongDMS(40,53,21,77,26,36),1120,30,'O','H'))
    caveList.append(cave('j-4',             latLongDMS(40,51,40,77,44,44),1040,3700,'G','QF'))
    caveList.append(cave('jacksonville',    latLongDMS(40,59,05,77,38,46),880,40,'O','W'))
    caveList.append(cave('kepler',          latLongDMS(40,43,14,77,55,09),1240,255,'CN','QH'))
    caveList.append(cave('madisonburg',     latLongDMS(40,55,43,77,31,07),1300,200,'O','F'))
    
    # 31-35
    caveList.append(cave('miller',          latLongDMS(40,42,27,77,57,10),1200,1000,'G','H'))
    caveList.append(cave('millheim',        latLongDMS(40,53,11,77,28,34),1080,250,'O','H'))
    caveList.append(cave('millheim south',  latLongDMS(40,52,46,77,27,55),1060,130,'O','W'))
    caveList.append(cave('mine',            latLongDMS(40,53,20,77,42,31),1060,220,'R','QH'))
    caveList.append(cave('noll',            latLongDMS(40,52,38,77,43,33),1040,420,'CN','H'))
    
    # 36-40
    caveList.append(cave('oak hall',        latLongDMS(40,47,55,77,48,22),1020,200,'P','QW'))
    caveList.append(cave("penn's",          latLongDMS(40,52,55,77,36,45),1151,1700,'C','W'))
    caveList.append(cave('penns shelter',   latLongDMS(40,52,54,77,36,47),1170,40,'O','H'))
    caveList.append(cave('pine creek',      latLongDMS(40,52,04,77,27,21),1040,30,'O','H'))
    caveList.append(cave('ping cr spr house',latlongDMS(40,52,15,77,27,16),1040,25,'O','W'))
    
    # 41-45
    caveList.append(cave('pine gr ms shelt',latLongDMS(40,43,40,77,53,05),1440,10,'O','H'))
    caveList.append(cave('pleasant gap',    latLongDMS(0,0,0,0,0,0), 0, 170, 'R', 'QH'))
    caveList.append(cave('poterfield fiss', latLongDMS(40,57,58,77,23,19), 1340,90,'P','H'))
    caveList.append(cave('prah',            latLongDMS(40,59,44,77,37,50), 900,1100,'O','QH'))
    caveList.append(cave('racoon',          latLongDMS(40,51,28,77,35,22), 1200,80,'CN','F'))
                    
    # 46-50
    caveList.append(cave('rebersburg',      latLongDMS(40,57,16,77,24,32), 1290,80,'R','H'))
    caveList.append(cave('roadside',        latLongDMS(40,55,45,77,27,56), 1240,40,'O','H'))
    caveList.append(cave('rock',            latLongDMS(40,50,48,77,49,32), 940,80,'O','H'))
    caveList.append(cave('rockview',        latLongDMS(40,49,53,77,47,16), 1190,350,'R','R(L)'))
    caveList.append(cave('rossman',         latLongDMS(40,52,48,77,30,45), 1210,235,'CO','F'))
                    
    # 51-55
                    
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
