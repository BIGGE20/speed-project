import requests, json, turtle

iss = turtle.Turtle()

def setup(window):
    global iss

    window.setup(1000,500)
    window.setworldcoordinates(-180,-90,180,90)
    window.bgpic('earth.gif')
    
    turtle.register_shape('iss.gif')
    turtle.shape('iss.gif')

def move_iss(long,lat):
    global iss

    iss.penup()
    iss.hideturtle()
    iss.goto(long,lat)
    iss.pendown()
    iss.hideturtle()

def track_iss():
    url = "http://api.open-notify.org/iss-now.json"

    response = requests.get(url)


    if response.text == 200:
       response_dict = json.loads(response.text)
       position = response_dict['iss_position']
    
       lat = float(position['latitude'])
       long = float(position['longitud=e'])
       
       move_iss(lat,long)
    else:
        print(f"Badagry,there is a problem {response.status_code}")
    tracker = turtle.getcanvas()

def main():
    global iss

    screen = turtle.Screen()
    setup(screen)
    track_iss()

main()
turtle.mainloop()