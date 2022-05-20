import random

import os
os.remove("data.csv")
os.remove("data.txt")
os.remove("data2.csv")


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

data_csv = '''
Series_Title|Released_Year|Genre|IMDB_Rating|Director|Star1|Star2
The Shawshank Redemption|1994|Drama|9.3|Frank Darabont|Tim Robbins|Morgan Freeman
The Godfather|1972|Crime,Drama|9.2|Francis Ford Coppola|Marlon Brando|Al Pacino
The Dark Knight|2008|Action,Crime,Drama|9.0|Christopher Nolan|Christian Bale|Heath Ledger
The Godfather: Part II|1974|Crime,Drama|9.0|Francis Ford Coppola|Al Pacino|Robert De Niro
12 Angry Men|1957|Crime,Drama|9.0|Sidney Lumet|Henry Fonda|Lee J. Cobb
The Lord of the Rings: The Return of the King|2003|Action,Adventure,Drama|8.9|Peter Jackson|Elijah Wood|Viggo Mortensen
Pulp Fiction|1994|Crime,Drama|8.9|Quentin Tarantino|John Travolta|Uma Thurman
Schindler's List|1993|Biography,Drama,History|8.9|Steven Spielberg|Liam Neeson|Ralph Fiennes
Inception|2010|Action,Adventure,Sci-Fi|8.8|Christopher Nolan|Leonardo DiCaprio|Joseph Gordon-Levitt
Fight Club|1999|Drama|8.8|David Fincher|Brad Pitt|Edward Norton
The Lord of the Rings: The Fellowship of the Ring|2001|Action,Adventure,Drama|8.8|Peter Jackson|Elijah Wood|Ian McKellen
Forrest Gump|1994|Drama,Romance|8.8|Robert Zemeckis|Tom Hanks|Robin Wright
Il buono, il brutto, il cattivo|1966|Western|8.8|Sergio Leone|Clint Eastwood|Eli Wallach
The Lord of the Rings: The Two Towers|2002|Action,Adventure,Drama|8.7|Peter Jackson|Elijah Wood|Ian McKellen
The Matrix|1999|Action,Sci-Fi|8.7|Lana Wachowski|Lilly Wachowski|Keanu Reeves
Goodfellas|1990|Biography,Crime,Drama|8.7|Martin Scorsese|Robert De Niro|Ray Liotta
Star Wars: Episode V - The Empire Strikes Back|1980|Action,Adventure,Fantasy|8.7|Irvin Kershner|Mark Hamill|Harrison Ford
One Flew Over the Cuckoo's Nest|1975|Drama|8.7|Milos Forman|Jack Nicholson|Louise Fletcher
Hamilton|2020|Biography,Drama,History|8.6|Thomas Kail|Lin-Manuel Miranda|Phillipa Soo
Gisaengchung|2019|Comedy,Drama,Thriller|8.6|Bong Joon Ho|Kang-ho Song|Lee Sun-kyun
Soorarai Pottru|2020|Drama|8.6|Sudha Kongara|Suriya|Madhavan
Interstellar|2014|Adventure,Drama,Sci-Fi|8.6|Christopher Nolan|Matthew McConaughey|Anne Hathaway
Cidade de Deus|2002|Crime,Drama|8.6|Fernando Meirelles|Kátia Lund|Alexandre Rodrigues
Sen to Chihiro no kamikakushi|2001|Animation,Adventure,Family|8.6|Hayao Miyazaki|Daveigh Chase|Suzanne Pleshette
Saving Private Ryan|1998|Drama,War|8.6|Steven Spielberg|Tom Hanks|Matt Damon
The Green Mile|1999|Crime,Drama,Fantasy|8.6|Frank Darabont|Tom Hanks|Michael Clarke Duncan
La vita è bella|1997|Comedy,Drama,Romance|8.6|Roberto Benigni|Roberto Benigni|Nicoletta Braschi
Se7en|1995|Crime,Drama,Mystery|8.6|David Fincher|Morgan Freeman|Brad Pitt
The Silence of the Lambs|1991|Crime,Drama,Thriller|8.6|Jonathan Demme|Jodie Foster|Anthony Hopkins
Star Wars|1977|Action,Adventure,Fantasy|8.6|George Lucas|Mark Hamill|Harrison Ford
Seppuku|1962|Action,Drama,Mystery|8.6|Masaki Kobayashi|Tatsuya Nakadai|Akira Ishihama
Shichinin no samurai|1954|Action,Adventure,Drama|8.6|Akira Kurosawa|Toshirô Mifune|Takashi Shimura
It's a Wonderful Life|1946|Drama,Family,Fantasy|8.6|Frank Capra|James Stewart|Donna Reed
Joker|2019|Crime,Drama,Thriller|8.5|Todd Phillips|Joaquin Phoenix|Robert De Niro
Whiplash|2014|Drama,Music|8.5|Damien Chazelle|Miles Teller|J.K. Simmons
The Intouchables|2011|Biography,Comedy,Drama|8.5|Olivier Nakache|Éric Toledano|François Cluzet
The Prestige|2006|Drama,Mystery,Sci-Fi|8.5|Christopher Nolan|Christian Bale|Hugh Jackman
The Departed|2006|Crime,Drama,Thriller|8.5|Martin Scorsese|Leonardo DiCaprio|Matt Damon
The Pianist|2002|Biography,Drama,Music|8.5|Roman Polanski|Adrien Brody|Thomas Kretschmann
Gladiator|2000|Action,Adventure,Drama|8.5|Ridley Scott|Russell Crowe|Joaquin Phoenix
American History X|1998|Drama|8.5|Tony Kaye|Edward Norton|Edward Furlong
The Usual Suspects|1995|Crime,Mystery,Thriller|8.5|Bryan Singer|Kevin Spacey|Gabriel Byrne
Léon|1994|Action,Crime,Drama|8.5|Luc Besson|Jean Reno|Gary Oldman
The Lion King|1994|Animation,Adventure,Drama|8.5|Roger Allers|Rob Minkoff|Matthew Broderick
Terminator 2: Judgment Day|1991|Action,Sci-Fi|8.5|James Cameron|Arnold Schwarzenegger|Linda Hamilton
Nuovo Cinema Paradiso|1988|Drama,Romance|8.5|Giuseppe Tornatore|Philippe Noiret|Enzo Cannavale
Hotaru no haka|1988|Animation,Drama,War|8.5|Isao Takahata|Tsutomu Tatsumi|Ayano Shiraishi
Back to the Future|1985|Adventure,Comedy,Sci-Fi|8.5|Robert Zemeckis|Michael J. Fox|Christopher Lloyd
Once Upon a Time in the West|1968|Western|8.5|Sergio Leone|Henry Fonda|Charles Bronson
Psycho|1960|Horror,Mystery,Thriller|8.5|Alfred Hitchcock|Anthony Perkins|Janet Leigh
Casablanca|1942|Drama,Romance,War|8.5|Michael Curtiz|Humphrey Bogart|Ingrid Bergman
Modern Times|1936|Comedy,Drama,Family|8.5|Charles Chaplin|Charles Chaplin|Paulette Goddard
City Lights|1931|Comedy,Drama,Romance|8.5|Charles Chaplin|Charles Chaplin|Virginia Cherrill
Capharnaüm|2018|Drama|8.4|Nadine Labaki|Zain Al Rafeea|Yordanos Shiferaw
Ayla: The Daughter of War|2017|Biography,Drama,History|8.4|Can Ulkay|Erdem Can|Çetin Tekindor
Vikram Vedha|2017|Action,Crime,Drama|8.4|Gayatri|Pushkar|Madhavan
Kimi no na wa.|2016|Animation,Drama,Fantasy|8.4|Makoto Shinkai|Ryûnosuke Kamiki|Mone Kamishiraishi
Dangal|2016|Action,Biography,Drama|8.4|Nitesh Tiwari|Aamir Khan|Sakshi Tanwar
Spider-Man: Into the Spider-Verse|2018|Animation,Action,Adventure|8.4|Bob Persichetti|Peter Ramsey|Rodney Rothman
Avengers: Endgame|2019|Action,Adventure,Drama|8.4|Anthony Russo|Joe Russo|Robert Downey Jr.
Avengers: Infinity War|2018|Action,Adventure,Sci-Fi|8.4|Anthony Russo|Joe Russo|Robert Downey Jr.
Coco|2017|Animation,Adventure,Family|8.4|Lee Unkrich|Adrian Molina|Anthony Gonzalez
Django Unchained|2012|Drama,Western|8.4|Quentin Tarantino|Jamie Foxx|Christoph Waltz
The Dark Knight Rises|2012|Action,Adventure|8.4|Christopher Nolan|Christian Bale|Tom Hardy
3 Idiots|2009|Comedy,Drama|8.4|Rajkumar Hirani|Aamir Khan|Madhavan
Taare Zameen Par|2007|Drama,Family|8.4|Aamir Khan|Amole Gupte|Darsheel Safary
WALL·E|2008|Animation,Adventure,Family|8.4|Andrew Stanton|Ben Burtt|Elissa Knight
The Lives of Others|2006|Drama,Mystery,Thriller|8.4|Florian Henckel von Donnersmarck|Ulrich Mühe|Martina Gedeck
Oldeuboi|2003|Action,Drama,Mystery|8.4|Chan-wook Park|Choi Min-sik|Yoo Ji-Tae
Memento|2000|Mystery,Thriller|8.4|Christopher Nolan|Guy Pearce|Carrie-Anne Moss
Mononoke-hime|1997|Animation,Action,Adventure|8.4|Hayao Miyazaki|Yôji Matsuda|Yuriko Ishida
Once Upon a Time in America|1984|Crime,Drama|8.4|Sergio Leone|Robert De Niro|James Woods
Raiders of the Lost Ark|1981|Action,Adventure|8.4|Steven Spielberg|Harrison Ford|Karen Allen
The Shining|1980|Drama,Horror|8.4|Stanley Kubrick|Jack Nicholson|Shelley Duvall
Apocalypse Now|1979|Drama,Mystery,War|8.4|Francis Ford Coppola|Martin Sheen|Marlon Brando
Alien|1979|Horror,Sci-Fi|8.4|Ridley Scott|Sigourney Weaver|Tom Skerritt
Anand|1971|Drama,Musical|8.4|Hrishikesh Mukherjee|Rajesh Khanna|Amitabh Bachchan
Tengoku to jigoku|1963|Crime,Drama,Mystery|8.4|Akira Kurosawa|Toshirô Mifune|Yutaka Sada
Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb|1964|Comedy|8.4|Stanley Kubrick|Peter Sellers|George C. Scott
Witness for the Prosecution|1957|Crime,Drama,Mystery|8.4|Billy Wilder|Tyrone Power|Marlene Dietrich
Paths of Glory|1957|Drama,War|8.4|Stanley Kubrick|Kirk Douglas|Ralph Meeker
Rear Window|1954|Mystery,Thriller|8.4|Alfred Hitchcock|James Stewart|Grace Kelly
Sunset Blvd.|1950|Drama,Film-Noir|8.4|Billy Wilder|William Holden|Gloria Swanson
The Great Dictator|1940|Comedy,Drama,War|8.4|Charles Chaplin|Charles Chaplin|Paulette Goddard
1917|2019|Drama,Thriller,War|8.3|Sam Mendes|Dean-Charles Chapman|George MacKay
Tumbbad|2018|Drama,Fantasy,Horror|8.3|Rahi Anil Barve|Anand Gandhi|Adesh Prasad
Andhadhun|2018|Crime,Drama,Music|8.3|Sriram Raghavan|Ayushmann Khurrana|Tabu
Drishyam|2013|Crime,Drama,Thriller|8.3|Jeethu Joseph|Mohanlal|Meena
Jagten|2012|Drama|8.3|Thomas Vinterberg|Mads Mikkelsen|Thomas Bo Larsen
Jodaeiye Nader az Simin|2011|Drama|8.3|Asghar Farhadi|Payman Maadi|Leila Hatami
Incendies|2010|Drama,Mystery,War|8.3|Denis Villeneuve|Lubna Azabal|Mélissa Désormeaux-Poulin
Miracle in cell NO.7|2019|Drama|8.3|Mehmet Ada Öztekin|Aras Bulut Iynemli|Nisa Sofiya Aksongur
Babam ve Oglum|2005|Drama,Family|8.3|Çagan Irmak|Çetin Tekindor|Fikret Kuskan
Inglourious Basterds|2009|Adventure,Drama,War|8.3|Quentin Tarantino|Brad Pitt|Diane Kruger
Eternal Sunshine of the Spotless Mind|2004|Drama,Romance,Sci-Fi|8.3|Michel Gondry|Jim Carrey|Kate Winslet
Amélie|2001|Comedy,Romance|8.3|Jean-Pierre Jeunet|Audrey Tautou|Mathieu Kassovitz
Snatch|2000|Comedy,Crime|8.3|Guy Ritchie|Jason Statham|Brad Pitt
Requiem for a Dream|2000|Drama|8.3|Darren Aronofsky|Ellen Burstyn|Jared Leto
American Beauty|1999|Drama|8.3|Sam Mendes|Kevin Spacey|Annette Bening
Good Will Hunting|1997|Drama,Romance|8.3|Gus Van Sant|Robin Williams|Matt Damon
Bacheha-Ye aseman|1997|Drama,Family,Sport|8.3|Majid Majidi|Mohammad Amir Naji|Amir Farrokh Hashemian
Toy Story|1995|Animation,Adventure,Comedy|8.3|John Lasseter|Tom Hanks|Tim Allen
Braveheart|1995|Biography,Drama,History|8.3|Mel Gibson|Mel Gibson|Sophie Marceau
Reservoir Dogs|1992|Crime,Drama,Thriller|8.3|Quentin Tarantino|Harvey Keitel|Tim Roth
Full Metal Jacket|1987|Drama,War|8.3|Stanley Kubrick|Matthew Modine|R. Lee Ermey
Idi i smotri|1985|Drama,Thriller,War|8.3|Elem Klimov|Aleksey Kravchenko|Olga Mironova
Aliens|1986|Action,Adventure,Sci-Fi|8.3|James Cameron|Sigourney Weaver|Michael Biehn
Amadeus|1984|Biography,Drama,History|8.3|Milos Forman|F. Murray Abraham|Tom Hulce
Scarface|1983|Crime,Drama|8.3|Brian De Palma|Al Pacino|Michelle Pfeiffer
Star Wars: Episode VI - Return of the Jedi|1983|Action,Adventure,Fantasy|8.3|Richard Marquand|Mark Hamill|Harrison Ford
Das Boot|1981|Adventure,Drama,Thriller|8.3|Wolfgang Petersen|Jürgen Prochnow|Herbert Grönemeyer
Taxi Driver|1976|Crime,Drama|8.3|Martin Scorsese|Robert De Niro|Jodie Foster
The Sting|1973|Comedy,Crime,Drama|8.3|George Roy Hill|Paul Newman|Robert Redford
A Clockwork Orange|1971|Crime,Drama,Sci-Fi|8.3|Stanley Kubrick|Malcolm McDowell|Patrick Magee
2001: A Space Odyssey|1968|Adventure,Sci-Fi|8.3|Stanley Kubrick|Keir Dullea|Gary Lockwood
Per qualche dollaro in più|1965|Western|8.3|Sergio Leone|Clint Eastwood|Lee Van Cleef
Lawrence of Arabia|1962|Adventure,Biography,Drama|8.3|David Lean|Peter O'Toole|Alec Guinness
The Apartment|1960|Comedy,Drama,Romance|8.3|Billy Wilder|Jack Lemmon|Shirley MacLaine
North by Northwest|1959|Adventure,Mystery,Thriller|8.3|Alfred Hitchcock|Cary Grant|Eva Marie Saint
Vertigo|1958|Mystery,Romance,Thriller|8.3|Alfred Hitchcock|James Stewart|Kim Novak
Singin' in the Rain|1952|Comedy,Musical,Romance|8.3|Stanley Donen|Gene Kelly|Gene Kelly
Ikiru|1952|Drama|8.3|Akira Kurosawa|Takashi Shimura|Nobuo Kaneko
Ladri di biciclette|1948|Drama|8.3|Vittorio De Sica|Lamberto Maggiorani|Enzo Staiola
Double Indemnity|1944|Crime,Drama,Film-Noir|8.3|Billy Wilder|Fred MacMurray|Barbara Stanwyck
Citizen Kane|1941|Drama,Mystery|8.3|Orson Welles|Orson Welles|Joseph Cotten
M - Eine Stadt sucht einen Mörder|1931|Crime,Mystery,Thriller|8.3|Fritz Lang|Peter Lorre|Ellen Widmann
Metropolis|1927|Drama,Sci-Fi|8.3|Fritz Lang|Brigitte Helm|Alfred Abel
The Kid|1921|Comedy,Drama,Family|8.3|Charles Chaplin|Charles Chaplin|Edna Purviance
Chhichhore|2019|Comedy,Drama|8.2|Nitesh Tiwari|Sushant Singh Rajput|Shraddha Kapoor
Uri: The Surgical Strike|2018|Action,Drama,War|8.2|Aditya Dhar|Vicky Kaushal|Paresh Rawal
K.G.F: Chapter 1|2018|Action,Drama|8.2|Prashanth Neel|Yash|Srinidhi Shetty
Green Book|2018|Biography,Comedy,Drama|8.2|Peter Farrelly|Viggo Mortensen|Mahershala Ali
Three Billboards Outside Ebbing, Missouri|2017|Comedy,Crime,Drama|8.2|Martin McDonagh|Frances McDormand|Woody Harrelson
Talvar|2015|Crime,Drama,Mystery|8.2|Meghna Gulzar|Irrfan Khan|Konkona Sen Sharma
Baahubali 2: The Conclusion|2017|Action,Drama|8.2|S.S. Rajamouli|Prabhas|Rana Daggubati
Klaus|2019|Animation,Adventure,Comedy|8.2|Sergio Pablos|Carlos Martínez López|Jason Schwartzman
Drishyam|2015|Crime,Drama,Mystery|8.2|Nishikant Kamat|Ajay Devgn|Shriya Saran
Queen|2013|Adventure,Comedy,Drama|8.2|Vikas Bahl|Kangana Ranaut|Rajkummar Rao
Mandariinid|2013|Drama,War|8.2|Zaza Urushadze|Lembit Ulfsak|Elmo Nüganen
Bhaag Milkha Bhaag|2013|Biography,Drama,Sport|8.2|Rakeysh Omprakash Mehra|Farhan Akhtar|Sonam Kapoor
Gangs of Wasseypur|2012|Action,Comedy,Crime|8.2|Anurag Kashyap|Manoj Bajpayee|Richa Chadha
Udaan|2010|Drama|8.2|Vikramaditya Motwane|Rajat Barmecha|Ronit Roy
Paan Singh Tomar|2012|Action,Biography,Crime|8.2|Tigmanshu Dhulia|Irrfan Khan|Mahie Gill
El secreto de sus ojos|2009|Drama,Mystery,Romance|8.2|Juan José Campanella|Ricardo Darín|Soledad Villamil
Warrior|2011|Action,Drama,Sport|8.2|Gavin O'Connor|Tom Hardy|Nick Nolte
Shutter Island|2010|Mystery,Thriller|8.2|Martin Scorsese|Leonardo DiCaprio|Emily Mortimer
Up|2009|Animation,Adventure,Comedy|8.2|Pete Docter|Bob Peterson|Edward Asner
The Wolf of Wall Street|2013|Biography,Crime,Drama|8.2|Martin Scorsese|Leonardo DiCaprio|Jonah Hill
Chak De! India|2007|Drama,Family,Sport|8.2|Shimit Amin|Shah Rukh Khan|Vidya Malvade
There Will Be Blood|2007|Drama|8.2|Paul Thomas Anderson|Daniel Day-Lewis|Paul Dano
Pan's Labyrinth|2006|Drama,Fantasy,War|8.2|Guillermo del Toro|Ivana Baquero|Ariadna Gil
Toy Story 3|2010|Animation,Adventure,Comedy|8.2|Lee Unkrich|Tom Hanks|Tim Allen
V for Vendetta|2005|Action,Drama,Sci-Fi|8.2|James McTeigue|Hugo Weaving|Natalie Portman
Rang De Basanti|2006|Comedy,Crime,Drama|8.2|Rakeysh Omprakash Mehra|Aamir Khan|Soha Ali Khan
Black|2005|Drama|8.2|Sanjay Leela Bhansali|Amitabh Bachchan|Rani Mukerji
Batman Begins|2005|Action,Adventure|8.2|Christopher Nolan|Christian Bale|Michael Caine
Swades: We, the People|2004|Drama|8.2|Ashutosh Gowariker|Shah Rukh Khan|Gayatri Joshi
Der Untergang|2004|Biography,Drama,History|8.2|Oliver Hirschbiegel|Bruno Ganz|Alexandra Maria Lara
Hauru no ugoku shiro|2004|Animation,Adventure,Family|8.2|Hayao Miyazaki|Chieko Baishô|Takuya Kimura
A Beautiful Mind|2001|Biography,Drama|8.2|Ron Howard|Russell Crowe|Ed Harris
Hera Pheri|2000|Action,Comedy,Crime|8.2|Priyadarshan|Akshay Kumar|Sunil Shetty
Lock, Stock and Two Smoking Barrels|1998|Action,Comedy,Crime|8.2|Guy Ritchie|Jason Flemyng|Dexter Fletcher
L.A. Confidential|1997|Crime,Drama,Mystery|8.2|Curtis Hanson|Kevin Spacey|Russell Crowe
Eskiya|1996|Crime,Drama,Thriller|8.2|Yavuz Turgul|Sener Sen|Ugur Yücel
Heat|1995|Crime,Drama,Thriller|8.2|Michael Mann|Al Pacino|Robert De Niro
Casino|1995|Crime,Drama|8.2|Martin Scorsese|Robert De Niro|Sharon Stone
Andaz Apna Apna|1994|Action,Comedy,Romance|8.2|Rajkumar Santoshi|Aamir Khan|Salman Khan
Unforgiven|1992|Drama,Western|8.2|Clint Eastwood|Clint Eastwood|Gene Hackman
Indiana Jones and the Last Crusade|1989|Action,Adventure|8.2|Steven Spielberg|Harrison Ford|Sean Connery
Dom za vesanje|1988|Comedy,Crime,Drama|8.2|Emir Kusturica|Davor Dujmovic|Bora Todorovic
Tonari no Totoro|1988|Animation,Family,Fantasy|8.2|Hayao Miyazaki|Hitoshi Takagi|Noriko Hidaka
Die Hard|1988|Action,Thriller|8.2|John McTiernan|Bruce Willis|Alan Rickman
Ran|1985|Action,Drama,War|8.2|Akira Kurosawa|Tatsuya Nakadai|Akira Terao
Raging Bull|1980|Biography,Drama,Sport|8.2|Martin Scorsese|Robert De Niro|Cathy Moriarty
Stalker|1979|Drama,Sci-Fi|8.2|Andrei Tarkovsky|Alisa Freyndlikh|Aleksandr Kaydanovskiy
Höstsonaten|1978|Drama,Music|8.2|Ingmar Bergman|Ingrid Bergman|Liv Ullmann
The Message|1976|Biography,Drama,History|8.2|Moustapha Akkad|Anthony Quinn|Irene Papas
Sholay|1975|Action,Adventure,Comedy|8.2|Ramesh Sippy|Sanjeev Kumar|Dharmendra
Monty Python and the Holy Grail|1975|Adventure,Comedy,Fantasy|8.2|Terry Gilliam|Terry Jones|Graham Chapman
The Great Escape|1963|Adventure,Drama,History|8.2|John Sturges|Steve McQueen|James Garner
To Kill a Mockingbird|1962|Crime,Drama|8.2|Robert Mulligan|Gregory Peck|John Megna
Yôjinbô|1961|Action,Drama,Thriller|8.2|Akira Kurosawa|Toshirô Mifune|Eijirô Tôno
Judgment at Nuremberg|1961|Drama,War|8.2|Stanley Kramer|Spencer Tracy|Burt Lancaster
Some Like It Hot|1959|Comedy,Music,Romance|8.2|Billy Wilder|Marilyn Monroe|Tony Curtis
Smultronstället|1957|Drama,Romance|8.2|Ingmar Bergman|Victor Sjöström|Bibi Andersson
Det sjunde inseglet|1957|Drama,Fantasy,History|8.2|Ingmar Bergman|Max von Sydow|Gunnar Björnstrand
Du rififi chez les hommes|1955|Crime,Drama,Thriller|8.2|Jules Dassin|Jean Servais|Carl Möhner
Dial M for Murder|1954|Crime,Thriller|8.2|Alfred Hitchcock|Ray Milland|Grace Kelly
Tôkyô monogatari|1953|Drama|8.2|Yasujirô Ozu|Chishû Ryû|Chieko Higashiyama
Rashômon|1950|Crime,Drama,Mystery|8.2|Akira Kurosawa|Toshirô Mifune|Machiko Kyô
All About Eve|1950|Drama|8.2|Joseph L. Mankiewicz|Bette Davis|Anne Baxter
The Treasure of the Sierra Madre|1948|Adventure,Drama,Western|8.2|John Huston|Humphrey Bogart|Walter Huston
To Be or Not to Be|1942|Comedy,War|8.2|Ernst Lubitsch|Carole Lombard|Jack Benny
The Gold Rush|1925|Adventure,Comedy,Drama|8.2|Charles Chaplin|Charles Chaplin|Mack Swain
Sherlock Jr.|1924|Action,Comedy,Romance|8.2|Buster Keaton|Buster Keaton|Kathryn McGuire
Portrait de la jeune fille en feu|2019|Drama,Romance|8.1|Céline Sciamma|Noémie Merlant|Adèle Haenel
Pink|2016|Drama,Thriller|8.1|Aniruddha Roy Chowdhury|Taapsee Pannu|Amitabh Bachchan
Koe no katachi|2016|Animation,Drama,Family|8.1|Naoko Yamada|Miyu Irino|Saori Hayami
Contratiempo|2016|Crime,Drama,Mystery|8.1|Oriol Paulo|Mario Casas|Ana Wagener
Ah-ga-ssi|2016|Drama,Romance,Thriller|8.1|Chan-wook Park|Kim Min-hee|Jung-woo Ha
Mommy|2014|Drama|8.1|Xavier Dolan|Anne Dorval|Antoine Olivier Pilon
Haider|2014|Action,Crime,Drama|8.1|Vishal Bhardwaj|Shahid Kapoor|Tabu
Logan|2017|Action,Drama,Sci-Fi|8.1|James Mangold|Hugh Jackman|Patrick Stewart
Room|2015|Drama,Thriller|8.1|Lenny Abrahamson|Brie Larson|Jacob Tremblay
Relatos salvajes|2014|Comedy,Drama,Thriller|8.1|Damián Szifron|Darío Grandinetti|María Marull
Soul|2020|Animation,Adventure,Comedy|8.1|Pete Docter|Kemp Powers|Jamie Foxx
Kis Uykusu|2014|Drama|8.1|Nuri Bilge Ceylan|Haluk Bilginer|Melisa Sözen
PK|2014|Comedy,Drama,Musical|8.1|Rajkumar Hirani|Aamir Khan|Anushka Sharma
OMG: Oh My God!|2012|Comedy,Drama,Fantasy|8.1|Umesh Shukla|Paresh Rawal|Akshay Kumar
The Grand Budapest Hotel|2014|Adventure,Comedy,Crime|8.1|Wes Anderson|Ralph Fiennes|F. Murray Abraham
Gone Girl|2014|Drama,Mystery,Thriller|8.1|David Fincher|Ben Affleck|Rosamund Pike
Ôkami kodomo no Ame to Yuki|2012|Animation,Drama,Fantasy|8.1|Mamoru Hosoda|Aoi Miyazaki|Takao Osawa
Hacksaw Ridge|2016|Biography,Drama,History|8.1|Mel Gibson|Andrew Garfield|Sam Worthington
Inside Out|2015|Animation,Adventure,Comedy|8.1|Pete Docter|Ronnie Del Carmen|Amy Poehler
Barfi!|2012|Comedy,Drama,Romance|8.1|Anurag Basu|Ranbir Kapoor|Priyanka Chopra
12 Years a Slave|2013|Biography,Drama,History|8.1|Steve McQueen|Chiwetel Ejiofor|Michael Kenneth Williams
Rush|2013|Action,Biography,Drama|8.1|Ron Howard|Daniel Brühl|Chris Hemsworth
Ford v Ferrari|2019|Action,Biography,Drama|8.1|James Mangold|Matt Damon|Christian Bale
Spotlight|2015|Biography,Crime,Drama|8.1|Tom McCarthy|Mark Ruffalo|Michael Keaton
Song of the Sea|2014|Animation,Adventure,Drama|8.1|Tomm Moore|David Rawle|Brendan Gleeson
Kahaani|2012|Mystery,Thriller|8.1|Sujoy Ghosh|Vidya Balan|Parambrata Chattopadhyay
Zindagi Na Milegi Dobara|2011|Comedy,Drama|8.1|Zoya Akhtar|Hrithik Roshan|Farhan Akhtar
Prisoners|2013|Crime,Drama,Mystery|8.1|Denis Villeneuve|Hugh Jackman|Jake Gyllenhaal
Mad Max: Fury Road|2015|Action,Adventure,Sci-Fi|8.1|George Miller|Tom Hardy|Charlize Theron
A Wednesday|2008|Action,Crime,Drama|8.1|Neeraj Pandey|Anupam Kher|Naseeruddin Shah
Gran Torino|2008|Drama|8.1|Clint Eastwood|Clint Eastwood|Bee Vang
Harry Potter and the Deathly Hallows: Part 2|2011|Adventure,Drama,Fantasy|8.1|David Yates|Daniel Radcliffe|Emma Watson
Okuribito|2008|Drama,Music|8.1|Yôjirô Takita|Masahiro Motoki|Ryôko Hirosue
Hachi: A Dog's Tale|2009|Biography,Drama,Family|8.1|Lasse Hallström|Richard Gere|Joan Allen
Mary and Max|2009|Animation,Comedy,Drama|8.1|Adam Elliot|Toni Collette|Philip Seymour Hoffman
How to Train Your Dragon|2010|Animation,Action,Adventure|8.1|Dean DeBlois|Chris Sanders|Jay Baruchel
Into the Wild|2007|Adventure,Biography,Drama|8.1|Sean Penn|Emile Hirsch|Vince Vaughn
No Country for Old Men|2007|Crime,Drama,Thriller|8.1|Ethan Coen|Joel Coen|Tommy Lee Jones
Lage Raho Munna Bhai|2006|Comedy,Drama,Romance|8.1|Rajkumar Hirani|Sanjay Dutt|Arshad Warsi
Million Dollar Baby|2004|Drama,Sport|8.1|Clint Eastwood|Hilary Swank|Clint Eastwood
Hotel Rwanda|2004|Biography,Drama,History|8.1|Terry George|Don Cheadle|Sophie Okonedo
Taegukgi hwinalrimyeo|2004|Action,Drama,War|8.1|Je-kyu Kang|Jang Dong-Gun|Won Bin
Before Sunset|2004|Drama,Romance|8.1|Richard Linklater|Ethan Hawke|Julie Delpy
Munna Bhai M.B.B.S.|2003|Comedy,Drama,Musical|8.1|Rajkumar Hirani|Sanjay Dutt|Arshad Warsi
Salinui chueok|2003|Crime,Drama,Mystery|8.1|Bong Joon Ho|Kang-ho Song|Kim Sang-kyung
Dil Chahta Hai|2001|Comedy,Drama,Romance|8.1|Farhan Akhtar|Aamir Khan|Saif Ali Khan
Kill Bill: Vol. 1|2003|Action,Crime,Drama|8.1|Quentin Tarantino|Uma Thurman|David Carradine
Finding Nemo|2003|Animation,Adventure,Comedy|8.1|Andrew Stanton|Lee Unkrich|Albert Brooks
Catch Me If You Can|2002|Biography,Crime,Drama|8.1|Steven Spielberg|Leonardo DiCaprio|Tom Hanks
Amores perros|2000|Drama,Thriller|8.1|Alejandro G. Iñárritu|Emilio Echevarría|Gael García Bernal
Monsters, Inc.|2001|Animation,Adventure,Comedy|8.1|Pete Docter|David Silverman|Lee Unkrich
Shin seiki Evangelion Gekijô-ban: Air/Magokoro wo, kimi ni|1997|Animation,Action,Drama|8.1|Hideaki Anno|Kazuya Tsurumaki|Megumi Ogata
Lagaan: Once Upon a Time in India|2001|Adventure,Drama,Musical|8.1|Ashutosh Gowariker|Aamir Khan|Raghuvir Yadav
The Sixth Sense|1999|Drama,Mystery,Thriller|8.1|M. Night Shyamalan|Bruce Willis|Haley Joel Osment
La leggenda del pianista sull'oceano|1998|Drama,Music,Romance|8.1|Giuseppe Tornatore|Tim Roth|Pruitt Taylor Vince
The Truman Show|1998|Comedy,Drama|8.1|Peter Weir|Jim Carrey|Ed Harris
Crna macka, beli macor|1998|Comedy,Crime,Romance|8.1|Emir Kusturica|Bajram Severdzan|Srdjan 'Zika' Todorovic
The Big Lebowski|1998|Comedy,Crime,Sport|8.1|Joel Coen|Ethan Coen|Jeff Bridges
Fa yeung nin wah|2000|Drama,Romance|8.1|Kar-Wai Wong|Tony Chiu-Wai Leung|Maggie Cheung
Trainspotting|1996|Drama|8.1|Danny Boyle|Ewan McGregor|Ewen Bremner
Fargo|1996|Crime,Drama,Thriller|8.1|Joel Coen|Ethan Coen|William H. Macy
Underground|1995|Comedy,Drama,War|8.1|Emir Kusturica|Predrag 'Miki' Manojlovic|Lazar Ristovski
La haine|1995|Crime,Drama|8.1|Mathieu Kassovitz|Vincent Cassel|Hubert Koundé
Dilwale Dulhania Le Jayenge|1995|Drama,Romance|8.1|Aditya Chopra|Shah Rukh Khan|Kajol
Before Sunrise|1995|Drama,Romance|8.1|Richard Linklater|Ethan Hawke|Julie Delpy
Trois couleurs: Rouge|1994|Drama,Mystery,Romance|8.1|Krzysztof Kieslowski|Irène Jacob|Jean-Louis Trintignant
Chung Hing sam lam|1994|Comedy,Crime,Drama|8.1|Kar-Wai Wong|Brigitte Lin|Takeshi Kaneshiro
Jurassic Park|1993|Action,Adventure,Sci-Fi|8.1|Steven Spielberg|Sam Neill|Laura Dern
In the Name of the Father|1993|Biography,Crime,Drama|8.1|Jim Sheridan|Daniel Day-Lewis|Pete Postlethwaite
Ba wang bie ji|1993|Drama,Music,Romance|8.1|Kaige Chen|Leslie Cheung|Fengyi Zhang
Dà hóng denglong gaogao guà|1991|Drama,History,Romance|8.1|Yimou Zhang|Gong Li|Jingwu Ma
Dead Poets Society|1989|Comedy,Drama|8.1|Peter Weir|Robin Williams|Robert Sean Leonard
Stand by Me|1986|Adventure,Drama|8.1|Rob Reiner|Wil Wheaton|River Phoenix
Platoon|1986|Drama,War|8.1|Oliver Stone|Charlie Sheen|Tom Berenger
Paris, Texas|1984|Drama|8.1|Wim Wenders|Harry Dean Stanton|Nastassja Kinski
Kaze no tani no Naushika|1984|Animation,Adventure,Fantasy|8.1|Hayao Miyazaki|Sumi Shimamoto|Mahito Tsujimura
The Thing|1982|Horror,Mystery,Sci-Fi|8.1|John Carpenter|Kurt Russell|Wilford Brimley
Pink Floyd: The Wall|1982|Drama,Fantasy,Music|8.1|Alan Parker|Bob Geldof|Christine Hargreaves
Fitzcarraldo|1982|Adventure,Drama|8.1|Werner Herzog|Klaus Kinski|Claudia Cardinale
Fanny och Alexander|1982|Drama|8.1|Ingmar Bergman|Bertil Guve|Pernilla Allwin
Blade Runner|1982|Action,Sci-Fi,Thriller|8.1|Ridley Scott|Harrison Ford|Rutger Hauer
The Elephant Man|1980|Biography,Drama|8.1|David Lynch|Anthony Hopkins|John Hurt
Life of Brian|1979|Comedy|8.1|Terry Jones|Graham Chapman|John Cleese
The Deer Hunter|1978|Drama,War|8.1|Michael Cimino|Robert De Niro|Christopher Walken
Rocky|1976|Drama,Sport|8.1|John G. Avildsen|Sylvester Stallone|Talia Shire
Network|1976|Drama|8.1|Sidney Lumet|Faye Dunaway|William Holden
Barry Lyndon|1975|Adventure,Drama,History|8.1|Stanley Kubrick|Ryan O'Neal|Marisa Berenson
Zerkalo|1975|Biography,Drama|8.1|Andrei Tarkovsky|Margarita Terekhova|Filipp Yankovskiy
Chinatown|1974|Drama,Mystery,Thriller|8.1|Roman Polanski|Jack Nicholson|Faye Dunaway
Paper Moon|1973|Comedy,Crime,Drama|8.1|Peter Bogdanovich|Ryan O'Neal|Tatum O'Neal
Viskningar och rop|1972|Drama|8.1|Ingmar Bergman|Harriet Andersson|Liv Ullmann
Solaris|1972|Drama,Mystery,Sci-Fi|8.1|Andrei Tarkovsky|Natalya Bondarchuk|Donatas Banionis
Le samouraï|1967|Crime,Drama,Mystery|8.1|Jean-Pierre Melville|Alain Delon|François Périer
Cool Hand Luke|1967|Crime,Drama|8.1|Stuart Rosenberg|Paul Newman|George Kennedy
Persona|1966|Drama,Thriller|8.1|Ingmar Bergman|Bibi Andersson|Liv Ullmann
Andrei Rublev|1966|Biography,Drama,History|8.1|Andrei Tarkovsky|Anatoliy Solonitsyn|Ivan Lapikov
La battaglia di Algeri|1966|Drama,War|8.1|Gillo Pontecorvo|Brahim Hadjadj|Jean Martin
El ángel exterminador|1962|Drama,Fantasy|8.1|Luis Buñuel|Silvia Pinal|Jacqueline Andere
What Ever Happened to Baby Jane?|1962|Drama,Horror,Thriller|8.1|Robert Aldrich|Bette Davis|Joan Crawford
Sanjuro|1962|Action,Comedy,Crime|8.1|Akira Kurosawa|Toshirô Mifune|Tatsuya Nakadai
The Man Who Shot Liberty Valance|1962|Drama,Western|8.1|John Ford|James Stewart|John Wayne
Ivanovo detstvo|1962|Drama,War|8.1|Andrei Tarkovsky|Eduard Abalov|Nikolay Burlyaev
Jungfrukällan|1960|Drama|8.1|Ingmar Bergman|Max von Sydow|Birgitta Valberg
Inherit the Wind|1960|Biography,Drama,History|8.1|Stanley Kramer|Spencer Tracy|Fredric March
Les quatre cents coups|1959|Crime,Drama|8.1|François Truffaut|Jean-Pierre Léaud|Albert Rémy
Ben-Hur|1959|Adventure,Drama,History|8.1|William Wyler|Charlton Heston|Jack Hawkins
Kakushi-toride no san-akunin|1958|Adventure,Drama|8.1|Akira Kurosawa|Toshirô Mifune|Misa Uehara
Le notti di Cabiria|1957|Drama|8.1|Federico Fellini|Giulietta Masina|François Périer
Kumonosu-jô|1957|Drama,History|8.1|Akira Kurosawa|Toshirô Mifune|Minoru Chiaki
The Bridge on the River Kwai|1957|Adventure,Drama,War|8.1|David Lean|William Holden|Alec Guinness
On the Waterfront|1954|Crime,Drama,Thriller|8.1|Elia Kazan|Marlon Brando|Karl Malden
Le salaire de la peur|1953|Adventure,Drama,Thriller|8.1|Henri-Georges Clouzot|Yves Montand|Charles Vanel
Ace in the Hole|1951|Drama,Film-Noir|8.1|Billy Wilder|Kirk Douglas|Jan Sterling
White Heat|1949|Action,Crime,Drama|8.1|Raoul Walsh|James Cagney|Virginia Mayo
The Third Man|1949|Film-Noir,Mystery,Thriller|8.1|Carol Reed|Orson Welles|Joseph Cotten
The Red Shoes|1948|Drama,Music,Romance|8.1|Michael Powell|Emeric Pressburger|Anton Walbrook
The Shop Around the Corner|1940|Comedy,Drama,Romance|8.1|Ernst Lubitsch|Margaret Sullavan|James Stewart
Rebecca|1940|Drama,Mystery,Romance|8.1|Alfred Hitchcock|Laurence Olivier|Joan Fontaine
Mr. Smith Goes to Washington|1939|Comedy,Drama|8.1|Frank Capra|James Stewart|Jean Arthur
Gone with the Wind|1939|Drama,History,Romance|8.1|Victor Fleming|George Cukor|Sam Wood
La Grande Illusion|1937|Drama,War|8.1|Jean Renoir|Jean Gabin|Dita Parlo
It Happened One Night|1934|Comedy,Romance|8.1|Frank Capra|Clark Gable|Claudette Colbert
La passion de Jeanne d'Arc|1928|Biography,Drama,History|8.1|Carl Theodor Dreyer|Maria Falconetti|Eugene Silvain
The Circus|1928|Comedy,Romance|8.1|Charles Chaplin|Charles Chaplin|Merna Kennedy
Sunrise: A Song of Two Humans|1927|Drama,Romance|8.1|F.W. Murnau|George O'Brien|Janet Gaynor
The General|1926|Action,Adventure,Comedy|8.1|Clyde Bruckman|Buster Keaton|Buster Keaton
Das Cabinet des Dr. Caligari|1920|Fantasy,Horror,Mystery|8.1|Robert Wiene|Werner Krauss|Conrad Veidt
Badhaai ho|2018|Comedy,Drama|8.0|Amit Ravindernath Sharma|Ayushmann Khurrana|Neena Gupta
Togo|2019|Adventure,Biography,Drama|8.0|Ericson Core|Willem Dafoe|Julianne Nicholson
Airlift|2016|Drama,History|8.0|Raja Menon|Akshay Kumar|Nimrat Kaur
Bajrangi Bhaijaan|2015|Action,Adventure,Comedy|8.0|Kabir Khan|Salman Khan|Harshaali Malhotra
Baby|2015|Action,Crime,Thriller|8.0|Neeraj Pandey|Akshay Kumar|Danny Denzongpa
La La Land|2016|Comedy,Drama,Music|8.0|Damien Chazelle|Ryan Gosling|Emma Stone
Lion|2016|Biography,Drama|8.0|Garth Davis|Dev Patel|Nicole Kidman
The Martian|2015|Adventure,Drama,Sci-Fi|8.0|Ridley Scott|Matt Damon|Jessica Chastain
Zootopia|2016|Animation,Adventure,Comedy|8.0|Byron Howard|Rich Moore|Jared Bush
Bãhubali: The Beginning|2015|Action,Drama|8.0|S.S. Rajamouli|Prabhas|Rana Daggubati
Kaguyahime no monogatari|2013|Animation,Adventure,Drama|8.0|Isao Takahata|Chloë Grace Moretz|James Caan
Wonder|2017|Drama,Family|8.0|Stephen Chbosky|Jacob Tremblay|Owen Wilson
Gully Boy|2019|Drama,Music,Romance|8.0|Zoya Akhtar|Vijay Varma|Nakul Roshan Sahdev
Special Chabbis|2013|Crime,Drama,Thriller|8.0|Neeraj Pandey|Akshay Kumar|Anupam Kher
Short Term 12|2013|Drama|8.0|Destin Daniel Cretton|Brie Larson|Frantz Turner
Serbuan maut 2: Berandal|2014|Action,Crime,Thriller|8.0|Gareth Evans|Iko Uwais|Yayan Ruhian
The Imitation Game|2014|Biography,Drama,Thriller|8.0|Morten Tyldum|Benedict Cumberbatch|Keira Knightley
Guardians of the Galaxy|2014|Action,Adventure,Comedy|8.0|James Gunn|Chris Pratt|Vin Diesel
Blade Runner 2049|2017|Action,Drama,Mystery|8.0|Denis Villeneuve|Harrison Ford|Ryan Gosling
Her|2013|Drama,Romance,Sci-Fi|8.0|Spike Jonze|Joaquin Phoenix|Amy Adams
Bohemian Rhapsody|2018|Biography,Drama,Music|8.0|Bryan Singer|Rami Malek|Lucy Boynton
The Revenant|2015|Action,Adventure,Drama|8.0|Alejandro G. Iñárritu|Leonardo DiCaprio|Tom Hardy
The Perks of Being a Wallflower|2012|Drama,Romance|8.0|Stephen Chbosky|Logan Lerman|Emma Watson
Tropa de Elite 2: O Inimigo Agora é Outro|2010|Action,Crime,Drama|8.0|José Padilha|Wagner Moura|Irandhir Santos
The King's Speech|2010|Biography,Drama,History|8.0|Tom Hooper|Colin Firth|Geoffrey Rush
The Help|2011|Drama|8.0|Tate Taylor|Emma Stone|Viola Davis
Deadpool|2016|Action,Adventure,Comedy|8.0|Tim Miller|Ryan Reynolds|Morena Baccarin
Darbareye Elly|2009|Drama,Mystery|8.0|Asghar Farhadi|Golshifteh Farahani|Shahab Hosseini
Dev.D|2009|Drama,Romance|8.0|Anurag Kashyap|Abhay Deol|Mahie Gill
Yip Man|2008|Action,Biography,Drama|8.0|Wilson Yip|Donnie Yen|Simon Yam
My Name Is Khan|2010|Drama|8.0|Karan Johar|Shah Rukh Khan|Kajol
Nefes: Vatan Sagolsun|2009|Action,Drama,Thriller|8.0|Levent Semerci|Erdem Can|Mete Horozoglu
Slumdog Millionaire|2008|Drama,Romance|8.0|Danny Boyle|Loveleen Tandan|Dev Patel
Black Swan|2010|Drama,Thriller|8.0|Darren Aronofsky|Natalie Portman|Mila Kunis
Tropa de Elite|2007|Action,Crime,Drama|8.0|José Padilha|Wagner Moura|André Ramiro
The Avengers|2012|Action,Adventure,Sci-Fi|8.0|Joss Whedon|Robert Downey Jr.|Chris Evans
Persepolis|2007|Animation,Biography,Drama|8.0|Vincent Paronnaud|Marjane Satrapi|Chiara Mastroianni
Dallas Buyers Club|2013|Biography,Drama|8.0|Jean-Marc Vallée|Matthew McConaughey|Jennifer Garner
The Pursuit of Happyness|2006|Biography,Drama|8.0|Gabriele Muccino|Will Smith|Thandie Newton
Blood Diamond|2006|Adventure,Drama,Thriller|8.0|Edward Zwick|Leonardo DiCaprio|Djimon Hounsou
The Bourne Ultimatum|2007|Action,Mystery,Thriller|8.0|Paul Greengrass|Matt Damon|Edgar Ramírez
Bin-jip|2004|Crime,Drama,Romance|8.0|Ki-duk Kim|Seung-Yun Lee|Hee Jae
Sin City|2005|Crime,Thriller|8.0|Frank Miller|Quentin Tarantino|Robert Rodriguez
Le scaphandre et le papillon|2007|Biography,Drama|8.0|Julian Schnabel|Laura Obiols|Mathieu Amalric
G.O.R.A.|2004|Adventure,Comedy,Sci-Fi|8.0|Ömer Faruk Sorak|Cem Yilmaz|Özge Özberk
Ratatouille|2007|Animation,Adventure,Comedy|8.0|Brad Bird|Jan Pinkava|Brad Garrett
Casino Royale|2006|Action,Adventure,Thriller|8.0|Martin Campbell|Daniel Craig|Eva Green
Kill Bill: Vol. 2|2004|Action,Crime,Thriller|8.0|Quentin Tarantino|Uma Thurman|David Carradine
Vozvrashchenie|2003|Drama|8.0|Andrey Zvyagintsev|Vladimir Garin|Ivan Dobronravov
Bom Yeoareum Gaeul Gyeoul Geurigo Bom|2003|Drama,Romance|8.0|Ki-duk Kim|Ki-duk Kim|Yeong-su Oh
Mar adentro|2014|Biography,Drama|8.0|Alejandro Amenábar|Javier Bardem|Belén Rueda
Cinderella Man|2005|Biography,Drama,History|8.0|Ron Howard|Russell Crowe|Renée Zellweger
Kal Ho Naa Ho|2003|Comedy,Drama,Musical|8.0|Nikkhil Advani|Preity Zinta|Shah Rukh Khan
Mou gaan dou|2002|Action,Crime,Drama|8.0|Andrew Lau|Alan Mak|Andy Lau
Pirates of the Caribbean: The Curse of the Black Pearl|2003|Action,Adventure,Fantasy|8.0|Gore Verbinski|Johnny Depp|Geoffrey Rush
Big Fish|2003|Adventure,Drama,Fantasy|8.0|Tim Burton|Ewan McGregor|Albert Finney
The Incredibles|2004|Animation,Action,Adventure|8.0|Brad Bird|Craig T. Nelson|Samuel L. Jackson
Yeopgijeogin geunyeo|2001|Comedy,Drama,Romance|8.0|Jae-young Kwak|Tae-Hyun Cha|Jun Ji-Hyun
Dogville|2003|Crime,Drama|8.0|Lars von Trier|Nicole Kidman|Paul Bettany
Vizontele|2001|Comedy,Drama|8.0|Yilmaz Erdogan|Ömer Faruk Sorak|Yilmaz Erdogan
Donnie Darko|2001|Drama,Mystery,Sci-Fi|8.0|Richard Kelly|Jake Gyllenhaal|Jena Malone
Magnolia|1999|Drama|8.0|Paul Thomas Anderson|Tom Cruise|Jason Robards
Dancer in the Dark|2000|Crime,Drama,Musical|8.0|Lars von Trier|Björk|Catherine Deneuve
The Straight Story|1999|Biography,Drama|8.0|David Lynch|Richard Farnsworth|Sissy Spacek
Pâfekuto burû|1997|Animation,Crime,Mystery|8.0|Satoshi Kon|Junko Iwao|Rica Matsumoto
Festen|1998|Drama|8.0|Thomas Vinterberg|Ulrich Thomsen|Henning Moritzen
Central do Brasil|1998|Drama|8.0|Walter Salles|Fernanda Montenegro|Vinícius de Oliveira
The Iron Giant|1999|Animation,Action,Adventure|8.0|Brad Bird|Eli Marienthal|Harry Connick Jr.
Knockin' on Heaven's Door|1997|Action,Crime,Comedy|8.0|Thomas Jahn|Til Schweiger|Jan Josef Liefers
Sling Blade|1996|Drama|8.0|Billy Bob Thornton|Billy Bob Thornton|Dwight Yoakam
Secrets & Lies|1996|Comedy,Drama|8.0|Mike Leigh|Timothy Spall|Brenda Blethyn
Twelve Monkeys|1995|Mystery,Sci-Fi,Thriller|8.0|Terry Gilliam|Bruce Willis|Madeleine Stowe
Kôkaku Kidôtai|1995|Animation,Action,Crime|8.0|Mamoru Oshii|Atsuko Tanaka|Iemasa Kayumi
The Nightmare Before Christmas|1993|Animation,Family,Fantasy|8.0|Henry Selick|Danny Elfman|Chris Sarandon
Groundhog Day|1993|Comedy,Fantasy,Romance|8.0|Harold Ramis|Bill Murray|Andie MacDowell
Bound by Honor|1993|Crime,Drama|8.0|Taylor Hackford|Damian Chapa|Jesse Borrego
Scent of a Woman|1992|Drama|8.0|Martin Brest|Al Pacino|Chris O'Donnell
Aladdin|1992|Animation,Adventure,Comedy|8.0|Ron Clements|John Musker|Scott Weinger
JFK|1991|Drama,History,Thriller|8.0|Oliver Stone|Kevin Costner|Gary Oldman
Beauty and the Beast|1991|Animation,Family,Fantasy|8.0|Gary Trousdale|Kirk Wise|Paige O'Hara
Dances with Wolves|1990|Adventure,Drama,Western|8.0|Kevin Costner|Kevin Costner|Mary McDonnell
Do the Right Thing|1989|Comedy,Drama|8.0|Spike Lee|Danny Aiello|Ossie Davis
Rain Man|1988|Drama|8.0|Barry Levinson|Dustin Hoffman|Tom Cruise
Akira|1988|Animation,Action,Sci-Fi|8.0|Katsuhiro Ôtomo|Mitsuo Iwata|Nozomu Sasaki
The Princess Bride|1987|Adventure,Family,Fantasy|8.0|Rob Reiner|Cary Elwes|Mandy Patinkin
Der Himmel über Berlin|1987|Drama,Fantasy,Romance|8.0|Wim Wenders|Bruno Ganz|Solveig Dommartin
Au revoir les enfants|1987|Drama,War|8.0|Louis Malle|Gaspard Manesse|Raphael Fejtö
Tenkû no shiro Rapyuta|1986|Animation,Adventure,Drama|8.0|Hayao Miyazaki|Mayumi Tanaka|Keiko Yokozawa
The Terminator|1984|Action,Sci-Fi|8.0|James Cameron|Arnold Schwarzenegger|Linda Hamilton
Gandhi|1982|Biography,Drama,History|8.0|Richard Attenborough|Ben Kingsley|John Gielgud
Kagemusha|1980|Drama,History,War|8.0|Akira Kurosawa|Tatsuya Nakadai|Tsutomu Yamazaki
Being There|1979|Comedy,Drama|8.0|Hal Ashby|Peter Sellers|Shirley MacLaine
Annie Hall|1977|Comedy,Romance|8.0|Woody Allen|Woody Allen|Diane Keaton
Jaws|1975|Adventure,Thriller|8.0|Steven Spielberg|Roy Scheider|Robert Shaw
Dog Day Afternoon|1975|Biography,Crime,Drama|8.0|Sidney Lumet|Al Pacino|John Cazale
Young Frankenstein|1974|Comedy|8.0|Mel Brooks|Gene Wilder|Madeline Kahn
Papillon|1973|Biography,Crime,Drama|8.0|Franklin J. Schaffner|Steve McQueen|Dustin Hoffman
The Exorcist|1973|Horror|8.0|William Friedkin|Ellen Burstyn|Max von Sydow
Sleuth|1972|Mystery,Thriller|8.0|Joseph L. Mankiewicz|Laurence Olivier|Michael Caine
The Last Picture Show|1971|Drama,Romance|8.0|Peter Bogdanovich|Timothy Bottoms|Jeff Bridges
Fiddler on the Roof|1971|Drama,Family,Musical|8.0|Norman Jewison|Topol|Norma Crane
Il conformista|1970|Drama|8.0|Bernardo Bertolucci|Jean-Louis Trintignant|Stefania Sandrelli
Butch Cassidy and the Sundance Kid|1969|Biography,Crime,Drama|8.0|George Roy Hill|Paul Newman|Robert Redford
Rosemary's Baby|1968|Drama,Horror|8.0|Roman Polanski|Mia Farrow|John Cassavetes
Planet of the Apes|1968|Adventure,Sci-Fi|8.0|Franklin J. Schaffner|Charlton Heston|Roddy McDowall
The Graduate|1967|Comedy,Drama,Romance|8.0|Mike Nichols|Dustin Hoffman|Anne Bancroft
Who's Afraid of Virginia Woolf?|1966|Drama|8.0|Mike Nichols|Elizabeth Taylor|Richard Burton
The Sound of Music|1965|Biography,Drama,Family|8.0|Robert Wise|Julie Andrews|Christopher Plummer
Doctor Zhivago|1965|Drama,Romance,War|8.0|David Lean|Omar Sharif|Julie Christie
Per un pugno di dollari|1964|Action,Drama,Western|8.0|Sergio Leone|Clint Eastwood|Gian Maria Volontè
8½|1963|Drama|8.0|Federico Fellini|Marcello Mastroianni|Anouk Aimée
Vivre sa vie: Film en douze tableaux|1962|Drama|8.0|Jean-Luc Godard|Anna Karina|Sady Rebbot
The Hustler|1961|Drama,Sport|8.0|Robert Rossen|Paul Newman|Jackie Gleason
La dolce vita|1960|Comedy,Drama|8.0|Federico Fellini|Marcello Mastroianni|Anita Ekberg
Rio Bravo|1959|Action,Drama,Western|8.0|Howard Hawks|John Wayne|Dean Martin
Anatomy of a Murder|1959|Crime,Drama,Mystery|8.0|Otto Preminger|James Stewart|Lee Remick
Touch of Evil|1958|Crime,Drama,Film-Noir|8.0|Orson Welles|Charlton Heston|Orson Welles
Cat on a Hot Tin Roof|1958|Drama|8.0|Richard Brooks|Elizabeth Taylor|Paul Newman
Sweet Smell of Success|1957|Drama,Film-Noir|8.0|Alexander Mackendrick|Burt Lancaster|Tony Curtis
The Killing|1956|Crime,Drama,Film-Noir|8.0|Stanley Kubrick|Sterling Hayden|Coleen Gray
The Night of the Hunter|1955|Crime,Drama,Film-Noir|8.0|Charles Laughton|Robert Mitchum|Shelley Winters
La Strada|1954|Drama|8.0|Federico Fellini|Anthony Quinn|Giulietta Masina
Les diaboliques|1955|Crime,Drama,Horror|8.0|Henri-Georges Clouzot|Simone Signoret|Véra Clouzot
Stalag 17|1953|Comedy,Drama,War|8.0|Billy Wilder|William Holden|Don Taylor
Roman Holiday|1953|Comedy,Romance|8.0|William Wyler|Gregory Peck|Audrey Hepburn
A Streetcar Named Desire|1951|Drama|8.0|Elia Kazan|Vivien Leigh|Marlon Brando
In a Lonely Place|1950|Drama,Film-Noir,Mystery|8.0|Nicholas Ray|Humphrey Bogart|Gloria Grahame
Kind Hearts and Coronets|1949|Comedy,Crime|8.0|Robert Hamer|Dennis Price|Alec Guinness
Rope|1948|Crime,Drama,Mystery|8.0|Alfred Hitchcock|James Stewart|John Dall
Out of the Past|1947|Crime,Drama,Film-Noir|8.0|Jacques Tourneur|Robert Mitchum|Jane Greer
Brief Encounter|1945|Drama,Romance|8.0|David Lean|Celia Johnson|Trevor Howard
Laura|1944|Drama,Film-Noir,Mystery|8.0|Otto Preminger|Gene Tierney|Dana Andrews
The Best Years of Our Lives|1946|Drama,Romance,War|8.0|William Wyler|Myrna Loy|Dana Andrews
Arsenic and Old Lace|1942|Comedy,Crime,Thriller|8.0|Frank Capra|Cary Grant|Priscilla Lane
The Maltese Falcon|1941|Film-Noir,Mystery|8.0|John Huston|Humphrey Bogart|Mary Astor
The Grapes of Wrath|1940|Drama,History|8.0|John Ford|Henry Fonda|Jane Darwell
The Wizard of Oz|1939|Adventure,Family,Fantasy|8.0|Victor Fleming|George Cukor|Mervyn LeRoy
La règle du jeu|1939|Comedy,Drama|8.0|Jean Renoir|Marcel Dalio|Nora Gregor
The Thin Man|1934|Comedy,Crime,Mystery|8.0|W.S. Van Dyke|William Powell|Myrna Loy
All Quiet on the Western Front|1930|Drama,War|8.0|Lewis Milestone|Lew Ayres|Louis Wolheim
Bronenosets Potemkin|1925|Drama,History,Thriller|8.0|Sergei M. Eisenstein|Aleksandr Antonov|Vladimir Barskiy
Knives Out|2019|Comedy,Crime,Drama|7.9|Rian Johnson|Daniel Craig|Chris Evans
Dil Bechara|2020|Comedy,Drama,Romance|7.9|Mukesh Chhabra|Sushant Singh Rajput|Sanjana Sanghi
Manbiki kazoku|2018|Crime,Drama|7.9|Hirokazu Koreeda|Lily Franky|Sakura Andô
Marriage Story|2019|Comedy,Drama,Romance|7.9|Noah Baumbach|Adam Driver|Scarlett Johansson
Call Me by Your Name|2017|Drama,Romance|7.9|Luca Guadagnino|Armie Hammer|Timothée Chalamet
I, Daniel Blake|2016|Drama|7.9|Ken Loach|Laura Obiols|Dave Johns
Isle of Dogs|2018|Animation,Adventure,Comedy|7.9|Wes Anderson|Bryan Cranston|Koyu Rankin
Hunt for the Wilderpeople|2016|Adventure,Comedy,Drama|7.9|Taika Waititi|Sam Neill|Julian Dennison
Captain Fantastic|2016|Comedy,Drama|7.9|Matt Ross|Viggo Mortensen|George MacKay
Sing Street|2016|Comedy,Drama,Music|7.9|John Carney|Ferdia Walsh-Peelo|Aidan Gillen
Thor: Ragnarok|2017|Action,Adventure,Comedy|7.9|Taika Waititi|Chris Hemsworth|Tom Hiddleston
Nightcrawler|2014|Crime,Drama,Thriller|7.9|Dan Gilroy|Jake Gyllenhaal|Rene Russo
Jojo Rabbit|2019|Comedy,Drama,War|7.9|Taika Waititi|Roman Griffin Davis|Thomasin McKenzie
Arrival|2016|Drama,Sci-Fi|7.9|Denis Villeneuve|Amy Adams|Jeremy Renner
Star Wars: Episode VII - The Force Awakens|2015|Action,Adventure,Sci-Fi|7.9|J.J. Abrams|Daisy Ridley|John Boyega
Before Midnight|2013|Drama,Romance|7.9|Richard Linklater|Ethan Hawke|Julie Delpy
X-Men: Days of Future Past|2014|Action,Adventure,Sci-Fi|7.9|Bryan Singer|Patrick Stewart|Ian McKellen
Bir Zamanlar Anadolu'da|2011|Crime,Drama|7.9|Nuri Bilge Ceylan|Muhammet Uzuner|Yilmaz Erdogan
The Artist|2011|Comedy,Drama,Romance|7.9|Michel Hazanavicius|Jean Dujardin|Bérénice Bejo
Edge of Tomorrow|2014|Action,Adventure,Sci-Fi|7.9|Doug Liman|Tom Cruise|Emily Blunt
Amour|2012|Drama,Romance|7.9|Michael Haneke|Jean-Louis Trintignant|Emmanuelle Riva
The Irishman|2019|Biography,Crime,Drama|7.9|Martin Scorsese|Robert De Niro|Al Pacino
Un prophète|2009|Crime,Drama|7.9|Jacques Audiard|Tahar Rahim|Niels Arestrup
Moon|2009|Drama,Mystery,Sci-Fi|7.9|Duncan Jones|Sam Rockwell|Kevin Spacey
Låt den rätte komma in|2008|Crime,Drama,Fantasy|7.9|Tomas Alfredson|Kåre Hedebrant|Lina Leandersson
District 9|2009|Action,Sci-Fi,Thriller|7.9|Neill Blomkamp|Sharlto Copley|David James
The Wrestler|2008|Drama,Sport|7.9|Darren Aronofsky|Mickey Rourke|Marisa Tomei
Jab We Met|2007|Comedy,Drama,Romance|7.9|Imtiaz Ali|Shahid Kapoor|Kareena Kapoor
Boyhood|2014|Drama|7.9|Richard Linklater|Ellar Coltrane|Patricia Arquette
4 luni, 3 saptamâni si 2 zile|2007|Drama|7.9|Cristian Mungiu|Anamaria Marinca|Laura Vasiliu
Star Trek|2009|Action,Adventure,Sci-Fi|7.9|J.J. Abrams|Chris Pine|Zachary Quinto
In Bruges|2008|Comedy,Crime,Drama|7.9|Martin McDonagh|Colin Farrell|Brendan Gleeson
The Man from Earth|2007|Drama,Fantasy,Mystery|7.9|Richard Schenkman|David Lee Smith|Tony Todd
Letters from Iwo Jima|2006|Action,Adventure,Drama|7.9|Clint Eastwood|Ken Watanabe|Kazunari Ninomiya
The Fall|2006|Adventure,Drama,Fantasy|7.9|Tarsem Singh|Lee Pace|Catinca Untaru
Life of Pi|2012|Adventure,Drama,Fantasy|7.9|Ang Lee|Suraj Sharma|Irrfan Khan
Fantastic Mr. Fox|2009|Animation,Adventure,Comedy|7.9|Wes Anderson|George Clooney|Meryl Streep
C.R.A.Z.Y.|2005|Comedy,Drama|7.9|Jean-Marc Vallée|Michel Côté|Marc-André Grondin
Les choristes|2004|Drama,Music|7.9|Christophe Barratier|Gérard Jugnot|François Berléand
Iron Man|2008|Action,Adventure,Sci-Fi|7.9|Jon Favreau|Robert Downey Jr.|Gwyneth Paltrow
Shaun of the Dead|2004|Comedy,Horror|7.9|Edgar Wright|Simon Pegg|Nick Frost
Gegen die Wand|2004|Drama,Romance|7.9|Fatih Akin|Birol Ünel|Sibel Kekilli
Mystic River|2003|Crime,Drama,Mystery|7.9|Clint Eastwood|Sean Penn|Tim Robbins
Harry Potter and the Prisoner of Azkaban|2004|Adventure,Family,Fantasy|7.9|Alfonso Cuarón|Daniel Radcliffe|Emma Watson
Ying xiong|2002|Action,Adventure,History|7.9|Yimou Zhang|Jet Li|Tony Chiu-Wai Leung
Hable con ella|2002|Drama,Mystery,Romance|7.9|Pedro Almodóvar|Rosario Flores|Javier Cámara
No Man's Land|2001|Comedy,Drama,War|7.9|Danis Tanovic|Branko Djuric|Rene Bitorajac
Cowboy Bebop: Tengoku no tobira|2001|Animation,Action,Crime|7.9|Shin'ichirô Watanabe|Tensai Okamura|Hiroyuki Okiura
The Bourne Identity|2002|Action,Mystery,Thriller|7.9|Doug Liman|Franka Potente|Matt Damon
Nueve reinas|2000|Crime,Drama,Thriller|7.9|Fabián Bielinsky|Ricardo Darín|Gastón Pauls
Children of Men|2006|Adventure,Drama,Sci-Fi|7.9|Alfonso Cuarón|Julianne Moore|Clive Owen
Almost Famous|2000|Adventure,Comedy,Drama|7.9|Cameron Crowe|Billy Crudup|Patrick Fugit
Mulholland Dr.|2001|Drama,Mystery,Thriller|7.9|David Lynch|Naomi Watts|Laura Harring
Toy Story 2|1999|Animation,Adventure,Comedy|7.9|John Lasseter|Ash Brannon|Lee Unkrich
Boogie Nights|1997|Drama|7.9|Paul Thomas Anderson|Mark Wahlberg|Julianne Moore
Mimi wo sumaseba|1995|Animation,Drama,Family|7.9|Yoshifumi Kondô|Yoko Honna|Issey Takahashi
Once Were Warriors|1994|Crime,Drama|7.9|Lee Tamahori|Rena Owen|Temuera Morrison
True Romance|1993|Crime,Drama,Romance|7.9|Tony Scott|Christian Slater|Patricia Arquette
Trois couleurs: Bleu|1993|Drama,Music,Mystery|7.9|Krzysztof Kieslowski|Juliette Binoche|Zbigniew Zamachowski
Jûbê ninpûchô|1993|Animation,Action,Adventure|7.9|Yoshiaki Kawajiri|Kôichi Yamadera|Emi Shinohara
Carlito's Way|1993|Crime,Drama,Thriller|7.9|Brian De Palma|Al Pacino|Sean Penn
Edward Scissorhands|1990|Drama,Fantasy,Romance|7.9|Tim Burton|Johnny Depp|Winona Ryder
My Left Foot: The Story of Christy Brown|1989|Biography,Drama|7.9|Jim Sheridan|Daniel Day-Lewis|Brenda Fricker
Crimes and Misdemeanors|1989|Comedy,Drama|7.9|Woody Allen|Martin Landau|Woody Allen
The Untouchables|1987|Crime,Drama,Thriller|7.9|Brian De Palma|Kevin Costner|Sean Connery
Hannah and Her Sisters|1986|Comedy,Drama|7.9|Woody Allen|Mia Farrow|Dianne Wiest
Brazil|1985|Drama,Sci-Fi|7.9|Terry Gilliam|Jonathan Pryce|Kim Greist
This Is Spinal Tap|1984|Comedy,Music|7.9|Rob Reiner|Rob Reiner|Michael McKean
A Christmas Story|1983|Comedy,Family|7.9|Bob Clark|Peter Billingsley|Melinda Dillon
The Blues Brothers|1980|Action,Adventure,Comedy|7.9|John Landis|John Belushi|Dan Aykroyd
Manhattan|1979|Comedy,Drama,Romance|7.9|Woody Allen|Woody Allen|Diane Keaton
All That Jazz|1979|Drama,Music,Musical|7.9|Bob Fosse|Roy Scheider|Jessica Lange
Dawn of the Dead|1978|Action,Adventure,Horror|7.9|George A. Romero|David Emge|Ken Foree
All the President's Men|1976|Biography,Drama,History|7.9|Alan J. Pakula|Dustin Hoffman|Robert Redford
La montaña sagrada|1973|Adventure,Drama,Fantasy|7.9|Alejandro Jodorowsky|Alejandro Jodorowsky|Horacio Salinas
Amarcord|1973|Comedy,Drama,Family|7.9|Federico Fellini|Magali Noël|Bruno Zanin
Le charme discret de la bourgeoisie|1972|Comedy|7.9|Luis Buñuel|Fernando Rey|Delphine Seyrig
Aguirre, der Zorn Gottes|1972|Action,Adventure,Biography|7.9|Werner Herzog|Klaus Kinski|Ruy Guerra
Harold and Maude|1971|Comedy,Drama,Romance|7.9|Hal Ashby|Ruth Gordon|Bud Cort
Patton|1970|Biography,Drama,War|7.9|Franklin J. Schaffner|George C. Scott|Karl Malden
The Wild Bunch|1969|Action,Adventure,Western|7.9|Sam Peckinpah|William Holden|Ernest Borgnine
Night of the Living Dead|1968|Horror,Thriller|7.9|George A. Romero|Duane Jones|Judith O'Dea
The Lion in Winter|1968|Biography,Drama,History|7.9|Anthony Harvey|Peter O'Toole|Katharine Hepburn
In the Heat of the Night|1967|Crime,Drama,Mystery|7.9|Norman Jewison|Sidney Poitier|Rod Steiger
Charade|1963|Comedy,Mystery,Romance|7.9|Stanley Donen|Cary Grant|Audrey Hepburn
The Manchurian Candidate|1962|Drama,Thriller|7.9|John Frankenheimer|Frank Sinatra|Laurence Harvey
Spartacus|1960|Adventure,Biography,Drama|7.9|Stanley Kubrick|Kirk Douglas|Laurence Olivier
L'avventura|1960|Drama,Mystery|7.9|Michelangelo Antonioni|Gabriele Ferzetti|Monica Vitti
Hiroshima mon amour|1959|Drama,Romance|7.9|Alain Resnais|Emmanuelle Riva|Eiji Okada
The Ten Commandments|1956|Adventure,Drama|7.9|Cecil B. DeMille|Charlton Heston|Yul Brynner
The Searchers|1956|Adventure,Drama,Western|7.9|John Ford|John Wayne|Jeffrey Hunter
East of Eden|1955|Drama|7.9|Elia Kazan|James Dean|Raymond Massey
High Noon|1952|Drama,Thriller,Western|7.9|Fred Zinnemann|Gary Cooper|Grace Kelly
Strangers on a Train|1951|Crime,Film-Noir,Thriller|7.9|Alfred Hitchcock|Farley Granger|Robert Walker
Harvey|1950|Comedy,Drama,Fantasy|7.9|Henry Koster|James Stewart|Wallace Ford
Miracle on 34th Street|1947|Comedy,Drama,Family|7.9|George Seaton|Edmund Gwenn|Maureen O'Hara
Notorious|1946|Drama,Film-Noir,Romance|7.9|Alfred Hitchcock|Cary Grant|Ingrid Bergman
The Big Sleep|1946|Crime,Film-Noir,Mystery|7.9|Howard Hawks|Humphrey Bogart|Lauren Bacall
The Lost Weekend|1945|Drama,Film-Noir|7.9|Billy Wilder|Ray Milland|Jane Wyman
The Philadelphia Story|1940|Comedy,Romance|7.9|George Cukor|Cary Grant|Katharine Hepburn
His Girl Friday|1940|Comedy,Drama,Romance|7.9|Howard Hawks|Cary Grant|Rosalind Russell
The Adventures of Robin Hood|1938|Action,Adventure,Romance|7.9|Michael Curtiz|William Keighley|Errol Flynn
A Night at the Opera|1935|Comedy,Music,Musical|7.9|Sam Wood|Edmund Goulding|Groucho Marx
King Kong|1933|Adventure,Horror,Sci-Fi|7.9|Merian C. Cooper|Ernest B. Schoedsack|Fay Wray
Freaks|1932|Drama,Horror|7.9|Tod Browning|Wallace Ford|Leila Hyams
Nosferatu|1922|Fantasy,Horror|7.9|F.W. Murnau|Max Schreck|Alexander Granach
The Gentlemen|2019|Action,Comedy,Crime|7.8|Guy Ritchie|Matthew McConaughey|Charlie Hunnam
Raazi|2018|Action,Drama,Thriller|7.8|Meghna Gulzar|Alia Bhatt|Vicky Kaushal
Sound of Metal|2019|Drama,Music|7.8|Darius Marder|Riz Ahmed|Olivia Cooke
Forushande|2016|Drama|7.8|Asghar Farhadi|Shahab Hosseini|Taraneh Alidoosti
Dunkirk|2017|Action,Drama,History|7.8|Christopher Nolan|Fionn Whitehead|Barry Keoghan
Perfetti sconosciuti|2016|Comedy,Drama|7.8|Paolo Genovese|Giuseppe Battiston|Anna Foglietta
Hidden Figures|2016|Biography,Drama,History|7.8|Theodore Melfi|Taraji P. Henson|Octavia Spencer
Paddington 2|2017|Adventure,Comedy,Family|7.8|Paul King|Ben Whishaw|Hugh Grant
Udta Punjab|2016|Action,Crime,Drama|7.8|Abhishek Chaubey|Shahid Kapoor|Alia Bhatt
Kubo and the Two Strings|2016|Animation,Action,Adventure|7.8|Travis Knight|Charlize Theron|Art Parkinson
M.S. Dhoni: The Untold Story|2016|Biography,Drama,Sport|7.8|Neeraj Pandey|Sushant Singh Rajput|Kiara Advani
Manchester by the Sea|2016|Drama|7.8|Kenneth Lonergan|Casey Affleck|Michelle Williams
Under sandet|2015|Drama,History,War|7.8|Martin Zandvliet|Roland Møller|Louis Hofmann
Rogue One|2016|Action,Adventure,Sci-Fi|7.8|Gareth Edwards|Felicity Jones|Diego Luna
Captain America: Civil War|2016|Action,Adventure,Sci-Fi|7.8|Anthony Russo|Joe Russo|Chris Evans
The Hateful Eight|2015|Crime,Drama,Mystery|7.8|Quentin Tarantino|Samuel L. Jackson|Kurt Russell
Little Women|2019|Drama,Romance|7.8|Greta Gerwig|Saoirse Ronan|Emma Watson
Loving Vincent|2017|Animation,Biography,Crime|7.8|Dorota Kobiela|Hugh Welchman|Douglas Booth
Pride|2014|Biography,Comedy,Drama|7.8|Matthew Warchus|Bill Nighy|Imelda Staunton
Le passé|2013|Drama,Mystery|7.8|Asghar Farhadi|Bérénice Bejo|Tahar Rahim
La grande bellezza|2013|Drama|7.8|Paolo Sorrentino|Toni Servillo|Carlo Verdone
The Lunchbox|2013|Drama,Romance|7.8|Ritesh Batra|Irrfan Khan|Nimrat Kaur
Vicky Donor|2012|Comedy,Romance|7.8|Shoojit Sircar|Ayushmann Khurrana|Yami Gautam
Big Hero 6|2014|Animation,Action,Adventure|7.8|Don Hall|Chris Williams|Ryan Potter
About Time|2013|Comedy,Drama,Fantasy|7.8|Richard Curtis|Domhnall Gleeson|Rachel McAdams
English Vinglish|2012|Comedy,Drama,Family|7.8|Gauri Shinde|Sridevi|Adil Hussain
Kaze tachinu|2013|Animation,Biography,Drama|7.8|Hayao Miyazaki|Hideaki Anno|Hidetoshi Nishijima
Toy Story 4|2019|Animation,Adventure,Comedy|7.8|Josh Cooley|Tom Hanks|Tim Allen
La migliore offerta|2013|Crime,Drama,Mystery|7.8|Giuseppe Tornatore|Geoffrey Rush|Jim Sturgess
Moonrise Kingdom|2012|Comedy,Drama,Romance|7.8|Wes Anderson|Jared Gilman|Kara Hayward
How to Train Your Dragon 2|2014|Animation,Action,Adventure|7.8|Dean DeBlois|Jay Baruchel|Cate Blanchett
The Big Short|2015|Biography,Comedy,Drama|7.8|Adam McKay|Christian Bale|Steve Carell
Kokuhaku|2010|Drama,Thriller|7.8|Tetsuya Nakashima|Takako Matsu|Yoshino Kimura
Ang-ma-reul bo-at-da|2010|Action,Crime,Drama|7.8|Jee-woon Kim|Lee Byung-Hun|Choi Min-sik
The Girl with the Dragon Tattoo|2011|Crime,Drama,Mystery|7.8|David Fincher|Daniel Craig|Rooney Mara
Captain Phillips|2013|Adventure,Biography,Crime|7.8|Paul Greengrass|Tom Hanks|Barkhad Abdi
Ajeossi|2010|Action,Crime,Drama|7.8|Jeong-beom Lee|Won Bin|Sae-ron Kim
Straight Outta Compton|2015|Biography,Drama,History|7.8|F. Gary Gray|O'Shea Jackson Jr.|Corey Hawkins
Madeo|2009|Crime,Drama,Mystery|7.8|Bong Joon Ho|Hye-ja Kim|Won Bin
Chugyeokja|2008|Action,Crime,Thriller|7.8|Hong-jin Na|Kim Yoon-seok|Jung-woo Ha
The Hobbit: The Desolation of Smaug|2013|Adventure,Fantasy|7.8|Peter Jackson|Ian McKellen|Martin Freeman
Das weiße Band - Eine deutsche Kindergeschichte|2009|Drama,History,Mystery|7.8|Michael Haneke|Christian Friedel|Ernst Jacobi
Män som hatar kvinnor|2009|Crime,Drama,Mystery|7.8|Niels Arden Oplev|Michael Nyqvist|Noomi Rapace
The Trial of the Chicago 7|2020|Drama,History,Thriller|7.8|Aaron Sorkin|Eddie Redmayne|Alex Sharp
Druk|2020|Comedy,Drama|7.8|Thomas Vinterberg|Mads Mikkelsen|Thomas Bo Larsen
The Fighter|2010|Biography,Drama,Sport|7.8|David O. Russell|Mark Wahlberg|Christian Bale
Taken|2008|Action,Thriller|7.8|Pierre Morel|Liam Neeson|Maggie Grace
The Boy in the Striped Pyjamas|2008|Drama,History,War|7.8|Mark Herman|Asa Butterfield|David Thewlis
Once|2007|Drama,Music,Romance|7.8|John Carney|Glen Hansard|Markéta Irglová
The Hobbit: An Unexpected Journey|2012|Adventure,Fantasy|7.8|Peter Jackson|Martin Freeman|Ian McKellen
Auf der anderen Seite|2007|Drama|7.8|Fatih Akin|Baki Davrak|Nurgül Yesilçay
Atonement|2007|Drama,Mystery,Romance|7.8|Joe Wright|Keira Knightley|James McAvoy
Drive|2011|Crime,Drama|7.8|Nicolas Winding Refn|Ryan Gosling|Carey Mulligan
American Gangster|2007|Biography,Crime,Drama|7.8|Ridley Scott|Denzel Washington|Russell Crowe
Avatar|2009|Action,Adventure,Fantasy|7.8|James Cameron|Sam Worthington|Zoe Saldana
Mr. Nobody|2009|Drama,Fantasy,Romance|7.8|Jaco Van Dormael|Jared Leto|Sarah Polley
Apocalypto|2006|Action,Adventure,Drama|7.8|Mel Gibson|Gerardo Taracena|Raoul Max Trujillo
Little Miss Sunshine|2006|Comedy,Drama|7.8|Jonathan Dayton|Valerie Faris|Steve Carell
Hot Fuzz|2007|Action,Comedy,Mystery|7.8|Edgar Wright|Simon Pegg|Nick Frost
The Curious Case of Benjamin Button|2008|Drama,Fantasy,Romance|7.8|David Fincher|Brad Pitt|Cate Blanchett
Veer-Zaara|2004|Drama,Family,Musical|7.8|Yash Chopra|Shah Rukh Khan|Preity Zinta
Adams æbler|2005|Comedy,Crime,Drama|7.8|Anders Thomas Jensen|Ulrich Thomsen|Mads Mikkelsen
Pride & Prejudice|2005|Drama,Romance|7.8|Joe Wright|Keira Knightley|Matthew Macfadyen
The World's Fastest Indian|2005|Biography,Drama,Sport|7.8|Roger Donaldson|Anthony Hopkins|Diane Ladd
Tôkyô goddofâzâzu|2003|Animation,Adventure,Comedy|7.8|Satoshi Kon|Shôgo Furuya|Tôru Emori
Serenity|2005|Action,Adventure,Sci-Fi|7.8|Joss Whedon|Nathan Fillion|Gina Torres
Walk the Line|2005|Biography,Drama,Music|7.8|James Mangold|Joaquin Phoenix|Reese Witherspoon
Ondskan|2003|Drama|7.8|Mikael Håfström|Andreas Wilson|Henrik Lundström
The Notebook|2004|Drama,Romance|7.8|Nick Cassavetes|Gena Rowlands|James Garner
Diarios de motocicleta|2004|Adventure,Biography,Drama|7.8|Walter Salles|Gael García Bernal|Rodrigo De la Serna
Lilja 4-ever|2002|Crime,Drama|7.8|Lukas Moodysson|Oksana Akinshina|Artyom Bogucharskiy
Les triplettes de Belleville|2003|Animation,Comedy,Drama|7.8|Sylvain Chomet|Michèle Caucheteux|Jean-Claude Donda
Gongdong gyeongbi guyeok JSA|2000|Action,Drama,Thriller|7.8|Chan-wook Park|Lee Yeong-ae|Lee Byung-Hun
The Count of Monte Cristo|2002|Action,Adventure,Drama|7.8|Kevin Reynolds|Jim Caviezel|Guy Pearce
Waking Life|2001|Animation,Drama,Fantasy|7.8|Richard Linklater|Ethan Hawke|Trevor Jack Brooks
Remember the Titans|2000|Biography,Drama,Sport|7.8|Boaz Yakin|Denzel Washington|Will Patton
Wo hu cang long|2000|Action,Adventure,Fantasy|7.8|Ang Lee|Yun-Fat Chow|Michelle Yeoh
Todo sobre mi madre|1999|Drama|7.8|Pedro Almodóvar|Cecilia Roth|Marisa Paredes
Cast Away|2000|Adventure,Drama,Romance|7.8|Robert Zemeckis|Tom Hanks|Helen Hunt
The Boondock Saints|1999|Action,Crime,Thriller|7.8|Troy Duffy|Willem Dafoe|Sean Patrick Flanery
The Insider|1999|Biography,Drama,Thriller|7.8|Michael Mann|Russell Crowe|Al Pacino
October Sky|1999|Biography,Drama,Family|7.8|Joe Johnston|Jake Gyllenhaal|Chris Cooper
Shrek|2001|Animation,Adventure,Comedy|7.8|Andrew Adamson|Vicky Jenson|Mike Myers
Titanic|1997|Drama,Romance|7.8|James Cameron|Leonardo DiCaprio|Kate Winslet
Hana-bi|1997|Crime,Drama,Romance|7.8|Takeshi Kitano|Takeshi Kitano|Kayoko Kishimoto
Gattaca|1997|Drama,Sci-Fi,Thriller|7.8|Andrew Niccol|Ethan Hawke|Uma Thurman
The Game|1997|Action,Drama,Mystery|7.8|David Fincher|Michael Douglas|Deborah Kara Unger
Breaking the Waves|1996|Drama|7.8|Lars von Trier|Emily Watson|Stellan Skarsgård
Ed Wood|1994|Biography,Comedy,Drama|7.8|Tim Burton|Johnny Depp|Martin Landau
What's Eating Gilbert Grape|1993|Drama|7.8|Lasse Hallström|Johnny Depp|Leonardo DiCaprio
Tombstone|1993|Action,Biography,Drama|7.8|George P. Cosmatos|Kevin Jarre|Kurt Russell
The Sandlot|1993|Comedy,Drama,Family|7.8|David Mickey Evans|Tom Guiry|Mike Vitar
The Remains of the Day|1993|Drama,Romance|7.8|James Ivory|Anthony Hopkins|Emma Thompson
Naked|1993|Comedy,Drama|7.8|Mike Leigh|David Thewlis|Lesley Sharp
The Fugitive|1993|Action,Crime,Drama|7.8|Andrew Davis|Harrison Ford|Tommy Lee Jones
A Bronx Tale|1993|Crime,Drama,Romance|7.8|Robert De Niro|Robert De Niro|Chazz Palminteri
Batman: Mask of the Phantasm|1993|Animation,Action,Crime|7.8|Kevin Altieri|Boyd Kirkland|Frank Paur
Lat sau san taam|1992|Action,Crime,Thriller|7.8|John Woo|Yun-Fat Chow|Tony Chiu-Wai Leung
Night on Earth|1991|Comedy,Drama|7.8|Jim Jarmusch|Winona Ryder|Gena Rowlands
La double vie de Véronique|1991|Drama,Fantasy,Music|7.8|Krzysztof Kieslowski|Irène Jacob|Wladyslaw Kowalski
Boyz n the Hood|1991|Crime,Drama|7.8|John Singleton|Cuba Gooding Jr.|Laurence Fishburne
Misery|1990|Drama,Thriller|7.8|Rob Reiner|James Caan|Kathy Bates
Awakenings|1990|Biography,Drama|7.8|Penny Marshall|Robert De Niro|Robin Williams
Majo no takkyûbin|1989|Animation,Adventure,Drama|7.8|Hayao Miyazaki|Kirsten Dunst|Minami Takayama
Glory|1989|Biography,Drama,History|7.8|Edward Zwick|Matthew Broderick|Denzel Washington
Dip huet seung hung|1989|Action,Crime,Drama|7.8|John Woo|Yun-Fat Chow|Danny Lee
Back to the Future Part II|1989|Adventure,Comedy,Sci-Fi|7.8|Robert Zemeckis|Michael J. Fox|Christopher Lloyd
Mississippi Burning|1988|Crime,Drama,History|7.8|Alan Parker|Gene Hackman|Willem Dafoe
Predator|1987|Action,Adventure,Sci-Fi|7.8|John McTiernan|Arnold Schwarzenegger|Carl Weathers
Evil Dead II|1987|Action,Comedy,Fantasy|7.8|Sam Raimi|Bruce Campbell|Sarah Berry
Ferris Bueller's Day Off|1986|Comedy|7.8|John Hughes|Matthew Broderick|Alan Ruck
Down by Law|1986|Comedy,Crime,Drama|7.8|Jim Jarmusch|Tom Waits|John Lurie
The Goonies|1985|Adventure,Comedy,Family|7.8|Richard Donner|Sean Astin|Josh Brolin
The Color Purple|1985|Drama|7.8|Steven Spielberg|Danny Glover|Whoopi Goldberg
The Breakfast Club|1985|Comedy,Drama|7.8|John Hughes|Emilio Estevez|Judd Nelson
The Killing Fields|1984|Biography,Drama,History|7.8|Roland Joffé|Sam Waterston|Haing S. Ngor
Ghostbusters|1984|Action,Comedy,Fantasy|7.8|Ivan Reitman|Bill Murray|Dan Aykroyd
The Right Stuff|1983|Adventure,Biography,Drama|7.8|Philip Kaufman|Sam Shepard|Scott Glenn
The King of Comedy|1982|Comedy,Crime,Drama|7.8|Martin Scorsese|Robert De Niro|Jerry Lewis
E.T. the Extra-Terrestrial|1982|Family,Sci-Fi|7.8|Steven Spielberg|Henry Thomas|Drew Barrymore
Kramer vs. Kramer|1979|Drama|7.8|Robert Benton|Dustin Hoffman|Meryl Streep
Days of Heaven|1978|Drama,Romance|7.8|Terrence Malick|Richard Gere|Brooke Adams
The Outlaw Josey Wales|1976|Western|7.8|Clint Eastwood|Clint Eastwood|Sondra Locke
The Man Who Would Be King|1975|Adventure,History,War|7.8|John Huston|Sean Connery|Michael Caine
The Conversation|1974|Drama,Mystery,Thriller|7.8|Francis Ford Coppola|Gene Hackman|John Cazale
La planète sauvage|1973|Animation,Sci-Fi|7.8|René Laloux|Barry Bostwick|Jennifer Drake
The Day of the Jackal|1973|Crime,Drama,Thriller|7.8|Fred Zinnemann|Edward Fox|Terence Alexander
Badlands|1973|Action,Crime,Drama|7.8|Terrence Malick|Martin Sheen|Sissy Spacek
Cabaret|1972|Drama,Music,Musical|7.8|Bob Fosse|Liza Minnelli|Michael York
Willy Wonka & the Chocolate Factory|1971|Family,Fantasy,Musical|7.8|Mel Stuart|Gene Wilder|Jack Albertson
Midnight Cowboy|1969|Drama|7.8|John Schlesinger|Dustin Hoffman|Jon Voight
Wait Until Dark|1967|Thriller|7.8|Terence Young|Audrey Hepburn|Alan Arkin
Guess Who's Coming to Dinner|1967|Comedy,Drama|7.8|Stanley Kramer|Spencer Tracy|Sidney Poitier
Bonnie and Clyde|1967|Action,Biography,Crime|7.8|Arthur Penn|Warren Beatty|Faye Dunaway
My Fair Lady|1964|Drama,Family,Musical|7.8|George Cukor|Audrey Hepburn|Rex Harrison
Mary Poppins|1964|Comedy,Family,Fantasy|7.8|Robert Stevenson|Julie Andrews|Dick Van Dyke
The Longest Day|1962|Action,Drama,History|7.8|Ken Annakin|Andrew Marton|Gerd Oswald
Jules et Jim|1962|Drama,Romance|7.8|François Truffaut|Jeanne Moreau|Oskar Werner
The Innocents|1961|Horror|7.8|Jack Clayton|Deborah Kerr|Peter Wyngarde
À bout de souffle|1960|Crime,Drama|7.8|Jean-Luc Godard|Jean-Paul Belmondo|Jean Seberg
Red River|1948|Action,Adventure,Drama|7.8|Howard Hawks|Arthur Rosson|John Wayne
Key Largo|1948|Action,Crime,Drama|7.8|John Huston|Humphrey Bogart|Edward G. Robinson
To Have and Have Not|1944|Adventure,Comedy,Film-Noir|7.8|Howard Hawks|Humphrey Bogart|Lauren Bacall
Shadow of a Doubt|1943|Film-Noir,Thriller|7.8|Alfred Hitchcock|Teresa Wright|Joseph Cotten
Stagecoach|1939|Adventure,Drama,Western|7.8|John Ford|John Wayne|Claire Trevor
The Lady Vanishes|1938|Mystery,Thriller|7.8|Alfred Hitchcock|Margaret Lockwood|Michael Redgrave
Bringing Up Baby|1938|Comedy,Family,Romance|7.8|Howard Hawks|Katharine Hepburn|Cary Grant
Bride of Frankenstein|1935|Drama,Horror,Sci-Fi|7.8|James Whale|Boris Karloff|Elsa Lanchester
Duck Soup|1933|Comedy,Musical,War|7.8|Leo McCarey|Groucho Marx|Harpo Marx
Scarface: The Shame of the Nation|1932|Action,Crime,Drama|7.8|Howard Hawks|Richard Rosson|Paul Muni
Frankenstein|1931|Drama,Horror,Sci-Fi|7.8|James Whale|Colin Clive|Mae Clarke
Roma|2018|Drama|7.7|Alfonso Cuarón|Yalitza Aparicio|Marina de Tavira
God's Own Country|2017|Drama,Romance|7.7|Francis Lee|Josh O'Connor|Alec Secareanu
Deadpool 2|2018|Action,Adventure,Comedy|7.7|David Leitch|Ryan Reynolds|Josh Brolin
Wind River|2017|Crime,Drama,Mystery|7.7|Taylor Sheridan|Kelsey Asbille|Jeremy Renner
Get Out|2017|Horror,Mystery,Thriller|7.7|Jordan Peele|Daniel Kaluuya|Allison Williams
Mission: Impossible - Fallout|2018|Action,Adventure,Thriller|7.7|Christopher McQuarrie|Tom Cruise|Henry Cavill
En man som heter Ove|2015|Comedy,Drama,Romance|7.7|Hannes Holm|Rolf Lassgård|Bahar Pars
What We Do in the Shadows|2014|Comedy,Horror|7.7|Jemaine Clement|Taika Waititi|Jemaine Clement
Omoide no Mânî|2014|Animation,Drama,Family|7.7|James Simone|Hiromasa Yonebayashi|Sara Takatsuki
The Theory of Everything|2014|Biography,Drama,Romance|7.7|James Marsh|Eddie Redmayne|Felicity Jones
Kingsman: The Secret Service|2014|Action,Adventure,Comedy|7.7|Matthew Vaughn|Colin Firth|Taron Egerton
The Fault in Our Stars|2014|Drama,Romance|7.7|Josh Boone|Shailene Woodley|Ansel Elgort
Me and Earl and the Dying Girl|2015|Comedy,Drama|7.7|Alfonso Gomez-Rejon|Thomas Mann|RJ Cyler
Birdman or (The Unexpected Virtue of Ignorance)|2014|Comedy,Drama|7.7|Alejandro G. Iñárritu|Michael Keaton|Zach Galifianakis
La vie d'Adèle|2013|Drama,Romance|7.7|Abdellatif Kechiche|Léa Seydoux|Adèle Exarchopoulos
Kai po che!|2013|Drama,Sport|7.7|Abhishek Kapoor|Amit Sadh|Sushant Singh Rajput
The Broken Circle Breakdown|2012|Drama,Music,Romance|7.7|Felix van Groeningen|Veerle Baetens|Johan Heldenbergh
Captain America: The Winter Soldier|2014|Action,Adventure,Sci-Fi|7.7|Anthony Russo|Joe Russo|Chris Evans
Rockstar|2011|Drama,Music,Musical|7.7|Imtiaz Ali|Ranbir Kapoor|Nargis Fakhri
Nebraska|2013|Adventure,Comedy,Drama|7.7|Alexander Payne|Bruce Dern|Will Forte
Wreck-It Ralph|2012|Animation,Adventure,Comedy|7.7|Rich Moore|John C. Reilly|Jack McBrayer
Le Petit Prince|2015|Animation,Adventure,Drama|7.7|Mark Osborne|Jeff Bridges|Mackenzie Foy
Detachment|2011|Drama|7.7|Tony Kaye|Adrien Brody|Christina Hendricks
Midnight in Paris|2011|Comedy,Fantasy,Romance|7.7|Woody Allen|Owen Wilson|Rachel McAdams
The Lego Movie|2014|Animation,Action,Adventure|7.7|Christopher Miller|Phil Lord|Chris Pratt
Gravity|2013|Drama,Sci-Fi,Thriller|7.7|Alfonso Cuarón|Sandra Bullock|George Clooney
Star Trek Into Darkness|2013|Action,Adventure,Sci-Fi|7.7|J.J. Abrams|Chris Pine|Zachary Quinto
Beasts of No Nation|2015|Drama,War|7.7|Cary Joji Fukunaga|Abraham Attah|Emmanuel Affadzi
The Social Network|2010|Biography,Drama|7.7|David Fincher|Jesse Eisenberg|Andrew Garfield
X: First Class|2011|Action,Adventure,Sci-Fi|7.7|Matthew Vaughn|James McAvoy|Michael Fassbender
The Hangover|2009|Comedy|7.7|Todd Phillips|Zach Galifianakis|Bradley Cooper
Skyfall|2012|Action,Adventure,Thriller|7.7|Sam Mendes|Daniel Craig|Javier Bardem
Silver Linings Playbook|2012|Comedy,Drama,Romance|7.7|David O. Russell|Bradley Cooper|Jennifer Lawrence
Argo|2012|Biography,Drama,Thriller|7.7|Ben Affleck|Ben Affleck|Bryan Cranston
(500) Days of Summer|2009|Comedy,Drama,Romance|7.7|Marc Webb|Zooey Deschanel|Joseph Gordon-Levitt
Harry Potter and the Deathly Hallows: Part 1|2010|Adventure,Family,Fantasy|7.7|David Yates|Daniel Radcliffe|Emma Watson
Gake no ue no Ponyo|2008|Animation,Adventure,Comedy|7.7|Hayao Miyazaki|Cate Blanchett|Matt Damon
Frost/Nixon|2008|Biography,Drama,History|7.7|Ron Howard|Frank Langella|Michael Sheen
Papurika|2006|Animation,Drama,Fantasy|7.7|Satoshi Kon|Megumi Hayashibara|Tôru Emori
Changeling|2008|Biography,Crime,Drama|7.7|Clint Eastwood|Angelina Jolie|Colm Feore
Flipped|2010|Comedy,Drama,Romance|7.7|Rob Reiner|Madeline Carroll|Callan McAuliffe
Toki o kakeru shôjo|2006|Animation,Adventure,Comedy|7.7|Mamoru Hosoda|Riisa Naka|Takuya Ishida
Death Note: Desu nôto|2006|Crime,Drama,Fantasy|7.7|Shûsuke Kaneko|Tatsuya Fujiwara|Ken'ichi Matsuyama
This Is England|2006|Crime,Drama|7.7|Shane Meadows|Thomas Turgoose|Stephen Graham
Ex Machina|2014|Drama,Sci-Fi,Thriller|7.7|Alex Garland|Alicia Vikander|Domhnall Gleeson
Efter brylluppet|2006|Drama|7.7|Susanne Bier|Mads Mikkelsen|Sidse Babett Knudsen
The Last King of Scotland|2006|Biography,Drama,History|7.7|Kevin Macdonald|James McAvoy|Forest Whitaker
Zodiac|2007|Crime,Drama,Mystery|7.7|David Fincher|Jake Gyllenhaal|Robert Downey Jr.
Lucky Number Slevin|2006|Action,Crime,Drama|7.7|Paul McGuigan|Josh Hartnett|Ben Kingsley
Joyeux Noël|2005|Drama,History,Music|7.7|Christian Carion|Diane Kruger|Benno Fürmann
Control|2007|Biography,Drama,Music|7.7|Anton Corbijn|Sam Riley|Samantha Morton
Tangled|2010|Animation,Adventure,Comedy|7.7|Nathan Greno|Byron Howard|Mandy Moore
Zwartboek|2006|Drama,Thriller,War|7.7|Paul Verhoeven|Carice van Houten|Sebastian Koch
Brokeback Mountain|2005|Drama,Romance|7.7|Ang Lee|Jake Gyllenhaal|Heath Ledger
3:10 to Yuma|2007|Action,Crime,Drama|7.7|James Mangold|Russell Crowe|Christian Bale
Crash|2004|Crime,Drama,Thriller|7.7|Paul Haggis|Don Cheadle|Sandra Bullock
Kung fu|2004|Action,Comedy,Fantasy|7.7|Stephen Chow|Stephen Chow|Wah Yuen
The Bourne Supremacy|2004|Action,Mystery,Thriller|7.7|Paul Greengrass|Matt Damon|Franka Potente
The Machinist|2004|Drama,Thriller|7.7|Brad Anderson|Christian Bale|Jennifer Jason Leigh
Ray|2004|Biography,Drama,Music|7.7|Taylor Hackford|Jamie Foxx|Regina King
Lost in Translation|2003|Comedy,Drama|7.7|Sofia Coppola|Bill Murray|Scarlett Johansson
Harry Potter and the Goblet of Fire|2005|Adventure,Family,Fantasy|7.7|Mike Newell|Daniel Radcliffe|Emma Watson
Man on Fire|2004|Action,Crime,Drama|7.7|Tony Scott|Denzel Washington|Christopher Walken
Coraline|2009|Animation,Drama,Family|7.7|Henry Selick|Dakota Fanning|Teri Hatcher
The Last Samurai|2003|Action,Drama|7.7|Edward Zwick|Tom Cruise|Ken Watanabe
The Magdalene Sisters|2002|Drama|7.7|Peter Mullan|Eileen Walsh|Dorothy Duffy
Good Bye Lenin!|2003|Comedy,Drama,Romance|7.7|Wolfgang Becker|Daniel Brühl|Katrin Saß
In America|2002|Drama|7.7|Jim Sheridan|Paddy Considine|Samantha Morton
I Am Sam|2001|Drama|7.7|Jessie Nelson|Sean Penn|Michelle Pfeiffer
Adaptation.|2002|Comedy,Drama|7.7|Spike Jonze|Nicolas Cage|Meryl Streep
Black Hawk Down|2001|Drama,History,War|7.7|Ridley Scott|Josh Hartnett|Ewan McGregor
Road to Perdition|2002|Crime,Drama,Thriller|7.7|Sam Mendes|Tom Hanks|Tyler Hoechlin
Das Experiment|2001|Drama,Thriller|7.7|Oliver Hirschbiegel|Moritz Bleibtreu|Christian Berkel
Billy Elliot|2000|Drama,Music|7.7|Stephen Daldry|Jamie Bell|Julie Walters
Hedwig and the Angry Inch|2001|Comedy,Drama,Music|7.7|John Cameron Mitchell|John Cameron Mitchell|Miriam Shor
Ocean's Eleven|2001|Crime,Thriller|7.7|Steven Soderbergh|George Clooney|Brad Pitt
Vampire Hunter D: Bloodlust|2000|Animation,Action,Fantasy|7.7|Yoshiaki Kawajiri|Andrew Philpot|John Rafter Lee
O Brother, Where Art Thou?|2000|Adventure,Comedy,Crime|7.7|Joel Coen|Ethan Coen|George Clooney
Interstate 60: Episodes of the Road|2002|Adventure,Comedy,Drama|7.7|Bob Gale|James Marsden|Gary Oldman
South Park: Bigger, Longer & Uncut|1999|Animation,Comedy,Fantasy|7.7|Trey Parker|Trey Parker|Matt Stone
Office Space|1999|Comedy|7.7|Mike Judge|Ron Livingston|Jennifer Aniston
Happiness|1998|Comedy,Drama|7.7|Todd Solondz|Jane Adams|Jon Lovitz
Training Day|2001|Crime,Drama,Thriller|7.7|Antoine Fuqua|Denzel Washington|Ethan Hawke
Rushmore|1998|Comedy,Drama,Romance|7.7|Wes Anderson|Jason Schwartzman|Bill Murray
Abre los ojos|1997|Drama,Mystery,Sci-Fi|7.7|Alejandro Amenábar|Eduardo Noriega|Penélope Cruz
Being John Malkovich|1999|Comedy,Drama,Fantasy|7.7|Spike Jonze|John Cusack|Cameron Diaz
As Good as It Gets|1997|Comedy,Drama,Romance|7.7|James L. Brooks|Jack Nicholson|Helen Hunt
The Fifth Element|1997|Action,Adventure,Sci-Fi|7.7|Luc Besson|Bruce Willis|Milla Jovovich
Le dîner de cons|1998|Comedy|7.7|Francis Veber|Thierry Lhermitte|Jacques Villeret
Donnie Brasco|1997|Biography,Crime,Drama|7.7|Mike Newell|Al Pacino|Johnny Depp
Shine|1996|Biography,Drama,Music|7.7|Scott Hicks|Geoffrey Rush|Armin Mueller-Stahl
Primal Fear|1996|Crime,Drama,Mystery|7.7|Gregory Hoblit|Richard Gere|Laura Linney
Hamlet|1996|Drama|7.7|Kenneth Branagh|Kenneth Branagh|Julie Christie
A Little Princess|1995|Drama,Family,Fantasy|7.7|Alfonso Cuarón|Liesel Matthews|Eleanor Bron
Do lok tin si|1995|Comedy,Crime,Drama|7.7|Kar-Wai Wong|Leon Lai|Michelle Reis
Il postino|1994|Biography,Comedy,Drama|7.7|Michael Radford|Massimo Troisi|Massimo Troisi
Clerks|1994|Comedy|7.7|Kevin Smith|Brian O'Halloran|Jeff Anderson
Short Cuts|1993|Comedy,Drama|7.7|Robert Altman|Andie MacDowell|Julianne Moore
Philadelphia|1993|Drama|7.7|Jonathan Demme|Tom Hanks|Denzel Washington
The Muppet Christmas Carol|1992|Comedy,Drama,Family|7.7|Brian Henson|Michael Caine|Kermit the Frog
Malcolm X|1992|Biography,Drama,History|7.7|Spike Lee|Denzel Washington|Angela Bassett
The Last of the Mohicans|1992|Action,Adventure,Drama|7.7|Michael Mann|Daniel Day-Lewis|Madeleine Stowe
Kurenai no buta|1992|Animation,Adventure,Comedy|7.7|Hayao Miyazaki|Shûichirô Moriyama|Tokiko Katô
Glengarry Glen Ross|1992|Crime,Drama,Mystery|7.7|James Foley|Al Pacino|Jack Lemmon
A Few Good Men|1992|Drama,Thriller|7.7|Rob Reiner|Tom Cruise|Jack Nicholson
Fried Green Tomatoes|1991|Drama|7.7|Jon Avnet|Kathy Bates|Jessica Tandy
Barton Fink|1991|Comedy,Drama,Thriller|7.7|Joel Coen|Ethan Coen|John Turturro
Miller's Crossing|1990|Crime,Drama,Thriller|7.7|Joel Coen|Ethan Coen|Gabriel Byrne
Who Framed Roger Rabbit|1988|Animation,Adventure,Comedy|7.7|Robert Zemeckis|Bob Hoskins|Christopher Lloyd
Spoorloos|1988|Mystery,Thriller|7.7|George Sluizer|Bernard-Pierre Donnadieu|Gene Bervoets
Withnail & I|1987|Comedy,Drama|7.7|Bruce Robinson|Richard E. Grant|Paul McGann
The Last Emperor|1987|Biography,Drama,History|7.7|Bernardo Bertolucci|John Lone|Joan Chen
Empire of the Sun|1987|Action,Drama,History|7.7|Steven Spielberg|Christian Bale|John Malkovich
Der Name der Rose|1986|Crime,Drama,Mystery|7.7|Jean-Jacques Annaud|Sean Connery|Christian Slater
Blue Velvet|1986|Drama,Mystery,Thriller|7.7|David Lynch|Isabella Rossellini|Kyle MacLachlan
The Purple Rose of Cairo|1985|Comedy,Fantasy,Romance|7.7|Woody Allen|Mia Farrow|Jeff Daniels
After Hours|1985|Comedy,Crime,Drama|7.7|Martin Scorsese|Griffin Dunne|Rosanna Arquette
Zelig|1983|Comedy|7.7|Woody Allen|Woody Allen|Mia Farrow
The Verdict|1982|Drama|7.7|Sidney Lumet|Paul Newman|Charlotte Rampling
Star Trek II: The Wrath of Khan|1982|Action,Adventure,Sci-Fi|7.7|Nicholas Meyer|William Shatner|Leonard Nimoy
First Blood|1982|Action,Adventure|7.7|Ted Kotcheff|Sylvester Stallone|Brian Dennehy
Ordinary People|1980|Drama|7.7|Robert Redford|Donald Sutherland|Mary Tyler Moore
Airplane!|1980|Comedy|7.7|Jim Abrahams|David Zucker|Jerry Zucker
Rupan sansei: Kariosutoro no shiro|1979|Animation,Adventure,Family|7.7|Hayao Miyazaki|Yasuo Yamada|Eiko Masuyama
Halloween|1978|Horror,Thriller|7.7|John Carpenter|Donald Pleasence|Jamie Lee Curtis
Le locataire|1976|Drama,Thriller|7.7|Roman Polanski|Roman Polanski|Isabelle Adjani
Love and Death|1975|Comedy,War|7.7|Woody Allen|Woody Allen|Diane Keaton
The Taking of Pelham One Two Three|1974|Action,Crime,Thriller|7.7|Joseph Sargent|Walter Matthau|Robert Shaw
Blazing Saddles|1974|Comedy,Western|7.7|Mel Brooks|Cleavon Little|Gene Wilder
Serpico|1973|Biography,Crime,Drama|7.7|Sidney Lumet|Al Pacino|John Randolph
Enter the Dragon|1973|Action,Crime,Drama|7.7|Robert Clouse|Bruce Lee|John Saxon
Deliverance|1972|Adventure,Drama,Thriller|7.7|John Boorman|Jon Voight|Burt Reynolds
The French Connection|1971|Action,Crime,Drama|7.7|William Friedkin|Gene Hackman|Roy Scheider
Dirty Harry|1971|Action,Crime,Thriller|7.7|Don Siegel|Clint Eastwood|Andrew Robinson
Where Eagles Dare|1968|Action,Adventure,War|7.7|Brian G. Hutton|Richard Burton|Clint Eastwood
The Odd Couple|1968|Comedy|7.7|Gene Saks|Jack Lemmon|Walter Matthau
The Dirty Dozen|1967|Action,Adventure,War|7.7|Robert Aldrich|Lee Marvin|Ernest Borgnine
Belle de jour|1967|Drama,Romance|7.7|Luis Buñuel|Catherine Deneuve|Jean Sorel
A Man for All Seasons|1966|Biography,Drama,History|7.7|Fred Zinnemann|Paul Scofield|Wendy Hiller
Repulsion|1965|Drama,Horror,Thriller|7.7|Roman Polanski|Catherine Deneuve|Ian Hendry
Zulu|1964|Drama,History,War|7.7|Cy Endfield|Stanley Baker|Jack Hawkins
Goldfinger|1964|Action,Adventure,Thriller|7.7|Guy Hamilton|Sean Connery|Gert Fröbe
The Birds|1963|Drama,Horror,Mystery|7.7|Alfred Hitchcock|Rod Taylor|Tippi Hedren
Cape Fear|1962|Drama,Thriller|7.7|J. Lee Thompson|Gregory Peck|Robert Mitchum
Peeping Tom|1960|Drama,Horror,Thriller|7.7|Michael Powell|Karlheinz Böhm|Anna Massey
The Magnificent Seven|1960|Action,Adventure,Western|7.7|John Sturges|Yul Brynner|Steve McQueen
Les yeux sans visage|1960|Drama,Horror|7.7|Georges Franju|Pierre Brasseur|Alida Valli
Invasion of the Body Snatchers|1956|Drama,Horror,Sci-Fi|7.7|Don Siegel|Kevin McCarthy|Dana Wynter
Rebel Without a Cause|1955|Drama|7.7|Nicholas Ray|James Dean|Natalie Wood
The Ladykillers|1955|Comedy,Crime|7.7|Alexander Mackendrick|Alec Guinness|Peter Sellers
Sabrina|1954|Comedy,Drama,Romance|7.7|Billy Wilder|Humphrey Bogart|Audrey Hepburn
The Quiet Man|1952|Comedy,Drama,Romance|7.7|John Ford|John Wayne|Maureen O'Hara
The Day the Earth Stood Still|1951|Drama,Sci-Fi|7.7|Robert Wise|Michael Rennie|Patricia Neal
The African Queen|1951|Adventure,Drama,Romance|7.7|John Huston|Humphrey Bogart|Katharine Hepburn
Gilda|1946|Drama,Film-Noir,Romance|7.7|Charles Vidor|Rita Hayworth|Glenn Ford
Fantasia|1940|Animation,Family,Fantasy|7.7|James Algar|Samuel Armstrong|Ford Beebe Jr.
The Invisible Man|1933|Horror,Sci-Fi|7.7|James Whale|Claude Rains|Gloria Stuart
Dark Waters|2019|Biography,Drama,History|7.6|Todd Haynes|Mark Ruffalo|Anne Hathaway
Searching|2018|Drama,Mystery,Thriller|7.6|Aneesh Chaganty|John Cho|Debra Messing
Once Upon a Time... in Hollywood|2019|Comedy,Drama|7.6|Quentin Tarantino|Leonardo DiCaprio|Brad Pitt
Nelyubov|2017|Drama|7.6|Andrey Zvyagintsev|Maryana Spivak|Aleksey Rozin
The Florida Project|2017|Drama|7.6|Sean Baker|Brooklynn Prince|Bria Vinaite
Just Mercy|2019|Biography,Crime,Drama|7.6|Destin Daniel Cretton|Michael B. Jordan|Jamie Foxx
Gifted|2017|Drama|7.6|Marc Webb|Chris Evans|Mckenna Grace
The Peanut Butter Falcon|2019|Adventure,Comedy,Drama|7.6|Tyler Nilson|Michael Schwartz|Zack Gottsagen
Victoria|2015|Crime,Drama,Romance|7.6|Sebastian Schipper|Laia Costa|Frederick Lau
Mustang|2015|Drama|7.6|Deniz Gamze Ergüven|Günes Sensoy|Doga Zeynep Doguslu
Guardians of the Galaxy Vol. 2|2017|Action,Adventure,Comedy|7.6|James Gunn|Chris Pratt|Zoe Saldana
Baby Driver|2017|Action,Crime,Drama|7.6|Edgar Wright|Ansel Elgort|Jon Bernthal
Only the Brave|2017|Action,Biography,Drama|7.6|Joseph Kosinski|Josh Brolin|Miles Teller
Bridge of Spies|2015|Drama,History,Thriller|7.6|Steven Spielberg|Tom Hanks|Mark Rylance
Incredibles 2|2018|Animation,Action,Adventure|7.6|Brad Bird|Craig T. Nelson|Holly Hunter
Moana|2016|Animation,Adventure,Comedy|7.6|Ron Clements|John Musker|Don Hall
Sicario|2015|Action,Crime,Drama|7.6|Denis Villeneuve|Emily Blunt|Josh Brolin
Creed|2015|Drama,Sport|7.6|Ryan Coogler|Michael B. Jordan|Sylvester Stallone
Leviafan|2014|Crime,Drama|7.6|Andrey Zvyagintsev|Aleksey Serebryakov|Elena Lyadova
Hell or High Water|2016|Action,Crime,Drama|7.6|David Mackenzie|Chris Pine|Ben Foster
Philomena|2013|Biography,Comedy,Drama|7.6|Stephen Frears|Judi Dench|Steve Coogan
Dawn of the Planet of the Apes|2014|Action,Adventure,Drama|7.6|Matt Reeves|Gary Oldman|Keri Russell
El cuerpo|2012|Mystery,Thriller|7.6|Oriol Paulo|Jose Coronado|Hugo Silva
Serbuan maut|2011|Action,Thriller|7.6|Gareth Evans|Iko Uwais|Ananda George
End of Watch|2012|Action,Crime,Drama|7.6|David Ayer|Jake Gyllenhaal|Michael Peña
Kari-gurashi no Arietti|2010|Animation,Adventure,Family|7.6|Hiromasa Yonebayashi|Amy Poehler|Mirai Shida
A Star Is Born|2018|Drama,Music,Romance|7.6|Bradley Cooper|Lady Gaga|Bradley Cooper
True Grit|2010|Drama,Western|7.6|Ethan Coen|Joel Coen|Jeff Bridges
Hævnen|2010|Drama,Romance|7.6|Susanne Bier|Mikael Persbrandt|Trine Dyrholm
Despicable Me|2010|Animation,Comedy,Crime|7.6|Pierre Coffin|Chris Renaud|Steve Carell
50/50|2011|Comedy,Drama,Romance|7.6|Jonathan Levine|Joseph Gordon-Levitt|Seth Rogen
Kick-Ass|2010|Action,Comedy,Crime|7.6|Matthew Vaughn|Aaron Taylor-Johnson|Nicolas Cage
Celda 211|2009|Action,Adventure,Crime|7.6|Daniel Monzón|Luis Tosar|Alberto Ammann
Moneyball|2011|Biography,Drama,Sport|7.6|Bennett Miller|Brad Pitt|Robin Wright
La piel que habito|2011|Drama,Horror,Thriller|7.6|Pedro Almodóvar|Antonio Banderas|Elena Anaya
Zombieland|2009|Adventure,Comedy,Fantasy|7.6|Ruben Fleischer|Jesse Eisenberg|Emma Stone
Die Welle|2008|Drama,Thriller|7.6|Dennis Gansel|Jürgen Vogel|Frederick Lau
Sherlock Holmes|2009|Action,Adventure,Mystery|7.6|Guy Ritchie|Robert Downey Jr.|Jude Law
The Blind Side|2009|Biography,Drama,Sport|7.6|John Lee Hancock|Quinton Aaron|Sandra Bullock
The Visitor|2007|Drama|7.6|Tom McCarthy|Richard Jenkins|Haaz Sleiman
Seven Pounds|2008|Drama|7.6|Gabriele Muccino|Will Smith|Rosario Dawson
Eastern Promises|2007|Action,Crime,Drama|7.6|David Cronenberg|Naomi Watts|Viggo Mortensen
Stardust|2007|Adventure,Family,Fantasy|7.6|Matthew Vaughn|Charlie Cox|Claire Danes
The Secret of Kells|2009|Animation,Adventure,Family|7.6|Tomm Moore|Nora Twomey|Evan McGuire
Inside Man|2006|Crime,Drama,Mystery|7.6|Spike Lee|Denzel Washington|Clive Owen
Gone Baby Gone|2007|Crime,Drama,Mystery|7.6|Ben Affleck|Morgan Freeman|Ed Harris
La Vie En Rose|2007|Biography,Drama,Music|7.6|Olivier Dahan|Marion Cotillard|Sylvie Testud
Huo Yuan Jia|2006|Action,Biography,Drama|7.6|Ronny Yu|Jet Li|Li Sun
The Illusionist|2006|Drama,Fantasy,Mystery|7.6|Neil Burger|Edward Norton|Jessica Biel
Dead Man's Shoes|2004|Crime,Drama,Thriller|7.6|Shane Meadows|Paddy Considine|Gary Stretch
Harry Potter and the Half-Blood Prince|2009|Action,Adventure,Family|7.6|David Yates|Daniel Radcliffe|Emma Watson
300|2006|Action,Drama|7.6|Zack Snyder|Gerard Butler|Lena Headey
Match Point|2005|Drama,Romance,Thriller|7.6|Woody Allen|Scarlett Johansson|Jonathan Rhys Meyers
Watchmen|2009|Action,Drama,Mystery|7.6|Zack Snyder|Jackie Earle Haley|Patrick Wilson
Lord of War|2005|Action,Crime,Drama|7.6|Andrew Niccol|Nicolas Cage|Ethan Hawke
Saw|2004|Horror,Mystery,Thriller|7.6|James Wan|Cary Elwes|Leigh Whannell
Synecdoche, New York|2008|Drama|7.6|Charlie Kaufman|Philip Seymour Hoffman|Samantha Morton
Mysterious Skin|2004|Drama|7.6|Gregg Araki|Brady Corbet|Joseph Gordon-Levitt
Jeux d'enfants|2003|Comedy,Drama,Romance|7.6|Yann Samuell|Guillaume Canet|Marion Cotillard
Un long dimanche de fiançailles|2004|Drama,Mystery,Romance|7.6|Jean-Pierre Jeunet|Audrey Tautou|Gaspard Ulliel
The Station Agent|2003|Comedy,Drama|7.6|Tom McCarthy|Peter Dinklage|Patricia Clarkson
21 Grams|2003|Crime,Drama,Thriller|7.6|Alejandro G. Iñárritu|Sean Penn|Benicio Del Toro
Boksuneun naui geot|2002|Crime,Drama,Thriller|7.6|Chan-wook Park|Kang-ho Song|Shin Ha-kyun
Finding Neverland|2004|Biography,Drama,Family|7.6|Marc Forster|Johnny Depp|Kate Winslet
25th Hour|2002|Drama|7.6|Spike Lee|Edward Norton|Barry Pepper
The Butterfly Effect|2004|Drama,Sci-Fi,Thriller|7.6|Eric Bress|J. Mackye Gruber|Ashton Kutcher
28 Days Later...|2002|Drama,Horror,Sci-Fi|7.6|Danny Boyle|Cillian Murphy|Naomie Harris
Batoru rowaiaru|2000|Action,Adventure,Drama|7.6|Kinji Fukasaku|Tatsuya Fujiwara|Aki Maeda
The Royal Tenenbaums|2001|Comedy,Drama|7.6|Wes Anderson|Gene Hackman|Gwyneth Paltrow
Y tu mamá también|2001|Drama|7.6|Alfonso Cuarón|Maribel Verdú|Gael García Bernal
Harry Potter and the Sorcerer's Stone|2001|Adventure,Family,Fantasy|7.6|Chris Columbus|Daniel Radcliffe|Rupert Grint
The Others|2001|Horror,Mystery,Thriller|7.6|Alejandro Amenábar|Nicole Kidman|Christopher Eccleston
Blow|2001|Biography,Crime,Drama|7.6|Ted Demme|Johnny Depp|Penélope Cruz
Enemy at the Gates|2001|Drama,History,War|7.6|Jean-Jacques Annaud|Jude Law|Ed Harris
Minority Report|2002|Action,Crime,Mystery|7.6|Steven Spielberg|Tom Cruise|Colin Farrell
The Hurricane|1999|Biography,Drama,Sport|7.6|Norman Jewison|Denzel Washington|Vicellous Shannon
American Psycho|2000|Comedy,Crime,Drama|7.6|Mary Harron|Christian Bale|Justin Theroux
Lola rennt|1998|Crime,Drama,Thriller|7.6|Tom Tykwer|Franka Potente|Moritz Bleibtreu
The Thin Red Line|1998|Drama,War|7.6|Terrence Malick|Jim Caviezel|Sean Penn
Mulan|1998|Animation,Adventure,Family|7.6|Tony Bancroft|Barry Cook|Ming-Na Wen
Fear and Loathing in Las Vegas|1998|Adventure,Comedy,Drama|7.6|Terry Gilliam|Johnny Depp|Benicio Del Toro
Funny Games|1997|Crime,Drama,Thriller|7.6|Michael Haneke|Susanne Lothar|Ulrich Mühe
Dark City|1998|Mystery,Sci-Fi,Thriller|7.6|Alex Proyas|Rufus Sewell|Kiefer Sutherland
Sleepers|1996|Crime,Drama,Thriller|7.6|Barry Levinson|Robert De Niro|Kevin Bacon
Lost Highway|1997|Mystery,Thriller|7.6|David Lynch|Bill Pullman|Patricia Arquette
Sense and Sensibility|1995|Drama,Romance|7.6|Ang Lee|Emma Thompson|Kate Winslet
Die Hard: With a Vengeance|1995|Action,Adventure,Thriller|7.6|John McTiernan|Bruce Willis|Jeremy Irons
Dead Man|1995|Adventure,Drama,Fantasy|7.6|Jim Jarmusch|Johnny Depp|Gary Farmer
The Bridges of Madison County|1995|Drama,Romance|7.6|Clint Eastwood|Clint Eastwood|Meryl Streep
Apollo 13|PG|Adventure,Drama,History|7.6|Ron Howard|Tom Hanks|Bill Paxton
Trois couleurs: Blanc|1994|Comedy,Drama,Romance|7.6|Krzysztof Kieslowski|Zbigniew Zamachowski|Julie Delpy
Falling Down|1993|Action,Crime,Drama|7.6|Joel Schumacher|Michael Douglas|Robert Duvall
Dazed and Confused|1993|Comedy|7.6|Richard Linklater|Jason London|Wiley Wiggins
My Cousin Vinny|1992|Comedy,Crime|7.6|Jonathan Lynn|Joe Pesci|Marisa Tomei
Omohide poro poro|1991|Animation,Drama,Romance|7.6|Isao Takahata|Miki Imai|Toshirô Yanagiba
Delicatessen|1991|Comedy,Crime|7.6|Marc Caro|Jean-Pierre Jeunet|Marie-Laure Dougnac
Home Alone|1990|Comedy,Family|7.6|Chris Columbus|Macaulay Culkin|Joe Pesci
The Godfather: Part III|1990|Crime,Drama|7.6|Francis Ford Coppola|Al Pacino|Diane Keaton
When Harry Met Sally...|1989|Comedy,Drama,Romance|7.6|Rob Reiner|Billy Crystal|Meg Ryan
The Little Mermaid|1989|Animation,Family,Fantasy|7.6|Ron Clements|John Musker|Jodi Benson
The Naked Gun: From the Files of Police Squad!|1988|Comedy,Crime|7.6|David Zucker|Leslie Nielsen|Priscilla Presley
Planes, Trains & Automobiles|1987|Comedy,Drama|7.6|John Hughes|Steve Martin|John Candy
Lethal Weapon|1987|Action,Crime,Thriller|7.6|Richard Donner|Mel Gibson|Danny Glover
Blood Simple|1984|Crime,Drama,Thriller|7.6|Joel Coen|Ethan Coen|John Getz
On Golden Pond|1981|Drama|7.6|Mark Rydell|Katharine Hepburn|Henry Fonda
Mad Max 2|1981|Action,Adventure,Sci-Fi|7.6|George Miller|Mel Gibson|Bruce Spence
The Warriors|1979|Action,Crime,Thriller|7.6|Walter Hill|Michael Beck|James Remar
The Muppet Movie|1979|Adventure,Comedy,Family|7.6|James Frawley|Jim Henson|Frank Oz
Escape from Alcatraz|1979|Action,Biography,Crime|7.6|Don Siegel|Clint Eastwood|Patrick McGoohan
Watership Down|1978|Animation,Adventure,Drama|7.6|Martin Rosen|John Hubley|John Hurt
Midnight Express|1978|Biography,Crime,Drama|7.6|Alan Parker|Brad Davis|Irene Miracle
Close Encounters of the Third Kind|1977|Drama,Sci-Fi|7.6|Steven Spielberg|Richard Dreyfuss|François Truffaut
The Long Goodbye|1973|Comedy,Crime,Drama|7.6|Robert Altman|Elliott Gould|Nina van Pallandt
Giù la testa|1971|Drama,War,Western|7.6|Sergio Leone|Rod Steiger|James Coburn
Kelly's Heroes|1970|Adventure,Comedy,War|7.6|Brian G. Hutton|Clint Eastwood|Telly Savalas
The Jungle Book|1967|Animation,Adventure,Family|7.6|Wolfgang Reitherman|Phil Harris|Sebastian Cabot
Blowup|1966|Drama,Mystery,Thriller|7.6|Michelangelo Antonioni|David Hemmings|Vanessa Redgrave
A Hard Day's Night|1964|Comedy,Music,Musical|7.6|Richard Lester|John Lennon|Paul McCartney
Breakfast at Tiffany's|1961|Comedy,Drama,Romance|7.6|Blake Edwards|Audrey Hepburn|George Peppard
Giant|1956|Drama,Western|7.6|George Stevens|Elizabeth Taylor|Rock Hudson
From Here to Eternity|1953|Drama,Romance,War|7.6|Fred Zinnemann|Burt Lancaster|Montgomery Clift
Lifeboat|1944|Drama,War|7.6|Alfred Hitchcock|Tallulah Bankhead|John Hodiak
The 39 Steps|1935|Crime,Mystery,Thriller|7.6|Alfred Hitchcock|Robert Donat|Madeleine Carroll
'''

with open("data.csv","w") as f : f.write(data_csv)

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
    
data_csv = '''X,Y,Type
3.514424835704529,3.80354339176155,c
-4.557945505385625,-5.589419579525727,c
-4.3903876914168976,0.24322780435462832,d
-2.116966947510181,7.806218107485899,e
-12.612257727006918,-13.081971449632146,a
-9.363912504065883,-6.17106153815503,d
12.58939763303236,-1.6510761992532998,b
4.118865883222618,4.480355011462123,c
-7.175140286190354,-0.26287742720310625,d
9.664993814621193,-3.477671628767073,e
11.159473787210214,9.008248862177595,e
-1.1992299622427383,3.9454692346567795,d
7.702387270343463,6.2959627935246605,b
7.449835647019956,6.446491023475581,b
-1.8373759508529108,-2.7807797177564977,b
-5.033869165763654,-4.50026570845038,e
-5.422759127550851,-12.047002405416812,a
4.927382888285469,5.494035659605024,e
-6.896071180338856,-2.041586092729812,e
-4.766903392191907,-4.355338136582851,b
-2.7353992600021,-2.0506613483779033,a
2.630618616548889,5.6680119242684635,c
5.923311878136267,2.617111463509069,c
10.021730929280753,-5.447709499048658,c
5.670283981743516,5.640411140497286,e
5.282030363327532,-5.245827216772547,e
6.504178145552274,4.487419079298183,c
6.9563825498730445,7.404423763083143,b
7.115712515831563,6.2394461798148875,b
12.911315070503196,-1.5006841846971692,b
13.563860969428095,13.652721286507322,b
7.868694215558092,5.070929114230406,b
-2.091182864567415,-1.9219556775621505,a
-5.52743370104974,-5.115255772916775,e
13.581213889454425,1.5893302270064673,b
0.7400428217469419,4.778611717647946,d
10.1603202915827,4.459689751826033,c
-3.8697398927970417,-4.407383149051373,e
-13.895777962911078,-12.77106244793054,a
-11.792814714702445,-11.851170511805721,a
4.886045762630742,3.3154456997206943,e
1.770612126867507,3.6926005080058735,d
-11.586693326733844,-11.138056646163754,a
5.169115299437015,3.823660525613635,c
-1.331770881289641,-2.4759575838220265,a
-9.023331471182598,-5.754460158198338,d
-2.14740466159095,-1.997068586330144,a
10.264873977623804,-5.136147889644473,c
9.435825948328946,-4.082074528075054,c
-14.112114262159947,-2.0917458729581355,a
12.418007691627661,-2.136772978692341,b
-7.97230439558415,9.762879032495569,e
9.287960188591121,8.61402574022068,b
-8.566986520494027,-6.541489455380383,d
2.704664558503522,4.634368787988622,d
3.5825003210006887,5.1094308336198955,e
2.5276518768471234,9.8957478945805,b
11.905647600131466,-2.2976917479873737,b
-1.5073892132961846,-2.217562368085583,a
4.595966152969602,4.583971945087069,c
5.05767536412486,4.64169712638105,e
-1.8777223517935004,-2.211327253214791,b
0.6416035500907533,3.0262751950701614,d
9.991892064160421,-4.4455224798074235,e
-3.706400863977212,-2.9147939540831356,b
3.991807270799436,4.301213262462062,c
-12.839936653560812,-11.33934363333291,a
-0.3604622003888416,3.7897953939022657,d
1.014273093090646,2.8005349291994266,d
3.8414546053258682,-10.487561716265784,a
9.611460125346277,-3.8107406229229985,e
-8.737711306757632,-5.5471318685305615,d
5.577131530369357,4.638407117543508,c
4.686375395241297,5.0916235791717686,e
-0.5931900544879998,-1.3681511307410879,a
9.736674465833607,-5.740501898750722,b
-5.990648187023464,10.377827541530412,c
10.713632217973744,-4.311827876794508,c
-3.258716014371826,-2.804276925097442,b
5.314280353758299,3.8811158975851328,e
-13.108588702994314,-13.123456363417437,a
10.133953107349312,-4.694300261081446,e
-0.5240637179306951,3.9612469844358853,d
-3.307279277598347,-2.850255082376091,a
9.385753115689852,-0.7802475177346846,e
9.39195715603482,-2.831842846651228,e
-2.5230782851031046,-2.3643228081193315,a
-3.2454179779757517,0.22434871235148357,a
-5.689851952251681,9.196468584253449,e
9.228892574141728,-5.71655163976157,c
-14.195072952331008,-13.146569808785767,a
-2.594650484457797,-2.9361810385009326,b
2.6156567987783754,2.750233489779011,d
-3.2498930344575783,-2.973650295381539,b
-8.089101820983453,-4.892784963510033,d
5.014421936544521,3.0568675172763067,c
-4.348392170616131,-4.3898959785555824,e
5.719670204217944,-5.800784194253468,d
-4.784602466662959,-4.849312479718635,e
-0.4897606620570194,-3.5354750194706175,a
5.894216595249801,-4.76072836923334,d
4.039455193954931,2.268415972979898,c
7.15170964504419,7.002399098426225,b
4.296912080259568,2.9957712038283524,e
6.96153704224931,6.783841729713992,b
5.978817230075646,6.338457656456157,b
3.701248822886207,6.024935780053058,e
5.538967275091585,-5.257953872332969,d
-9.286428030842018,-6.851376125766878,d
5.8906345079751565,-6.200477412728777,d
-0.8914247663294217,4.57262659913304,d
-0.2052314124042116,-0.8057213025309071,a
12.715131037511194,-2.8945981233904563,b
-11.06480277192597,-11.445933840457725,a
5.694072114665043,-4.1860415481966395,d
-3.240505985655691,-2.072256885729093,a
-2.7041392137123,-2.17579685167307,a
-2.810175887927309,-2.550736589047419,a
1.8003783273020808,2.129205224218301,d
4.182508367364531,4.287379573823669,c
-5.500777248962983,9.101166871555087,b
5.9019340656632355,-5.549492688560818,d
10.684785981549503,-5.457929942537166,c
1.8661203987341888,4.04551989796807,d
6.286271815654266,7.281698557903127,b
-5.192151219163003,-8.647634526710753,a
-4.421970302555195,-6.180092214378941,c
5.475485520026994,3.3241344146968332,c
6.051332738023393,5.2109499065035445,c
-2.3023067953246543,-2.1581129230383365,a
-1.1730726075475428,-0.8136707522595215,a
5.678655395833875,4.276804781851528,e
-9.243275267991365,-6.259753337156575,d
-4.123466660061589,-4.393626937627037,e
7.9573853321296655,7.075174955630821,b
-9.125125690777226,-6.30344391843553,d
5.010077132509476,4.597835789149412,e
0.3068070338973228,5.768975393492149,d
10.90246554162301,-4.810362640486183,c
-2.7742294100065656,-0.8117247100407985,a
2.8456639921136695,-10.357948440879486,a
4.559751639196252,6.042104265195598,e
5.782299748907246,4.345887552961695,c
9.886916749838853,-4.548726325824392,c
-4.878565350962754,-6.173899461294072,c
7.071360966328082,5.3142330713621,b
10.080088800039112,-4.602990352611027,c
0.062238151963981636,5.122254847599573,d
-3.098107893667425,-3.7483207470798474,a
2.5636349266626404,3.4205966737264353,d
11.623023999179718,-1.628278294724951,b
-5.065826956500147,-5.336256579269638,e
1.1830766999220335,3.6549062202987996,d
-1.899287193126193,-2.8485367085193913,a
7.000378919792489,-4.957455673740478,d
4.351100571791676,3.682122334798195,c
10.050782737608918,-3.588581420224231,e
5.128220380337294,-5.774175481794462,d
-3.2616641303223,-3.7883903596017987,e
-1.0470365120482668,-1.734380215608161,a
-6.528891400603225,-6.948197869077619,c
10.01774087563429,-3.23999773562572,e
7.238360368096735,6.926203895957752,b
3.1231801606805476,-9.660649137899869,a
4.54066956401985,2.9922062231163635,e
5.455163389255635,2.879636184891994,c
-1.2119551546467324,-2.1403825333328164,a
-0.07515509402959619,3.843550617279115,d
-8.036962207117803,-5.565660114068177,d
3.41310868911917,-10.310595127103117,a
11.193666457506367,-7.9746307888106,c
-7.9695019930820585,1.9025365040165596,e
4.833095416805497,5.41764003932332,e
6.131975703810662,4.055382866319732,e
5.387351392923361,-4.861401419787322,d
-9.201807120644999,-5.632599371085385,d
9.12360921712815,-4.205948610619377,e
-10.115542855762625,-0.4226083106633922,d
8.238170288147932,7.402678242945356,b
11.147225082581858,-2.146072691681189,b
6.31195619781087,6.16263860781093,b
2.0860422713746694,2.9194180658490327,d
-6.337343861196462,-7.95302892896159,c
5.802237754124948,5.243034085664753,c
-4.502478924754298,-2.471976473649671,a
12.456122568706745,-1.6798458521853155,b
9.566364299274257,-4.723786053711254,e
0.9955743926916862,3.033611228383977,d
0.7944522604854498,1.9874386504655384,a
-3.2981650164807146,-2.7175781614262315,a
10.687049652700408,-4.271296511326269,c
5.693371867867377,-3.90752644032737,c
-2.425035039569912,-2.6091529302504934,b
11.280216768204216,-1.3017896472321207,b
2.4772772618914694,10.784782195044738,c
1.442289062207717,-4.96760851480359,b
10.536043571205953,-4.907668242361449,c
10.75087201643775,-5.158468012901348,c
6.119321393088574,4.413960640838528,c
3.4441901605526457,5.2634003396805795,c
6.318456930480314,-5.983078133822344,d
-2.7677816132769824,-2.147867025364417,b
4.221307012848284,4.604475481464075,e
5.200857971774113,-5.430696352939604,d
-2.9587164890830007,-2.1745794713796993,a
-0.3649853717194178,3.9328019402316254,d
-5.20875652812035,-5.677441292257579,c
9.288685845426766,-4.415688433662683,c
9.294045019229888,-4.930554415110156,c
6.001923799121658,4.453487777697463,e
11.254141320197252,-3.1096657989204104,b
-12.000558831814072,-11.715507504072662,a
-5.452325405920631,-5.257590146685492,e
-5.6426898231281095,-5.032296797918411,e
10.903029682701892,-4.835020676864678,e
7.271407644631269,6.962487118678407,b
7.87823023214172,9.015199802304213,b
10.094079199394407,2.7985918314523577,e
-2.186262034595412,-2.4989649520369506,b
-2.503403808181119,4.649818701260045,b
-2.031343369440001,-3.16379439647738,a
12.398675703385342,-1.9382492127915247,b
-5.567495319714661,-7.022340609707626,c
-10.557617429936665,-7.5877907043155695,d
-9.615564010798147,-3.2287574775657735,a
-8.754699261325165,-6.066810297730381,d
-13.589586190359121,-13.289783530528718,a
7.776238459873799,5.429421800940043,b
-11.78768040582374,-11.742222906236854,a
1.5507136132473391,4.2026191024040465,a
'''

with open("data.csv","w") as f : f.write(data_csv)
    
