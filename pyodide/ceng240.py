import random

import os
#os.remove("data.csv")
#os.remove("data.txt")
#os.remove("data2.csv")


filecontent='''15 95 91 8 100
21 91 83 87 40
82 83 56 84 75
67 82 18 0 83
95 8 25 41 73
'''
with open("input.txt","w") as f : f.write(filecontent)


filecontent='''HARTSFIELD INTL,ATLANTA
BALTO/WASH INTL,BALTIMORE
LOGAN INTL,BOSTON
DOUGLAS MUNI,CHARLOTTE
MIDWAY,CHICAGO
O'HARE INTL,CHICAGO
DALLAS/FT WORTH INTL,DALLAS
LOVE FIELD,DALLAS
STAPLETON INTL,DENVER
DETROIT CITY,DETROIT
WAYNE COUNTY,DETROIT
WILLOW RUN,DETROIT
HONOLULU INTL,HONOLULU
INTERCONTINENTAL,HOUSTON
HOBBY,HOUSTON
ELLINGTON FIELD,HOUSTON
MC CARRAN INTL,LAS VEGAS
HOLLYWOOD-BURBANK,LOS ANGELES
LONG BEACH,LOS ANGELES
LOS ANGELES INTL,LOS ANGELES
ORANGE COUNTY,LOS ANGELES
MIAMI INTL,MIAMI
FT LAUDERDALE INTL,MIAMI
MINNEAPOLIS/ST PAUL,MINNEAPOLIS
NEWARK,NEWARK
JOHN F KENNEDY INTL, NEW YORK
LA GUARDIA,NEW YORK
ORLANDO INTL,ORLANDO
INTERNATIONAL,PHILADELPHIA
SKY HARBOR INTL,PHOENIX
GREATER PITTSBURGH,PITTSBURGH
LAMBERT-ST LOUIS,ST LOUIS
SALT LAKE CITY INTL,SALT LAKE CITY
SAN DIEGO INTL,SAN DIEGO
BUCHANAN FIELD,SAN FRANCISCO
OAKLAND METRO INTL,SAN FRANCISCO
SAN FRANCISCO INTL,SAN FRANCISCO
SEATTLE-TACOMA INTL,SEATTLE
TAMPA INTL,TAMPA
DULLES INTL,WASHINGTON
WASHINGTON NATIONAL,WASHINGTON
ALBUQUERQUE INTL,ALBUQUERQUE
ANCHORAGE INTL,ANCHORAGE
MUELLER MUNI,AUSTIN
GREATER BUFFALO INTL,BUFFALO
GREATER CINCINNATI,CINCINNATI
HOPKINS INTL,CLEVELAND
PORT COLUMBUS INTL,COLUMBUS
LOCKBURN AFB,COLUMBUS
COX/DAYTON INTL,DAYTON
EL PASO INTL,EL PASO
SOUTHWEST,FORT MYERS
BRADLEY INTL,HARTFORD
INDIANAPOLIS INTL,INDIANAPOLIS
JACKSONVILLE INTL,JACKSONVILLE
KAHULUI,MAUI
INTERNATIONAL,KANSAS CITY
LIHUE,KAUAI
MEMPHIS INTL,MEMPHIS
GENERAL MITCHELL,MILWAUKEE
METROPOLITAN,NASHVILLE
INTL/MOISANT FIELD,NEW ORLEANS
NORFOLK REGIONAL,NORFOLK
WILL ROGERS WORLD,OKLAHOMA CITY
ONTARIO INTL,ONTARIO
PORTLAND INTL,PORTLAND
RALEIGH-DURHAM,RALEIGH
RENO INTL,RENO
ROCHESTER-MONROE CTY,ROCHESTER
SACRAMENTO METRO,SACRAMENTO
SAN ANTONIO INTL,SAN ANTONIO
SAN JOSE MUNI,SAN JOSE
HANCOCK,SYRACUSE
TUCSON INTL,TUCSON
TULSA INTL,TULSA
PALM BEACH INTL,WEST PALM BEACH
AKRON-CANTON,AKRON
ALBANY COUNTY,ALBANY
ALLENTOWN-BETHEHEM,ALLENTOWN
AMARILLO,AMARILLO
RYAN,BATON ROUGE
LOGAN FIELD,BILLINGS
BIRMINGHAM MUNI,BIRMINGHAM
BOISE AIR TERMINAL,BOISE
HARLINGEN INDUSTRIAL,BROWNSVILLE
BURLINGTON INTL,BURLINGTON
CEDAR RAPIDS MUNI,CEDAR RAPIDS
CHARLESTON AFB/MUNI,CHARLESTON
LOVELL FIELD,CHATTANOOGA
PETERSON FIELD,COLORADO SPRINGS
COLUMBIA METRO,COLUMBIA
CORPUS CHRISTI INTL,CORPUS CHRISTI
DAYTONA BEACH REG,DAYTONA BEACH
DES MOINES MUNI,DES MOINES
MAHLON SWEET FIELD,EUGENE
FAIRBANKS INTL,FAIRBANKS
MUNI/BAER FIELD,FORT WAYNE
FRESNO AIR TERMINAL,FRESNO
KENT COUNTY,GRAND RAPIDS
GREENSBORO-HP-WS REG,GREENSBORO
GREENVILLE/SPARTANBG,GREENVILLE
HARRISBURG INTL,HARRISBURG
GENERAL LYMAN FIELD,HILO
MADISON COUNTY,HUNTSVILLE
PALM SPRINGS MUNI,INDIO
LONG ISLAND-MCARTHUR,ISLIP
THOMPSON FIELD,JACKSON
KE-AHOLE,KAILUA-KONA
MCGHEE TYSON,KNOXVILLE
BLUE GRASS,LEXINGTON
ADAMS FIELD,LITTLE ROCK
STANDIFORD FIELD,LOUISVILLE
LUBBOCK REGIONAL,LUBBOCK
TRUAX FIELD,MADISON
MUNICIPAL,MANCHESTER
CAPE KENNEDY REG,MELBOURNE
MIDLAND REGIONAL,MIDLAND
BATES FIELD,MOBILE
QUAD CITY,MOLINE
EPPLEY AIRFIELD,OMAHA
PENSACOLA REGIONAL,PENSACOLA
PORTLAND INTL JETPRT,PORTLAND
FRANCIS GREEN STATE,PROVIDENCE
BYRD FLYING FIELD,RICHMOND
ROANOKE MUNI,ROANOKE
TRI CITY,SAGINAW
SANTA BARBARA,SANTA BARBARA
SARASOTA-BRADENTON,SARASOTA
SAVANNAH INTL,SAVANNAH
SHREVEPORT REGIONAL,SHREVEPORT
FOSS FIELD,SIOUX FALLS
MICHIANA REGIONAL,SOUTH BEND
SPOKANE INTL,SPOKANE
TALLAHASSEE REGIONAL,TALLAHASSEE
MID-CONTINENT,WICHITA
'''
with open("data.txt","w") as f : f.write(filecontent)
    

def get_gpa(student_id, semester_no):
    student_ids = [4567890, 5678901, 6789012, 7890123, 8901234, 9012345, 2171544, 2315477, 2424937]
    grades = fill_gpa(student_id)
    random.seed(student_id + semester_no)
    rand = random.random()
    if student_id not in student_ids: # ID's which does not exist in the database
        raise KeyError
    elif rand > 0.25:
        return grades[semester_no-1]
    elif rand < 0.125:
        raise ValueError
    else:
        raise IndexError

def fill_gpa(student_id):
    random.seed(student_id)
    gpas = []
    for sem in range(8):
        gpas.append(round((random.random() + 1) * 2, 2)) # gpa's are in [2.0, 4.0]
    return gpas

ufo_txt = '''datetime,city,state,country,shape,duration (seconds),latitude,longitude 
10/10/1949,san marcos,tx,us,cylinder,2700,29.8830556,-97.9411111
10/10/1984,white plains,ny,us,formation,20,41.0338889,-73.7633333
10/10/1998,las vegas,nv,us,circle,2700,36.1750000,-115.1363889
10/10/2002,philomath,or,us,unknown,5,44.5402778,-123.3663889
10/10/2005,loretto,pa,us,triangle,300,40.5030556,-78.6305556
10/10/2007,grove city,pa,us,unknown,3600,41.1577778,-80.0888889
10/10/2010,harrisburg,pa,us,circle,240,40.2736111,-76.8847222
10/10/2012,san diego,ca,us,sphere,240,32.7152778,-117.1563889
10/10/2013,lost creek,wv,us,triangle,45,39.1611111,-80.3522222
10/11/1999,augusta,ks,us,light,600,37.6866667,-96.9763889
10/11/2004,salinas,ca,us,formation,2700,36.6777778,-121.6544444
10/11/2007,tega cay,sc,us,light,1800,35.0241667,-81.0280556
10/11/2011,omaha,il,us,chevron,120,37.8902778,-88.3030556
10/11/2013,naples,fl,us,light,7200,26.1416667,-81.795
10/1/1966,anacortes,wa,us,light,1200,48.5127778,-122.6113889
10/1/1975,maricopa,az,us,changing,1200,33.0580556,-112.0469444
10/1/1985,lawrence,ks,us,sphere,300,38.9716667,-95.235
10/1/1994,new york city,ny,us,disk,15,40.7141667,-74.0063889
10/1/1998,portland,or,us,light,5,45.5236111,-122.675
10/1/2000,wheaton,md,us,triangle,300,39.0397222,-77.0555556
10/1/2002,grants,nm,us,fireball,10,35.1472222,-107.8508333
10/1/2005,oak forest,il,us,light,3600,41.6027778,-87.7438889
10/1/2005,west palm beach,fl,us,teardrop,60,26.7052778,-80.0366667
10/1/2006,winslow,az,us,fireball,15,35.0241667,-110.6966667
10/1/2007,granville,oh,us,sphere,120,40.0680556,-82.5197222
10/1/2008,garrett,in,us,triangle,4,41.3494444,-85.1355556
10/1/2011,clinton,ms,us,circle,300,32.3413889,-90.3216667
10/1/2013,bel air,md,us,flash,4,39.5358333,-76.3486111
10/12/1995,pueblo,co,us,triangle,10,38.2544444,-104.6086111
10/12/2001,phoenix,az,us,formation,120,33.4483333,-112.0733333
10/12/2004,rocklin,ca,us,triangle,3600,38.7908333,-121.2347222
10/12/2008,reading,pa,us,diamond,300,40.3355556,-75.9272222
10/12/2011,waco,tx,us,changing,900,31.5491667,-97.1463889
10/12/2012,cabin creek,wv,us,unknown,40,38.1958333,-81.4777778
10/12/2013,sundridge (canada),on,ca,sphere,15,45.766667,-79.4
10/13/2000,newton,ks,us,fireball,90,38.0466667,-97.3447222
10/13/2003,pocatello,id,us,oval,10,42.8713889,-112.4447222
10/13/2005,mesa,az,us,light,90,33.4222222,-111.8219444
10/13/2008,newburyport,ma,us,light,300,42.8125000,-70.8777778
10/13/2010,allen,tx,us,unknown,10,33.1030556,-96.6702778
10/13/2012,lemont,il,us,oval,2400,41.6736111,-88.0016667
10/13/2013,raymond,oh,us,unknown,600,40.3347222,-83.4658333
10/14/1999,mead  (near spokane),wa,us,light,3,47.7675000,-117.3538889
10/14/2002,porterville,ca,us,fireball,60,36.0652778,-119.0158333
10/14/2005,amarillo,tx,us,sphere,420,35.2219444,-101.8308333
10/14/2008,valparaiso,in,us,formation,5,41.4730556,-87.0611111
10/14/2011,scottsdale,az,us,triangle,240,33.5091667,-111.8983333
10/14/2012,lakewood,nj,us,light,180,40.0977778,-74.2180556
10/15/1954,blanco,tx,us,other,300,30.0977778,-98.4211111
10/15/1970,westland,mi,us,unknown,20,42.3241667,-83.4002778
10/15/1976,eveleth,mn,us,light,900,47.4625000,-92.5397222
10/15/1983,california valley,ca,us,disk,600,35.3200000,-120.0058333
10/15/1988,ottawa (canada),on,ca,triangle,2700,45.416667,-75.7
10/15/1993,portsmouth,nh,us,light,60,43.0716667,-70.7630556
10/15/1997,dallas,tx,us,light,300,32.7833333,-96.8
10/15/1998,dallas,tx,us,disk,10,32.7833333,-96.8
10/15/2000,nassau bay,tx,us,oval,4,29.5444444,-95.0908333
10/15/2001,moses lake,wa,us,fireball,20,47.1302778,-119.2769444
10/15/2003,granada hills,ca,us,disk,900,34.2647222,-118.5222222
10/15/2004,mckenzie bridge,or,us,flash,300,44.1752778,-122.1627778
10/15/2005,seattle,wa,us,cylinder,90,47.6063889,-122.3308333
10/15/2007,mission,sd,us,light,600,43.3058333,-100.6577778
10/15/2009,lancaster,sc,us,flash,3,34.7202778,-80.7711111
10/15/2011,anson,tx,us,changing,10,32.7563889,-99.8958333
10/15/2013,boise,id,us,chevron,30,43.6136111,-116.2025
10/16/1999,houston,tx,us,oval,20,29.7630556,-95.3630556
10/16/2003,sumner,wa,us,changing,6300,47.2033333,-122.2391667
10/16/2007,ridgefield,ct,us,sphere,15,41.2813889,-73.4986111
10/16/2010,salem,or,us,sphere,480,44.9430556,-123.0338889
10/16/2012,st. paul,va,us,sphere,600,36.9052778,-82.3111111
10/17/1967,cherokee village,ar,us,circle,2100,36.2977778,-91.5158333
10/17/2000,tucson,az,us,diamond,600,32.2216667,-110.9258333
10/17/2004,sterling,il,us,formation,12,41.7886111,-89.6961111
10/17/2008,santa ana,ca,us,disk,900,33.7455556,-117.8669444
10/17/2010,phoenix,az,us,light,4,33.4483333,-112.0733333
10/17/2012,san rafael,ca,us,flash,10,37.9736111,-122.53
10/18/1990,forest city,nc,us,disk,14400,35.3338889,-81.8652778
10/18/2003,everett,wa,us,sphere,30,47.9791667,-122.2008333
10/18/2004,ada,ok,us,triangle,180,34.7744444,-96.6780556
10/18/2008,dallas,tx,us,light,7,32.7833333,-96.8
10/18/2012,san diego,ca,us,circle,900,32.7152778,-117.1563889
10/18/2013,lawrenceville,ga,us,other,180,33.9561111,-83.9880556
10/19/1999,round rock,tx,us,sphere,300,30.5080556,-97.6786111
10/19/2005,marlboro,ma,us,circle,1200,42.7166667,-70.9736111
10/19/2008,hilo,hi,us,sphere,600,19.7297222,-155.09
10/19/2011,hinsdale,ma,us,fireball,120,42.4386111,-73.1258333
10/19/2013,murphysboro,il,us,other,600,37.7644444,-89.335
10/19/2013,jupiter,fl,us,light,300,26.9338889,-80.0944444
10/20/1994,plant city,fl,us,disk,300,28.0183333,-82.1130556
10/20/1999,kingston,wa,us,light,3,47.7988889,-122.4969444
10/20/2003,hampton,fl,us,sphere,15,29.8641667,-82.1311111
10/20/2005,denver,co,us,cigar,60,39.7391667,-104.9841667
10/20/2007,rock falls,wi,us,light,900,44.7186111,-91.6897222
10/20/2009,cincinnati,oh,us,light,10,39.1619444,-84.4569444
10/20/2011,clermont,fl,us,light,3600,28.5491667,-81.7730556
10/20/2012,cumberland,md,us,light,1800,39.6527778,-78.7627778
10/21/1998,campbell,ca,us,other,600,37.2872222,-121.9488889
10/21/2003,waterford,ny,us,triangle,30,42.7925000,-73.6816667
10/21/2007,holden,la,us,diamond,1800,30.5041667,-90.6691667
10/21/2010,otis,or,us,light,1800,45.0244444,-123.9452778
10/21/2012,morris,il,us,formation,300,41.3572222,-88.4211111
10/21/2013,two rivers,wi,us,oval,900,44.1538889,-87.5691667
10/2/2001,latrobe,pa,us,fireball,2,40.3211111,-79.3797222
10/2/2005,providence,ri,us,changing,300,41.8238889,-71.4133333
10/2/2008,philadelphia,pa,us,egg,30,39.9522222,-75.1641667
10/2/2012,yelm,wa,us,light,3600,46.9422222,-122.6047222
10/2/2013,orrington,me,us,changing,600,44.7311111,-68.8269444
10/22/2001,verona,wi,us,triangle,7,42.9908333,-89.5330556
10/22/2005,liverpool,ny,us,unknown,1800,43.1063889,-76.2180556
10/22/2007,hillsborough,nj,us,triangle,300,40.4775000,-74.6272222
10/22/2010,pittsburgh,pa,us,sphere,120,40.4405556,-79.9961111
10/22/2012,cincinnati,oh,us,circle,120,39.1619444,-84.4569444
10/22/2013,ossipee,nh,us,circle,5,43.6852778,-71.1172222
10/23/1999,norwood,pa,us,triangle,900,39.8916667,-75.3
10/23/2004,vista,ca,us,sphere,600,33.2000000,-117.2416667
10/23/2007,hanford,ca,us,cylinder,240,36.3275000,-119.6447222
10/23/2010,hockessin,de,us,sphere,900,39.7875000,-75.6969444
10/23/2011,lambertville,nj,us,disk,120,40.3658333,-74.9433333
10/23/2013,marlboro,nj,us,triangle,90,40.3152778,-74.2466667
10/24/1977,winnipeg (canada),mb,ca,triangle,60,49.883333,-97.166667
10/24/2001,evanston,wy,us,oval,18000,41.2683333,-110.9625
10/24/2005,surprise,az,us,other,120,33.6305556,-112.3325
10/24/2008,chesapeake,va,us,triangle,60,36.8188889,-76.2752778
10/24/2011,port angeles,wa,us,light,300,48.1183333,-123.4294444
10/24/2012,montreal (canada),qc,ca,changing,3,45.5,-73.583333
10/24/2013,irving,tx,us,cylinder,240,32.8138889,-96.9486111
10/25/1998,pell city (33.56&#39 52&quot;n - 86.15&#39 00&quot; w),al,us,sphere,3,33.5861111,-86.2861111
10/25/2003,trotwood,oh,us,other,120,39.7972222,-84.3113889
10/25/2007,philadelphia,pa,us,oval,60,39.9522222,-75.1641667
10/25/2009,the woodlands,tx,us,unknown,45,30.1577778,-95.4891667
10/25/2011,seattle,wa,us,light,60,47.6063889,-122.3308333
10/25/2013,waukee,ia,us,circle,420,41.6116667,-93.885
10/26/1999,melbourne beach,fl,us,triangle,7200,28.0680556,-80.5605556
10/26/2003,allen,tx,us,unknown,120,33.1030556,-96.6702778
10/26/2007,duluth,mn,us,oval,1800,46.7833333,-92.1063889
10/26/2009,collingdale,pa,us,light,2,39.9116667,-75.2775
10/26/2013,brighton,co,us,formation,240,39.9852778,-104.82
10/27/1999,tucson,az,us,fireball,10,32.2216667,-110.9258333
10/27/2004,woodside (queens),ny,us,chevron,3,40.7452778,-73.9058333
10/27/2008,blossom,tx,us,sphere,1200,33.6613889,-95.3855556
10/27/2011,tuscaloosa,al,us,circle,60,33.2097222,-87.5691667
10/27/2013,marstons mills,ma,us,formation,1320,41.6561111,-70.4166667
10/28/1999,phoenix,az,us,changing,1200,33.4483333,-112.0733333
10/28/2003,pasadena,md,us,unknown,7200,39.1072222,-76.5713889
10/28/2006,overland park,ks,us,triangle,6,38.9822222,-94.6705556
10/28/2008,jackson,tn,us,circle,120,35.6144444,-88.8138889
10/28/2010,tracy,ca,us,circle,900,37.7397222,-121.4241667
10/28/2011,red hill,pa,us,unknown,240,40.3727778,-75.4813889
10/29/1997,glen alpine,nc,us,light,60,35.7288889,-81.7794444
10/29/2001,rancho cucamonga,ca,us,fireball,540,34.1063889,-117.5922222
10/29/2005,surprise,az,us,light,60,33.6305556,-112.3325
10/29/2008,abilene,tx,us,light,900,32.4486111,-99.7327778
10/29/2010,vicksburg,ms,us,other,15,32.3525000,-90.8777778
10/29/2012,omaha,ne,us,rectangle,180,41.2586111,-95.9375
10/30/1996,pittsburgh,pa,us,disk,240,40.4405556,-79.9961111
10/30/2002,santa barbara,ca,us,triangle,4,34.4208333,-119.6972222
10/30/2005,porterville,ca,us,sphere,30,36.0652778,-119.0158333
10/30/2008,pound,va,us,triangle,6,37.1236111,-82.6013889
10/30/2010,tuttle,ok,us,triangle,1200,35.2908333,-97.8119444
10/30/2012,atwood,ks,us,light,90,39.8066667,-101.0416667
10/31/1976,garland,tx,us,other,120,32.9125000,-96.6386111
10/31/1999,san diego  (spring valley) (20 mi. e of sd airport),ca,us,fireball,45,32.7152778,-117.1563889
10/31/2000,whitmore lake,mi,us,circle,120,42.4394444,-83.7438889
10/31/2003,hamilton (canada),on,ca,unknown,300,43.25,-79.833333
10/31/2004,frankfort,il,us,light,1500,41.4958333,-87.8486111
10/31/2004,tinley park,il,us,sphere,600,41.5733333,-87.7844444
10/31/2005,charlottesville,va,us,other,120,38.0291667,-78.4769444
10/31/2005,orland park,il,us,formation,2,41.6302778,-87.8538889
10/31/2008,springfield,or,us,fireball,600,44.0463889,-123.0208333
10/31/2010,pittsburgh,pa,us,fireball,60,40.4405556,-79.9961111
10/31/2011,monroe,mi,us,fireball,120,41.9163889,-83.3977778
10/31/2013,arcanum,oh,us,unknown,15,39.9900000,-84.5533333
10/3/2000,los angeles,ca,us,unknown,60,34.0522222,-118.2427778
10/3/2004,new york city (brooklyn),ny,us,light,3600,40.7141667,-74.0063889
10/3/2006,lakewood,ca,us,fireball,240,33.8536111,-118.1330556
10/3/2009,trenton,nc,us,formation,18,35.0669444,-77.3530556
10/3/2012,san francisco,ca,us,circle,120,37.7750000,-122.4183333
10/3/2013,diamond springs,ca,us,circle,600,38.6947222,-120.8138889
10/4/2000,richwood,tx,us,fireball,20,29.0558333,-95.4097222
10/4/2005,chanute,ks,us,light,120,37.6791667,-95.4569444
10/4/2007,boyne falls,mi,us,triangle,8,45.1680556,-84.9161111
10/4/2012,roanoke,va,us,cylinder,30,37.2708333,-79.9416667
10/4/2013,fairbanks,ak,us,fireball,180,64.8377778,-147.7163889
10/5/1999,chesapeake,va,us,other,30,36.8188889,-76.2752778
10/5/2003,wapakoneta,oh,us,light,1200,40.5677778,-84.1936111
10/5/2007,selah,wa,us,oval,120,46.6541667,-120.5288889
10/5/2010,livingston,tx,us,light,60,30.7108333,-94.9327778
10/5/2012,tulsa,ok,us,formation,120,36.1538889,-95.9925
10/5/2013,spokane,wa,us,sphere,300,47.6588889,-117.425
10/6/2001,park forest,il,us,triangle,15,41.4913889,-87.6744444
10/6/2004,oakland,ca,us,other,240,37.8044444,-122.2697222
10/6/2007,boonville,in,us,light,1800,38.0491667,-87.2741667
10/6/2010,lexington,ky,us,other,30,37.9886111,-84.4777778
10/6/2012,ocean beach,ca,us,disk,120,32.7444444,-117.2611111
10/6/2013,ashford,ct,us,fireball,900,41.8730556,-72.1219444
10/7/2001,kennett,mo,us,triangle,3,36.2361111,-90.0555556
10/7/2004,chandler,az,us,light,600,33.3061111,-111.8405556
10/7/2008,ronkonkoma,ny,us,egg,5400,40.8152778,-73.1127778
10/7/2011,topsail beach,nc,us,circle,180,34.3650000,-77.6308333
10/8/1987,wytheville,va,us,light,720,36.9483333,-81.085
10/8/2003,rising sun,md,us,other,600,39.6977778,-76.0630556
10/8/2006,grosse pointe woods,mi,us,light,5400,42.4436111,-82.9069444
10/8/2009,gila bend,az,us,formation,600,32.9477778,-112.7161111
10/8/2011,binghamton,ny,us,unknown,900,42.0986111,-75.9183333
10/8/2013,burlington,vt,us,light,30,44.4758333,-73.2125
10/9/1998,pikeville (farmingdale drive),nc,us,disk,60,35.4969444,-77.9822222
10/9/2004,lancaster,sc,us,rectangle,1800,34.7202778,-80.7711111
10/9/2008,santa maria,ca,us,other,15,34.9530556,-120.4347222
10/9/2010,san angelo,tx,us,fireball,5,31.4636111,-100.4366667
10/9/2011,new bedford,ma,us,fireball,1680,41.6361111,-70.9347222
10/9/2013,tempe,az,us,unknown,600,33.4147222,-111.9086111
1/10/1987,el centro (approaching from west),ca,us,sphere,300,32.7919444,-115.5622222
1/10/2001,bellingham,wa,us,triangle,180,48.7597222,-122.4869444
1/10/2005,savannah,ga,us,sphere,15,32.0833333,-81.1
1/10/2008,clearwater beach,fl,us,other,10,27.9769444,-82.8280556
1/10/2010,butler,mo,us,chevron,120,38.2538000,-94.3356
1/10/2013,milford,ma,us,triangle,60,42.1397222,-71.5166667
11/10/1995,brownsville,tx,us,circle,600,25.9013889,-97.4972222
11/10/2002,ivesdale,il,us,light,30,39.9433333,-88.4552778
11/10/2005,eastpointe,mi,us,teardrop,30,42.4683333,-82.9555556
11/10/2008,oakland,tn,us,fireball,15,35.2288889,-89.515
11/10/2011,stockbridge,ga,us,formation,600,33.5441667,-84.2338889
11/10/2012,moncton (canada),nb,ca,circle,300,46.083333,-64.766667
11/10/2013,irving,tx,us,fireball,40,32.8138889,-96.9486111
11/11/1999,el centro (50 miles west of&#44 on hwy 8),ca,us,cigar,120,32.7919444,-115.5622222
11/11/2003,brandon,fl,us,disk,900,27.9375000,-82.2861111
11/11/2006,redwood city,ca,us,light,15,37.4852778,-122.2352778
11/11/2010,wallkill,ny,us,other,240,41.6055556,-74.1844444
11/11/2012,leesburg,va,us,cylinder,30,39.1155556,-77.5638889
11/1/1962,valparaiso,fl,us,cigar,300,30.5083333,-86.5027778
11/1/1984,honey grove,tx,us,disk,300,33.5833333,-95.9097222
11/1/1996,federal way,wa,us,circle,2,47.3225000,-122.3113889
11/1/1999,san diego,ca,us,egg,600,32.7152778,-117.1563889
11/1/2001,huntington,wv,us,unknown,60,38.4191667,-82.4452778
1/11/2001,rockford,il,us,light,600,42.2711111,-89.0938889
11/1/2002,williamsburg,va,us,chevron,10,37.2705556,-76.7077778
1/11/2004,stony point,ny,us,light,300,41.2294444,-73.9875
11/1/2006,galveston,tx,us,cigar,2,29.3011111,-94.7975
11/1/2007,mars hill,nc,us,circle,2,35.8263889,-82.5494444
1/11/2009,dover,de,us,circle,2700,39.1580556,-75.5247222
11/1/2010,marietta,ga,us,chevron,30,33.9525000,-84.55
11/1/2011,washingtonville,ny,us,triangle,300,41.4277778,-74.1663889
11/1/2012,omaha,ne,us,rectangle,300,41.2586111,-95.9375
11/1/2013,lake elsinore,ca,us,sphere,600,33.6680556,-117.3263889
1/11/2014,new york city (queens),ny,us,light,60,40.7141667,-74.0063889
11/12/2000,orlando,fl,us,circle,5,28.5380556,-81.3794444
11/12/2004,memphis,tn,us,triangle,30,35.1494444,-90.0488889
11/12/2008,quail valley,ca,us,circle,600,33.7069444,-117.2441667
11/12/2010,san francisco,ca,us,other,20,37.7750000,-122.4183333
11/12/2012,lancaster,pa,us,changing,120,40.0377778,-76.3058333
11/13/1974,new orleans,la,us,disk,25,29.9544444,-90.075
11/13/2002,chillicothe,oh,us,other,60,39.3330556,-82.9825
11/13/2006,charlotte,nc,us,circle,300,35.2269444,-80.8433333
11/13/2009,celina,tx,us,circle,180,33.3244444,-96.7841667
11/13/2011,crandall,tx,us,disk,30,32.6277778,-96.4555556
11/13/2013,wadsworth,oh,us,cigar,7200,41.0255556,-81.73
11/14/1996,corvallis,mt,us,sphere,3,46.3141667,-114.1119444
11/14/1997,olympia,wa,us,fireball,30,47.0380556,-122.8994444
11/14/2002,kennesaw,ga,us,sphere,60,34.0233333,-84.6155556
11/14/2005,mandeville,la,us,fireball,10,30.3580556,-90.0655556
11/14/2009,rockingham,nc,us,triangle,10,34.9391667,-79.7741667
11/14/2012,lake ronkonkoma,ny,us,sphere,60,40.8350000,-73.1316667
11/14/2013,north conway,nh,us,formation,10,44.0536111,-71.1288889
11/15/1974,cordova,ak,us,disk,18000,60.5427778,-145.7575
11/15/1986,girdwood,ak,us,sphere,120,60.9425000,-149.1663889
11/15/1994,mountain city,tn,us,triangle,1200,36.4744444,-81.805
11/15/1998,cranston,ri,us,light,5,41.7797222,-71.4377778
11/15/2001,boyne city,mi,us,diamond,1800,45.2166667,-85.0138889
11/15/2003,athens,al,us,triangle,15,34.8027778,-86.9716667
11/15/2005,phoenix,az,us,circle,420,33.4483333,-112.0733333
11/15/2007,hurst,tx,us,circle,12,32.8233333,-97.1702778
11/15/2010,lakewood,wa,us,changing,1200,47.1719444,-122.5172222
11/15/2012,coral springs,fl,us,light,120,26.2708333,-80.2708333
11/15/2013,ocala,fl,us,diamond,300,29.1869444,-82.1402778
11/16/1999,griffith,in,us,flash,120,41.5283333,-87.4236111
11/16/1999,cookeville,tn,us,oval,20,36.1627778,-85.5016667
11/16/1999,chillicothe,oh,us,light,30,39.3330556,-82.9825
11/16/1999,springfield,oh,us,fireball,60,39.9241667,-83.8088889
11/16/1999,columbus,oh,us,light,120,39.9611111,-82.9988889
11/16/1999,burlingame,ca,us,other,1,37.5841667,-122.365
11/16/2003,wentzville,mo,us,light,3,38.8113889,-90.8527778
11/16/2006,panama city,fl,us,light,40,30.1586111,-85.6602778
11/16/2009,ventura,ca,us,formation,7,34.2783333,-119.2922222
11/16/2012,brainard (6 mi. e of; on hwy. 92),ne,us,unknown,300,41.1838889,-97.0036111
11/16/2013,jamestown,ri,us,fireball,480,41.4969444,-71.3677778
11/17/1997,clearwater beach,fl,us,oval,3600,27.9769444,-82.8280556
11/17/1999,sumrall,ms,us,unknown,120,31.4172222,-89.5422222
11/17/2004,salinas,ca,us,circle,60,36.6777778,-121.6544444
11/17/2008,alvin,tx,us,other,10,29.4236111,-95.2438889
11/17/2009,salt lake city,ut,us,unknown,1,40.7608333,-111.8902778
11/17/2011,houston,tx,us,other,10,29.7630556,-95.3630556
11/17/2012,phoenix,az,us,light,60,33.4483333,-112.0733333
11/18/1998,gainesville,fl,us,triangle,90,29.6513889,-82.325
11/18/2001,kahului,hi,us,disk,7200,20.8947222,-156.47
11/18/2001,miami beach,fl,us,sphere,10,25.7902778,-80.1302778
11/18/2004,mendham,nj,us,light,1200,40.7758333,-74.6011111
11/18/2007,sudbury (canada),on,ca,circle,300,46.5,-80.966667
11/18/2010,olivehurst,ca,us,formation,420,39.0955556,-121.5511111
11/18/2012,russell springs,ky,us,fireball,600,37.0561111,-85.0886111
11/19/1988,sunnyvale,ca,us,other,3600,37.3688889,-122.0352778
11/19/2002,stover,mo,us,circle,14400,38.4408333,-92.9916667
11/19/2003,chicago (west suburbs),il,us,light,300,41.8500000,-87.65
11/19/2006,center valley,pa,us,disk,60,40.5291667,-75.3936111
11/19/2009,sidney,tx,us,light,3,31.9491667,-98.7369444
11/19/2012,houlton,me,us,teardrop,1800,46.1261111,-67.8408333
11/19/2013,laguna niguel,ca,us,rectangle,600,33.5225000,-117.7066667
1/1/1974,kent,wa,us,cigar,300,47.3811111,-122.2336111
1/1/1995,travelers rest,sc,us,triangle,8,34.9675000,-82.4436111
1/1/2000,gurnee,il,us,light,60.3,42.3702778,-87.9019444
1/1/2003,burbank,ca,us,triangle,300,34.1808333,-118.3080556
1/1/2005,brentwood,ca,us,rectangle,600,37.9319444,-121.6947222
1/1/2007,lake station,in,us,light,300,41.5750000,-87.2388889
1/1/2008,jacksonville,fl,us,fireball,600,30.3319444,-81.6558333
1/1/2009,markle,in,us,circle,120,40.8291667,-85.3355556
1/1/2010,walworth,wi,us,sphere,420,42.5311111,-88.5994444
1/1/2011,miami,fl,us,other,600,25.7738889,-80.1938889
1/1/2012,port charlotte,fl,us,changing,900,26.9758333,-82.0908333
1/1/2012,lynchburg,va,us,light,420,37.4136111,-79.1425
1/1/2013,bristol,pa,us,oval,420,40.1005556,-74.8522222
1/1/2013,jacksonville beach,fl,us,disk,900,30.2944444,-81.3933333
1/1/2014,trussville,al,us,light,300,33.6197222,-86.6088889
1/1/2014,spanish fork,ut,us,unknown,900,40.1150000,-111.6541667
1/1/2014,gilroy,ca,us,formation,300,37.0058333,-121.5672222
11/20/1987,uvalde,tx,us,circle,3,29.2094444,-99.7858333
11/20/1999,sudbury (canada),on,ca,cylinder,90,46.5,-80.966667
11/20/2003,riverside,ca,us,circle,15,33.9533333,-117.3952778
11/20/2006,peabody,ma,us,circle,60,42.5277778,-70.9291667
11/20/2009,leavenworth,ks,us,sphere,60,39.3111111,-94.9222222
11/20/2013,fresno,ca,us,light,180,36.7477778,-119.7713889
11/21/1995,washburn,nd,us,triangle,20,47.2891667,-101.0286111
11/21/2003,mesa,az,us,egg,2,33.4222222,-111.8219444
11/21/2007,denton,tx,us,circle,60,33.2147222,-97.1327778
11/21/2010,albuquerque,nm,us,other,360,35.0844444,-106.6505556
11/21/2012,lake jackson,tx,us,circle,900,29.0336111,-95.4341667
11/2/1997,lyons,co,us,unknown,240,40.2247222,-105.2708333
1/12/2001,covington,va,us,circle,180,37.7933333,-79.9941667
11/2/2003,dallas,tx,us,flash,3,32.7833333,-96.8
1/12/2005,lancaster,ca,us,triangle,1200,34.6980556,-118.1358333
1/12/2007,meriden,ct,us,circle,20,41.5380556,-72.8075
11/2/2008,gregory,sd,us,sphere,600,43.2322222,-99.43
11/2/2009,madison,oh,us,triangle,1800,41.7711111,-81.05
1/12/2011,winter springs,fl,us,rectangle,1200,28.6986111,-81.3083333
1/12/2012,rosemount,mn,us,triangle,60,44.7394444,-93.1255556
1/12/2013,clayton,ga,us,oval,300,34.8780556,-83.4011111
1/12/2014,marion,sc,us,disk,180,34.1780556,-79.4008333
11/22/2000,delta (canada),bc,ca,cigar,120,50.183333,-98.316667
11/22/2003,airdrie (canada),ab,ca,unknown,1200,51.266667,-114.016667
11/22/2006,price,ut,us,teardrop,1800,39.5994444,-110.81
11/22/2010,topeka,ks,us,fireball,3,39.0483333,-95.6777778
11/22/2012,medford,or,us,diamond,240,42.3266667,-122.8744444
11/22/2013,anacortes,wa,us,light,600,48.5127778,-122.6113889
11/23/1998,sycamore,il,us,triangle,5,41.9888889,-88.6866667
11/23/2002,swaledale,ia,us,circle,300,42.9786111,-93.3166667
11/23/2005,bertram,tx,us,light,120,30.7436111,-98.0552778
11/23/2008,summerville,sc,us,light,900,33.0183333,-80.1758333
11/23/2012,brockton,ma,us,sphere,2,42.0833333,-71.0188889
11/24/1984,columbus,wi,us,cigar,10,43.3380556,-89.0152778
11/24/2002,santa fe,nm,us,chevron,10,35.6869444,-105.9372222
11/24/2006,wakeeney (near; trego county) (e on interstate 70),ks,us,other,6,39.0250000,-99.8791667
11/24/2009,canoga park,ca,us,other,40,34.2011111,-118.5972222
11/24/2012,salt lake city,ut,us,light,1200,40.7608333,-111.8902778
11/24/2013,greenville,nc,us,light,60,35.6125000,-77.3666667
11/25/2000,camarillo,ca,us,light,10,34.2163889,-119.0366667
11/25/2005,bloomington,in,us,cone,10800,39.1652778,-86.5263889
11/25/2009,chinle,az,us,other,420,36.1544444,-109.5519444
11/25/2012,las vegas,nv,us,unknown,3,36.1750000,-115.1363889
11/26/1976,houston,tx,us,circle,900,29.7630556,-95.3630556
11/26/2003,the dalles,or,us,light,10,45.5947222,-121.1775
11/26/2006,olympia,wa,us,light,3,47.0380556,-122.8994444
11/26/2009,mesa,az,us,fireball,120,33.4222222,-111.8219444
11/26/2013,amber,ok,us,disk,3600,35.1602778,-97.8788889
11/27/1998,standale,mi,us,triangle,5,42.9725000,-85.7763889
11/27/2003,ridgefield,wa,us,unknown,60,45.8152778,-122.7413889
11/27/2006,ocklawaha,fl,us,changing,900,29.0425000,-81.9294444
11/27/2010,tuttle,ok,us,teardrop,5,35.2908333,-97.8119444
11/27/2013,phoenix,az,us,triangle,30,33.4483333,-112.0733333
11/28/2001,redwood city,ca,us,light,15,37.4852778,-122.2352778
11/28/2003,bismarck,nd,us,other,1200,46.8083333,-100.7833333
11/28/2006,franklin,nc,us,light,3,35.1822222,-83.3816667
11/28/2007,boiling springs,pa,us,triangle,180,40.1497222,-77.1286111
11/28/2010,monroe,ct,us,other,180,41.3325000,-73.2077778
11/28/2013,polk city,fl,us,sphere,10,28.1822222,-81.8241667
11/28/2013,sobieski,wi,us,fireball,120,44.7208333,-88.0719444
11/29/2001,golden,co,us,light,3,39.7555556,-105.2205556
11/29/2005,grove hill,al,us,triangle,5,31.7086111,-87.7772222
11/29/2011,glendora,ca,us,circle,2700,34.1361111,-117.8644444
11/29/2013,shelby,oh,us,formation,60,40.8813889,-82.6619444
11/30/1999,jackson (west of),mi,us,fireball,3,42.2458333,-84.4013889
11/30/2003,st. louis,mo,us,unknown,600,38.6272222,-90.1977778
11/30/2007,heath,oh,us,unknown,900,40.0227778,-82.4447222
11/30/2012,union city,ca,us,light,600,37.5958333,-122.0180556
11/30/2013,kearneysville,wv,us,fireball,300,39.3880556,-77.8858333
11/3/2000,bend,or,us,circle,300,44.0583333,-121.3141667
11/3/2003,everett,wa,us,circle,300,47.9791667,-122.2008333
1/13/2005,milwaukee,wi,us,formation,20,43.0388889,-87.9063889
11/3/2005,concord,ca,us,flash,2,37.9780556,-122.03
11/3/2007,corona,ca,us,other,120,33.8752778,-117.5655556
11/3/2009,laurel,md,us,sphere,20,39.0991667,-76.8486111
11/3/2010,albany,ny,us,light,10800,42.6525000,-73.7566667
11/3/2012,denton,tx,us,disk,7200,33.2147222,-97.1327778
11/3/2012,florissant,mo,us,sphere,120,38.7891667,-90.3225
1/13/2013,candler,nc,us,triangle,900,35.5363889,-82.6930556
1/14/1991,derry,nh,us,disk,120,42.8805556,-71.3277778
11/4/2001,dublin,oh,us,cigar,625,40.0991667,-83.1141667
1/14/2003,grandview,mo,us,oval,300,38.8858333,-94.5327778
1/14/2006,mendenhall,ms,us,diamond,180,31.9616667,-89.87
1/14/2007,walnut creek,ca,us,unknown,180,37.9063889,-122.0638889
1/14/2009,argyle,tx,us,disk,360,33.1211111,-97.1830556
11/4/2010,reno,nv,us,formation,2,39.5297222,-119.8127778
1/14/2012,fort mill,sc,us,light,480,35.0072222,-80.9452778
1/14/2013,scottsdale,az,us,fireball,3600,33.5091667,-111.8983333
1/14/2014,west kelowna (canada),bc,ca,other,900,49.9,-119.483333
1/15/1981,davenport,ia,us,cigar,1260,41.5236111,-90.5775
1/15/1997,columbia,sc,us,light,4,34.0005556,-81.035
11/5/1999,springfield (14 mi. s of&#44 near highlandville),mo,us,fireball,240,37.2152778,-93.2980556
1/15/2002,st. albert (canada),ab,ca,light,120,53.633333,-113.633333
11/5/2003,alexandria,va,us,unknown,2,38.8047222,-77.0472222
11/5/2004,grand prairie,tx,us,unknown,3600,32.7458333,-96.9975
11/5/2005,laramie,wy,us,light,2,41.3113889,-105.5905556
11/5/2007,kansas city,ks,us,circle,60,39.1141667,-94.6272222
1/15/2008,dixon,il,us,unknown,30,41.8388889,-89.4794444
11/5/2009,grapevine,tx,us,light,300,32.9341667,-97.0777778
11/5/2010,jackson,ca,us,oval,30,38.3488889,-120.7730556
11/5/2012,kenilworth,nj,us,unknown,600,40.6763889,-74.2911111
11/5/2012,del mar,ca,us,triangle,10,32.9594444,-117.2644444
11/5/2013,mayflower,ar,us,triangle,1300,34.9569444,-92.4272222
11/6/1989,kingman (north of&#44 mt. tipton area),az,us,sphere,60,35.1894444,-114.0522222
1/16/2001,kent,wa,us,light,3600,47.3811111,-122.2336111
1/16/2003,escondido,ca,us,cone,600,33.1191667,-117.0855556
11/6/2005,ellsinore,mo,us,fireball,20,36.9341667,-90.7466667
1/16/2007,burbank,ca,us,disk,4,34.1808333,-118.3080556
1/16/2008,denver,in,us,triangle,2700,40.8661111,-86.0775
1/16/2010,corona,ca,us,triangle,300,33.8752778,-117.5655556
1/16/2011,new york,ny,us,light,300,40.7141667,-74.0063889
1/16/2012,surrey (canada),bc,ca,cylinder,30,49.136353351,-122.821343315
1/16/2014,cary,nc,us,triangle,600,35.7913889,-78.7813889
11/7/1999,northbrook,il,us,diamond,300,42.1275000,-87.8288889
1/17/2002,indianola,ia,us,light,5,41.3580556,-93.5572222
1/17/2003,panorama city,ca,us,circle,900,34.2247222,-118.4488889
11/7/2005,bastrop,tx,us,light,900,30.1102778,-97.315
11/7/2006,aurora,il,us,unknown,30,41.7605556,-88.32
1/17/2008,st. catharines (canada),on,ca,sphere,600,43.166667,-79.233333
11/7/2009,reno,nv,us,cylinder,2,39.5297222,-119.8127778
1/17/2011,coeur d&#39alene,id,us,circle,25,47.6777778,-116.7794444
11/7/2012,orlando,fl,us,light,5,28.5380556,-81.3794444
11/7/2013,longmont,co,us,sphere,10,40.1672222,-105.1013889
11/8/1997,saugus,ca,us,other,1800,34.4113889,-118.5391667
11/8/2001,barrington,il,us,oval,300,42.1538889,-88.1361111
11/8/2003,west bloomfield,mi,us,fireball,6,42.5377778,-83.2330556
11/8/2003,portland,me,us,other,4,43.6613889,-70.2558333
11/8/2005,enterprise,al,us,light,10,31.3150000,-85.8552778
11/8/2006,new braunfels,tx,us,fireball,10,29.7027778,-98.1241667
1/18/2008,new hampton,ny,us,circle,1200,41.4108333,-74.4075
1/18/2009,fremont,ca,us,fireball,3,37.5483333,-121.9875
1/18/2010,whitehall,mt,us,sphere,2,45.8708333,-112.0966667
11/8/2012,mckinleyville,ca,us,circle,300,40.9466667,-124.0994444
1/18/2012,ceres,ca,us,fireball,180,37.5950000,-120.9566667
11/8/2013,tomball,tx,us,triangle,1080,30.0969444,-95.6158333
1/18/2014,lake havasu city,az,us,fireball,300,34.4838889,-114.3216667
11/9/1999,cave spring,ga,us,disk,180,34.1075000,-85.3363889
11/9/2002,tempe,az,us,sphere,4,33.4147222,-111.9086111
11/9/2005,newborn,ga,us,triangle,600,33.5169444,-83.6961111
11/9/2007,destin,fl,us,rectangle,180,30.3933333,-86.4958333
11/9/2008,mcdonough,ga,us,other,2,33.4472222,-84.1469444
11/9/2010,lexington,ky,us,unknown,180,37.9886111,-84.4777778
11/9/2012,kutztown,pa,us,unknown,40,40.5172222,-75.7777778
11/9/2012,ketchikan,ak,us,light,7200,55.3422222,-131.6461111
11/9/2013,ralston,ne,us,chevron,10,41.2052778,-96.0422222
1/20/1969,lake wales,fl,us,disk,300,27.9011111,-81.5861111
1/20/2001,poughquag,ny,us,circle,300,41.6088889,-73.6822222
1/20/2007,elizabeth,wv,us,circle,420,39.0633333,-81.3952778
1/20/2008,oak lawn,il,us,oval,20,41.7108333,-87.7580556
1/20/2012,tonawanda,ny,us,other,600,43.0202778,-78.8805556
1/20/2014,morganton,nc,us,circle,300,35.7452778,-81.685
12/10/1999,sherman oaks,ca,us,other,300,34.1511111,-118.4483333
12/10/2004,adrian,mi,us,triangle,120,41.8975000,-84.0372222
12/10/2007,smyrna,ga,us,other,1200,33.8838889,-84.5144444
12/10/2008,edwardsville,il,us,oval,2,38.8113889,-89.9530556
12/10/2012,omaha,ne,us,sphere,900,41.2586111,-95.9375
12/10/2013,fairbanks,ak,us,unknown,14,64.8377778,-147.7163889
12/11/2004,coconut creek,fl,us,diamond,300,26.2513889,-80.1791667
12/11/2007,madison,al,us,circle,540,34.6991667,-86.7483333
12/11/2011,avalon,ca,us,light,10,33.3427778,-118.3269444
12/11/2013,powell,wy,us,chevron,10,44.7538889,-108.7566667
12/1/1989,grand canyon (north rim),az,us,formation,1800,36.0544444,-112.1386111
12/1/2000,kilauea,hi,us,fireball,10,22.2119444,-159.4122222
12/1/2001,sneads ferry,nc,us,disk,86400,34.5525000,-77.3975
12/1/2002,warren,or,us,sphere,900,45.8191667,-122.8477778
12/1/2003,baltimore,md,us,chevron,2,39.2902778,-76.6125
1/21/2005,sentinel,az,us,teardrop,300,32.8580556,-113.2125
12/1/2007,tupper lake,ny,us,circle,30,44.1669444,-74.5383333
12/1/2009,woodbridge,nj,us,rectangle,420,40.5575000,-74.285
12/1/2010,carterville,il,us,triangle,180,37.7600000,-89.0772222
12/1/2011,manassas,va,us,formation,180,38.7508333,-77.4755556
12/1/2013,lake ariel,pa,us,fireball,60,41.4538889,-75.3830556
12/12/1973,kirkland,wa,us,triangle,180,47.6816667,-122.2075
12/12/2004,phoenix,az,us,sphere,120,33.4483333,-112.0733333
12/12/2007,charlotte,nc,us,changing,600,35.2269444,-80.8433333
12/12/2009,daly city,ca,us,triangle,1800,37.7058333,-122.4608333
12/12/2012,nashua,nh,us,sphere,120,42.7652778,-71.4680556
12/12/2013,grovetown,ga,us,light,1200,33.4502778,-82.1983333
12/13/2002,centreville,va,us,teardrop,120,38.8402778,-77.4291667
12/13/2005,harrisburg,pa,us,formation,900,40.2736111,-76.8847222
12/13/2008,new hope,mn,us,diamond,900,45.0380556,-93.3863889
12/13/2012,abington,pa,us,triangle,90,40.1205556,-75.1183333
12/13/2013,princeton,wv,us,circle,180,37.3661111,-81.1027778
12/14/1991,tell city,in,us,circle,30,37.9513889,-86.7677778
12/14/2003,rocklin,ca,us,circle,1,38.7908333,-121.2347222
12/14/2007,kingsland,ga,us,triangle,900,30.7997222,-81.69
12/14/2011,rocklin,ca,us,formation,30,38.7908333,-121.2347222
12/14/2013,phoenix,az,us,fireball,5,33.4483333,-112.0733333
12/15/1993,laguna beach,ca,us,oval,45,33.5422222,-117.7822222
12/15/1998,oroville,ca,us,light,1200,39.5138889,-121.5552778
12/15/2002,hazelton (17 km north) (canada),bc,ca,light,240,55.25,-127.666667
12/15/2004,charleston,mo,us,unknown,600,36.9208333,-89.3505556
12/15/2007,newark,de,us,circle,900,39.6836111,-75.75
12/15/2011,st. petersburg,fl,us,other,3,27.7705556,-82.6794444
12/15/2013,escondido,ca,us,sphere,180,33.1191667,-117.0855556
12/16/2002,coral springs,fl,us,oval,180,26.2708333,-80.2708333
12/16/2006,port huron,mi,us,sphere,600,42.9708333,-82.425
12/16/2008,chino,ca,us,fireball,240,34.0122222,-117.6880556
12/16/2012,haleiwa,hi,us,oval,3,21.5902778,-158.1125
12/17/1997,burlington,vt,us,diamond,180,44.4758333,-73.2125
12/17/2003,austell,ga,us,light,2700,33.8125000,-84.6344444
12/17/2010,rio rico,az,us,circle,720,31.4713889,-110.9758333
12/17/2012,delray beach,fl,us,fireball,300,26.4611111,-80.0730556
12/18/2000,spokane,wa,us,light,7200,47.6588889,-117.425
12/18/2005,warwick,ri,us,triangle,360,41.7000000,-71.4166667
12/18/2008,pompano beach,fl,us,cylinder,1,26.2375000,-80.125
12/18/2012,attalla,al,us,light,30,34.0216667,-86.0886111
12/19/1999,santa fe,nm,us,circle,10,35.6869444,-105.9372222
12/19/2005,lockport,il,us,circle,660,41.5894444,-88.0577778
12/19/2011,billings,mt,us,light,7,45.7833333,-108.5
12/19/2013,santa paula,ca,us,light,1800,34.3541667,-119.0583333
1/2/2002,fort mcmurray (canada),ab,ca,cone,7200,56.733333,-111.383333
1/2/2007,chicago,il,us,formation,120,41.8500000,-87.65
1/2/2009,ballinger,tx,us,other,5400,31.7380556,-99.9469444
1/2/2012,san francisco,ca,us,unknown,75,37.7750000,-122.4183333
12/20/1970,meriden,ct,us,unknown,600,41.5380556,-72.8075
12/20/2000,monroe,ct,us,triangle,300,41.3325000,-73.2077778
12/20/2006,corydon,in,us,light,20,38.2119444,-86.1219444
12/20/2010,newark,nj,us,light,600,40.7355556,-74.1727778
12/20/2012,yelm,wa,us,oval,420,46.9422222,-122.6047222
12/21/2001,bellevue,ne,us,sphere,180,41.1366667,-95.8905556
12/21/2006,maricopa,az,us,light,600,33.0580556,-112.0469444
12/21/2012,webster,tx,us,changing,5400,29.5375000,-95.1180556
12/21/2013,burbank,ca,us,light,300,34.1808333,-118.3080556
12/2/2001,springfield,oh,us,light,5,39.9241667,-83.8088889
1/22/2003,salisbury,md,us,light,10,38.3605556,-75.5997222
12/2/2005,lexington,ky,us,circle,60,37.9886111,-84.4777778
12/2/2008,borrego springs,ca,us,disk,60,33.2558333,-116.3741667
1/22/2009,las vegas,nv,us,diamond,30,36.1750000,-115.1363889
12/2/2011,redding,ca,us,light,10,40.5866667,-122.3905556
1/22/2013,arlington,tx,us,triangle,240,32.7355556,-97.1077778
12/22/1965,houston (west of),tx,us,formation,180,29.7630556,-95.3630556
12/22/2003,pahoa,hi,us,circle,240,19.4975000,-154.9508333
12/22/2008,hammonton,nj,us,triangle,300,39.6363889,-74.8027778
12/22/2012,sanbornton,nh,us,triangle,600,43.4891667,-71.5827778
12/23/1987,ocala,fl,us,triangle,120,29.1869444,-82.1402778
12/23/2003,gasport,ny,us,light,10800,43.1991667,-78.5763889
12/23/2006,ventura,ca,us,light,3,34.2783333,-119.2922222
12/23/2010,manteno,il,us,egg,300,41.2505556,-87.8313889
12/23/2012,venice,fl,us,fireball,300,27.0994444,-82.4544444
12/24/1972,colorado springs,co,us,disk,120,38.8338889,-104.8208333
12/24/2001,las vegas,nv,us,rectangle,120,36.1750000,-115.1363889
12/24/2005,plantation,fl,us,fireball,90,26.1272222,-80.2333333
12/24/2008,rochester,ny,us,other,120,43.1547222,-77.6158333
12/24/2011,clarks green,pa,us,unknown,120,41.4927778,-75.7
12/24/2012,lake barrington,il,us,triangle,480,42.2125000,-88.1525
12/24/2013,bethel park,pa,us,circle,180,40.3275000,-80.0397222
12/24/2013,rapid city,sd,us,cylinder,2400,44.0805556,-103.2305556
12/25/2000,miami,fl,us,egg,600,25.7738889,-80.1938889
12/25/2004,saskatoon (canada),sk,ca,triangle,600,52.133333,-106.666667
12/25/2008,south burlington,vt,us,light,1800,44.4669444,-73.1713889
12/25/2011,cedar rapids,ia,us,fireball,50,42.0083333,-91.6438889
12/25/2012,landover,md,us,light,25,38.9338889,-76.8969444
12/25/2013,mccordsville,in,us,sphere,300,39.9080556,-85.9227778
12/26/1999,vancouver,wa,us,unknown,15,45.6388889,-122.6602778
12/26/2003,sicamous (canada),bc,ca,light,37800,50.833333,-119.0
12/26/2010,fort lauderdale,fl,us,other,5,26.1219444,-80.1436111
12/26/2013,little rock,ar,us,cigar,180,34.7463889,-92.2894444
12/27/2000,saco,me,us,triangle,180,43.5008333,-70.4433333
12/27/2005,manhattan,ks,us,cross,180,39.1836111,-96.5713889
12/27/2010,chatham (canada),on,ca,circle,300,42.4,-82.183333
12/27/2013,marietta,mn,us,light,120,45.0083333,-96.4172222
12/28/1998,kure beach,nc,us,cone,300,33.9966667,-77.9075
12/28/2004,terre haute,in,us,light,900,39.4666667,-87.4138889
12/28/2008,peoria,il,us,other,600,40.6936111,-89.5888889
12/28/2012,edwards,il,us,light,6,40.7458333,-89.7441667
12/28/2013,orlando,fl,us,unknown,1800,28.5380556,-81.3794444
12/29/2002,santa rosa,ca,us,circle,6,38.4405556,-122.7133333
12/29/2007,silverdale,wa,us,triangle,300,47.6447222,-122.6936111
12/29/2010,elmhurst,il,us,sphere,30,41.8994444,-87.9402778
12/29/2012,edmond,ok,us,circle,40,35.6527778,-97.4777778
12/30/1999,gansevoort,ny,us,sphere,5,43.1961111,-73.6522222
12/30/2005,great bend,ks,us,fireball,900,38.3644444,-98.7644444
12/30/2010,cayucos,ca,us,oval,10,35.4427778,-120.8911111
12/30/2013,coloma,mi,us,formation,180,42.1861111,-86.3083333
12/31/1999,las vegas,nv,us,circle,600,36.1750000,-115.1363889
12/31/2003,olive branch,ms,us,disk,300,34.9616667,-89.8294444
12/31/2006,brawley,ca,us,circle,120,32.9786111,-115.5294444
12/31/2008,carver,ma,us,unknown,20,41.8833333,-70.7630556
12/31/2010,temecula,ca,us,fireball,240,33.4936111,-117.1475
12/31/2011,alton bay,nh,us,sphere,120,43.4686111,-71.2325
12/31/2011,pasadena,ca,us,circle,300,34.1477778,-118.1436111
12/31/2012,londonderry,nh,us,light,180,42.8650000,-71.3744444
12/31/2012,hollywood,ca,us,fireball,300,34.0983333,-118.3258333
12/31/2013,new port richey,fl,us,disk,1200,28.2438889,-82.7194444
12/31/2013,magna,ut,us,circle,2700,40.7091667,-112.1008333
1/23/1980,virginia beach,va,us,cylinder,1200,36.8527778,-75.9783333
12/3/2001,brock,tx,us,fireball,300,32.6761111,-97.9405556
12/3/2003,whitmore lake,mi,us,unknown,2700,42.4394444,-83.7438889
12/3/2005,norwalk,ca,us,light,300,33.9022222,-118.0808333
1/23/2007,hoover,al,us,triangle,120,33.4052778,-86.8113889
1/23/2009,hightstown,nj,us,triangle,60,40.2694444,-74.5236111
12/3/2011,st. louis (afton),mo,us,circle,180,38.6272222,-90.1977778
12/3/2012,scituate,ma,us,light,2700,42.1958333,-70.7263889
1/23/2014,tabernacle,nj,us,unknown,240,39.8438889,-74.7105556
1/24/1998,san bernardino,ca,us,sphere,1800,34.1083333,-117.2888889
12/4/2003,whitehouse station,nj,us,circle,2,40.6152778,-74.7708333
12/4/2005,west los angeles,ca,us,light,3600,34.0522222,-118.2427778
1/24/2007,spokane,wa,us,triangle,60,47.6588889,-117.425
1/24/2008,hammond,in,us,unknown,180,41.5833333,-87.5
1/24/2009,pipe creek,tx,us,light,1800,29.7233333,-98.9355556
12/4/2012,albuquerque,nm,us,diamond,1800,35.0844444,-106.6505556
12/4/2013,jacksonville,fl,us,cigar,600,30.3319444,-81.6558333
1/24/2014,lubbock,tx,us,light,180,33.5777778,-101.8547222
12/5/1999,coolidge,az,us,triangle,40,32.9777778,-111.5169444
12/5/2001,ferrum,va,us,oval,60,36.9227778,-80.0136111
12/5/2003,sedona,az,us,disk,360,34.8697222,-111.7602778
12/5/2005,cheyenne,wy,us,unknown,5,41.1400000,-104.8197222
1/25/2007,aurora,co,us,light,30,39.7294444,-104.8313889
12/5/2008,south hiram,me,us,teardrop,5,43.8127778,-70.8780556
12/5/2010,milford,ct,us,circle,30,41.2222222,-73.0569444
12/5/2012,hamilton (canada),on,ca,light,600,43.25,-79.833333
1/25/2013,hope,me,us,triangle,60,44.2650000,-69.1594444
1/25/2014,calgary (canada),ab,ca,changing,300,51.083333,-114.083333
12/6/2000,roswell,nm,us,triangle,360,33.3941667,-104.5225
12/6/2002,san diego,ca,us,chevron,60,32.7152778,-117.1563889
12/6/2006,warrington,pa,us,triangle,180,40.2491667,-75.1344444
12/6/2008,marana,az,us,sphere,20,32.4366667,-111.2247222
1/26/2009,owasso,ok,us,triangle,600,36.2694444,-95.8544444
1/26/2011,lehi,ut,us,formation,600,40.3916667,-111.85
1/26/2012,beaumont,tx,us,triangle,120,30.0858333,-94.1016667
1/26/2014,wetumpka,al,us,sphere,60,32.5436111,-86.2119444
12/7/1999,emory,tx,us,sphere,3,32.8744444,-95.7652778
12/7/2003,toms river,nj,us,unknown,1440,39.9536111,-74.1983333
12/7/2005,parsippany,nj,us,other,300,40.8577778,-74.4263889
1/27/2008,tazewell,tn,us,light,10,36.4541667,-83.5694444
12/7/2010,santee,ca,us,oval,300,32.8383333,-116.9730556
12/7/2012,houston,tx,us,unknown,2,29.7630556,-95.3630556
12/7/2013,charleston (james island),sc,us,other,60,32.7763889,-79.9311111
1/27/2014,alameda,ca,us,diamond,5,37.7652778,-122.2405556
1/28/2000,rohnert park,ca,us,light,15,38.3397222,-122.7
1/28/2003,national city,ca,us,unknown,60,32.6780556,-117.0983333
1/28/2005,waianae,hi,us,triangle,1,21.4447222,-158.19
12/8/2006,griffithsville,wv,us,cylinder,45,38.2386111,-81.9894444
1/28/2008,waynesburg,oh,us,triangle,10,40.6677778,-81.2575
1/28/2010,stillwater,mn,us,light,900,45.0563889,-92.8058333
12/8/2012,spindale,nc,us,circle,300,35.3600000,-81.9294444
12/8/2013,homosassa,fl,us,light,900,28.7811111,-82.6152778
1/29/1989,montgomery,il,us,unknown,5,41.7305556,-88.3458333
12/9/2000,mesa,az,us,light,900,33.4222222,-111.8219444
1/29/2003,los angeles,ca,us,egg,30,34.0522222,-118.2427778
1/29/2006,el paso,tx,us,circle,900,31.7586111,-106.4863889
1/29/2008,tilton,nh,us,formation,300,43.4422222,-71.5894444
1/29/2010,madison county,nc,us,diamond,60,36.3852778,-79.9597222
12/9/2011,sarasota,fl,us,unknown,300,27.3361111,-82.5308333
12/9/2013,buffalo,wy,us,light,1800,44.3483333,-106.6983333
1/30/1987,kenai,ak,us,light,5,60.5544444,-151.2583333
1/30/2005,ottawa (canada),on,ca,oval,300,45.416667,-75.7
1/30/2009,baker,la,us,light,600,30.5880556,-91.1680556
1/30/2014,boscawen,nh,us,circle,300,43.3150000,-71.6213889
1/31/2002,helotes,tx,us,sphere,30,29.5777778,-98.6894444
1/31/2007,burlington,ia,us,triangle,720,40.8075000,-91.1127778
1/31/2009,canyon lake,tx,us,fireball,4,29.8750000,-98.2622222
1/31/2014,moncton (canada),nb,ca,fireball,2,46.083333,-64.766667
1/3/2001,portland,or,us,sphere,20,45.5236111,-122.675
1/3/2007,charlotte,nc,us,light,1800,35.2269444,-80.8433333
1/3/2009,st. petersburg,fl,us,oval,300,27.7705556,-82.6794444
1/3/2012,oswego,il,us,sphere,3600,41.6827778,-88.3513889
1/3/2014,morton,il,us,other,900,40.6127778,-89.4591667
1/4/2003,elsberry,mo,us,flash,2,39.1666667,-90.7808333
1/4/2006,gulf breeze,fl,us,fireball,600,30.3569444,-87.1638889
1/4/2009,ventura,ca,us,chevron,1200,34.2783333,-119.2922222
1/4/2012,keene,nh,us,cone,14400,42.9336111,-72.2786111
1/4/2014,berea,oh,us,fireball,4,41.3661111,-81.8544444
1/5/1999,alamogordo,nm,us,disk,900,32.8994444,-105.9597222
1/5/2002,new york city (brooklyn),ny,us,disk,15,40.7141667,-74.0063889
1/5/2007,douglas,mi,us,other,240,42.6433333,-86.2005556
1/5/2011,guymon,ok,us,circle,180,36.6827778,-101.4811111
1/5/2014,columbia,mo,us,light,25,38.9516667,-92.3338889
1/6/2003,montclair,ca,us,fireball,10,34.0775000,-117.6888889
1/6/2009,rancho cucamonga,ca,us,light,1380,34.1063889,-117.5922222
1/6/2012,new york city (queens),ny,us,fireball,15,40.7141667,-74.0063889
1/6/2013,whitefish,mt,us,other,120,48.4111111,-114.3366667
1/7/1999,charlotte,nc,us,triangle,300,35.2269444,-80.8433333
1/7/2003,palos heights,il,us,cross,600,41.6680556,-87.7963889
1/7/2007,cleveland,oh,us,unknown,7200,41.4994444,-81.6955556
1/7/2010,southampton,ny,us,formation,30,40.8841667,-72.39
1/7/2014,savannah,ga,us,light,7,32.0833333,-81.1
1/8/2001,crookston,mn,us,other,2,47.7741667,-96.6077778
1/8/2006,palm springs,ca,us,rectangle,22,33.8302778,-116.5444444
1/8/2008,san jose,ca,us,triangle,7200,37.3394444,-121.8938889
1/8/2012,parkville,mo,us,light,120,39.1950000,-94.6819444
1/8/2014,westfield,wi,us,light,300,43.8836111,-89.4933333
1/9/2002,duncan (canada),bc,ca,light,180,48.783333,-123.7
1/9/2008,valdosta,ga,us,diamond,10,30.8325000,-83.2786111
1/9/2011,terrebonne,or,us,circle,109800,44.3530556,-121.1766667
1/9/2014,scottsdale,az,us,light,900,33.5091667,-111.8983333
2/10/2001,san diego,ca,us,fireball,600,32.7152778,-117.1563889
2/10/2005,waukesha,wi,us,sphere,10,43.0116667,-88.2313889
2/10/2010,eaton rapids,mi,us,other,3,42.5091667,-84.6558333
2/10/2014,wilmington,nc,us,triangle,300,34.2255556,-77.945
2/11/2002,milton,wv,us,cylinder,900,38.4344444,-82.1325
2/11/2006,erwinna,pa,us,light,3600,40.5005556,-75.0730556
2/11/2009,kelso,wa,us,light,20,46.1469444,-122.9072222
2/11/2014,st. louis,mo,us,cigar,180,38.6272222,-90.1977778
2/1/1997,elizabeth,nj,us,sphere,30,40.6638889,-74.2111111
2/1/2003,crown point,in,us,oval,3,41.4169444,-87.3652778
2/1/2007,los angeles,ca,us,fireball,45,34.0522222,-118.2427778
2/1/2010,marana,az,us,light,180,32.4366667,-111.2247222
2/1/2012,fullerton,ca,us,fireball,300,33.8702778,-117.9244444
2/1/2014,portland,or,us,light,3,45.5236111,-122.675
2/12/2002,concord,nc,us,light,240,35.4086111,-80.5797222
2/12/2007,lynn haven,fl,us,disk,15,30.2452778,-85.6483333
2/12/2010,yakima,wa,us,fireball,15,46.6022222,-120.5047222
2/12/2014,missoula,mt,us,fireball,300,46.8722222,-113.9930556
2/13/2003,south paris,me,us,sphere,14400,44.2236111,-70.5138889
2/13/2008,phoenix,az,us,light,780,33.4483333,-112.0733333
2/13/2010,sunnyvale,ca,us,formation,15,37.3688889,-122.0352778
2/13/2014,chapmansboro,tn,us,other,900,36.3122222,-87.1413889
2/14/2000,hermitage,ar,us,sphere,60,33.4463889,-92.1738889
2/14/2004,newtown,pa,us,oval,2,40.2291667,-74.9372222
2/14/2007,stone mountain,ga,us,disk,240,33.8080556,-84.1702778
2/14/2011,iron mountain,mi,us,circle,300,45.8202778,-88.0658333
2/14/2013,connersville,in,us,light,20,39.6411111,-85.1411111
2/15/1931,holyoke (6-8 miles southwest of),co,us,oval,60,40.5844444,-102.3019444
2/15/1990,brockton,ma,us,other,600,42.0833333,-71.0188889
2/15/1999,worcester,ma,us,unknown,30,42.2625000,-71.8027778
2/15/2003,surrey (canada),bc,ca,sphere,1800,49.136353351,-122.821343315
2/15/2005,seattle,wa,us,other,300,47.6063889,-122.3308333
2/15/2008,los angeles,ca,us,light,1200,34.0522222,-118.2427778
2/15/2011,salisbury,nc,us,light,240,35.6708333,-80.4744444
2/15/2014,las vegas,nv,us,fireball,120,36.1750000,-115.1363889
2/16/2001,china,tx,us,light,1800,30.0477778,-94.3355556
2/16/2004,terre haute,in,us,flash,5,39.4666667,-87.4138889
2/16/2008,edmonton (canada),ab,ca,light,3600,53.55,-113.5
2/16/2011,santa maria,ca,us,circle,12,34.9530556,-120.4347222
2/16/2014,cambria,ca,us,circle,240,35.5641667,-121.0797222
2/17/2003,price,ut,us,fireball,10,39.5994444,-110.81
2/17/2006,san manuel,tx,us,circle,180,26.5641667,-98.1208333
2/17/2009,madison,nj,us,light,600,40.7597222,-74.4175
2/17/2013,forest grove,or,us,fireball,1200,45.5200000,-123.1094444
2/18/2001,cabazon,ca,us,cigar,300,33.9175000,-116.7863889
2/18/2006,silverdale,wa,us,unknown,150,47.6447222,-122.6936111
2/18/2011,lebanon,oh,us,other,600,39.4352778,-84.2030556
2/18/2014,houston,tx,us,disk,480,29.7630556,-95.3630556
2/19/2001,sedalia,mo,us,changing,1,38.7044444,-93.2280556
2/19/2008,cheney,wa,us,flash,3,47.4875000,-117.5747222
2/19/2011,snohomish,wa,us,light,5,47.9130556,-122.0969444
2/19/2014,tucson,az,us,light,3,32.2216667,-110.9258333
2/20/2000,athens,oh,us,cylinder,90,39.3291667,-82.1013889
2/20/2004,phoenix,az,us,disk,900,33.4483333,-112.0733333
2/20/2008,myrtle beach,sc,us,light,30,33.6888889,-78.8869444
2/20/2009,egan,la,us,diamond,30,30.2366667,-92.5058333
2/20/2013,huber heights,oh,us,unknown,300,39.8438889,-84.1247222
2/21/2000,corvallis,or,us,fireball,10,44.5647222,-123.2608333
2/21/2006,north kingstown,ri,us,other,60,41.5500000,-71.4666667
2/21/2009,corona,ca,us,circle,40,33.8752778,-117.5655556
2/21/2014,anchorage,ak,us,oval,4,61.2180556,-149.9002778
2/2/1980,georgetown,de,us,triangle,1200,38.6900000,-75.3858333
2/2/2002,martinsville,il,us,triangle,1800,39.3355556,-87.8819444
2/2/2005,west covina,ca,us,other,600,34.0900000,-117.8894444
2/2/2009,maryville,tn,us,light,60,35.7563889,-83.9705556
2/2/2012,orem,ut,us,light,60,40.2969444,-111.6938889
2/2/2014,ann arbor,mi,us,triangle,30,42.2708333,-83.7263889
2/22/2002,belleville,il,us,cylinder,900,38.5200000,-89.9838889
2/22/2007,durham,nh,us,changing,900,43.1338889,-70.9269444
2/22/2011,gillsville,ga,us,oval,180,34.3077778,-83.6336111
2/22/2014,savannah,mo,us,other,5,39.9416667,-94.83
2/23/1998,ossipee,nh,us,light,60,43.6852778,-71.1172222
2/23/2003,college station,tx,us,circle,60,30.6277778,-96.3341667
2/23/2007,denver,co,us,unknown,2,39.7391667,-104.9841667
2/23/2011,cathedral city,ca,us,sphere,3600,33.7797222,-116.4644444
2/23/2014,fritch,tx,us,light,300,35.6397222,-101.6027778
2/24/2001,kettering,oh,us,light,45,39.6894444,-84.1688889
2/24/2005,coal hill,ar,us,light,1800,35.4372222,-93.6727778
2/24/2008,elizabeth,nj,us,sphere,30,40.6638889,-74.2111111
2/24/2013,marion,in,us,cigar,900,40.5583333,-85.6591667
2/25/1998,harrisburg,pa,us,cigar,1380,40.2736111,-76.8847222
2/25/2005,seeley lake,mt,us,light,1800,47.1794444,-113.4836111
2/25/2009,marlborough,ct,us,triangle,600,41.6313889,-72.4602778
2/25/2012,charlotte,nc,us,cross,3,35.2269444,-80.8433333
2/26/2000,goshen,in,us,light,600,41.5822222,-85.8344444
2/26/2006,tampa,fl,us,unknown,1800,27.9472222,-82.4586111
2/26/2011,gillam (canada),mb,ca,rectangle,900,56.35,-94.7
2/26/2014,seattle,wa,us,triangle,300,47.6063889,-122.3308333
2/27/1999,chloride,az,us,light,900,35.4144444,-114.1986111
2/27/2005,reno,nv,us,unknown,5100,39.5297222,-119.8127778
2/27/2008,lake havasu city,az,us,oval,30,34.4838889,-114.3216667
2/27/2012,coventry,ri,us,fireball,2,41.7000000,-71.6833333
2/27/2014,attica,ny,us,circle,300,42.8641667,-78.2805556
2/28/2003,farmington,ct,us,unknown,240,41.7197222,-72.8325
2/28/2007,madison,al,us,triangle,720,34.6991667,-86.7483333
2/28/2011,fresno,ca,us,oval,600,36.7477778,-119.7713889
2/28/2014,saco,me,us,fireball,30,43.5008333,-70.4433333
2/29/2008,broken arrow,ok,us,light,2820,36.0525000,-95.7905556
2/3/2002,baltimore,md,us,circle,22,39.2902778,-76.6125
2/3/2007,pomona,ca,us,disk,180,34.0552778,-117.7513889
2/3/2012,merlin,or,us,circle,1200,42.5175000,-123.4186111
2/4/2000,houston,tx,us,triangle,120,29.7630556,-95.3630556
2/4/2004,san marcos,tx,us,teardrop,30,29.8830556,-97.9411111
2/4/2007,cole camp,mo,us,fireball,15,38.4600000,-93.2025
2/4/2011,libertyville,il,us,circle,2,42.2830556,-87.9530556
2/4/2013,remsen,ny,us,cylinder,300,43.3269444,-75.1872222
2/5/2003,concord,nc,us,changing,3600,35.4086111,-80.5797222
2/5/2009,maple valley,wa,us,triangle,180,47.4066667,-122.0375
2/5/2011,fayetteville,nc,us,light,14400,35.0525000,-78.8786111
2/5/2014,columbia falls,mt,us,light,600,48.3725000,-114.1805556
2/6/2002,irmo,sc,us,triangle,240,34.0858333,-81.1833333
2/6/2007,chandler,az,us,triangle,180,33.3061111,-111.8405556
2/6/2010,vernon,nj,us,triangle,180,41.1983333,-74.4836111
2/6/2013,blossvale,ny,us,light,180,43.2797222,-75.6438889
2/7/2000,sebring,fl,us,light,1800,27.4952778,-81.4411111
2/7/2005,biggs,ca,us,diamond,900,39.4125000,-121.7116667
2/7/2010,modesto,ca,us,sphere,1200,37.6391667,-120.9958333
2/7/2014,houma,la,us,circle,20,29.5955556,-90.7194444
2/8/2001,ventura,ca,us,other,300,34.2783333,-119.2922222
2/8/2005,san jose,ca,us,unknown,8,37.3394444,-121.8938889
2/8/2009,grand rapids,mi,us,triangle,20,42.9633333,-85.6680556
2/8/2012,marana,az,us,light,600,32.4366667,-111.2247222
2/8/2014,coral springs,fl,us,oval,120,26.2708333,-80.2708333
2/9/2002,belleville,mi,us,formation,3,42.2047222,-83.4852778
2/9/2005,san diego,ca,us,disk,180,32.7152778,-117.1563889
2/9/2009,penticton (canada),bc,ca,sphere,1800,49.5,-119.583333
2/9/2014,jacksonville,fl,us,fireball,300,30.3319444,-81.6558333
3/10/1999,glen burnie,md,us,unknown,1800,39.1625000,-76.625
3/10/2004,marietta,ga,us,cigar,180,33.9525000,-84.55
3/10/2006,tulsa,ok,us,changing,2400,36.1538889,-95.9925
3/10/2010,west liberty,il,us,triangle,2700,39.8794444,-91.1077778
3/10/2012,pendleton,in,us,triangle,2700,39.9975000,-85.7466667
3/10/2014,hagerstown,md,us,unknown,5,39.6416667,-77.7202778
3/11/2001,fort erie (canada),on,ca,triangle,5,42.9,-78.933333
3/11/2006,rockport,wv,us,light,600,39.0741667,-81.5533333
3/11/2008,upper saddle river (woodcliff lake),nj,us,fireball,4,41.0583333,-74.0988889
3/11/2013,maricopa,az,us,light,300,33.0580556,-112.0469444
3/1/1979,medford,or,us,unknown,300,42.3266667,-122.8744444
3/1/1996,byron,ny,us,formation,10800,43.0797222,-78.0641667
3/1/2001,madison,al,us,circle,20,34.6991667,-86.7483333
3/1/2005,manassas,va,us,sphere,2,38.7508333,-77.4755556
3/1/2008,indianapolis,in,us,disk,900,39.7683333,-86.1580556
3/1/2011,worthington,oh,us,circle,3,40.0930556,-83.0180556
3/1/2014,apollo beach,fl,us,oval,600,27.7727778,-82.4077778
3/12/1997,santa fe,nm,us,other,120,35.6869444,-105.9372222
3/12/2001,granite falls,wa,us,light,40,48.0841667,-121.9675
3/12/2005,joyce,wa,us,light,6,48.1366667,-123.7327778
3/12/2009,boise,id,us,sphere,300,43.6136111,-116.2025
3/12/2012,palmer,ak,us,sphere,40,61.5997222,-149.1127778
3/13/1997,scottsdale,az,us,triangle,1800,33.5091667,-111.8983333
3/13/1997,phoenix,az,us,formation,300,33.4483333,-112.0733333
3/13/1999,fowlerville (east south east of),mi,us,fireball,3,42.6605556,-84.0730556
3/13/2002,lac du bonnet (canada),mb,ca,sphere,1800,50.266667,-96.05
3/13/2006,san diego,ca,us,circle,7200,32.7152778,-117.1563889
3/13/2008,simi valley,ca,us,sphere,180,34.2694444,-118.7805556
3/13/2012,newark,oh,us,circle,240,40.0580556,-82.4013889
3/13/2014,jupiter,fl,us,triangle,300,26.9338889,-80.0944444
3/14/2002,hartland,me,us,circle,1800,44.8833333,-69.4480556
3/14/2005,bluefield,wv,us,other,20,37.2697222,-81.2225
3/14/2008,denver,co,us,other,120,39.7391667,-104.9841667
3/14/2012,orleans,ma,us,flash,14400,41.7897222,-69.9902778
3/14/2013,dallas,tx,us,oval,10,32.7833333,-96.8
3/15/1974,tula,ms,us,circle,1800,34.2327778,-89.3622222
3/15/1990,farmville,nc,us,disk,1800,35.5952778,-77.5855556
3/15/1998,gunnison (30 miles ne of),co,us,disk,30,38.5458333,-106.9247222
3/15/2001,san francisco (golden gate bridge),ca,us,other,10,37.7750000,-122.4183333
3/15/2003,arvada,co,us,egg,120,39.8027778,-105.0869444
3/15/2005,hanceville,al,us,triangle,10,34.0605556,-86.7675
3/15/2007,easley,sc,us,unknown,300,34.8297222,-82.6016667
3/15/2009,muscatine,ia,us,triangle,20,41.4244444,-91.0430556
3/15/2013,montoursville,pa,us,circle,7200,41.2541667,-76.9208333
3/16/1997,yuma (desert&#44 on olgiby rd.&#44 16 mi. ne. of  yuma),az,us,triangle,2700,32.7252778,-114.6236111
3/16/2004,san luis obispo,ca,us,flash,3,35.2827778,-120.6586111
3/16/2008,prineville,or,us,other,10,44.3000000,-120.8333333
3/16/2011,wayland,mi,us,oval,45,42.6738889,-85.6447222
3/16/2013,belmont,nc,us,other,50,35.2427778,-81.0375
3/17/1999,chicago,il,us,triangle,3600,41.8500000,-87.65
3/17/2004,san diego,ca,us,circle,10800,32.7152778,-117.1563889
3/17/2009,simi valley,ca,us,triangle,300,34.2694444,-118.7805556
3/17/2012,airway heights,wa,us,sphere,40,47.6447222,-117.5922222
3/18/2001,orangevale,ca,us,fireball,5,38.6786111,-121.2247222
3/18/2005,antioch,il,us,circle,120,42.4772222,-88.0955556
3/18/2009,webster city,ia,us,light,10,42.4694444,-93.8158333
3/18/2012,reading,mo,us,circle,40,39.4913889,-91.1322222
3/18/2014,medford,or,us,disk,4260,42.3266667,-122.8744444
3/19/2003,parma,oh,us,triangle,600,41.4047222,-81.7230556
3/19/2007,matteson,il,us,light,1080,41.5038889,-87.7130556
3/19/2011,ewing,nj,us,oval,120,40.2697222,-74.8002778
3/19/2013,new paltz,ny,us,fireball,180,41.7475000,-74.0872222
3/20/1995,fayetteville,nc,us,cylinder,300,35.0525000,-78.8786111
3/20/2003,hampden,ma,us,disk,180,42.0638889,-72.4138889
3/20/2008,beaverton,or,us,oval,10,45.4872222,-122.8025
3/20/2011,lafayette,co,us,light,2700,39.9936111,-105.0891667
3/20/2013,shelby,ia,us,unknown,300,41.5161111,-95.45
3/21/1978,medford,or,us,disk,480,42.3266667,-122.8744444
3/21/2004,champlin,mn,us,fireball,10,45.1888889,-93.3972222
3/21/2006,kokomo,in,us,light,7,40.4863889,-86.1336111
3/21/2009,riverton,ut,us,other,3600,40.5219444,-111.9383333
3/21/2014,kennesaw,ga,us,triangle,120,34.0233333,-84.6155556
3/2/2002,redwood valley,ca,us,unknown,2400,39.2655556,-123.2033333
3/2/2007,churchton,md,us,oval,3,38.8025000,-76.5372222
3/2/2011,phoenix,az,us,unknown,15,33.4483333,-112.0733333
3/2/2013,sudbury,ma,us,chevron,60,42.3833333,-71.4166667
3/22/1998,doylestown,pa,us,disk,300,40.3100000,-75.1302778
3/22/2006,fontana,ca,us,unknown,900,34.0922222,-117.4341667
3/22/2010,fountain inn,sc,us,disk,540,34.6888889,-82.1958333
3/22/2013,alexandria,va,us,unknown,3,38.8047222,-77.0472222
3/23/1999,chesapeake,va,us,oval,10,36.8188889,-76.2752778
3/23/2004,porterville,ca,us,circle,20,36.0652778,-119.0158333
3/23/2009,south zanesville,oh,us,sphere,10,39.8991667,-82.0063889
3/23/2012,davenport,wa,us,other,120,47.6541667,-118.1488889
3/24/1997,manassas,va,us,formation,25,38.7508333,-77.4755556
3/24/2006,lubbock,tx,us,circle,30,33.5777778,-101.8547222
3/24/2010,eden,nc,us,circle,600,36.4883333,-79.7669444
3/24/2012,fresh meadows,ny,us,light,300,40.7347222,-73.7938889
3/25/1998,alexandria,la,us,triangle,120,31.3111111,-92.445
3/25/2005,rogers,ar,us,rectangle,1,36.3319444,-94.1183333
3/25/2008,los angeles,ca,us,cone,120,34.0522222,-118.2427778
3/25/2012,orlando,fl,us,triangle,3,28.5380556,-81.3794444
3/26/1996,irvine,ca,us,cone,300,33.6694444,-117.8222222
3/26/2004,bradenton,fl,us,other,240,27.4986111,-82.575
3/26/2009,mills river,nc,us,formation,600,35.3883333,-82.5669444
3/26/2013,lake oswego,or,us,triangle,360,45.4208333,-122.6694444
3/27/1998,clifton park (30 min north of albany),ny,us,other,900,42.8655556,-73.7713889
3/27/2005,los alamitos,ca,us,formation,2700,33.8030556,-118.0716667
3/27/2010,los angeles,ca,us,unknown,45,34.0522222,-118.2427778
3/27/2013,columbia,tn,us,formation,360,35.6150000,-87.0352778
3/28/2000,bouse,az,us,light,10,33.9325000,-114.005
3/28/2004,chesapeake,oh,us,light,600,38.4277778,-82.4572222
3/28/2009,east wenatchee,wa,us,cylinder,3,47.4158333,-120.2919444
3/28/2014,laveen,az,us,light,300,33.3627778,-112.1686111
3/29/2001,apollo,pa,us,light,900,40.5813889,-79.5666667
3/29/2005,austin,tx,us,triangle,300,30.2669444,-97.7427778
3/29/2009,white lake,nc,us,fireball,15,34.6402778,-78.4841667
3/29/2012,morehead,ky,us,light,1800,38.1838889,-83.4327778
3/29/2014,altoona,ks,us,sphere,1800,37.5238889,-95.6611111
3/30/2002,salome,az,us,cylinder,10800,33.7811111,-113.6138889
3/30/2007,rockville,md,us,cigar,15,39.0838889,-77.1530556
3/30/2010,wise,va,us,light,600,36.9758333,-82.5758333
3/30/2013,tyler,tx,us,fireball,60,32.3511111,-95.3008333
3/31/1980,canoga park,ca,us,disk,60,34.2011111,-118.5972222
3/31/2004,naples,fl,us,sphere,2400,26.1416667,-81.795
3/31/2008,eagle river,ak,us,light,1200,61.3213889,-149.5677778
3/31/2011,russellville,ar,us,triangle,180,35.2783333,-93.1336111
3/31/2014,virginia beach,va,us,disk,30,36.8527778,-75.9783333
3/3/2001,pontotoc,ms,us,light,3600,34.2477778,-88.9986111
3/3/2006,mcminnville,tn,us,fireball,3,35.6833333,-85.77
3/3/2011,uintah,ut,us,light,60,41.1441667,-111.9225
3/3/2013,medford,ma,us,cylinder,5,42.4183333,-71.1066667
3/4/1999,colville,wa,us,fireball,2,48.5466667,-117.9044444
3/4/2005,sacramento,ca,us,sphere,10,38.5816667,-121.4933333
3/4/2009,tacoma,wa,us,light,180,47.2530556,-122.4430556
3/4/2014,tucson,az,us,triangle,300,32.2216667,-110.9258333
3/5/2001,duluth,mn,us,triangle,300,46.7833333,-92.1063889
3/5/2007,bremerton,wa,us,light,600,47.5675000,-122.6313889
3/5/2010,new hartford,ct,us,light,300,41.8822222,-72.9775
3/5/2012,mccaysville,ga,us,light,900,34.9861111,-84.3713889
3/6/1993,pittsburgh,pa,us,triangle,1800,40.4405556,-79.9961111
3/6/2004,perth amboy,nj,us,formation,15,40.5066667,-74.2658333
3/6/2008,quaker hill,ct,us,disk,480,41.4033333,-72.1063889
3/6/2011,las vegas,nv,us,circle,300,36.1750000,-115.1363889
3/7/1995,geneva (canada),ny,us,light,2700,42.8688889,-76.9780556
3/7/1999,champaign,il,us,formation,300,40.1163889,-88.2433333
3/7/2004,winter springs,fl,us,egg,15,28.6986111,-81.3083333
3/7/2007,ellensburg,wa,us,triangle,30,46.9966667,-120.5466667
3/7/2011,culpeper,va,us,triangle,7200,38.4730556,-77.9969444
3/7/2014,houma,la,us,sphere,180,29.5955556,-90.7194444
3/8/2003,englewood,co,us,unknown,1800,39.6477778,-104.9872222
3/8/2006,bordentown,nj,us,circle,20,40.1461111,-74.7122222
3/8/2008,salisbury,nc,us,cylinder,120,35.6708333,-80.4744444
3/8/2012,blue bell,pa,us,triangle,180,40.1522222,-75.2666667
3/9/2000,portland,me,us,light,120,43.6613889,-70.2558333
3/9/2004,warthen,ga,us,triangle,120,33.1019444,-82.8038889
3/9/2007,san dimas,ca,us,oval,600,34.1066667,-117.8058333
3/9/2012,mesa,az,us,rectangle,300,33.4222222,-111.8219444
3/9/2013,portland,or,us,triangle,45,45.5236111,-122.675
4/10/1993,omaha,ne,us,egg,30,41.2586111,-95.9375
4/10/2002,phoenixville,pa,us,light,1800,40.1302778,-75.5152778
4/10/2008,dandridge,tn,us,light,600,36.0152778,-83.415
4/10/2010,fargo,nd,us,formation,15,46.8772222,-96.7894444
4/10/2014,oakland park,fl,us,triangle,14400,26.1719444,-80.1322222
4/11/1997,houma,la,us,circle,10,29.5955556,-90.7194444
4/11/2004,truro (canada),ns,ca,light,78,45.366667,-63.3
4/11/2008,wauseon,oh,us,circle,30,41.5491667,-84.1416667
4/11/2012,seneca,il,us,light,3,41.3111111,-88.6097222
4/11/2014,campbell,ca,us,oval,360,37.2872222,-121.9488889
4/1/1972,indianapolis,in,us,disk,3600,39.7683333,-86.1580556
4/1/1994,megargel,tx,us,unknown,600,33.4508333,-98.9241667
4/1/2000,lake havasu city,az,us,light,600,34.4838889,-114.3216667
4/1/2003,phoenix,az,us,triangle,60,33.4483333,-112.0733333
4/1/2006,miami,fl,us,circle,35,25.7738889,-80.1938889
4/1/2010,reynoldsburg,oh,us,other,300,39.9547222,-82.8122222
4/1/2013,colorado springs,co,us,circle,1800,38.8338889,-104.8208333
4/12/1986,oak lawn,il,us,other,1200,41.7108333,-87.7580556
4/12/2004,ajax (canada),on,ca,other,900,43.85,-79.016667
4/12/2008,spring,tx,us,light,10,30.0797222,-95.4169444
4/12/2012,marion,oh,us,unknown,300,40.5886111,-83.1286111
4/12/2014,lenwood,ca,us,other,60,34.8766667,-117.1030556
4/13/2001,rothschild,wi,us,unknown,30,44.8872222,-89.62
4/13/2005,bentonville,ar,us,light,1800,36.3727778,-94.2086111
4/13/2010,mahomet,il,us,triangle,900,40.1952778,-88.4041667
4/13/2013,los angeles,ca,us,fireball,360,34.0522222,-118.2427778
4/14/1999,oak ridge,tn,us,oval,120,36.0102778,-84.2697222
4/14/2005,guelph (canada),on,ca,triangle,10,43.55,-80.25
4/14/2008,minneapolis,mn,us,light,900,44.9800000,-93.2636111
4/14/2011,carrollton,oh,us,oval,120,40.5727778,-81.0858333
4/14/2013,new castle,pa,us,light,3600,41.0036111,-80.3472222
4/15/1953,los angeles,ca,us,fireball,5,34.0522222,-118.2427778
4/15/1976,winchester,ky,us,disk,300,37.9900000,-84.1797222
4/15/1990,thornwood,ny,us,light,300,41.1233333,-73.7794444
4/15/1997,charlotte,nc,us,unknown,10,35.2269444,-80.8433333
4/15/2000,tokeland,wa,us,unknown,600,46.7066667,-123.9805556
4/15/2004,hayden,id,us,light,60,47.7661111,-116.7855556
4/15/2006,irvine,pa,us,unknown,300,41.8391667,-79.2686111
4/15/2008,holbrook,az,us,sphere,60,34.9022222,-110.1575
4/15/2012,bohemia,ny,us,oval,180,40.7691667,-73.1155556
4/15/2014,lordsburg,nm,us,cylinder,900,32.3502778,-108.7080556
4/16/2002,highlands ranch,co,us,cylinder,120,39.5538889,-104.9688889
4/16/2005,lafayette,in,us,flash,60,40.4166667,-86.8752778
4/16/2008,durham,nc,us,disk,10,35.9938889,-78.8988889
4/16/2009,newark,oh,us,light,3600,40.0580556,-82.4013889
4/16/2012,bethpage,ny,us,flash,1,40.7441667,-73.4825
4/17/1991,new boston,tx,us,oval,240,33.4597222,-94.4152778
4/17/2002,san antonio,tx,us,light,180,29.4238889,-98.4933333
4/17/2007,goodlettsville,tn,us,circle,60,36.3230556,-86.7133333
4/17/2009,york,pa,us,light,10,39.9625000,-76.7280556
4/17/2012,myrtle beach,sc,us,light,15,33.6888889,-78.8869444
4/18/1981,long beach,ca,us,formation,5,33.7669444,-118.1883333
4/18/2004,pinson,tn,us,other,7,35.4900000,-88.7205556
4/18/2008,venice,ca,us,light,30,33.9908333,-118.4591667
4/18/2012,virginia beach,va,us,sphere,20,36.8527778,-75.9783333
4/18/2014,chico,ca,us,disk,1080,39.7286111,-121.8363889
4/19/2003,lafayette,ky,us,sphere,30,36.6811111,-87.6202778
4/19/2006,morinville (canada),ab,ca,other,180,53.8,-113.65
4/19/2009,oak harbor,wa,us,unknown,60,48.2933333,-122.6419444
4/19/2013,bay point,ca,us,light,180,38.0291667,-121.9605556
4/20/1980,dayton,oh,us,cigar,300,39.7588889,-84.1916667
4/20/2001,owings mills,md,us,flash,7,39.4194444,-76.7805556
4/20/2004,toronto (canada),on,ca,disk,600,43.666667,-79.416667
4/20/2008,schererville,in,us,triangle,3480,41.4788889,-87.4547222
4/20/2010,philadelphia,pa,us,triangle,600,39.9522222,-75.1641667
4/20/2013,hercules,ca,us,sphere,30,38.0172222,-122.2875
4/20/2014,seattle,wa,us,formation,5,47.6063889,-122.3308333
4/21/2003,houston (canada),bc,ca,triangle,10,54.4,-126.65
4/21/2007,tacoma,wa,us,light,300,47.2530556,-122.4430556
4/21/2009,embarrass,mn,us,light,15,47.6591667,-92.1977778
4/21/2012,paris,mi,us,unknown,1500,43.7733333,-85.5025
4/2/1974,birmingham (wisteria dr.&#44 .5 mi down),al,us,disk,180,33.5205556,-86.8025
4/2/2005,phoenix,az,us,triangle,10,33.4483333,-112.0733333
4/2/2008,incline village,nv,us,light,1395,39.2513889,-119.9719444
4/2/2012,lloydminster (canada),sk,ca,disk,14400,53.283333,-110.0
4/22/1967,gibson,ny,us,oval,180,42.1400000,-77.0311111
4/22/2001,fairhaven,ma,us,sphere,300,41.6375000,-70.9041667
4/22/2006,pismo beach,ca,us,light,360,35.1427778,-120.6402778
4/22/2009,west chester,pa,us,cigar,5,39.8494444,-75.3561111
4/22/2012,royse city,tx,us,formation,600,32.9750000,-96.3322222
4/22/2014,fletcher,nc,us,triangle,20,35.4305556,-82.5013889
4/23/2000,scarborough (toronto) (canada),on,ca,disk,10,43.75,-79.2
4/23/2006,bluefield,wv,us,fireball,40,37.2697222,-81.2225
4/23/2009,lake charles,la,us,triangle,120,30.2263889,-93.2172222
4/23/2012,rio rancho,nm,us,light,60,35.2333333,-106.6638889
4/24/1997,new brighton,mn,us,triangle,2700,45.0655556,-93.2016667
4/24/2003,conyers,ga,us,fireball,2,33.6675000,-84.0177778
4/24/2007,loveland,oh,us,unknown,40,39.2688889,-84.2638889
4/24/2009,ottawa (canada),on,ca,disk,60,45.416667,-75.7
4/24/2012,cedar rapids,ia,us,light,420,42.0083333,-91.6438889
4/24/2014,debary,fl,us,light,60,28.8827778,-81.3088889
4/25/1999,ann arbor,mi,us,formation,15,42.2708333,-83.7263889
4/25/2005,lexington,ky,us,disk,1200,37.9886111,-84.4777778
4/25/2009,batavia,oh,us,triangle,60,39.0769444,-84.1769444
4/25/2013,indianapolis,in,us,light,30,39.7683333,-86.1580556
4/26/1996,mcallen,tx,us,disk,300,26.2030556,-98.2297222
4/26/2004,lincoln,ne,us,circle,15,40.8000000,-96.6666667
4/26/2008,henning,tn,us,triangle,30,35.6727778,-89.5733333
4/26/2012,bremen,in,us,oval,3600,41.4463889,-86.1480556
4/26/2014,gilbert,az,us,triangle,60,33.3527778,-111.7883333
4/27/2001,spokane,wa,us,sphere,12,47.6588889,-117.425
4/27/2007,kaneohe,hi,us,sphere,15,21.4180556,-157.8036111
4/27/2009,tuxedo (on us hwy 25&#44 between tuxedo and i-26 exit),nc,us,other,300,35.2252778,-82.4297222
4/27/2013,crown point,in,us,sphere,120,41.4169444,-87.3652778
4/27/2014,chatsworth,ca,us,circle,120,34.2572222,-118.6002778
4/28/2000,bossier city,la,us,chevron,10,32.5158333,-93.7319444
4/28/2004,bakersfield,ca,us,light,2700,35.3733333,-119.0177778
4/28/2010,virginia beach,va,us,light,3600,36.8527778,-75.9783333
4/28/2012,algoma,wi,us,unknown,60,44.6088889,-87.4325
4/29/2000,floral park,ny,us,disk,15,40.7236111,-73.7052778
4/29/2005,pembroke pines,fl,us,fireball,180,26.0027778,-80.2241667
4/29/2006,college place,wa,us,circle,180,46.0494444,-118.3872222
4/29/2007,elwood,il,us,unknown,15,41.4038889,-88.1116667
4/29/2011,altamonte springs,fl,us,fireball,7,28.6608333,-81.3658333
4/29/2014,stanford,ca,us,circle,1200,37.4241667,-122.165
4/30/2001,baltimore,md,us,light,1500,39.2902778,-76.6125
4/30/2005,murrieta,ca,us,circle,60,33.5538889,-117.2130556
4/30/2009,frisco,tx,us,unknown,300,33.1505556,-96.8233333
4/30/2013,batavia,il,us,circle,45,41.8500000,-88.3125
4/3/1999,converse,tx,us,light,120,29.5177778,-98.3158333
4/3/2006,tidewater,or,us,fireball,3,44.4113889,-123.8991667
4/3/2010,las vegas,nv,us,light,10,36.1750000,-115.1363889
4/3/2014,muscle shoals,al,us,cylinder,120,34.7447222,-87.6675
4/4/2000,fort wayne,in,us,oval,300,41.1305556,-85.1288889
4/4/2004,south bend,in,us,sphere,15,41.6833333,-86.25
4/4/2008,lake havasu city,az,us,other,300,34.4838889,-114.3216667
4/4/2012,orlando,fl,us,changing,180,28.5380556,-81.3794444
4/5/1995,rio grande (puerto rico),pr,us,unknown,18000,18.3822222,-65.8316667
4/5/2003,los alamos,ca,us,cigar,60,34.7444444,-120.2772222
4/5/2006,graham,wa,us,disk,1800,47.0530556,-122.2930556
4/5/2011,new castle,pa,us,other,30,41.0036111,-80.3472222
4/5/2014,wakefield,ma,us,other,300,42.5063889,-71.0733333
4/6/1994,grosse pointe,mi,us,light,5,42.3861111,-82.9119444
4/6/2006,mccamey (near),tx,us,oval,120,31.1358333,-102.2238889
4/6/2010,san marcos,ca,us,oval,30,33.1433333,-117.1652778
4/6/2013,mesa,az,us,formation,600,33.4222222,-111.8219444
4/6/2014,edison,nj,us,flash,300,40.5186111,-74.4125
4/7/2004,columbia falls,mt,us,light,240,48.3725000,-114.1805556
4/7/2007,arlington,va,us,light,1200,38.8902778,-77.0844444
4/7/2010,montmagny (canada),qc,ca,disk,7200,46.966667,-70.55
4/7/2013,williamsport,md,us,light,7200,39.6005556,-77.8208333
4/8/2002,middletown (suburb),oh,us,triangle,6,39.5150000,-84.3983333
4/8/2005,hagerstown,md,us,unknown,600,39.6416667,-77.7202778
4/8/2010,downey,ca,us,sphere,3600,33.9400000,-118.1316667
4/8/2012,seattle,wa,us,sphere,300,47.6063889,-122.3308333
4/9/1998,colorado springs,co,us,other,4,38.8338889,-104.8208333
4/9/2004,ford city,pa,us,disk,15,40.7722222,-79.53
4/9/2006,orland,ca,us,sphere,60,39.7475000,-122.1952778
4/9/2010,plainview,ny,us,unknown,300,40.7763889,-73.4677778
4/9/2012,dysart,ia,us,light,120,42.1716667,-92.3061111
4/9/2014,newport,or,us,oval,3600,44.6369444,-124.0522222
5/10/1997,neoga (6 mi. west),il,us,triangle,300,39.3194444,-88.4527778
5/10/2002,indianapolis,in,us,fireball,5,39.7683333,-86.1580556
5/10/2006,denver,co,us,cigar,30,39.7391667,-104.9841667
5/10/2010,oak lawn,il,us,circle,600,41.7108333,-87.7580556
5/11/1982,piscataway,nj,us,disk,300,40.4991667,-74.3994444
5/11/2004,los angeles,ca,us,oval,600,34.0522222,-118.2427778
5/11/2007,memphis,tn,us,disk,120,35.1494444,-90.0488889
5/11/2011,harrington,wa,us,unknown,600,47.4811111,-118.2533333
5/11/2013,orlando,fl,us,light,240,28.5380556,-81.3794444
5/1/1969,estill,sc,us,cigar,2700,32.7547222,-81.2422222
5/1/1979,gainesville,fl,us,fireball,600,29.6513889,-82.325
5/1/1991,garden grove,ca,us,sphere,2700,33.7738889,-117.9405556
5/1/1998,cleveland,oh,us,light,15,41.4994444,-81.6955556
5/1/2001,noble,ok,us,rectangle,120,35.1391667,-97.3944444
5/1/2004,cotati,ca,us,light,30,38.3269444,-122.7061111
5/1/2007,crosby,mn,us,circle,180,46.4822222,-93.9575
5/1/2011,pocatello,id,us,light,180,42.8713889,-112.4447222
5/1/2014,honolulu,hi,us,other,5,21.3069444,-157.8583333
5/12/1976,grapevine,ca,us,egg,40,34.9416667,-118.9291667
5/12/2001,susanville,ca,us,sphere,15,40.4163889,-120.6519444
5/12/2005,truckee,ca,us,other,1800,39.3280556,-120.1822222
5/12/2010,chesapeake,va,us,fireball,8,36.8188889,-76.2752778
5/12/2012,north sioux city,sd,us,fireball,300,42.5272222,-96.4827778
5/13/1995,seattle (west side),wa,us,triangle,120,47.6063889,-122.3308333
5/13/2002,mosinee,wi,us,triangle,900,44.7930556,-89.7030556
5/13/2006,baltimore,md,us,light,1200,39.2902778,-76.6125
5/13/2012,cleveland,oh,us,triangle,420,41.4994444,-81.6955556
5/14/1999,dixon,il,us,triangle,300,41.8388889,-89.4794444
5/14/2004,jacksonville,nc,us,other,300,34.7538889,-77.4305556
5/14/2008,chesterland,oh,us,light,2,41.5222222,-81.3380556
5/14/2012,ottawa (canada),on,ca,flash,120,45.416667,-75.7
5/15/1966,mentone,al,us,egg,10,34.5794444,-85.5905556
5/15/1977,salem,or,us,cigar,900,44.9430556,-123.0338889
5/15/1987,temple,tx,us,cigar,120,31.0980556,-97.3425
5/15/1996,willard,mo,us,cigar,2700,37.3050000,-93.4283333
5/15/2000,bushkill,pa,us,circle,180,41.0933333,-75.0022222
5/15/2002,morrow,ga,us,light,900,33.5830556,-84.3394444
5/15/2004,los angeles,ca,us,light,900,34.0522222,-118.2427778
5/15/2006,littleton,co,us,other,600,39.6133333,-105.0161111
5/15/2009,willamina,or,us,formation,10,45.0788889,-123.4847222
5/15/2011,sun city,az,us,triangle,300,33.5975000,-112.2711111
5/15/2013,mashpee,ma,us,other,600,41.6483333,-70.4816667
5/16/2003,round rock,tx,us,other,3600,30.5080556,-97.6786111
5/16/2007,mesquite,tx,us,unknown,10,32.7666667,-96.5988889
5/16/2012,lozeau,mt,us,triangle,480,47.1166667,-114.7791667
5/17/1998,belle vernon,pa,us,other,2400,40.1250000,-79.8666667
5/17/2004,batesville,ar,us,light,240,35.7697222,-91.6408333
5/17/2009,fargo,nd,us,other,15,46.8772222,-96.7894444
5/17/2013,bellport,ny,us,triangle,1800,40.7569444,-72.9397222
5/18/2001,dania beach (fishing pier),fl,us,light,120,26.0519444,-80.1441667
5/18/2006,jacumba,ca,us,cigar,120,32.6175000,-116.1888889
5/18/2009,golden valley,az,us,cone,1800,35.2233333,-114.2222222
5/18/2013,dallas,tx,us,sphere,15,32.7833333,-96.8
5/19/1999,union city,tn,us,other,37800,36.4241667,-89.0569444
5/19/2005,ledgewood,nj,us,egg,6,40.8811111,-74.6563889
5/19/2009,villa rica,ga,us,sphere,1800,33.7319444,-84.9191667
5/19/2012,grayson,ga,us,changing,1200,33.8941667,-83.9558333
5/19/2013,carol stream,il,us,triangle,7,41.9125000,-88.1347222
5/20/1995,san diego (ocean beach),ca,us,light,180,32.7152778,-117.1563889
5/20/2000,santa clarita,ca,us,light,180,34.3916667,-118.5416667
5/20/2004,montrose,co,us,circle,3,38.4783333,-107.8755556
5/20/2007,sacramento,ca,us,fireball,5,38.5816667,-121.4933333
5/20/2010,ashton,id,us,other,1,44.0716667,-111.4475
5/20/2012,port dover (canada),on,ca,sphere,40,42.783333,-80.2
5/21/2000,new smyrna beach,fl,us,unknown,10,29.0255556,-80.9272222
5/21/2004,harrison,oh,us,changing,6660,39.2619444,-84.82
5/21/2008,cuba,mo,us,light,45,38.0627778,-91.4033333
5/21/2011,royal oak,mi,us,oval,300,42.4894444,-83.1447222
5/2/1998,los angeles,ca,us,triangle,20,34.0522222,-118.2427778
5/2/2005,big lake,tx,us,light,37800,31.1913889,-101.46
5/2/2009,heidenheimer,tx,us,triangle,180,31.0180556,-97.3025
5/2/2014,camden,tn,us,sphere,5,36.0588889,-88.0977778
5/22/2001,encino,ca,us,sphere,10,34.1591667,-118.5002778
5/22/2005,santa ana,ca,us,light,45,33.7455556,-117.8669444
5/22/2010,san francisco,ca,us,oval,60,37.7750000,-122.4183333
5/22/2012,florence,al,us,light,5,34.7997222,-87.6772222
5/23/2002,sacramento,ca,us,unknown,900,38.5816667,-121.4933333
5/23/2006,tranquillity,ca,us,circle,180,36.6488889,-120.2516667
5/23/2010,algonac,mi,us,fireball,420,42.6183333,-82.5311111
5/23/2013,morrisville,vt,us,light,300,44.5616667,-72.5988889
5/24/2003,littleton,co,us,other,720,39.6133333,-105.0161111
5/24/2009,las cruces,nm,us,circle,900,32.3122222,-106.7777778
5/24/2012,burlington,ia,us,light,60,40.8075000,-91.1127778
5/25/1991,hampstead,nh,us,disk,120,42.8744444,-71.1816667
5/25/2004,omaha (near),ne,us,cone,75,41.2586111,-95.9375
5/25/2008,scarborough,me,us,triangle,25,43.5780556,-70.3222222
5/25/2011,delafield,wi,us,formation,492,43.0608333,-88.4036111
5/25/2013,redford,mi,us,fireball,900,42.3833333,-83.2966667
5/26/2001,olympia,wa,us,disk,240,47.0380556,-122.8994444
5/26/2007,wilmington,nc,us,oval,1200,34.2255556,-77.945
5/26/2012,mason city,ia,us,other,240,43.1536111,-93.2008333
5/26/2013,jacksonville,nc,us,light,300,34.7538889,-77.4305556
5/26/2013,kalamazoo,mi,us,light,120,42.2916667,-85.5872222
5/27/2003,joplin,mo,us,unknown,10,37.0841667,-94.5130556
5/27/2007,maple grove,mn,us,disk,7200,45.0725000,-93.4555556
5/27/2011,englewood,co,us,cigar,45,39.6477778,-104.9872222
5/27/2013,north tonawanda,ny,us,other,120,43.0386111,-78.8644444
5/28/2002,bakersfield,ca,us,unknown,20,35.3733333,-119.0177778
5/28/2007,chilliwack (canada),bc,ca,triangle,60,49.166667,-121.95
5/28/2010,green bay,wi,us,unknown,45,44.5191667,-88.0197222
5/28/2012,kaysville,ut,us,light,1200,41.0352778,-111.9377778
5/29/1999,cheraw,co,us,triangle,1200,38.1069444,-103.5097222
5/29/2005,riverview,fl,us,unknown,15,27.8658333,-82.3266667
5/29/2010,commerce,ca,us,circle,180,34.0005556,-118.1588889
5/29/2012,buffalo,mo,us,triangle,45,37.6459000,-93.0942
5/30/1999,el paso,tx,us,sphere,900,31.7586111,-106.4863889
5/30/2004,nipomo,ca,us,fireball,1200,35.0427778,-120.475
5/30/2008,gold bar,wa,us,unknown,300,47.8569444,-121.6958333
5/30/2011,austin,tx,us,light,600,30.2669444,-97.7427778
5/31/1965,shasta lake,ca,us,disk,3600,40.6805556,-122.3697222
5/31/2004,baton rouge,la,us,circle,90,30.4505556,-91.1544444
5/31/2009,lithia springs,ga,us,sphere,600,33.7938889,-84.6605556
5/31/2013,green island,ny,us,triangle,4,42.7441667,-73.6919444
5/3/2000,surprise (witnessed from),az,us,unknown,2700,33.6305556,-112.3325
5/3/2006,hollywood,fl,us,triangle,7200,26.0108333,-80.1497222
5/3/2010,whitman,ma,us,triangle,30,42.0805556,-70.9361111
5/3/2013,seattle,wa,us,other,3,47.6063889,-122.3308333
5/3/2014,parkersburg,wv,us,light,300,39.2666667,-81.5616667
5/4/2001,richmond,va,us,other,120,37.5536111,-77.4605556
5/4/2006,westminster,ca,us,fireball,40,33.7591667,-118.0058333
5/4/2011,san francisco,ca,us,light,1200,37.7750000,-122.4183333
5/4/2013,joliet,il,us,fireball,2400,41.5250000,-88.0816667
5/5/1970,new york city,ny,us,changing,300,40.7141667,-74.0063889
5/5/1999,orlando,fl,us,other,300,28.5380556,-81.3794444
5/5/2004,bellingham,wa,us,light,900,48.7597222,-122.4869444
5/5/2007,beaverton,or,us,triangle,600,45.4872222,-122.8025
5/5/2011,ovalo,tx,us,oval,20,32.1727778,-99.8075
5/5/2012,granada hills,ca,us,oval,300,34.2647222,-118.5222222
5/5/2014,santa rosa beach,fl,us,fireball,480,30.3958333,-86.2288889
5/6/2001,santa rosa,ca,us,unknown,10,38.4405556,-122.7133333
5/6/2006,westminster,co,us,light,15,39.8366667,-105.0366667
5/6/2010,jacksonville,fl,us,triangle,73800,30.3319444,-81.6558333
5/6/2013,florence,sc,us,changing,180,34.1952778,-79.7627778
5/7/1999,roy,ut,us,changing,1440,41.1616667,-112.0255556
5/7/2005,laconia,nh,us,disk,10,43.5277778,-71.4708333
5/7/2008,calhoun,ga,us,disk,240,34.5025000,-84.9511111
5/7/2013,coatesville,pa,us,circle,120,39.9830556,-75.8241667
5/8/1999,everett,wa,us,light,600,47.9791667,-122.2008333
5/8/2005,black canyon city,az,us,unknown,600,34.0708333,-112.15
5/8/2009,reedville,va,us,unknown,3600,37.8419444,-76.2761111
5/8/2012,clovis,ca,us,light,600,36.8252778,-119.7019444
5/9/2000,lawton,ok,us,sphere,10,34.6086111,-98.39
5/9/2006,fayetteville,ar,us,cigar,600,36.0625000,-94.1572222
5/9/2010,edmonton (canada),ab,ca,fireball,8,53.55,-113.5
6/10/1952,chicago (south suburb),il,us,circle,600,41.8500000,-87.65
6/10/1977,stockton,ca,us,disk,1800,37.9577778,-121.2897222
6/10/1997,knoxville,tn,us,triangle,60,35.9605556,-83.9208333
6/10/2001,anchorage,ak,us,egg,900,61.2180556,-149.9002778
6/10/2005,moose jaw (canada),sk,ca,oval,1200,50.4,-105.55
6/10/2008,houston,tx,us,light,60,29.7630556,-95.3630556
6/10/2011,red oak,tx,us,triangle,300,32.5175000,-96.8041667
6/11/1953,vancouver (canada),bc,ca,disk,30,49.25,-123.133333
6/11/2001,saginaw,mi,us,triangle,600,43.4194444,-83.9508333
6/11/2007,middleton,wi,us,sphere,90,43.0972222,-89.5041667
6/11/2011,lake stevens,wa,us,unknown,1,48.0152778,-122.0625
6/11/2013,myrtle beach,sc,us,formation,15,33.6888889,-78.8869444
6/1/1958,middlesex,nc,us,circle,3600,35.7900000,-78.2041667
6/1/1963,waukegan,il,us,formation,900,42.3636111,-87.8447222
6/1/1966,pleasantville,ny,us,disk,3600,41.1327778,-73.7930556
6/1/1968,columbia,sc,us,triangle,10,34.0005556,-81.035
6/1/1971,holliday,tx,us,disk,14400,33.8161111,-98.6947222
6/1/1973,landis,nc,us,light,60,35.5455556,-80.6111111
6/1/1975,nashville,tn,us,triangle,300,36.1658333,-86.7844444
6/1/1976,orlando,fl,us,cylinder,600,28.5380556,-81.3794444
6/1/1977,shelby,oh,us,circle,2,40.8813889,-82.6619444
6/1/1978,sterling park (near dulles airport),va,us,disk,1800,39.0036111,-77.4008333
6/1/1980,auxvasse,mo,us,disk,600,39.0180556,-91.8969444
6/1/1982,tullahoma county,tn,us,formation,120,35.3619444,-86.2094444
6/1/1984,ravenna,mi,us,circle,1500,43.1894444,-85.9369444
6/1/1987,iowa,la,us,unknown,15,30.2366667,-93.0136111
6/1/1989,mansfield,oh,us,other,120,40.7583333,-82.5155556
6/1/1990,fullerton,ca,us,disk,600,33.8702778,-117.9244444
6/1/1993,wolcott,ny,us,unknown,900,43.2205556,-76.8152778
6/1/1994,scottville,mi,us,changing,300,43.9547222,-86.28
6/1/1995,pensacola,fl,us,flash,300,30.4211111,-87.2169444
6/1/1997,houston,tx,us,chevron,300,29.7630556,-95.3630556
6/1/1998,winston-salem (north of),nc,us,circle,180,36.0997222,-80.2444444
6/1/1999,georgetown,il,us,other,600,39.9752778,-87.6358333
6/1/2000,san francisco,ca,us,fireball,10,37.7750000,-122.4183333
6/1/2003,cullman,al,us,oval,300,34.1747222,-86.8436111
6/1/2006,bodie (near),ca,us,circle,7200,38.2122222,-119.0111111
6/1/2008,dora,mo,us,light,3,36.7769444,-92.2172222
6/1/2010,chesterfield,va,us,unknown,7200,37.3769444,-77.5061111
6/1/2012,st. paul,mn,us,cylinder,120,44.9444444,-93.0930556
6/1/2013,cottage grove,mn,us,changing,7,44.8277778,-92.9436111
6/12/1998,montebello,ca,us,light,3,34.0094444,-118.1044444
6/12/2005,chicago,il,us,triangle,180,41.8500000,-87.65
6/12/2009,palm coast,fl,us,light,120,29.5847222,-81.2080556
6/12/2012,new york city,ny,us,other,5,40.7141667,-74.0063889
6/13/1991,st. petersburg,fl,us,other,10,27.7705556,-82.6794444
6/13/2002,omaha,ne,us,light,120,41.2586111,-95.9375
6/13/2005,bertram,tx,us,oval,300,30.7436111,-98.0552778
6/13/2009,doswell,va,us,circle,120,37.8600000,-77.4644444
6/13/2012,columbus,oh,us,oval,15,39.9611111,-82.9988889
6/14/1986,new rochelle,ny,us,triangle,300,40.9113889,-73.7827778
6/14/2002,glendale,ca,us,disk,60,34.1425000,-118.2541667
6/14/2007,three rocks,ca,us,light,600,36.5025000,-120.3905556
6/14/2008,edmonds,wa,us,circle,5,47.8108333,-122.3761111
6/14/2011,pinole,ca,us,sphere,960,38.0044444,-122.2977778
6/14/2012,cranston,ri,us,fireball,60,41.7797222,-71.4377778
6/15/1955,daytona beach,fl,us,fireball,120,29.2105556,-81.0230556
6/15/1963,newaygo,mi,us,sphere,7200,43.4197222,-85.8
6/15/1966,mcclellandtown,pa,us,disk,10800,39.8869444,-79.8669444
6/15/1969,little rock,ar,us,cylinder,60,34.7463889,-92.2894444
6/15/1973,whitesburg,ky,us,light,1200,37.1183333,-82.8269444
6/15/1975,florence,sc,us,rectangle,2700,34.1952778,-79.7627778
6/15/1977,newport,or,us,light,600,44.6369444,-124.0522222
6/15/1979,san jose,ca,us,disk,2400,37.3394444,-121.8938889
6/15/1982,new york city (staten island),ny,us,cigar,300,40.7141667,-74.0063889
6/15/1985,seward,ak,us,disk,5,60.1041667,-149.4422222
6/15/1990,springfield,or,us,oval,1200,44.0463889,-123.0208333
6/15/1993,memphis,tn,us,fireball,2,35.1494444,-90.0488889
6/15/1995,washington,ut,us,unknown,180,37.1305556,-113.5075
6/15/1996,coeur d&#39alene,id,us,formation,180,47.6777778,-116.7794444
6/15/1997,silver city,nm,us,unknown,30,32.7700000,-108.2797222
6/15/1999,silverton,tx,us,cigar,1200,34.4741667,-101.3041667
6/15/2001,naperville,il,us,sphere,480,41.7858333,-88.1472222
6/15/2002,corona,ca,us,fireball,900,33.8752778,-117.5655556
6/15/2004,palm beach,fl,us,other,600,26.7052778,-80.0366667
6/15/2005,lagrange,ny,us,light,2,41.4486111,-74.2858333
6/15/2007,monroe,mi,us,fireball,8,41.9163889,-83.3977778
6/15/2010,burlington (canada),on,ca,light,300,43.316667,-79.8
6/15/2012,pittsburgh (general area),pa,us,oval,120,40.4405556,-79.9961111
6/15/2013,garden plain,ks,us,light,180,37.6583333,-97.6833333
6/16/1998,meadville,pa,us,teardrop,2,41.6413889,-80.1516667
6/16/2004,milan,tn,us,sphere,10,35.9197222,-88.7588889
6/16/2008,jefferson city,mo,us,unknown,1800,38.5766667,-92.1733333
6/16/2011,green river,wy,us,sphere,45,41.5286111,-109.4655556
6/16/2012,san diego,ca,us,light,600,32.7152778,-117.1563889
6/17/1977,columbia,nc,us,oval,900,35.9175000,-76.2525
6/17/2001,tampa,fl,us,diamond,60,27.9472222,-82.4586111
6/17/2005,palm springs,ca,us,other,60,33.8302778,-116.5444444
6/17/2008,phoenix,az,us,formation,5,33.4483333,-112.0733333
6/17/2011,burlington,vt,us,light,300,44.4758333,-73.2125
6/17/2013,bangor,me,us,light,60,44.8011111,-68.7783333
6/18/2000,monroe,ny,us,rectangle,60,41.3305556,-74.1872222
6/18/2004,blountville,tn,us,other,55,36.5330556,-82.3269444
6/18/2006,paulsboro,nj,us,flash,20,39.8302778,-75.2408333
6/18/2009,arlington,ia,us,light,240,42.7491667,-91.6711111
6/18/2012,loveland,oh,us,light,180,39.2688889,-84.2638889
6/19/1996,tampa,fl,us,disk,240,27.9472222,-82.4586111
6/19/2003,reston,va,us,sphere,10,38.9686111,-77.3413889
6/19/2005,silverdale,wa,us,rectangle,30,47.6447222,-122.6936111
6/19/2007,seattle,wa,us,light,180,47.6063889,-122.3308333
6/19/2009,azle,tx,us,fireball,2,32.8950000,-97.5455556
6/19/2011,albany,ny,us,fireball,60,42.6525000,-73.7566667
6/19/2013,stuart,ia,us,light,4,41.5033333,-94.3183333
6/20/1979,orlando,fl,us,circle,600,28.5380556,-81.3794444
6/20/1994,oroville,wa,us,triangle,180,48.9391667,-119.4344444
6/20/1999,las vegas,nv,us,oval,300,36.1750000,-115.1363889
6/20/2003,chicago (over lake michigan),il,us,teardrop,120,41.8500000,-87.65
6/20/2006,santa fe springs,ca,us,egg,120,33.9472222,-118.0844444
6/20/2007,wheatland,nd,us,circle,120,46.9075000,-97.345
6/20/2009,boulder,co,us,light,300,40.0150000,-105.27
6/20/2012,laramie,wy,us,circle,300,41.3113889,-105.5905556
6/20/2013,north myrtle beach,sc,us,fireball,60,33.8158333,-78.6802778
6/21/1998,waveland,ms,us,oval,300,30.2866667,-89.3761111
6/21/2003,candler,nc,us,unknown,900,35.5363889,-82.6930556
6/21/2007,mobile,al,us,fireball,2,30.6941667,-88.0430556
6/21/2009,worcester,vt,us,other,900,44.3736111,-72.5502778
6/21/2012,loveland,co,us,light,300,40.3977778,-105.0744444
6/21/2013,grand rapids,mi,us,fireball,360,42.9633333,-85.6680556
6/2/2004,pahrump,nv,us,formation,3600,36.2083333,-115.9830556
6/2/2008,minneapolis,mn,us,light,1200,44.9800000,-93.2636111
6/2/2011,carthage,tn,us,light,5,36.2522222,-85.9516667
6/2/2013,morden (canada),mb,ca,light,120,45.1,-64.933333
6/22/1998,belgrade (outside&#44 dry creekroad),mt,us,unknown,3600,45.7761111,-111.1761111
6/22/2003,baltimore,md,us,diamond,120,39.2902778,-76.6125
6/22/2007,pottsville,pa,us,sphere,60,40.6855556,-76.1958333
6/22/2010,prescott,az,us,light,1800,34.5400000,-112.4677778
6/22/2012,marine city,mi,us,light,900,42.7194444,-82.4922222
6/22/2013,northampton,ma,us,oval,300,42.3250000,-72.6416667
6/23/1985,hinton (canada),ab,ca,other,40,53.4,-117.583333
6/23/2001,fernandina beach,fl,us,circle,300,30.6694444,-81.4627778
6/23/2005,italy,tx,us,light,30,32.1838889,-96.8844444
6/23/2007,old station,ca,us,light,60,40.6752778,-121.4297222
6/23/2009,curtisville,pa,us,triangle,300,40.6422222,-79.8511111
6/23/2012,downey,ca,us,oval,20,33.9400000,-118.1316667
6/23/2013,las vegas,nv,us,triangle,3600,36.1750000,-115.1363889
6/24/1999,bouse,az,us,cylinder,600,33.9325000,-114.005
6/24/2004,gilroy,ca,us,light,240,37.0058333,-121.5672222
6/24/2006,mcallen,tx,us,light,3600,26.2030556,-98.2297222
6/24/2009,tomball,tx,us,light,1800,30.0969444,-95.6158333
6/24/2011,seminary,ms,us,circle,600,31.5622222,-89.4975
6/24/2012,ypsilanti,mi,us,triangle,900,42.2411111,-83.6130556
6/25/1976,phoenix,az,us,disk,37800,33.4483333,-112.0733333
6/25/2001,mount vernon,wa,us,triangle,180,48.4213889,-122.3327778
6/25/2002,aberdeen,wa,us,circle,15,46.9755556,-123.8144444
6/25/2006,allen park,mi,us,other,60,42.2575000,-83.2111111
6/25/2010,dade city,fl,us,teardrop,2,28.3644444,-82.1961111
6/25/2012,north cove,nc,us,oval,10,35.8358333,-81.9891667
6/25/2013,miami,fl,us,light,600,25.7738889,-80.1938889
6/26/2002,sabina,oh,us,sphere,2,39.4886111,-83.6369444
6/26/2004,sagamore hills,oh,us,fireball,600,41.3116667,-81.5683333
6/26/2008,cuchara,co,us,light,1800,37.3791667,-105.0997222
6/26/2010,seattle,wa,us,light,120,47.6063889,-122.3308333
6/26/2013,cinnaminson,nj,us,light,30,39.9966667,-74.9930556
6/27/2001,missoula,mt,us,changing,5,46.8722222,-113.9930556
6/27/2004,wheeling,wv,us,light,5,40.0638889,-80.7211111
6/27/2009,fairborn,oh,us,triangle,300,39.8208333,-84.0194444
6/27/2012,o&#39fallon,mo,us,circle,180,38.8105556,-90.6997222
6/28/1964,alexandria,va,us,disk,600,38.8047222,-77.0472222
6/28/2002,wisconsin dells,wi,us,egg,120,43.6275000,-89.7708333
6/28/2006,crescent city,ca,us,unknown,2,41.7561111,-124.2005556
6/28/2009,phoenix,az,us,diamond,1800,33.4483333,-112.0733333
6/28/2011,hermitage,tn,us,triangle,180,36.1961111,-86.6225
6/28/2013,oak harbor,wa,us,cylinder,85,48.2933333,-122.6419444
6/29/2000,jefferson city,mo,us,triangle,1200,38.5766667,-92.1733333
6/29/2005,harbor springs,mi,us,light,5,45.4316667,-84.9919444
6/29/2009,sarasota,fl,us,unknown,540,27.3361111,-82.5308333
6/29/2012,alexandria,mn,us,triangle,30,45.8852778,-95.3772222
6/29/2013,stanton,ia,us,sphere,90,40.9816667,-95.1038889
6/30/1951,jackson heights,ny,us,disk,5,40.7555556,-73.8858333
6/30/1959,campbellsport,wi,us,circle,1200,43.5977778,-88.2788889
6/30/1966,mendota,ca,us,disk,300,36.7536111,-120.3805556
6/30/1968,stockton,ca,us,disk,600,37.9577778,-121.2897222
6/30/1974,new york city (bronx),ny,us,circle,600,40.7141667,-74.0063889
6/30/1977,whittier,ca,us,triangle,7200,33.9791667,-118.0319444
6/30/1981,sharon springs,ny,us,circle,14400,42.7958333,-74.6175
6/30/1987,st. cloud,fl,us,other,120,28.2486111,-81.2813889
6/30/1995,canton,oh,us,unknown,300,40.7988889,-81.3786111
6/30/1998,jackson,ms,us,cylinder,180,32.2986111,-90.1847222
6/30/2001,st. thomas (canada),on,ca,formation,300,42.783333,-81.183333
6/30/2003,syracuse,ny,us,fireball,1800,43.0480556,-76.1477778
6/30/2005,beaverton,or,us,light,120,45.4872222,-122.8025
6/30/2006,raddle,il,us,triangle,480,37.7788889,-89.5866667
6/30/2008,wolf point,mt,us,sphere,120,48.0905556,-105.64
6/30/2011,fort collins,co,us,flash,3,40.5852778,-105.0838889
6/30/2012,mesa,az,us,triangle,120,33.4222222,-111.8219444
6/30/2013,prescott,az,us,fireball,30,34.5400000,-112.4677778
6/3/2001,denver,co,us,disk,420,39.7391667,-104.9841667
6/3/2005,englewood,co,us,circle,60,39.6477778,-104.9872222
6/3/2011,kenefic,ok,us,other,120,34.1480556,-96.3619444
6/3/2013,los angeles,ca,us,fireball,900,34.0522222,-118.2427778
6/4/2001,fresno,ca,us,sphere,7200,36.7477778,-119.7713889
6/4/2006,santa ana,ca,us,formation,1200,33.7455556,-117.8669444
6/4/2011,avon,ct,us,disk,4,41.8097222,-72.8311111
6/4/2013,twin falls,id,us,sphere,1438,42.5630556,-114.46
6/5/2000,sargent,ga,us,unknown,300,33.4322222,-84.8694444
6/5/2004,jasper,ar,us,triangle,30,36.0080556,-93.1863889
6/5/2007,bloomington,in,us,unknown,10,39.1652778,-86.5263889
6/5/2010,sacramento,ca,us,light,20,38.5816667,-121.4933333
6/5/2013,roanoke,va,us,light,60,37.2708333,-79.9416667
6/6/1971,victorville,ca,us,light,1800,34.5361111,-117.2902778
6/6/1998,elba,ny,us,light,20,43.0772222,-78.1872222
6/6/2002,las vegas,nv,us,sphere,180,36.1750000,-115.1363889
6/6/2006,boise,id,us,triangle,60,43.6136111,-116.2025
6/6/2008,smithville,mo,us,oval,60,39.3869444,-94.5808333
6/6/2010,lake elsinore,ca,us,oval,2700,33.6680556,-117.3263889
6/6/2013,commerce city,co,us,fireball,120,39.8083333,-104.9333333
6/7/2000,modesto,ca,us,sphere,240,37.6391667,-120.9958333
6/7/2004,christmas valley,or,us,other,2400,43.2363889,-120.6358333
6/7/2008,annapolis,md,us,changing,3600,38.9783333,-76.4925
6/7/2010,oak lawn,il,us,light,60,41.7108333,-87.7580556
6/7/2013,elkhart,in,us,fireball,180,41.6819444,-85.9766667
6/8/1999,pasco,wa,us,light,600,46.2397222,-119.0994444
6/8/2005,neosho,mo,us,sphere,3600,36.8688889,-94.3677778
6/8/2008,minneapolis,mn,us,light,60,44.9800000,-93.2636111
6/8/2012,baldwin park,ca,us,fireball,240,34.0852778,-117.96
6/8/2013,emmett,id,us,sphere,120,43.8736111,-116.4983333
6/9/2000,germantown,md,us,triangle,60,39.1730556,-77.2719444
6/9/2003,avondale,az,us,sphere,180,33.4355556,-112.3488889
6/9/2008,miami,fl,us,rectangle,2,25.7738889,-80.1938889
6/9/2012,portland,or,us,formation,60,45.5236111,-122.675
6/9/2013,west hartford,ct,us,light,4,41.7636111,-72.6855556
7/10/1978,grand rapids,mi,us,triangle,300,42.9633333,-85.6680556
7/10/1997,lafayette,in,us,fireball,900,40.4166667,-86.8752778
7/10/2002,tooele,ut,us,fireball,60,40.5308333,-112.2975
7/10/2004,los angeles,ca,us,light,10,34.0522222,-118.2427778
7/10/2008,jasper,in,us,circle,900,38.3913889,-86.9311111
7/10/2010,cougar,wa,us,other,600,46.0516667,-122.2983333
7/10/2010,millville,pa,us,light,3600,41.1202778,-76.5302778
7/10/2012,baltimore,md,us,sphere,600,39.2902778,-76.6125
7/11/1997,allison park (hampton twp.),pa,us,cylinder,360,40.5594444,-79.9588889
7/11/2002,newark,oh,us,circle,2700,40.0580556,-82.4013889
7/11/2005,niagara falls (canada),on,ca,teardrop,600,43.1,-79.05
7/11/2008,lansing,il,us,triangle,120,41.5647222,-87.5388889
7/11/2010,everett,wa,us,circle,900,47.9791667,-122.2008333
7/11/2012,redding,ca,us,light,120,40.5866667,-122.3905556
7/1/1947,maywood,ca,us,disk,120,33.9866667,-118.1844444
7/1/1965,moberly,mo,us,light,900,39.4183333,-92.4380556
7/1/1972,provo (south of),ut,us,disk,1800,40.2338889,-111.6577778
7/1/1977,burnet,tx,us,light,1800,30.7580556,-98.2280556
7/1/1981,indian springs,nv,us,light,2700,36.5697222,-115.6697222
7/1/1988,tucson,az,us,triangle,600,32.2216667,-110.9258333
7/1/1991,mulliken,mi,us,disk,1325,42.7622222,-84.8963889
7/1/1995,wenksville,pa,us,light,1200,39.9900000,-77.3108333
7/1/1999,morganton,nc,us,diamond,30,35.7452778,-81.685
7/1/2000,stockton,ca,us,disk,900,37.9577778,-121.2897222
7/1/2003,moses lake,wa,us,other,7200,47.1302778,-119.2769444
7/1/2006,decatur,mi,us,light,1200,42.1080556,-85.9744444
7/1/2009,irving,tx,us,oval,10,32.8138889,-96.9486111
7/1/2011,mount forest (canada),on,ca,fireball,600,43.966667,-80.733333
7/1/2011,niagara falls (canada),on,ca,flash,1,43.1,-79.05
7/1/2013,shorewood,il,us,other,60,41.5200000,-88.2016667
7/12/1995,salt lake city,ut,us,disk,1200,40.7608333,-111.8902778
7/12/2001,arlington,wa,us,light,3,48.1988889,-122.1238889
7/12/2004,st. cloud,mn,us,sphere,60,45.5608333,-94.1622222
7/12/2007,hesperia,ca,us,light,4,34.4263889,-117.3
7/12/2009,pittsburgh,pa,us,sphere,180,40.4405556,-79.9961111
7/12/2012,viola,de,us,other,120,39.0427778,-75.5722222
7/12/2013,new castle,va,us,triangle,300,37.5000000,-80.1111111
7/13/2000,gilbert,az,us,circle,900,33.3527778,-111.7883333
7/13/2002,paramus,nj,us,formation,70,40.9444444,-74.0758333
7/13/2005,longville,mn,us,light,600,46.9863889,-94.2111111
7/13/2007,st. louis,mo,us,triangle,240,38.6272222,-90.1977778
7/13/2009,cathedral city,ca,us,oval,1200,33.7797222,-116.4644444
7/13/2011,dunbar,wv,us,light,1800,38.3605556,-81.7375
7/13/2012,winnipeg (canada),mb,ca,oval,240,49.883333,-97.166667
7/13/2013,hudson,oh,us,fireball,120,41.2400000,-81.4408333
7/14/1987,sacramento,ca,us,other,60,38.5816667,-121.4933333
7/14/2001,new holland,pa,us,light,240,40.1016667,-76.0855556
7/14/2005,palm harbor (clearwater),fl,us,light,1320,28.0777778,-82.7638889
7/14/2007,mahwah,nj,us,sphere,7,41.0886111,-74.1441667
7/14/2009,three rivers,ca,us,light,30,36.4388889,-118.9036111
7/14/2012,airway heights,wa,us,light,180,47.6447222,-117.5922222
7/14/2013,georgetown,ky,us,sphere,300,38.2097222,-84.5588889
7/15/1947,morehouse,mo,us,cylinder,1140,36.8472222,-89.6852778
7/15/1960,goldsboro,nc,us,sphere,120,35.3847222,-77.9930556
7/15/1965,whitesburg,ky,us,light,2700,37.1183333,-82.8269444
7/15/1969,fairfax,ca,us,disk,60,37.9872222,-122.5877778
7/15/1974,live oak,ca,us,triangle,300,39.2758333,-121.6588889
7/15/1975,summerside (canada),pe,ca,rectangle,300,46.4,-63.783333
7/15/1978,santa fe (pecos wilderness),nm,us,light,900,35.6869444,-105.9372222
7/15/1981,fayetteville,ar,us,other,180,36.0625000,-94.1572222
7/15/1986,elmvale (canada),on,ca,light,1200,44.583333,-79.866667
7/15/1991,mckinney,tx,us,unknown,600,33.1975000,-96.615
7/15/1995,hesperia,ca,us,fireball,600,34.4263889,-117.3
7/15/1997,reedsville,wv,us,triangle,60,39.5105556,-79.7986111
7/15/1998,sterling,va,us,disk,900,39.0061111,-77.4288889
7/15/2000,los angeles,ca,us,triangle,60,34.0522222,-118.2427778
7/15/2001,wilmington,ca,us,fireball,1200,33.7800000,-118.2616667
7/15/2002,bothell,wa,us,oval,900,47.7625000,-122.2041667
7/15/2003,taylorsville,ut,us,flash,120,40.6677778,-111.9380556
7/15/2005,iowa city (near&#44 on i-380),ia,us,sphere,600,41.6611111,-91.53
7/15/2006,port dover (canada),on,ca,disk,120,42.783333,-80.2
7/15/2007,yuba city,ca,us,triangle,120,39.1405556,-121.6158333
7/15/2009,manchester,tn,us,other,30,35.4816667,-86.0886111
7/15/2010,ocoee,tn,us,circle,3600,35.1222222,-84.7188889
7/15/2012,florence,mt,us,triangle,60,46.6316667,-114.0780556
7/16/1981,mont-tremblant (canada),pq,ca,disk,2700,46.2,-74.633333
7/16/2001,new york city (manhattan) (great lawn),ny,us,diamond,60,40.7141667,-74.0063889
7/16/2006,chicago,il,us,circle,30,41.8500000,-87.65
7/16/2009,oakwood,tx,us,light,30,31.5847222,-95.8488889
7/16/2011,sarasota,fl,us,diamond,300,27.3361111,-82.5308333
7/16/2013,prior lake,mn,us,sphere,600,44.7133333,-93.4225
7/17/1999,sewell,nj,us,triangle,15,39.7663889,-75.1447222
7/17/2003,kirkland,wa,us,other,3,47.6816667,-122.2075
7/17/2005,loveland,co,us,light,120,40.3977778,-105.0744444
7/17/2008,colfax,wi,us,light,30,44.9975000,-91.7269444
7/17/2010,seattle,wa,us,formation,600,47.6063889,-122.3308333
7/17/2012,dade city,fl,us,sphere,300,28.3644444,-82.1961111
7/18/1970,custer,mt,us,light,1200,46.1291667,-107.5544444
7/18/1999,robbins,tx,us,circle,1200,31.2552778,-96.1225
7/18/2004,kirkland,wa,us,sphere,600,47.6816667,-122.2075
7/18/2008,federalsburg,md,us,disk,120,38.6941667,-75.7725
7/18/2009,pound ridge,ny,us,other,10,41.2086111,-73.5752778
7/18/2011,vancouver,wa,us,sphere,600,45.6388889,-122.6602778
7/18/2012,myrtle beach,sc,us,light,300,33.6888889,-78.8869444
7/19/1978,mojave,ca,us,light,300,35.0525000,-118.1730556
7/19/2003,charleston,sc,us,circle,900,32.7763889,-79.9311111
7/19/2006,murfreesboro,tn,us,cylinder,15,35.8455556,-86.3902778
7/19/2009,ocean city,nj,us,light,240,39.2775000,-74.575
7/19/2012,seaside,or,us,sphere,120,45.9933333,-123.9213889
7/20/1962,springdale,ar,us,light,1200,36.1866667,-94.1286111
7/20/1977,milwaukee,wi,us,formation,300,43.0388889,-87.9063889
7/20/1996,clear lake,tx,us,teardrop,300,33.0780556,-96.495
7/20/2001,middletown,oh,us,light,15,39.5150000,-84.3983333
7/20/2004,federal way,wa,us,unknown,30,47.3225000,-122.3113889
7/20/2006,shoreview,mn,us,cigar,60,45.0791667,-93.1469444
7/20/2008,west bloomfield,mi,us,sphere,120,42.5377778,-83.2330556
7/20/2010,ida,mi,us,fireball,600,41.9108333,-83.5736111
7/20/2012,princeton,in,us,circle,2700,38.3552778,-87.5675
7/21/1998,houston,tx,us,other,900,29.7630556,-95.3630556
7/21/2003,port angeles,wa,us,sphere,300,48.1183333,-123.4294444
7/21/2007,nashville,tn,us,sphere,1800,36.1658333,-86.7844444
7/21/2008,pueblo,co,us,rectangle,10800,38.2544444,-104.6086111
7/21/2011,rochester,ny,us,changing,60,43.1547222,-77.6158333
7/21/2012,vacaville,ca,us,light,1140,38.3566667,-121.9866667
7/2/1977,glen head,ny,us,cigar,240,40.8352778,-73.6241667
7/2/2002,kansas city,mo,us,oval,180,39.0997222,-94.5783333
7/2/2005,portsmouth,oh,us,triangle,7200,38.7316667,-82.9977778
7/2/2009,vergas,mn,us,formation,120,46.6566667,-95.805
7/2/2011,hilo,hi,us,light,2400,19.7297222,-155.09
7/2/2012,fairborn,oh,us,flash,2,39.8208333,-84.0194444
7/22/1977,atwater,ca,us,disk,180,37.3477778,-120.6080556
7/22/2001,wellington county (canada),on,ca,other,300,46.433333,-64.0
7/22/2005,jacksonville,fl,us,light,1800,30.3319444,-81.6558333
7/22/2008,lake charles,la,us,circle,480,30.2263889,-93.2172222
7/22/2011,custer,sd,us,circle,300,43.7666667,-103.5983333
7/22/2012,frederick,md,us,circle,900,39.4141667,-77.4108333
7/23/1999,marietta,oh,us,cigar,45,39.4152778,-81.455
7/23/2002,montreal (canada),pq,ca,triangle,7200,45.5,-73.583333
7/23/2004,los angeles,ca,us,flash,900,34.0522222,-118.2427778
7/23/2008,lafayette,in,us,light,2400,40.4166667,-86.8752778
7/23/2011,ursa,il,us,light,3600,40.0747222,-91.3672222
7/23/2012,chico,ca,us,circle,480,39.7286111,-121.8363889
7/24/1999,philadelphia,pa,us,flash,60,39.9522222,-75.1641667
7/24/2004,frostburg,md,us,unknown,900,39.6580556,-78.9286111
7/24/2008,phoenix,az,us,unknown,35,33.4483333,-112.0733333
7/24/2010,oklahoma city,ok,us,circle,10800,35.4675000,-97.5161111
7/24/2012,brighton,mi,us,unknown,1,42.5294444,-83.7802778
7/25/1971,allentown,pa,us,light,180,40.6083333,-75.4905556
7/25/1999,moses lake,wa,us,sphere,300,47.1302778,-119.2769444
7/25/2002,shirley,ny,us,formation,180,40.8013889,-72.8680556
7/25/2005,vancouver (canada),bc,ca,formation,1380,49.25,-123.133333
7/25/2008,phoenix,az,us,light,30,33.4483333,-112.0733333
7/25/2009,union,ms,us,light,10,32.5713889,-89.1213889
7/25/2012,leroy,mi,us,oval,7200,45.2200000,-83.5208333
7/25/2013,hagerstown,md,us,oval,2,39.6416667,-77.7202778
7/26/1999,bricktown,nj,us,rectangle,20,40.0591667,-74.1375
7/26/2003,cranbrook (canada),bc,ca,light,120,49.516667,-115.766667
7/26/2006,phoenix,az,us,cigar,300,33.4483333,-112.0733333
7/26/2009,plains,pa,us,circle,900,41.2752778,-75.8505556
7/26/2012,arcata,ca,us,formation,240,40.8666667,-124.0816667
7/27/1983,san antonio,tx,us,cigar,900,29.4238889,-98.4933333
7/27/2001,new york city,ny,us,oval,15,40.7141667,-74.0063889
7/27/2004,woodinville,wa,us,teardrop,2100,47.7544444,-122.1622222
7/27/2007,north myrtle beach,sc,us,fireball,5,33.8158333,-78.6802778
7/27/2010,shelbyville,in,us,light,1800,39.5213889,-85.7769444
7/27/2012,stevensville,md,us,light,900,38.9805556,-76.3147222
7/27/2013,pawtucket,ri,us,circle,120,41.8786111,-71.3830556
7/28/1992,sioux falls,sd,us,light,1800,43.5500000,-96.7
7/28/2002,sedona,az,us,oval,20,34.8697222,-111.7602778
7/28/2005,oshkosh,wi,us,disk,900,44.0247222,-88.5425
7/28/2007,austin,tx,us,circle,180,30.2669444,-97.7427778
7/28/2010,lansing,mi,us,light,600,42.7325000,-84.5555556
7/28/2012,olathe,ks,us,light,360,38.8813889,-94.8188889
7/29/1987,edmonton (canada),ab,ca,triangle,180,53.55,-113.5
7/29/2004,puyallup,wa,us,fireball,600,47.1855556,-122.2916667
7/29/2006,myrtle beach,sc,us,flash,5400,33.6888889,-78.8869444
7/29/2010,canton,oh,us,fireball,2700,40.7988889,-81.3786111
7/29/2012,ann arbor,mi,us,cylinder,1200,42.2708333,-83.7263889
7/29/2013,tacoma (northeast area),wa,us,sphere,5,47.2530556,-122.4430556
7/30/1997,corpus christi,tx,us,oval,300,27.8002778,-97.3961111
7/30/2003,bushkill,pa,us,formation,120,41.0933333,-75.0022222
7/30/2006,indialantic,fl,us,fireball,900,28.0891667,-80.5658333
7/30/2008,russellville,ar,us,formation,10800,35.2783333,-93.1336111
7/30/2011,new york city (staten island),ny,us,fireball,60,40.7141667,-74.0063889
7/30/2012,ypsilanti,mi,us,oval,300,42.2411111,-83.6130556
7/31/1984,middlebury,ct,us,other,900,41.5277778,-73.1280556
7/31/2002,liberty,oh,us,other,900,39.7200000,-84.325
7/31/2005,eugene,or,us,rectangle,60,44.0522222,-123.0855556
7/31/2008,santa fe,nm,us,light,2400,35.6869444,-105.9372222
7/31/2010,wichita,ks,us,diamond,300,37.6922222,-97.3372222
7/31/2011,lakeside,ca,us,fireball,900,32.8572222,-116.9213889
7/31/2013,elk grove,ca,us,circle,5,38.4088889,-121.3705556
7/3/2000,kewaunee,wi,us,disk,180,44.4583333,-87.5030556
7/3/2004,madison,in,us,light,60,38.7358333,-85.38
7/3/2007,stanwood,wa,us,disk,10,48.2413889,-122.3694444
7/3/2008,elkhart,in,us,oval,120,41.6819444,-85.9766667
7/3/2010,baltimore,oh,us,oval,240,39.8452778,-82.6008333
7/3/2010,lancaster,pa,us,circle,600,40.0377778,-76.3058333
7/3/2011,mableton,ga,us,sphere,300,33.8186111,-84.5825
7/3/2011,crystal lake,il,us,unknown,180,42.2411111,-88.3161111
7/3/2012,grayling,mi,us,circle,300,44.6613889,-84.7147222
7/3/2013,eugene,or,us,flash,300,44.0522222,-123.0855556
7/4/1977,toppenish,wa,us,disk,300,46.3775000,-120.3075
7/4/1995,woodlake,ca,us,cylinder,60,36.4136111,-119.0977778
7/4/1997,chesterfield,mo,us,light,2,38.6630556,-90.5769444
7/4/1997,frontenac,mo,us,light,5,38.6355556,-90.415
7/4/2000,windsor heights,ia,us,light,3600,41.5977778,-93.7080556
7/4/2002,sherman,ny,us,cigar,45,42.1591667,-79.5955556
7/4/2003,ottawa (canada),on,ca,light,10,45.416667,-75.7
7/4/2004,casselberry,fl,us,light,180,28.6775000,-81.3280556
7/4/2005,granite falls,wa,us,sphere,60,48.0841667,-121.9675
7/4/2007,kalispell,mt,us,unknown,10,48.1958333,-114.3119444
7/4/2008,athens,ga,us,light,240,33.9608333,-83.3780556
7/4/2008,albuquerque,nm,us,sphere,4,35.0844444,-106.6505556
7/4/2009,el cajon,ca,us,light,960,32.7947222,-116.9616667
7/4/2009,fond du lac,wi,us,fireball,300,43.7730556,-88.4469444
7/4/2009,alpena,mi,us,oval,120,45.0616667,-83.4327778
7/4/2010,huntsville,al,us,other,7200,34.7302778,-86.5861111
7/4/2010,mulberry,ar,us,circle,360,35.5005556,-94.0513889
7/4/2010,great falls,mt,us,unknown,120,47.5002778,-111.3
7/4/2010,portsmouth,oh,us,light,180,38.7316667,-82.9977778
7/4/2010,womelsdorf,pa,us,other,120,40.3616667,-76.1844444
7/4/2010,hellertown,pa,us,teardrop,120,40.5794444,-75.3411111
7/4/2011,antigo,wi,us,light,20,45.1402778,-89.1522222
7/4/2011,hawthorne,ca,us,fireball,180,33.9163889,-118.3516667
7/4/2011,portland,tn,us,circle,60,36.5816667,-86.5163889
7/4/2011,star,id,us,fireball,120,43.6922222,-116.4925
7/4/2012,ocean city,md,us,cylinder,20,38.3363889,-75.0852778
7/4/2012,cedar park,tx,us,circle,300,30.5050000,-97.82
7/4/2012,pottstown,pa,us,fireball,300,40.2452778,-75.65
7/4/2012,tacoma,wa,us,fireball,3600,47.2530556,-122.4430556
7/4/2012,medical lake,wa,us,fireball,300,47.5730556,-117.6811111
7/4/2012,birmingham,al,us,oval,540,33.5205556,-86.8025
7/4/2013,aiken,sc,us,circle,60,33.5602778,-81.7197222
7/4/2013,heyworth,il,us,circle,600,40.3133333,-88.9736111
7/4/2013,boise,id,us,circle,60,43.6136111,-116.2025
7/4/2013,black rock,ar,us,light,240,36.1083333,-91.0972222
7/4/2013,miami,fl,us,fireball,900,25.7738889,-80.1938889
7/5/1985,peekskill,ny,us,triangle,480,41.2900000,-73.9208333
7/5/2000,kingman,az,us,other,120,35.1894444,-114.0522222
7/5/2003,sedona,az,us,triangle,120,34.8697222,-111.7602778
7/5/2006,tucson,az,us,light,180,32.2216667,-110.9258333
7/5/2008,ashland,ky,us,circle,300,38.4783333,-82.6380556
7/5/2010,east greenville,pa,us,fireball,180,40.4063889,-75.5022222
7/5/2012,tacoma,wa,us,light,300,47.2530556,-122.4430556
7/5/2013,valdosta,ga,us,fireball,180,30.8325000,-83.2786111
7/6/1981,ellwood city,pa,us,sphere,20,40.8616667,-80.2866667
7/6/2002,salt lake city,ut,us,other,4,40.7608333,-111.8902778
7/6/2004,cleveland,oh,us,unknown,20,41.4994444,-81.6955556
7/6/2008,new glasgow (canada),ns,ca,changing,2,45.583333,-62.633333
7/6/2010,dorchester,ma,us,sphere,60,42.2972222,-71.075
7/6/2012,allentown,pa,us,unknown,60,40.6083333,-75.4905556
7/6/2013,st. petersburg,fl,us,fireball,120,27.7705556,-82.6794444
7/6/2013,bristol,nh,us,formation,480,43.5911111,-71.7372222
7/7/1968,houston,tx,us,disk,900,29.7630556,-95.3630556
7/7/1995,west milford,nj,us,triangle,900,40.5686111,-75.095
7/7/2000,los angeles,ca,us,light,600,34.0522222,-118.2427778
7/7/2001,rockford,il,us,light,3,42.2711111,-89.0938889
7/7/2004,conyers,ga,us,other,2,33.6675000,-84.0177778
7/7/2007,fort wayne,in,us,fireball,1200,41.1305556,-85.1288889
7/7/2009,london,ky,us,circle,180,37.1288889,-84.0833333
7/7/2011,milton,vt,us,unknown,60,44.6397222,-73.1108333
7/7/2012,altoona,pa,us,circle,180,40.5186111,-78.395
7/7/2013,lindenhurst,ny,us,circle,120,40.6866667,-73.3738889
7/8/1995,ravenna,oh,us,unknown,600,41.1575000,-81.2422222
7/8/2003,clermont,in,us,disk,300,39.8097222,-86.3225
7/8/2006,mansfield,tx,us,oval,13,32.5630556,-97.1413889
7/8/2009,etobicoke (canada),on,ca,unknown,90,43.7,-79.566667
7/8/2012,oakland,ca,us,circle,600,37.8044444,-122.2697222
7/9/1964,chicago,il,us,disk,30,41.8500000,-87.65
7/9/2001,spring valley,ca,us,sphere,300,32.7447222,-116.9980556
7/9/2004,elizabethton,tn,us,circle,30,36.3486111,-82.2108333
7/9/2007,sarasota,fl,us,cigar,120,27.3361111,-82.5308333
7/9/2010,springfield,mo,us,disk,300,37.2152778,-93.2980556
7/9/2011,san fernando,ca,us,oval,2,34.2819444,-118.4380556
7/9/2013,buckeye,az,us,light,1350,33.3702778,-112.5830556
8/10/1981,salinas,ca,us,disk,600,36.6777778,-121.6544444
8/10/1996,seattle,wa,us,triangle,600,47.6063889,-122.3308333
8/10/2001,cedar hill,tx,us,light,3600,32.5883333,-96.9558333
8/10/2002,ashland,or,us,unknown,120,42.1947222,-122.7083333
8/10/2005,lake city,mi,us,disk,120,44.3352778,-85.215
8/10/2008,madison,wi,us,other,120,43.0730556,-89.4011111
8/10/2011,yakima,wa,us,light,120,46.6022222,-120.5047222
8/10/2012,franklin,tn,us,fireball,180,35.9250000,-86.8688889
8/10/2013,bristol,nh,us,circle,30,43.5911111,-71.7372222
8/11/1999,ettersburg,ca,us,rectangle,120,40.1386111,-123.9961111
8/11/2002,san rafael,ca,us,light,5,37.9736111,-122.53
8/11/2005,goleta,ca,us,flash,1,34.4358333,-119.8266667
8/11/2007,tiskilwa,il,us,light,1200,41.2922222,-89.5061111
8/11/2010,el paso,tx,us,light,120,31.7586111,-106.4863889
8/11/2011,annapolis,md,us,rectangle,5,38.9783333,-76.4925
8/11/2012,san diego,ca,us,circle,600,32.7152778,-117.1563889
8/1/1948,new york city (brooklyn),ny,us,circle,600,40.7141667,-74.0063889
8/1/1965,st. louis,mo,us,sphere,120,38.6272222,-90.1977778
8/1/1973,scituate,ma,us,triangle,900,42.1958333,-70.7263889
8/1/1978,reading,pa,us,formation,300,40.3355556,-75.9272222
8/1/1988,north hampton,nh,us,rectangle,300,42.9725000,-70.8302778
8/1/1994,beloit,wi,us,triangle,45,42.5083333,-89.0316667
8/1/1998,st. louis,mo,us,light,120,38.6272222,-90.1977778
8/1/2000,turkey,tx,us,circle,86400,34.3925000,-100.8972222
8/1/2002,parma,oh,us,sphere,300,41.4047222,-81.7230556
8/1/2005,bowmanville (canada),on,ca,teardrop,5,43.9,-78.683333
8/1/2008,palestine,tx,us,teardrop,180,31.7619444,-95.6305556
8/1/2009,vero beach,fl,us,light,300,27.6383333,-80.3975
8/1/2011,newport news,va,us,light,20,36.9786111,-76.4283333
8/1/2013,coeur d&#39alene,id,us,sphere,120,47.6777778,-116.7794444
8/12/1995,arlington,wa,us,triangle,600,48.1988889,-122.1238889
8/12/2000,wallingford,ct,us,triangle,10,41.4569444,-72.8236111
8/12/2002,beaver falls,pa,us,light,15,40.7519444,-80.3194444
8/12/2004,boulder,mt,us,light,45,46.2366667,-112.12
8/12/2007,van wert,oh,us,sphere,30,40.8694444,-84.5841667
8/12/2007,orlando,fl,us,triangle,60,28.5380556,-81.3794444
8/12/2010,ingonish (canada),ns,ca,light,3600,46.683333,-60.366667
8/12/2011,cheektowaga (buffalo),ny,us,light,120,42.9033333,-78.755
8/12/2012,red bay (canada),on,ca,circle,120.0,51.733333,-56.416667
8/12/2013,menomonee  falls,wi,us,triangle,90.0,43.1788889,-88.1172222
8/13/2000,bothell,wa,us,rectangle,60.0,47.7625,-122.2041667
8/13/2003,houston (canada),bc,ca,other,300.0,54.4,-126.65
8/13/2006,socastee,sc,us,sphere,180.0,33.6833333,-78.9986111
8/13/2009,keswick (canada),on,ca,unknown,3600.0,44.25,-79.466667
8/13/2010,kingston,wa,us,triangle,300.0,47.7988889,-122.4969444
8/13/2011,truckee,ca,us,diamond,120.0,39.3280556,-120.1822222
8/13/2013,mchenry,il,us,unknown,60.0,42.3333333,-88.2666667
8/14/1984,buckingham (canada),pq,ca,unknown,1200.0,45.583333,-75.416667
8/14/2001,strathroy (canada),on,ca,triangle,900.0,42.95,-81.616667
8/14/2005,blairsville,ga,us,sphere,10.0,34.8761111,-83.9583333
8/14/2008,tumwater,wa,us,light,300.0,47.0075,-122.9080556
8/14/2010,mt. pleasant,pa,us,triangle,90.0,40.1488889,-79.5413889
8/14/2011,dixon,il,us,disk,20.0,41.8388889,-89.4794444
8/14/2013,key west,fl,us,cigar,300.0,24.5552778,-81.7827778
8/15/1955,eagle pass,tx,us,cigar,600.0,28.7088889,-100.4991667
8/15/1967,westford,ma,us,unknown,1200.0,42.5791667,-71.4383333
8/15/1973,farmers branch,tx,us,disk,900.0,32.9263889,-96.8958333
8/15/1977,rockford,mn,us,unknown,7200.0,45.0883333,-93.7341667
8/15/1980,apollo,pa,us,sphere,900.0,40.5813889,-79.5666667
8/15/1985,sagamore hills,oh,us,rectangle,300.0,41.3116667,-81.5683333
8/15/1988,buchanan,ny,us,circle,60.0,41.2619444,-73.9386111
8/15/1994,denver,co,us,other,5.0,39.7391667,-104.9841667
8/15/1996,lexington,va,us,light,5.0,37.7838889,-79.4430556
8/15/1998,simi valley,ca,us,light,120.0,34.2694444,-118.7805556
8/15/1999,jenks,ok,us,light,30.0,36.0227778,-95.9680556
8/15/2000,burke,va,us,circle,1200.0,38.7933333,-77.2719444
8/15/2002,ocean city,md,us,fireball,3600.0,38.3363889,-75.0852778
8/15/2003,ogdensburg,nj,us,light,300.0,41.0816667,-74.5927778
8/15/2004,niagara falls (canada),on,ca,light,600.0,43.1,-79.05
8/15/2006,trout lake,wa,us,flash,240.0,45.9975,-121.5269444
8/15/2007,santa rosa,ca,us,chevron,480.0,38.4405556,-122.7133333
8/15/2009,chicago,il,us,triangle,20.0,41.85,-87.65
8/15/2010,portland,or,us,sphere,180.0,45.5236111,-122.675
8/15/2012,omak,wa,us,teardrop,1200.0,48.4111111,-119.5263889
8/15/2013,coeur d&#39alene,id,us,light,60.0,47.6777778,-116.7794444
8/16/1999,bentonville,in,us,fireball,60.0,39.7452778,-85.1941667
8/16/2003,wheaton,il,us,cylinder,120.0,41.8661111,-88.1069444
8/16/2005,leander,tx,us,light,15.0,30.5786111,-97.8527778
8/16/2008,grand island,ne,us,oval,300.0,40.925,-98.3416667
8/16/2011,kingsport,tn,us,cylinder,10.0,36.5483333,-82.5619444
8/16/2013,fenton,mo,us,circle,20.0,38.5130556,-90.4358333
8/17/1982,vacaville,ca,us,fireball,480.0,38.3566667,-121.9866667
8/17/2001,vail,co,us,unknown,5.0,39.6402778,-106.3736111
8/17/2003,wichita,ks,us,cigar,20.0,37.6922222,-97.3372222
8/17/2006,florence,or,us,light,540.0,43.9827778,-124.0986111
8/17/2010,arlington,tx,us,triangle,1800.0,32.7355556,-97.1077778
8/17/2012,kansas city,ks,us,cigar,45.0,39.1141667,-94.6272222
8/17/2013,gloucester,ma,us,circle,180.0,42.6158333,-70.6625
8/18/1987,lincoln (near),il,us,disk,30.0,40.1483333,-89.3647222
8/18/2001,errol,nh,us,triangle,20.0,44.7813889,-71.1383333
8/18/2004,whitesboro,ny,us,light,240.0,43.1219444,-75.2919444
8/18/2007,sacramento,ca,us,cigar,60.0,38.5816667,-121.4933333
8/18/2010,bellevue,wa,us,other,5.0,47.6105556,-122.1994444
8/18/2012,binghamton,ny,us,unknown,120.0,42.0986111,-75.9183333
8/18/2012,pentwater,mi,us,sphere,600.0,43.7816667,-86.4330556
8/19/1989,cleveland,oh,us,disk,20.0,41.4994444,-81.6955556
8/19/2001,victoria (canada),bc,ca,light,30.0,46.216667,-63.483333
8/19/2004,st. louis park,mn,us,sphere,7200.0,44.9483333,-93.3477778
8/19/2006,point roberts,wa,us,circle,900.0,48.9855556,-123.0766667
8/19/2008,sylacauga,al,us,unknown,10.0,33.1730556,-86.2516667
8/19/2010,halifax (canada),ns,ca,light,1200.0,44.65,-63.6
8/19/2012,virginia beach,va,us,other,25.0,36.8527778,-75.9783333
8/20/1960,pittsburgh,pa,us,sphere,300.0,40.4405556,-79.9961111
8/20/1983,peoria county,il,us,cigar,60.0,40.6936111,-89.5888889
8/20/1994,carthage,mo,us,unknown,180.0,37.1763889,-94.31
8/20/2000,bellevue (capehart),ne,us,teardrop,10.0,41.1366667,-95.8905556
8/20/2002,prestonsburg,ky,us,other,2.0,37.6655556,-82.7716667
8/20/2004,new haven,in,us,teardrop,120.0,41.0705556,-85.0144444
8/20/2006,bend,or,us,oval,2700.0,44.0583333,-121.3141667
8/20/2007,greece,ny,us,cylinder,3600.0,43.2097222,-77.6933333
8/20/2010,nampa,id,us,cigar,300.0,43.5408333,-116.5625
8/20/2011,independence,mo,us,light,600.0,39.0911111,-94.4152778
8/20/2013,boston,ma,us,light,120.0,42.3583333,-71.0602778
8/21/2000,angus (canada),on,ca,unknown,7200.0,44.316667,-79.883333
8/21/2003,essexville,mi,us,light,240.0,43.6152778,-83.8419444
8/21/2004,peterborough (canada),on,ca,oval,120.0,44.3,-78.333333
8/21/2005,rockford,il,us,other,180.0,42.2711111,-89.0938889
8/21/2008,halifax (canada),ns,ca,formation,60.0,44.65,-63.6
8/21/2010,felton,de,us,changing,60.0,39.0083333,-75.5783333
8/21/2012,myrtle beach,sc,us,fireball,240.0,33.6888889,-78.8869444
8/2/1997,sikeston,mo,us,light,2.0,36.8766667,-89.5877778
8/2/2002,camarillo,ca,us,other,15.0,34.2163889,-119.0366667
8/2/2006,klamath falls,or,us,flash,180.0,42.225,-121.7805556
8/2/2008,chehalis,wa,us,unknown,30.0,46.6622222,-122.9627778
8/2/2011,silver spring,md,us,sphere,3600.0,38.9905556,-77.0263889
8/2/2013,flagstaff,az,us,formation,180.0,35.1980556,-111.6505556
8/22/1989,grahamsville,ny,us,rectangle,300.0,41.8477778,-74.5483333
8/22/2002,river falls,wi,us,disk,1800.0,44.8613889,-92.6236111
8/22/2004,woodbury,ct,us,disk,10.0,41.5444444,-73.2094444
8/22/2007,marfa,tx,us,cigar,600.0,30.3077778,-104.0186111
8/22/2009,flowery branch,ga,us,light,30.0,34.185,-83.9252778
8/22/2012,merrick,ny,us,triangle,1200.0,40.6627778,-73.5519444
8/22/2013,lehi,ut,us,unknown,180.0,40.3916667,-111.85
8/23/2002,louisville,ky,us,light,1800.0,38.2541667,-85.7594444
8/23/2005,marietta,ga,us,triangle,45.0,33.9525,-84.55
8/23/2008,hickory,nc,us,flash,2.0,35.7330556,-81.3413889
8/23/2010,gahanna,oh,us,oval,1800.0,40.0191667,-82.8794444
8/23/2012,chicago,il,us,fireball,30.0,41.85,-87.65
8/23/2013,davenport,ia,us,sphere,180.0,41.5236111,-90.5775
8/24/2001,kennebunk,me,us,formation,120.0,43.3838889,-70.5452778
8/24/2003,littleton,ma,us,sphere,90.0,42.5375,-71.5125
8/24/2006,farmington,mn,us,flash,1.0,44.6402778,-93.1433333
8/24/2009,toronto (canada),on,ca,light,2.0,43.666667,-79.416667
8/24/2012,northport,ny,us,fireball,600.0,40.9008333,-73.3436111
8/24/2013,elmira,ny,us,sphere,180.0,42.0897222,-76.8080556
8/24/2013,lake wales,fl,us,fireball,20.0,27.9011111,-81.5861111
8/25/1995,cheektowaga (near),ny,us,unknown,6.0,42.9033333,-78.755
8/25/2001,deer park,wa,us,light,5.0,47.9544444,-117.4758333
8/25/2004,social hill,ar,us,cigar,15.0,34.3319444,-92.9130556
8/25/2008,guelph (canada),on,ca,sphere,45.0,43.55,-80.25
8/25/2010,nashville,tn,us,fireball,1800.0,36.1658333,-86.7844444
8/25/2012,joliet,il,us,light,300.0,41.525,-88.0816667
8/25/2012,parkersburg,wv,us,light,30.0,39.2666667,-81.5616667
8/26/1990,punxsutawney,pa,us,sphere,900.0,40.9436111,-78.9711111
8/26/2003,orlando,fl,us,circle,180.0,28.5380556,-81.3794444
8/26/2006,fall city,wa,us,light,15.0,47.5675,-121.8875
8/26/2010,springdale,ar,us,cigar,5.0,36.1866667,-94.1286111
8/26/2012,mineral,va,us,changing,1800.0,38.0105556,-77.9088889
8/26/2013,greensburg,pa,us,fireball,120.0,40.3013889,-79.5391667
8/27/2003,westminster,co,us,triangle,15.0,39.8366667,-105.0366667
8/27/2005,mitchell,sd,us,circle,240.0,43.7094444,-98.0294444
8/27/2007,davie,fl,us,unknown,60.0,26.0625,-80.2333333
8/27/2010,cabot,ar,us,light,2.0,34.9744444,-92.0163889
8/27/2011,howard,oh,us,fireball,60.0,40.4075,-82.3269444
8/27/2013,garland,tx,us,fireball,600.0,32.9125,-96.6386111
8/28/2000,lenexa,ks,us,light,600.0,38.9536111,-94.7333333
8/28/2003,eunice,la,us,light,300.0,30.4941667,-92.4175
8/28/2007,moreno valley,ca,us,triangle,120.0,33.9375,-117.2297222
8/28/2009,trenton,nj,us,rectangle,1200.0,40.2169444,-74.7433333
8/28/2011,east brunswick,nj,us,sphere,3600.0,40.4277778,-74.4163889
8/28/2013,kapoho,hi,us,light,600.0,19.5061111,-154.8486111
8/29/2001,newmarket (canada),on,ca,triangle,10.0,44.05,-79.45
8/29/2004,new york city (brooklyn),ny,us,circle,180.0,40.7141667,-74.0063889
8/29/2008,south elgin,il,us,sphere,30.0,41.9941667,-88.2922222
8/29/2010,irondequoit,ny,us,cylinder,40.0,43.2133333,-77.58
8/29/2012,columbus,oh,us,fireball,60.0,39.9611111,-82.9988889
8/30/1967,lansing,ks,us,unknown,300.0,39.2486111,-94.9
8/30/2001,owatonna,mn,us,unknown,1200.0,44.0838889,-93.2258333
8/30/2003,rome,pa,us,circle,5.0,41.8583333,-76.3411111
8/30/2004,albuquerque,nm,us,unknown,180.0,35.0844444,-106.6505556
8/30/2008,appleton,wi,us,other,60.0,44.2619444,-88.4152778
8/30/2011,white house,tn,us,fireball,60.0,36.4702778,-86.6513889
8/30/2013,corpus christi,tx,us,circle,60.0,27.8002778,-97.3961111
8/31/1994,stockton (south of),ca,us,circle,120.0,37.9577778,-121.2897222
8/31/2003,barrie (canada),on,ca,unknown,5.0,44.383333,-79.7
8/31/2004,bristol,tn,us,other,1200.0,36.595,-82.1888889
8/31/2004,bellefonte,pa,us,other,900.0,40.9133333,-77.7786111
8/31/2008,waterloo,ia,us,light,2100.0,42.4927778,-92.3427778
8/31/2010,sacramento,ca,us,rectangle,180.0,38.5816667,-121.4933333
8/31/2012,spring hill,tn,us,cigar,10.0,35.7511111,-86.93
8/31/2013,bowmanville (canada),on,ca,light,120.0,43.9,-78.683333
8/3/1999,blue ridge summit (area),pa,us,unknown,720.0,39.7241667,-77.4716667
8/3/2002,sullivan,il,us,light,10.0,39.5994444,-88.6077778
8/3/2006,south pasadena,ca,us,fireball,5.0,34.1161111,-118.1494444
8/3/2008,scotch plains,nj,us,cigar,2.0,40.6552778,-74.3902778
8/3/2011,south point,oh,us,light,2400.0,38.4177778,-82.5863889
8/3/2012,lyndhurst,nj,us,fireball,28.0,40.8119444,-74.1247222
8/3/2013,fresno,ca,us,light,420.0,36.7477778,-119.7713889
8/4/2000,gilbert,az,us,light,120.0,33.3527778,-111.7883333
8/4/2003,ouray,co,us,other,180.0,38.0227778,-107.6708333
8/4/2006,hazard,ky,us,unknown,300.0,37.2494444,-83.1933333
8/4/2008,davie,fl,us,formation,300.0,26.0625,-80.2333333
8/4/2011,kingman,az,us,oval,600.0,35.1894444,-114.0522222
8/4/2012,exeter,nh,us,light,600.0,42.9813889,-70.9483333
8/4/2013,west jordan,ut,us,light,600.0,40.5,-111.95
8/5/1999,meridian,id,us,light,30.0,43.6122222,-116.3905556
8/5/2003,ashland,or,us,oval,5.0,42.1947222,-122.7083333
8/5/2006,corpus christi,tx,us,disk,7.0,27.8002778,-97.3961111
8/5/2008,phoenix,az,us,triangle,120.0,33.4483333,-112.0733333
8/5/2011,hialeah,fl,us,fireball,3.0,25.8572222,-80.2783333
8/5/2012,burlington (canada),on,ca,circle,20.0,43.316667,-79.8
8/6/1986,hutchinson,ks,us,triangle,2700.0,38.0608333,-97.9294444
8/6/2002,ahwahnee,ca,us,light,240.0,37.3655556,-119.7252778
8/6/2005,los angeles (sw of),ca,us,light,60.0,34.0522222,-118.2427778
8/6/2008,hartwell,ga,us,light,180.0,34.3527778,-82.9322222
8/6/2011,canyon lake,ca,us,triangle,5.0,33.685,-117.2722222
8/6/2012,thousand oaks,ca,us,light,5.0,34.1705556,-118.8366667
8/6/2013,clarkston,wa,us,light,240.0,46.4163889,-117.0441667
8/7/1994,port richey,fl,us,egg,15.0,28.2713889,-82.7197222
8/7/2002,richardson,tx,us,unknown,18000.0,32.9480556,-96.7294444
8/7/2005,medicine bow,wy,us,light,2040.0,41.8955556,-106.2041667
8/7/2008,lancaster,oh,us,unknown,120.0,39.7136111,-82.5994444
8/7/2011,big sur,ca,us,formation,10800.0,36.2702778,-121.8063889
8/7/2012,johnson city,tn,us,cigar,180.0,36.3133333,-82.3536111
8/7/2013,desert center,ca,us,unknown,72000.0,33.7125,-115.4013889
8/8/1974,mentor,oh,us,disk,600.0,41.6661111,-81.3397222
8/8/1998,houston (canada),bc,ca,disk,600.0,54.4,-126.65
8/8/2003,manchester,nh,us,diamond,30.0,42.9955556,-71.4552778
8/8/2006,vancouver (canada),bc,ca,light,2.0,49.25,-123.133333
8/8/2009,buena vista,co,us,light,900.0,38.8422222,-106.1305556
8/8/2011,commerce city,co,us,light,60.0,39.8083333,-104.9333333
8/8/2012,myrtle beach,sc,us,sphere,30.0,33.6888889,-78.8869444
8/8/2013,belmont,nh,us,unknown,240.0,43.4452778,-71.4783333
8/9/2000,houston county,tn,us,sphere,60.0,35.2413889,-87.9177778
8/9/2004,sacramento,ca,us,light,600.0,38.5816667,-121.4933333
8/9/2007,mcallen,tx,us,sphere,600.0,26.2030556,-98.2297222
8/9/2010,new york city (central park),ny,us,circle,30.0,40.7141667,-74.0063889
8/9/2013,battle ground,wa,us,fireball,300.0,45.7811111,-122.5322222
9/10/1976,albany,ny,us,circle,120.0,42.6525,-73.7566667
9/10/1999,pollock pines,ca,us,light,1200.0,38.7613889,-120.5855556
9/10/2003,valley springs,ca,us,circle,120.0,38.1916667,-120.8280556
9/10/2004,mount cobb,pa,us,unknown,900.0,41.4133333,-75.4936111
9/10/2007,loveland,co,us,triangle,35.0,40.3977778,-105.0744444
9/10/2010,bend,or,us,triangle,300.0,44.0583333,-121.3141667
9/10/2011,landers,ca,us,circle,2.0,34.2661111,-116.3922222
9/10/2012,lebanon,pa,us,sphere,10.0,40.3408333,-76.4116667
9/11/1999,vernal,ut,us,chevron,360.0,40.4555556,-109.5280556
9/11/2001,albuquerque,nm,us,sphere,600.0,35.0844444,-106.6505556
9/11/2003,mandeville,la,us,triangle,1200.0,30.3580556,-90.0655556
9/11/2005,chapel hill,nc,us,unknown,310.0,35.9130556,-79.0561111
9/11/2009,mesa,az,us,light,1800.0,33.4222222,-111.8219444
9/11/2011,wasilla,ak,us,triangle,2.0,61.5813889,-149.4394444
9/11/2012,newport,mi,us,fireball,2700.0,42.0022222,-83.3086111
9/1/1962,seattle,wa,us,circle,180.0,47.6063889,-122.3308333
9/1/1976,ahwahnee,ca,us,fireball,120.0,37.3655556,-119.7252778
9/1/1981,port jervis,ny,us,triangle,1200.0,41.375,-74.6930556
9/1/1991,st. louis,mo,us,rectangle,180.0,38.6272222,-90.1977778
9/1/1998,jonesville,il,us,cigar,600.0,41.3113889,-89.0713889
9/1/1999,eugene,or,us,light,5.0,44.0522222,-123.0855556
9/1/2001,crete,il,us,oval,120.0,41.4444444,-87.6313889
9/1/2003,springfield,va,us,teardrop,120.0,38.7891667,-77.1875
9/1/2005,jefferson city,tn,us,light,25.0,36.1222222,-83.4925
9/1/2007,crestone,co,us,triangle,1800.0,37.9963889,-105.6991667
9/1/2009,omaha,ne,us,sphere,240.0,41.2586111,-95.9375
9/1/2011,aurora,co,us,cylinder,120.0,39.7294444,-104.8313889
9/1/2012,grove city,pa,us,light,300.0,41.1577778,-80.0888889
9/1/2013,salt lake city,ut,us,sphere,1800.0,40.7608333,-111.8902778
9/12/1982,mason city,ia,us,sphere,60.0,43.1536111,-93.2008333
9/12/2001,los angeles,ca,us,circle,60.0,34.0522222,-118.2427778
9/12/2003,beach city,tx,us,light,420.0,29.6619444,-94.8897222
9/12/2005,tucson,az,us,other,1200.0,32.2216667,-110.9258333
9/12/2009,miamisburg,oh,us,triangle,600.0,39.6427778,-84.2866667
9/12/2011,la porte,tx,us,circle,300.0,29.6655556,-95.0191667
9/12/2012,murrells inlet,sc,us,circle,15.0,33.5508333,-79.0416667
9/13/1998,weed,ca,us,fireball,8.0,41.4227778,-122.385
9/13/2001,tulsa,ok,us,unknown,240.0,36.1538889,-95.9925
9/13/2004,south phoenix,az,us,light,900.0,33.4066667,-112.0727778
9/13/2007,loveland,oh,us,fireball,180.0,39.2688889,-84.2638889
9/13/2010,quakertown,pa,us,light,300.0,40.4416667,-75.3419444
9/13/2013,owensboro,ky,us,fireball,15.0,37.7741667,-87.1133333
9/14/1996,battle mountain,nv,us,disk,300.0,40.6422222,-116.9333333
9/14/2002,jacksonville beach,fl,us,triangle,30.0,30.2944444,-81.3933333
9/14/2005,shoreview,mn,us,sphere,40.0,45.0791667,-93.1469444
9/14/2008,san juan capistrano,ca,us,circle,300.0,33.5016667,-117.6616667
9/14/2010,concord,ca,us,cylinder,2100.0,37.9780556,-122.03
9/14/2012,ponca,ne,us,cylinder,6.0,42.5625,-96.7052778
9/14/2013,grosse ile,mi,us,fireball,120.0,42.1291667,-83.1444444
9/15/1961,wahoo,ne,us,egg,300.0,41.2113889,-96.62
9/15/1972,tupelo,ms,us,oval,180.0,34.2575,-88.7033333
9/15/1978,shelby,oh,us,triangle,600.0,40.8813889,-82.6619444
9/15/1987,liverpool,ny,us,cigar,3.0,43.1063889,-76.2180556
9/15/1995,wyoming,pa,us,unknown,600.0,41.3116667,-75.8377778
9/15/1998,gladwin,mi,us,unknown,3600.0,43.9808333,-84.4863889
9/15/2000,belfield,nd,us,disk,900.0,46.8852778,-103.1991667
9/15/2002,rockford,il,us,disk,120.0,42.2711111,-89.0938889
9/15/2003,trenton,oh,us,fireball,0.7,39.4808333,-84.4577778
9/15/2005,laconia,nh,us,light,600.0,43.5277778,-71.4708333
9/15/2007,springfield,mo,us,triangle,7200.0,37.2152778,-93.2980556
9/15/2009,loleta,ca,us,light,1200.0,40.6411111,-124.2241667
9/15/2012,ft. myers,fl,us,changing,1200.0,26.6402778,-81.8725
9/15/2012,chicago,il,us,light,300.0,41.85,-87.65
9/16/1998,san diego (point loma/ocean beach area),ca,us,light,900.0,32.7152778,-117.1563889
9/16/2002,brea,ca,us,disk,2.0,33.9166667,-117.8991667
9/16/2005,maypearl,tx,us,unknown,1440.0,32.3130556,-97.0113889
9/16/2008,ingleside,il,us,teardrop,300.0,42.3811111,-88.1397222
9/16/2012,wildomar,ca,us,circle,3.0,33.5988889,-117.2791667
9/17/1994,elizabeth,nj,us,disk,180.0,40.6638889,-74.2111111
9/17/2002,chowchilla,ca,us,unknown,8.0,37.1230556,-120.2591667
9/17/2005,griffin,ga,us,light,2700.0,33.2466667,-84.2641667
9/17/2007,oroville,ca,us,triangle,30.0,39.5138889,-121.5552778
9/17/2009,oshawa (canada),on,ca,flash,12.0,43.9,-78.866667
9/17/2011,bartlett,il,us,disk,180.0,41.995,-88.1855556
9/17/2012,sumter,sc,us,light,240.0,33.9202778,-80.3416667
9/18/1999,john day (clyde holliday camp ground&#44 7 miles west of),or,us,light,1200.0,44.4161111,-118.9519444
9/18/2003,kamloops (canada),bc,ca,sphere,60.0,50.666667,-120.333333
9/18/2005,plantation,fl,us,light,300.0,26.1272222,-80.2333333
9/18/2009,boise,id,us,light,1200.0,43.6136111,-116.2025
9/18/2011,la barge,wy,us,circle,900.0,42.2619444,-110.1938889
9/18/2013,boise,id,us,formation,35.0,43.6136111,-116.2025
9/19/2000,houston,tx,us,sphere,1800.0,29.7630556,-95.3630556
9/19/2002,rancho santa margarita,ca,us,unknown,15.0,33.6408333,-117.6022222
9/19/2003,hutchinson,ks,us,triangle,20.0,38.0608333,-97.9294444
9/19/2007,ireland,in,us,cylinder,20.0,38.4147222,-86.9994444
9/19/2009,hanover,pa,us,light,60.0,39.8005556,-76.9833333
9/19/2009,glens falls,ny,us,circle,40.0,43.3094444,-73.6444444
9/19/2009,neptune city,nj,us,light,15.0,40.2,-74.0283333
9/19/2009,lancaster,pa,us,light,15.0,40.0377778,-76.3058333
9/19/2012,pittsburgh,pa,us,circle,300.0,40.4405556,-79.9961111
9/20/1973,mansfield,oh,us,oval,6.0,40.7583333,-82.5155556
9/20/1995,wilberforce,oh,us,oval,309.0,39.7161111,-83.8777778
9/20/2002,danville,ca,us,disk,120.0,37.8216667,-121.9988889
9/20/2005,belfair,wa,us,circle,300.0,47.4508333,-122.8261111
9/20/2007,mount sterling,ky,us,rectangle,120.0,38.0563889,-83.9433333
9/20/2009,mahanoy city,pa,us,light,3.0,40.8125,-76.1419444
9/20/2011,sioux falls,sd,us,light,393.0,43.55,-96.7
9/20/2013,calgary (canada),ab,ca,other,300.0,51.083333,-114.083333
9/21/1999,hamilton,mt,us,disk,300.0,46.2469444,-114.1594444
9/21/2003,san francisco,ca,us,other,600.0,37.775,-122.4183333
9/21/2005,winnisquam,nh,us,light,300.0,43.5013889,-71.5125
9/21/2007,west chester,oh,us,triangle,180.0,39.0875,-81.9227778
9/21/2010,cicero,ny,us,circle,1.0,43.1755556,-76.1197222
9/21/2012,sharpsville,pa,us,circle,1200.0,41.2591667,-80.4722222
9/21/2013,medina,oh,us,fireball,600.0,41.1383333,-81.8638889
9/2/1998,schaumburg,il,us,oval,30.0,42.0333333,-88.0833333
9/2/2003,edmonds,wa,us,light,600.0,47.8108333,-122.3761111
9/2/2005,lisbon,oh,us,cigar,180.0,40.7719444,-80.7683333
9/2/2007,modesto (on i-5; 130 miles south of sacramento),ca,us,triangle,40.0,37.6391667,-120.9958333
9/2/2009,winnipeg (canada),mb,ca,triangle,7200.0,49.883333,-97.166667
9/2/2011,san antonio,tx,us,triangle,10.0,29.4238889,-98.4933333
9/2/2012,white rock (canada),bc,ca,other,7200.0,49.033333,-122.816667
9/22/1986,fredericksburg,va,us,triangle,180.0,38.3030556,-77.4608333
9/22/2000,tacoma (northeast),wa,us,disk,5.0,47.2530556,-122.4430556
9/22/2004,memphis,tx,us,sphere,1800.0,34.7247222,-100.5336111
9/22/2005,yorba linda,ca,us,triangle,120.0,33.8886111,-117.8122222
9/22/2007,toledo,oh,us,triangle,10800.0,41.6638889,-83.5552778
9/22/2010,lakewood,il,us,oval,240.0,41.9166667,-88.1975
9/22/2012,mesa,az,us,circle,600.0,33.4222222,-111.8219444
9/22/2013,auburn,me,us,fireball,15.0,44.0977778,-70.2316667
9/23/1997,denison,ia,us,disk,300.0,42.0177778,-95.355
9/23/1998,everett,wa,us,fireball,2.0,47.9791667,-122.2008333
9/23/2002,springfield,mo,us,fireball,2.0,37.2152778,-93.2980556
9/23/2005,vancouver (canada),bc,ca,triangle,10.0,49.25,-123.133333
9/23/2008,lake orion,mi,us,circle,60.0,42.7844444,-83.2397222
9/23/2011,indian rocks beach,fl,us,other,60.0,27.875,-82.8513889
9/23/2013,conway,sc,us,disk,1080.0,33.8358333,-79.0480556
9/24/1998,vancouver (canada),bc,ca,circle,5.0,49.25,-123.133333
9/24/2003,fort lauderdale,fl,us,triangle,120.0,26.1219444,-80.1436111
9/24/2007,corona,ca,us,circle,15.0,33.8752778,-117.5655556
9/24/2011,kimball,wi,us,diamond,540.0,46.4819444,-90.3058333
9/24/2013,virginia beach,va,us,formation,300.0,36.8527778,-75.9783333
9/25/1998,milwaukee (80 miles nw of&#44 6000ft msl),wi,us,oval,20.0,43.0388889,-87.9063889
9/25/2002,fayette,mo,us,disk,2.0,39.1458333,-92.6836111
9/25/2004,st. louis park,mn,us,oval,600.0,44.9483333,-93.3477778
9/25/2007,wilmington,nc,us,light,60.0,34.2255556,-77.945
9/25/2010,cedar rapids,ia,us,circle,180.0,42.0083333,-91.6438889
9/25/2011,ft. smith,ar,us,light,10.0,35.3858333,-94.3983333
9/25/2013,olathe,ks,us,light,1800.0,38.8813889,-94.8188889
9/26/2000,ankeny,ia,us,triangle,60.0,41.7297222,-93.6055556
9/26/2004,englewood,co,us,sphere,1200.0,39.6477778,-104.9872222
9/26/2007,aloha,or,us,diamond,300.0,45.4944444,-122.8658333
9/26/2010,sayville,ny,us,other,20.0,40.7358333,-73.0825
9/26/2012,middlebury,in,us,light,120.0,41.6752778,-85.7061111
9/26/2013,franksville,wi,us,fireball,180.0,42.76,-87.9133333
9/27/2001,tallahassee,fl,us,triangle,60.0,30.4380556,-84.2808333
9/27/2006,torrance,ca,us,oval,60.0,33.8358333,-118.3397222
9/27/2009,key west,fl,us,oval,5.0,24.5552778,-81.7827778
9/27/2012,bellingham,wa,us,sphere,300.0,48.7597222,-122.4869444
9/27/2013,fairborn,oh,us,flash,180.0,39.8208333,-84.0194444
9/28/2002,seattle,wa,us,fireball,120.0,47.6063889,-122.3308333
9/28/2004,davenport,fl,us,disk,20.0,28.1611111,-81.6019444
9/28/2008,new columbia,pa,us,circle,60.0,41.0408333,-76.8672222
9/28/2010,san francisco,ca,us,light,300.0,37.775,-122.4183333
9/28/2012,los angeles,ca,us,unknown,300.0,34.0522222,-118.2427778
9/28/2013,athens,ga,us,circle,300.0,33.9608333,-83.3780556
9/28/2013,osprey,fl,us,chevron,30.0,27.1958333,-82.4905556
9/29/2001,las vegas,nv,us,other,1200.0,36.175,-115.1363889
9/29/2005,spring valley,ca,us,egg,10.0,32.7447222,-116.9980556
9/29/2008,okmulgee,ok,us,light,60.0,35.6233333,-95.9602778
9/29/2011,memphis,tn,us,light,420.0,35.1494444,-90.0488889
9/29/2012,erie,pa,us,fireball,600.0,42.1291667,-80.0852778
9/30/1966,huntington,wv,us,circle,60.0,38.4191667,-82.4452778
9/30/2000,canoga park,ca,us,sphere,300.0,34.2011111,-118.5972222
9/30/2003,yukon,ok,us,disk,40.0,35.5066667,-97.7622222
9/30/2005,ventura,ca,us,sphere,8.0,34.2783333,-119.2922222
9/30/2005,tinley park,il,us,circle,600.0,41.5733333,-87.7844444
9/30/2007,mercersburg,pa,us,unknown,240.0,39.8277778,-77.9036111
9/30/2010,terrebonne (rural area),mn,us,light,3600.0,47.8325,-96.1330556
9/30/2012,honokowai,hi,us,cone,18000.0,20.9541667,-156.6897222
9/3/1999,san jose,ca,us,other,2.0,37.3394444,-121.8938889
9/3/2003,arlington,tx,us,light,105.0,32.7355556,-97.1077778
9/3/2006,mount olive,nc,us,sphere,30.0,35.1963889,-78.0666667
9/3/2009,healy,ak,us,light,3600.0,63.8569444,-148.9661111
9/3/2011,katy,tx,us,rectangle,3000.0,29.7855556,-95.8241667
9/3/2012,marlboro,ma,us,fireball,600.0,42.7166667,-70.9736111
9/4/1999,indianapolis,in,us,cylinder,300.0,39.7683333,-86.1580556
9/4/2003,mariposa,ca,us,fireball,2.0,37.485,-119.9652778
9/4/2005,boonville,nc,us,cigar,10800.0,36.2325,-80.7083333
9/4/2009,seven hills,oh,us,fireball,60.0,41.3952778,-81.6763889
9/4/2011,carrollton,tx,us,unknown,120.0,32.9536111,-96.89
9/4/2013,clarksville,ar,us,flash,1.0,35.4713889,-93.4663889
9/5/1998,charleston,sc,us,fireball,5.0,32.7763889,-79.9311111
9/5/2002,madison,wi,us,other,600.0,43.0730556,-89.4011111
9/5/2006,mar vista (west los angeles),ca,us,light,20.0,34.0047222,-118.43
9/5/2009,aurora,co,us,unknown,120.0,39.7294444,-104.8313889
9/5/2011,miami,fl,us,circle,20.0,25.7738889,-80.1938889
9/5/2013,bellingham,ma,us,circle,25.0,42.0866667,-71.475
9/6/1999,minneapolis,mn,us,unknown,2.0,44.98,-93.2636111
9/6/2002,fraser,co,us,triangle,60.0,39.945,-105.8166667
9/6/2005,morgan hill,ca,us,light,60.0,37.1305556,-121.6533333
9/6/2008,quincy,mi,us,formation,240.0,41.9441667,-84.8838889
9/6/2012,cogar,ok,us,circle,180.0,35.3338889,-98.1302778
9/7/1981,solomon,ks,us,other,120.0,38.9194444,-97.3708333
9/7/2000,syracuse,ny,us,triangle,300.0,43.0480556,-76.1477778
9/7/2003,cypress,tx,us,circle,1.5,29.9688889,-95.6969444
9/7/2007,doyline,la,us,triangle,20.0,32.5355556,-93.4108333
9/7/2010,chelmsford,ma,us,light,600.0,42.5997222,-71.3677778
9/7/2013,tomball,tx,us,disk,30.0,30.0969444,-95.6158333
9/8/1999,prairie view,il,us,light,5.0,42.1991667,-87.9555556
9/8/2002,granby,ct,us,oval,300.0,41.9538889,-72.7891667
9/8/2006,hampton,nh,us,light,300.0,42.9375,-70.8394444
9/8/2009,santa clara,ca,us,sphere,20.0,37.3541667,-121.9541667
9/8/2011,north wilkesboro,nc,us,light,3.0,36.1583333,-81.1477778
9/8/2012,wichita,ks,us,cylinder,30.0,37.6922222,-97.3372222
9/9/1968,tracy,ca,us,unknown,1200.0,37.7397222,-121.4241667
9/9/2001,detroit,mi,us,disk,300.0,42.3313889,-83.0458333
9/9/2003,tallahassee,fl,us,other,900.0,30.4380556,-84.2808333
9/9/2007,antelope,ca,us,other,900.0,38.7083333,-121.3288889
9/9/2009,colebrook,nh,us,other,120.0,44.8944444,-71.4963889
9/9/2011,chula vista,ca,us,light,480.0,32.64,-117.0833333
9/9/2013,struthers,oh,us,unknown,120.0,41.0525,-80.6080556
'''
with open("ufo_rep.txt","w") as f : f.write(ufo_txt)





def flight_time(flight_id):
    flights = {'PC7079': '10:00', 'TK5767': '10:30', 'PC3024': '11:30', 'TK1202': '11:45', 'TK5936': '12:15', 'TK4793': '13:20', 'TK5610': '14:00', 'TK2988': '14:15', 'PC2410': '14:32', 'TK9571': '14:50', 'TK5759': '15:00', 'PC6360': '12:00', 'PC5834': '13:00', 'TK7161': '16:30', 'TK9699': '17:10', 'TK6221': '20:00', 'TK5836': '19:00', 'PC1603': '18:00', 'PC8987': '19:10', 'TK9880': '11:11', 'TK5644': '13:26', 'PC3272': '20:20', 'PC1662': '10:10', 'PC6640': '11:30', 'PC6323': '12:00', 'PC3690': '12:35', 'TK4399': '13:00', 'TK4147': '14:00', 'TK4373': '15:00', 'PC1030': '16:10', 'PC7288': '17:30', 'PC9163': '18:18', 'PC1465': '19:25', 'PC1076': '20:00', 'PC4685': '22:00', 'TK4354': '22:30', 'PC2605': '23:05', 'TK1988': '23:30', 'PC3475': '09:00', 'TK3016': '09:20', 'PC1097': '10:00', 'PC4720': '10:30', 'TK9736': '10:14', 'TK5844': '11:00', 'TK4665': '12:00', 'PC2272': '12:15', 'PC2641': '13:00', 'TK7746': '14:00', 'TK8316': '17:00', 'PC2344': '17:18', 'PC2349': '17:51', 'PC7984': '18:30', 'TK3738': '19:00', 'PC9135': '20:00', 'PC5474': '20:30', 'TK3852': '21:21', 'TK5299': '22:15', 'PC3178': '08:00', 'TK4406': '07:00', 'PC5702': '06:13', 'TK5686': '09:09', 'PC9783': '10:16', 'PC1984': '13:01', 'TK3359': '14:17', 'PC7795': '13:12', 'TK3561': '14:29', 'PC2421': '15:00', 'PC1670': '17:00', 'TK9415': '13:00', 'PC6433': '14:02', 'PC8684': '20:00', 'PC9461': '21:19', 'PC5297': '16:13', 'PC4163': '13:16', 'PC4931': '18:19', 'TK5055': '23:45', 'TK8274': '19:20', 'TK5451': '00:00'}
    return flights[flight_id]

sample_20201_txt = '''
PC7079,Amasya,Giresun
TK5767,Samsun,Denizli
PC3024,Giresun,Erzincan
PC6323,Antalya,Ankara
TK4399,Antalya,Ankara
PC3690,Antalya,Ankara
TK3852,Ankara,Antalya
TK5299,Ankara,Antalya
PC5155,Ankara,Antalya
TK3561,Ankara,Malatya
TK9215,Antalya,Samsun
PC2421,Giresun,Erzincan
'''

def custom_sort(lst):
    return sorted(lst, key=lambda x:x[1], reverse=True)

with open("sample_20201.txt","w") as f : f.write(sample_20201_txt)

sample_txt = '''113596,CHE,20.25,65.75,10
131832,METE,50.25,80.25,15.75
126310,CENG,35,0.25,45.25
112020,CENG,90.25,75,55.25
170088,CHE,5,40.75,70
137843,CENG,35,5.25,0.75
153543,CHE,100,70.25,65.25
131745,CENG,10.25,15,35.25
195579,CENG,65.5,15.75,75.75
132426,CHE,35,10.25,35.75
'''

with open("sample.txt","w") as f : f.write(sample_txt)

    
