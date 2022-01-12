import turtle
#Ventana
wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#Marcador
MarcadorA = 0
MarcadorB = 0

#JugadorA
JugadorA = turtle.Turtle()
JugadorA.speed(0)
JugadorA.shape("square")
JugadorA.color("white")
JugadorA.penup()
JugadorA.goto(-350,0)
JugadorA.shapesize(stretch_wid=5, stretch_len=1)

#JugadorB
JugadorB = turtle.Turtle()
JugadorB.speed(0)
JugadorB.shape("square")
JugadorB.color("white")
JugadorB.penup()
JugadorB.goto(350,0)
JugadorB.shapesize(stretch_wid=5, stretch_len=1)

#Pelota
Pelota = turtle.Turtle()
Pelota.speed(0)
Pelota.shape("circle")
Pelota.color("white")
Pelota.penup()
Pelota.goto(0,0)

#Modificar estas variables para cambiar la velocidad de la pelota
Pelota.dx = 2
Pelota.dy = 2

#Linea Division
Division = turtle.Turtle()
Division.color("white")
Division.goto(0,400)
Division.goto(0,-400)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jugador A: 0		Jugador B: 0", align = "center", font=("Courier", 24, "normal"))

#Funciones
def jugadorA_up():
	y = JugadorA.ycor()
	y += 20
	JugadorA.sety(y)

def jugadorA_down():
	y = JugadorA.ycor()
	y -= 20
	JugadorA.sety(y)

def jugadorB_up():
	y = JugadorB.ycor()
	y += 20
	JugadorB.sety(y)

def jugadorB_down():
	y = JugadorB.ycor()
	y -= 20
	JugadorB.sety(y)

#Teclado
wn.listen()
wn.onkeypress(jugadorA_up, "w")
wn.onkeypress(jugadorA_down, "s")
wn.onkeypress(jugadorB_up, "Up")
wn.onkeypress(jugadorB_down, "Down")

while True:
	wn.update()

	Pelota.setx(Pelota.xcor() + Pelota.dx)
	Pelota.sety(Pelota.ycor() + Pelota.dy)

	#Revisa colisiones con los bordes de la ventana
	if Pelota.ycor() > 290:
		Pelota.dy *= -1
	if Pelota.ycor() < -290:
		Pelota.dy *= -1

	# Si la pelota sale por la izq o derecha, esta regresa al centro.
	if Pelota.xcor() > 390:
		Pelota.goto(0,0)
		Pelota.dx *= -1
		MarcadorA += 1
		pen.clear()
		pen.write("Jugador A: {}		Jugador B: {}".format(MarcadorA,MarcadorB), align = "center", font=("Courier", 24, "normal"))

	if Pelota.xcor() < -390:
		Pelota.goto(0,0)
		Pelota.dx *= -1
		MarcadorB += 1
		pen.clear()
		pen.write("Jugador A: {}		Jugador B: {}".format(MarcadorA,MarcadorB), align = "center", font=("Courier", 24, "normal"))

	if ((Pelota.xcor() > 340 and Pelota.xcor() < 350)
		and (Pelota.ycor() < JugadorB.ycor() + 50
		and Pelota.ycor() > JugadorB.ycor() - 50)):
		Pelota.dx *= -1
		Pelota.dy *= -1

	if ((Pelota.xcor() < -340 and Pelota.xcor() > -350)
		and (Pelota.ycor() < JugadorA.ycor() + 50
		and Pelota.ycor() > JugadorA.ycor() - 50)):
		Pelota.dx *= -1
		Pelota.dy *= -1