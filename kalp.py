import turtle

# Ekran ayarları
ekran = turtle.Screen()
ekran.bgcolor("white")
ekran.title("Senin İçin Bir Kalp")

# Turtle ayarları
t = turtle.Turtle()
t.color("red")
t.begin_fill()
t.width(3)
t.speed(3) # Çizim hızı (1 en yavaş, 10 en hızlı)

# Kalbin sol tarafı
t.left(140)
t.forward(180)
t.circle(-90, 200)

# Kalbin sağ tarafı (yön düzeltme)
t.left(120)
t.circle(-90, 200)
t.forward(180)

# İçini doldur
t.end_fill()

# Çizim bittiğinde turtle'ı gizle
t.hideturtle()

# Ekrana tıklayınca kapanması için
ekran.exitonclick()