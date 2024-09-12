import turtle
import random

# Fenster erstellen
screen = turtle.Screen()
screen.title("Fantastisches Spirograph-Muster")
screen.bgcolor("black")

# Schildkröte erstellen
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)  # Maximale Geschwindigkeit der Schildkröte
t.pensize(2)  # Strichstärke der Linien

# Farbenliste
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan"]

# Funktion zum Zeichnen eines Spirographen
def draw_spirograph(radius, step_size):
    for _ in range(int(360 / step_size)):
        t.color(random.choice(colors))  # Wähle eine zufällige Farbe für jede Linie
        t.circle(radius)  # Zeichne einen Kreis
        t.right(step_size)  # Drehe die Schildkröte für den nächsten Kreis

# Spirograph-Muster zeichnen
radius = 100
step_size = 10
for _ in range(36):  # Zeichne 36 verschiedene Spirographen
    draw_spirograph(radius, step_size)
    radius += 20  # Erhöhe den Radius für den nächsten Spirographen
    step_size -= 0.1  # Reduziere den Schrittwinkel für komplexere Muster

# Hauptschleife des Programms
screen.mainloop()
