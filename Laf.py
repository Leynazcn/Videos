import turtle
import random

# --- Ekran Ayarları ---
ekran = turtle.Screen()
ekran.title("Anlamlı Mesaj ve Havai Fişekler ✨")
ekran.bgcolor("#0F172A") # Koyu lacivert gece gökyüzü
ekran.setup(width=900, height=600)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# --- Fonksiyonlar ---

def havai_fisek_patlat(x, y, renkler):
    """Belirtilen noktada ışınsal havai fişek oluşturur."""
    fisek = turtle.Turtle()
    fisek.hideturtle()
    fisek.speed(0)
    fisek.penup()
    fisek.goto(x, y)
    fisek.pendown()
    
    isin_sayisi = 20
    for _ in range(isin_sayisi):
        fisek.color(random.choice(renkler))
        fisek.width(random.randint(1, 3))
        uzunluk = random.randint(30, 90)
        fisek.forward(uzunluk)
        fisek.backward(uzunluk)
        fisek.left(360 / isin_sayisi)

# --- Çizim Aşamaları ---

# 1. Havai Fişeklerin Çizimi
canli_renkler = ["#FF5733", "#33FF57", "#3380FF", "#F3FF33", "#FF33F3", "#00FFFF", "#FFD700"]

# Ekranın farklı yerlerinde 8 adet havai fişek patlatıyoruz
for _ in range(8):
    x_pos = random.randint(-380, 380)
    y_pos = random.randint(-150, 220)
    havai_fisek_patlat(x_pos, y_pos, canli_renkler)

# 2. Yazının Ekrana Basılması
mesaj = "Çok dar bakmazsan canın sıkılmaz böyle"

# Yazının arkasında parlama efekti için gölge
t.penup()
t.goto(2, -12) # Hafif kayık koordinat
t.color("#1E293B") # Koyu gölge rengi
t.write(mesaj, align="center", font=("Arial", 22, "bold"))

# Ana Beyaz Yazı
t.goto(0, -10)
t.color("#F8FAFC") # Parlak beyaz
t.write(mesaj, align="center", font=("Arial", 22, "bold"))

ekran.exitonclick()