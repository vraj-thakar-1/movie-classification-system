""" 
- enter 'a'  to add a movie, 
- 'l'  to see your movie
- 'f' to find a movie
- 'q' to quit:

- Add a movie
- see your movie
- Find a movie
- stop running the program

Tasks:
[]: decide where to store movies
[]: what is the format of a movie
[]: Show the user the main interface and get their input
[]: Allow users to add a movie
[]: Show all their movies
[]: Find a  movie
[]: Stop the program
"""

movies= [{'name': 'vraj', 'director': 'vrajjj', 'year': 4934}, {'name': 'sdkjf', 'director': "skjf", 
'year': 3983}, {'name': 'slkjf;fj', 'director': 'fhsoif;h', 'year': 90348903}]
"""
movie={
    'name':(str),
    'director':(str),
    year:(int)
    
    }
"""

def menu():
    user_input = input(""" enter :
- 'a'  to add a movie, 
- 'l'  to see your movie
- 'f' to find a movie
- 'q' to quit 
- "s" to store
: """)
    while user_input != "q":
        if user_input == "a":
            print("Adding a movie")
            add_movie()
        elif user_input == "l":
            print("show movies")
            show_movie(movies)
        elif user_input == "f":
            print("find movies")
            find_movie()
        elif user_input == "s":
            print("store movies")
            store_movie(movies)
        else:
            print("Invalid input")
        user_input = input(""" enter :
- 'a'  to add a movie, 
- 'l'  to see your movie
- 'f' to find a movie
- 'q' to quit 
: """)



def add_movie():
    name=input('enter movie name: ')
    director =input('enter director name: ')
    year=int(input('enter year: '))
    movies.append(  {
    'name':name,
    'director':director,
    "year":year
    
    })

def show_movie(mov):
    print("----------------------------------------------------------------")
    for i in mov:
        print(f"movie name: {i['name']}")
        print(f"movie director: {i['director']}")  
        print(f"Year of Release : {i['year']}")
        print("----------------------------------------------------------------")
    

def find_movie():
    find_by = input("what property of the movie are you looking for [name/director/year]? :")
    if find_by == "name" or find_by == "director":
        looking_for = str(input ("what are you searching for? :"))
    else:
        looking_for = int(input ("what are you searching for? :"))
        
    founded =find_by_atttributes(looking_for,lambda x:x[find_by]) # anonymous functions passed by hof
    show_movie(founded)
    
def find_by_atttributes(expected, founder):
    # here founder is a function and return value of the searching element
    found=[]
    for i in movies:
        if expected==founder(i):
            found.append(i)
    return found
def store_movie(mov):
    with open("./movies.txt","w") as f:
        for i in mov:
            f.write(f""" movie name: {i['name']} \n movie director: {i['director']}\n Year of Release : {i['year']}\n ---------------------------------\n""")
        
    
menu()
print(movies)