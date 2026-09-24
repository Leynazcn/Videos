import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Hipnotik Renkli Çiçek")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.colormode(255)

# ----------------------------------------------------
# 1. ADIM: ÖNCE GÖVDE VE YAPRAKLARI ÇİZİYORUZ
# ----------------------------------------------------

# 🌿 GÖVDE
t.penup()
t.goto(0, -20)        # Çiçeğin biraz altından başlatıyoruz
t.setheading(-90)     # Aşağı bak
t.pendown()

t.pencolor("forest green")
t.pensize(8)
t.forward(230)

# 🍃 SOL YAPRAK
t.penup()
t.goto(0, -100)
t.setheading(210)
t.pendown()

t.pencolor("limegreen")
t.pensize(3)

for i in range(2):
    t.circle(40, 60)
    t.left(120)

# 🍃 SAĞ YAPRAK
t.penup()
t.goto(0, -160)
t.setheading(-30)
t.pendown()

for i in range(2):
    t.circle(40, 60)
    t.left(120)

# 🍃 İKİNCİ YAPRAKLAR
t.penup()
t.goto(0, -210)
t.setheading(30)
t.pendown()

for i in range(2):
    t.circle(30, 60)
    t.left(120)

# ----------------------------------------------------
# 2. ADIM: ÇİÇEĞİ EN ÜSTE ÇİZİYORUZ
# ----------------------------------------------------

t.penup()
t.goto(0, 0)          # Tam merkeze geri dön
t.setheading(0)       # Açıyı sıfırla
t.pendown()

hue = 0.0
total_shapes = 60

# 🌸 ÇİÇEK (Gövdenin üstüne geleceği için bağlantı yerini örtecek)
for i in range(total_shapes):
    color = colorsys.hsv_to_rgb(hue, 0.9, 1)

    r = int(color[0] * 255)
    g = int(color[1] * 255)
    b = int(color[2] * 255)

    t.pencolor(r, g, b)
    t.pensize(i / 30 + 1)

    # Desen çizimi
    t.circle(i * 1.5, 90)
    t.left(90)
    t.circle(i * 1.5, 90)
    t.left(18)

    # Renk tonunu ilerlet
    hue += 0.01

# Pencere kapanmasın
turtle.done()