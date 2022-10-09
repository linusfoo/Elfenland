from tkinter import *
import os
import requests
import time
import json
import http.client
from multiprocessing import Process
from functools import partial
import pygame


# Designing window for registration
# label for register error remove
# join game display room 
# create game show waiting lobby
# IP = "24.48.89.199"
    
IP = "10.121.120.252"

def getCreator(id):
    import base64
    import json
    with open("savedGames.json",'r',encoding='utf-8') as file:
        file_data = json.load(file)  
        all_games = file_data["savedGames"]   
        for game in all_games:
            print(game["id"] , id)
            if game["id"] == id:
                host= game["host"]
                game_id = game["gameid"]
                break              
                # b = data.encode("utf-8")
                # b = base64.b64decode(b)
                # g = pickle.loads(b)
    return host, game_id

# IP = "10.121.181.187"
# IP = "localhost"

def quit(self):
    self.root.destroy()


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("600x350")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Register your account for Elfenland ", bg="yellow").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=2, bg="yellow", command=register_user).pack()


# window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("600x350")
    Label(login_screen, text="Please enter your username and password").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button
# pop up screen for successful registration
def register_user():
    username_info = username.get()
    password_info = password.get()
    headers = {'content-type': 'application/json'}
    url = 'http://' + IP + ':4242/oauth/token?grant_type=password&username=' + "maex" + '&password=' + "abc123_ABC123"
    x = requests.post(url, headers, auth=("bgp-client-name", "bgp-client-pw"))
    admin_access_token = validate_url(x.json()['access_token'])
    # print(admin_access_token)
    url = 'http://' + IP + ':4242/api/users/' + username_info + '?access_token=' + admin_access_token
    # print(url)
    headers = {'Content-Type': 'application/json'}
    body = {
        "name": username_info,
        "password": password_info,
        "preferredColour": "01FFFF",
        "role": "ROLE_PLAYER"
    }
    conn = http.client.HTTPConnection(IP + ':4242')
    conn.request('PUT', url, json.dumps(body), headers)
    res = conn.getresponse()
    data = res.read()
    # print(type(data))
    if res.status == 400:  # for force
        if data.decode('utf-8') == "Password does not comply to password policy. ":
            label = Label(register_screen, text=(data.decode(
                'utf-8') + "\nPassword must have at least 1 UpperCase, 1 LowerCase, 1 number and 1 special character"),
                          fg="green", font=("calibri", 11)).pack()

        else:
            Label(register_screen, text=(data.decode('utf-8') + "\nPlease try another username"), fg="green",
                  font=("calibri", 11)).pack()
    else:
        global registration_success
        registration_success = Toplevel(main_screen)
        registration_success.title("Registration Successful!")
        registration_success.geometry("150x150")
        Label(registration_success, text="Registration Successful!", fg="green", font=("calibri", 11)).pack()
        Button(registration_success, text="OK ", width=10, height=1, command=delete_registration_success).pack()

    username_entry.delete(0, END)
    password_entry.delete(0, END)


def delete_registration_success():
    registration_success.destroy()
    register_screen.withdraw()


def check_start(id):
    import http.client
    created = False
    while created == False:
        try:
            conn = http.client.HTTPConnection(IP + ':4242')
            conn.request('GET', '/api/sessions/' + id)
            res = conn.getresponse()
            data = res.read()
            created = True
        except:
            http.client.CONTINUE
    if created:
        return json.loads(data.decode('utf-8'))["launched"]

def getSaveGameID(id):
    import http.client
    created = False
    while created == False:
        try:
            conn = http.client.HTTPConnection(IP + ':4242')
            conn.request('GET', '/api/sessions/' + id)
            res = conn.getresponse()
            data = res.read()
            created = True
        except:
            http.client.CONTINUE
    if created:
        return json.loads(data.decode('utf-8'))["savegameid"]



# Implementing event on login button


def get_game_services():
    gameServices = []
    url = 'http://' + IP + ':4242/api/gameservices'
    req = requests.get(url)

    gameNames = req.json()

    for game in gameNames:
        gameServices.append(game["name"])

    return gameServices


def hasSavedGame():
    gameServices = get_game_services()
    playerList = []
    headers = {'content-type': 'application/json'}
    url = 'http://' + IP + ':4242/oauth/token?grant_type=password&username=' + "maex" + '&password=' + "abc123_ABC123"
    x = requests.post(url, headers, auth=("bgp-client-name", "bgp-client-pw"))
    admin_access_token = validate_url(x.json()['access_token'])

    for game in gameServices:
        url = 'http://' + IP + ':4242/api/gameservices/' + game + '/savegames?access_token=' + admin_access_token
        x = requests.get(url)
        games = x.json()
        print(games)
        for g in games:
            # print(g)
            playerList.extend(g["players"])

    print(*playerList)
    return playerList


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    # username1 = "marcus"
    # password1 = "ABC_abc123"
    import requests
    ##GET TOKEN
    headers = {'content-type': 'application/json'}
    import requests
    url = 'http://' + IP + ':4242/oauth/token?grant_type=password&username=' + username1 + '&password=' + password1
    x = requests.post(url, headers, auth=("bgp-client-name", "bgp-client-pw"))
    if (x.status_code != 200):
        if (x.status_code == 400):  # invalid username
            password_not_recognised()
    else:
        global access_token_player
        global username_player
        access_token_player = validate_url(x.json()['access_token'])
        username_player = username1

        players = hasSavedGame()
        # player has a saved game
        if username_player in players:
            print(hasSavedGame())
            login_success_relogin()
            print("executed relogin")
        else:
            login_success()
            print("login executed")


# return a list of available gameServices


def validate_url(org):
    if "+" in org:
        org = org.replace("+", "%2B")
    return org


# def create_session():
#     global create_game_screen
#     headers = {'Content-Type': 'application/json'}
#     body = {
#         "creator": username_player,
#         "game": "Elfenland",
#         "savegame": "",
#     }

#     conn = http.client.HTTPConnection( IP + ':4242')
#     conn.request('POST', '/api/sessions?access_token=' + access_token_player, json.dumps(body), headers)
#     res = conn.getresponse()
#     data = res.read()
#     # if res.status == 200:
#     print("game register success")
#     global game_ID
#     game_ID = data.decode('utf-8')

def registerGame():
    headers = {'Content-Type': 'application/json', 'authorization': 'Basic YmdwLWNsaWVudC1uYW1lOmJncC1jbGllbnQtcHc='}
    body = """{
        "location": 'http://10.121.120.252/Elfenland' ,
        "maxSessionPlayers": "6",
        "minSessionPlayers": "2",
        "name": "Elfenland",
        "displayName": "Elfenland",
        "webSupport": "true"
    }"""
    url = 'http://' + IP + ':4242/oauth/token?grant_type=password&username=' + "ELfanland" + '&password=' + "Group_11"
    x = requests.post(url, headers, auth=("bgp-client-name", "bgp-client-pw"))
    service_access_token = validate_url(x.json()['access_token'])

    url = 'http://' + IP + ':4242/api/gameservices/Elfenland?access_token=' + service_access_token

    req = requests.put(url, headers=headers, data=body)


def delete_all_sessions(ids):
    # import http.client
    for id in ids:
        conn = http.client.HTTPConnection(IP + ':4242')
        conn.request('DELETE', '/api/sessions/' + id + '?access_token=' + access_token_player)
        res = conn.getresponse()
        data = res.read()
        if res.status == 400:
            headers = {'content-type': 'application/json'}
            url = 'http://' + IP + ':4242/oauth/token?grant_type=password&username=' + "ELfanland" + '&password=' + "Group_11"
            x = requests.post(url, headers, auth=("bgp-client-name", "bgp-client-pw"))
            service_access_token = validate_url(x.json()['access_token'])
            # print(admin_access_token)

            conn = http.client.HTTPConnection(IP + ':4242')
            conn.request('DELETE', '/api/sessions/' + id + '?access_token=' + service_access_token)
            res = conn.getresponse()
            data = res.read()


def get_session_detail(id):
    import http.client
    created = False
    while created == False:
        try:
            conn = http.client.HTTPConnection(IP + ':4242')
            conn.request('GET', '/api/sessions/' + str(id))
            res = conn.getresponse()
            data = res.read()
            created = True
        except:
            continue
    if created:
        return data


def get_sessions():
    import requests
    url = 'http://' + IP + ':4242/api/sessions?hash=' + access_token_player
    headers = {'cookie': 'JSESSIONID=54B2765BECFB1BBFE5BE8B1442E45782',
               'authorization': 'Basic YmdwLWNsaWVudC1uYW1lOmJncC1jbGllbnQtcHc=', 'user-agent': 'advanced-rest-client',
               'accept': '*/*'}
    req = requests.get(url, headers=headers)
    # print(req.status_code)
    # print(req.headers)
    # print (req.json())
    game_ID_list = json.loads(req.text)["sessions"].keys()
    # delete_all_sessions(game_ID_list)
    # print(game_ID_list)
    sessions = []
    save_list= []
    id_list = []
    c = 0
    for id in game_ID_list:
       
        
        global owner
        launched = (list(req.json().get("sessions", {}).values())[c].get("launched"))
        owner = (list(req.json().get("sessions", {}).values())[c].get("creator"))
        save_id = (list(req.json().get("sessions", {}).values())[c].get("savegameid"))
        
        c += 1
             
        if not launched:
            print(id,launched,owner,save_id)
            id_list.append(id)
            if save_id != "" and len(save_list) >0 and  save_id in save_list:
                i = save_list.index(save_id)
                # sessions.pop(i)
                sessions[i] = "Host: " + owner + "\n (" + str(len(json.loads(req.text)["sessions"][id]["players"])) + "/6) - " + str(save_id)
                id_list[i] = id
                # save_list.append(save_id)s
            else:
                sessions.append(
                    "Host: " + owner + "\n (" + str(len(json.loads(req.text)["sessions"][id]["players"])) + "/6) - " + str(save_id))
                save_list.append(save_id)
    # print(id_list)
    return sessions, id_list


def join_session(id):
    created = False
    while created == False:
        try:
            conn = http.client.HTTPConnection(IP + ':4242')
            url = '/api/sessions/' + str(id) + '/players/' + username_player + '?access_token=' + access_token_player
            print(url)
            conn.request('PUT', url)
            res = conn.getresponse()
            data = res.read()
            created = True
            if res.status == 200:
                print("join success")
                # waiting_room_player(id)
            elif res.status == 400:
                print("already joined")
                break
            else:
                print(res.status, res.reason)
        except:
            continue


def quit_session(id):
    quit = False
    while quit == False:
        try:
            conn = http.client.HTTPConnection(IP + ':4242')
            conn.request('DELETE',
                         '/api/sessions/' + id + '/players/' + username_player + '?access_token=' + access_token_player)
            res = conn.getresponse()
            data = res.read()
            quit = True
        except:
            continue


# def start_player(id):
#     print(check_start(id))
#     if check_start(id):
#         print("start second client")
#         from client import main
#         p = Process(target=main)
#     else:
#         main_screen.after(500000, start_player(id))


def delete_login_success():
    login_success_screen.destroy()
    main_screen.withdraw()

    waiting()


def login_success():
    login_screen.destroy()
    main_screen.withdraw()
    global login_success_screen
    login_success_screen = Toplevel(main_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("550x300")


    Label(login_success_screen, text="Login Success! Which game do you want to play?", fg="green",
          font=("calibri", 14)).pack()
    Button(login_success_screen, text="Elfenland", width=30,
           height=4, command=delete_login_success).pack()
    Button(login_success_screen, text="Elfengold", width=30,
           height=4, command=delete_login_success).pack()


def login_success_relogin():
    login_screen.destroy()
    main_screen.withdraw()
    global login_success_relogin_screen
    login_success_relogin_screen = Toplevel(main_screen)
    login_success_relogin_screen.title("Welcome Back")
    login_success_relogin_screen.geometry("550x300")

    Label(login_success_relogin_screen, text="Login Success! Would you like to continue saved game?", fg="green",
          font=("calibri", 14)).pack()

    Button(login_success_relogin_screen, text="Load and continue saved game", width=30, height=4, command=load_game).pack()

    Button(login_success_relogin_screen, text="Join or create game", width=30,
           height=4, command=login_success).pack()


# Designing popup for log   in invalid password

def load_game():

    def create_button(x, y, width, height, hovercolor, defaultcolor,clicked):
        mouse = pygame.mouse.get_pos()
        # Mouse get pressed can run without an integer, but needs a 3 or 5 to indicate how many buttons
        click = pygame.mouse.get_pressed(3)
        toggle = False
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(screen, hovercolor, (x, y, width, height))
            if click[0] == 1:
                if toggle:
                    toggle = False
                    time.sleep(0.1)
                else:
                    toggle = True
                    time.sleep(0.1)
        else:
            pygame.draw.rect(screen, defaultcolor, (x, y, width, height))

        if toggle and clicked:
            return True
    global load_screen
    load_screen = Toplevel(main_screen)


    global font
    global screen
    global slategrey
    global lightgrey
    global blackish
    global white
    global smallfont
    global bigfont
    global darkgrey
    global salmon
    global lightsalmon
    global gold
    global NAVY_BLUE
    global screen_height
    global screen_width
    screen_width = 1435
    screen_height = 850
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.init()
    run = True
    FPS = 80
    WIDTH, HEIGHT = 1435, 850
    MAP_WIDTH = 900
    MAP_HEIGHT = 650
    LEFT_BORDER_WIDTH = 80
    TOP_BORDER_WIDTH = 80
    # Initialize constants
    font = pygame.font.SysFont("comicsansms", 30)
    smallfont = pygame.font.SysFont("comicsansms", 14)
    bigfont = pygame.font.SysFont("comicsansms", 35, bold=True)
    slategrey = (112, 128, 144)
    lightgrey = (165, 175, 185)
    darkgrey = (50, 50, 50)
    salmon = (250, 128, 114)
    lightsalmon = (255, 160, 122)
    blackish = (10, 10, 10)
    white = (255, 255, 255)
    black = (0, 0, 0)
    gold = (255, 215, 0)
    pygame.display.set_caption("load games")

    NAVY_BLUE = (42, 93, 142)


    header = font.render("Select Game to Load", True, white)
    back = font.render("Back", True, blackish)
    headers = {'content-type': 'application/json'}
    url = 'http://' + IP + ':4242/oauth/token?grant_type=password&username=' + "maex" + '&password=' + "abc123_ABC123"
    x = requests.post(url, headers, auth=("bgp-client-name", "bgp-client-pw"))
    admin_access_token = validate_url(x.json()['access_token'])
    backButton = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            screen.fill((0, 0, 0))
            backButton = create_button(25, 10, 150, 100, lightgrey, slategrey,event.type == pygame.MOUSEBUTTONDOWN)
            if backButton:
                pygame.quit()
                # break
            screen.blit(back, (70, 35))
            screen.blit(header, ((screen_width - header.get_width()) / 2, 70))

            gameServices = get_game_services()
            saved_game_list = []
            
            created = False
            for game in gameServices:
                # display = ""
                url = 'http://' + IP + ':4242/api/gameservices/' + game + '/savegames?access_token=' + admin_access_token
                x = requests.get(url)
                games = x.json()
                for g in games:
                    display = ""
                    display+= "ID: "+ str(g["savegameid"]) + "  [" + str(g["gamename"]) + "]"
                    saved_game_list.append(display)
        
                for i in range(0,len(games)):
                    p = font.render(saved_game_list[i], True, blackish)
                    playerButton = create_button(screen_width / 2 - 250, 205 + i * 100, 550, 75, slategrey, slategrey,event.type == pygame.MOUSEBUTTONDOWN)
                    screen.blit(p, ( screen_width / 2 - 250   + ( 225 -p.get_width()/2), 215 + i * 100))
                    if playerButton:
                        print("loading game")
                        ##GET GAME + createor
                        print(saved_game_list[i])
                        host, id = getCreator(games[i]["savegameid"])
                        if username_player == host:
                                   
                            while created == False:
                                try:
                                    headers = {'Content-Type': 'application/json'}
                                    body = {
                                        "creator": username_player,
                                        "game": "Elfenland",
                                        "savegame": games[i]["savegameid"],
                                    }

                                    conn = http.client.HTTPConnection(IP + ':4242')
                                    conn.request('POST', '/api/sessions?access_token=' + access_token_player, json.dumps(body), headers)
                                    res = conn.getresponse()
                                    data = res.read()
                                    # if res.status == 200:
                                    print("Session creation success")
                                    global game_ID
                                    game_ID = data.decode('utf-8')
                                    waiting_room = Waiting_room(username_player, game_ID)
                                    created = True
                                except:
                                    continue
                    
                    
                        else:
                            print("not host")
                        break
             
                if created:
               
                    waiting_room.display_host()


            pygame.display.update()  

                ##WAITINGROOM

            # a = create_button(screen_width / 2 - 250, 200 + (i * 100), 500, 75, darkgrey, darkgrey)
        pygame.display.update()
        
        
        




def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ", fg="red", font=("calibri", 11)).pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def launch_session(id):
    import requests

    headers = {'authorization': 'Basic YmdwLWNsaWVudC1uYW1lOmJncC1jbGllbnQtcHc='}
    url = 'http://' + IP + ':4242/api/sessions/' + str(id) + '?access_token=' + access_token_player
    x = requests.post(url, headers, auth=("bgp-client-name", "bgp-client-pw"))
    print(x.status_code)
    print("launched Session")

# def launch_session(id):
#     import requests

#     headers = {'authorization': 'Basic YmdwLWNsaWVudC1uYW1lOmJncC1jbGllbnQtcHc='}
#     url = 'http://' + IP + ':4242/api/sessions/' + str(id) + '?access_token=' + access_token_player
#     x = requests.post(url, headers, auth=("bgp-client-name", "bgp-client-pw"))
#     print(x.status_code)
#     print("launched Session")


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    registerGame()
    global main_screen
    global USERNAME
    main_screen = Tk()
    main_screen.geometry("500x350")
    main_screen.title("Account Login")
    Label(text="Welcome to Elfenland! Please select your choice", bg="yellow", width="300", height="2",
          font=("Calibri", 16)).pack()
    Label(text="").pack()
    Button(text="Login", height="3", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="3", width="30", command=register).pack()

    main_screen.mainloop()



def waiting():
    global font
    global screen
    global slategrey
    global lightgrey
    global blackish
    global white
    global smallfont
    global bigfont
    global darkgrey
    global salmon
    global lightsalmon
    global gold
    global NAVY_BLUE
    global screen_height
    global screen_width
    screen_width = 1435
    screen_height = 850
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.init()
    run = True
    FPS = 80
    WIDTH, HEIGHT = 1435, 850
    MAP_WIDTH = 900
    MAP_HEIGHT = 650
    LEFT_BORDER_WIDTH = 80
    TOP_BORDER_WIDTH = 80
    pygame.display.set_caption("Elfenroads")
    # Initialize constants
    font = pygame.font.SysFont("comicsansms", 30)
    smallfont = pygame.font.SysFont("comicsansms", 14)
    bigfont = pygame.font.SysFont("comicsansms", 35, bold=True)
    slategrey = (112, 128, 144)
    lightgrey = (165, 175, 185)
    darkgrey = (50, 50, 50)
    salmon = (250, 128, 114)
    lightsalmon = (255, 160, 122)
    blackish = (10, 10, 10)
    white = (255, 255, 255)
    black = (0, 0, 0)
    gold = (255, 215, 0)



    NAVY_BLUE = (42, 93, 142)


    selection()

def create_button(x, y, width, height, hovercolor, defaultcolor,clicked):
    mouse = pygame.mouse.get_pos()
    # Mouse get pressed can run without an integer, but needs a 3 or 5 to indicate how many buttons
    click = pygame.mouse.get_pressed(3)
    toggle = False
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hovercolor, (x, y, width, height))
        if click[0] == 1:
            if toggle:
                toggle = False
                # time.sleep(0.1)
            else:
                toggle = True
                # time.sleep(0.1)
    else:
        pygame.draw.rect(screen, defaultcolor, (x, y, width, height))

    if toggle and clicked:
        return True



def choose_menu():
    WelcomeText = font.render("Welcome to Elfenland! Please choose one of the following", True, slategrey)
    CreateText = font.render("Create New Game", True, blackish)
    JoinText = font.render("Join exisiting Game", True, blackish)
    QuitText = font.render("Quit", True, blackish)
    # blackText = font.render("Black", True, blackish)
    # purpleText = font.render("Purple", True, blackish)
    # greenText = font.render("Green", True, blackish)
    # yellowText = font.render("Yellow", True, blackish)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            screen.fill(NAVY_BLUE)
            screen.blit(WelcomeText, ((screen_width - WelcomeText.get_width()) / 2, 100))
            create = create_button((screen_width / 2 - 175), int(screen_height * .33) - 25, 300, 100, lightgrey,
                                slategrey,event.type == pygame.MOUSEBUTTONDOWN)
            screen.blit(CreateText, (screen_width / 2 - 150, int(screen_height * .33)))
            join = create_button((screen_width / 2 - 175), int(screen_height * .33) + 100, 300, 100, lightgrey,
                                slategrey,event.type == pygame.MOUSEBUTTONDOWN)
            screen.blit(JoinText, (screen_width / 2 - 155, int(screen_height * .33) + 125))
            quit = create_button((screen_width / 2 - 175), int(screen_height * .33) + 225, 300, 100, lightgrey,
                                slategrey,event.type == pygame.MOUSEBUTTONDOWN)
            screen.blit(QuitText, (screen_width / 2 - 50, int(screen_height * .33) + 255))

            if create:
                return "create"
            if join:
                return "join"
            if quit:
                pygame.quit()
                exit()

        
        pygame.display.update()

def createSession():
    created = False
    while created == False:
        try:
            headers = {'Content-Type': 'application/json'}
            body = {
                "creator": username_player,
                "game": "Elfenland",
                "savegame": "",
            }

            conn = http.client.HTTPConnection(IP + ':4242')
            conn.request('POST', '/api/sessions?access_token=' + access_token_player, json.dumps(body), headers)
            res = conn.getresponse()
            data = res.read()
            # if res.status == 200:
            print("Session creation success")
            global game_ID
            game_ID = data.decode('utf-8')
            waiting_room = Waiting_room(username_player, game_ID)
            created = True

        except:
            continue
    if created:
        waiting_room.display_host()

def join_session_screen():
    chooseText = font.render("Choose an existing game to join", True, slategrey)
    back = font.render("Back", True, blackish)
    while True:
        backButton = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            sessions, ids = get_sessions()

            screen.fill((0, 0, 0))
            backButton = create_button(25, 10, 150, 100, lightgrey, slategrey,event.type == pygame.MOUSEBUTTONDOWN)
            screen.blit(back, (70, 35))
            if backButton:
                break
            screen.blit(chooseText, ((screen_width - chooseText.get_width()) / 2, 100))
            s = len(sessions)
            for i in range(0, s):

                #change game id for 
                t = font.render(sessions[i], True, blackish)
                
                # if event.type == pygame.MOUSEBUTTONDOWN:
                joinButton = create_button(screen_width / 2 - 325, 200 + (i * 125), 650, 100, lightgrey, slategrey,event.type == pygame.MOUSEBUTTONDOWN)
                screen.blit(t, (screen_width / 2 - 225, 225 + (i * 125)))
                if joinButton:
                    join_session(ids[i])
                    w = Waiting_room(username_player, ids[i])
                    w.display_player()
        
                

               

     

            
        if backButton:
            selection()
        pygame.display.update()
class myButton:
    def __init__(self):
        self._text = "3"
        self.counter = 1

    def text(self):
        self.counter *= -1
        if self.counter < 0:
            self._text = "4"
        else:
            self._text = "3"

    def draw(self, x, y):
        myText = font.render(self._text, True, blackish)
        screen.blit(myText, (x, y))

class myButton1:
    def __init__(self):
        self._text = "No destination"
        self.counter = 1

    def text(self):
        self.counter *= -1
        if self.counter < 0:
            self._text = "With destination"
        else:
            self._text = "No destination"
    def text(self):
            self.counter *= -1
            if self.counter < 0:
                self._text = "With destination"
            else:
                self._text = "No destination"

    def draw(self, x, y):
        myText = font.render(self._text, True, blackish)
        screen.blit(myText, (x, y))

class Waiting_room:


    
    def __init__(self, player, gameID):
        self.player = player
        self.players = []
        self.id = gameID

    def display_host(self):
        owner = username_player
        from variant import Variant

        ret = ""

        playerText = font.render("Players in waiting room: ", True, slategrey)
        startGameText = font.render("startGame" + ret, True, blackish)
        back = font.render("Back", True, blackish)
        roundText = font.render("Game round:", True, slategrey)
        roundText1 = myButton()
        destText = font.render("Destination Town:", True, slategrey)
        destText1 = myButton1()

        while True:
            backButton = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                data = get_session_detail(self.id)
                self.players = json.loads(data)['players']

                screen.fill((0, 0, 0))
                backButton = create_button(25, 10, 150, 100, lightgrey, slategrey,event.type == pygame.MOUSEBUTTONDOWN)
                screen.blit(back, (70, 35))

                startButton = create_button(screen_width / 2 - 150, 750, 300, 100, lightsalmon, salmon,event.type == pygame.MOUSEBUTTONDOWN)
                screen.blit(playerText, ((screen_width - playerText.get_width()) / 2 - 200, 70))
                screen.blit(startGameText, (screen_width / 2 - 75, 775))
                for i in range(0, len(self.players)):
                    # if self.players[i] != self.player:
                    playerButton = create_button(screen_width / 2 - 450, 170 + (i * 100), 500, 75, slategrey, slategrey,event.type == pygame.MOUSEBUTTONDOWN)
                    p = font.render(self.players[i], True, blackish)
                    screen.blit(p, ((screen_width - p.get_width()) / 2 - 200, 185 + i * 100))
                for i in range(len(self.players), 6):
                    playerButton = create_button(screen_width / 2 - 450, 170 + (i * 100), 500, 75, darkgrey, darkgrey,event.type == pygame.MOUSEBUTTONDOWN)

                # game round
                screen.blit(roundText, ((screen_width - roundText.get_width()) / 2 + 400, 80))
                roundButton = create_button(screen_width / 2 + 250, 170, 300, 75, lightgrey, slategrey,event.type == pygame.MOUSEBUTTONDOWN)
                roundText1.draw(screen_width / 2 + 400, 190)
                if roundButton:
                    roundText1.text()
                    print(roundText1._text)

                # game destination
                screen.blit(destText, ((screen_width - roundText.get_width()) / 2 + 370, 280))
                destButton = create_button(screen_width / 2 + 250, 370, 300, 75, lightgrey, slategrey,event.type == pygame.MOUSEBUTTONDOWN)
                destText1.draw(screen_width / 2 + 275, 390)
                if destButton:
                    destText1.text()
                    print(destText1._text)

                if backButton:
                    delete_all_sessions([self.id])
                    print("session deleted")
                    break

                if startButton and len(self.players) >=3: ##TO CHANGE
                    saveID = getSaveGameID(self.id)
                    launch_session(self.id)
                    if saveID == '':
                        
                        from client import main
                        if roundText1._text == '3':
                            if destText1._text == "No destination":
                                return main(username_player, Variant.elfenland_org, len(self.players),owner,game_ID,saveID)
                            else:
                                return main(username_player, Variant.elfenland_destination, len(self.players),owner,game_ID,saveID)

                        else:
                            if destText1._text == "No destination":
                                return main(username_player, Variant.elfenland_4, len(self.players),owner,game_ID,saveID)
                            else:
                                return main(username_player, Variant.elfenland_destination_4, len(self.players),owner,game_ID,saveID)
                    else:
                        from loadedClient import main
                        main(username_player, None, len(self.players),owner,game_ID,saveID)


            if backButton:
                selection()

            pygame.display.update()
        

    def display_player(self):

        ret = ""
        for player in self.players:
            ret + player + "\n"
        playerText = font.render("Players in waiting room: \n" + ret, True, slategrey)
        back = font.render("Back", True, blackish)

        while True:
            backButton = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                # sessions, ids = get_sessions()
                # if not (self.id in ids):
                #     break

                data = get_session_detail(self.id)
                self.players = json.loads(data)['players']
                screen.fill((0, 0, 0))
                backButton = create_button(25, 10, 150, 100, lightgrey, slategrey,event.type == pygame.MOUSEBUTTONDOWN)
                screen.blit(back, (70, 35))
                # print(check_start(self.id) )
                if (check_start(self.id)):
                    from variant import Variant
                    saveID = getSaveGameID(self.id)
                    if saveID == '':
                        from client import main
                        main(username_player, None, None,owner,None,None)
                    else:
                        from loadedClient import main
                        main(username_player, None, None,owner,None,saveID)
                screen.blit(playerText, ((screen_width / 2 - 150, 100)))
                for i in range(0, len(self.players)):
                    #  if self.players[i] != self.player:
                    playerButton = create_button(screen_width / 2 - 250, 200 + (i * 100), 500, 75, slategrey, slategrey,event.type == pygame.MOUSEBUTTONDOWN)
                    p = font.render(self.players[i], True, blackish)
                    screen.blit(p, ((screen_width - p.get_width()) / 2, 215 + i * 100))
                for i in range(len(self.players), 6):
                    playerButton = create_button(screen_width / 2 - 250, 200 + (i * 100), 500, 75, darkgrey, darkgrey,event.type == pygame.MOUSEBUTTONDOWN)

                if backButton:
                    quit_session(self.id)
                    print("session quit")
                    break
            if backButton:
                break           
           
            pygame.display.update()

        join_session_screen()

    

    

def selection():
    choice = choose_menu()
    if choice == "create":
        createSession()
    if choice == "join":
        join_session_screen()

   


if __name__ == '__main__':
    main_account_screen()
