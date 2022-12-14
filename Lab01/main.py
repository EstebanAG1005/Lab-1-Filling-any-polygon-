# SR1 Point 
# Graficas por computadora 
# Esteban Aldana Guerra 20591


from Filling import Render, color

r = Render()

width = 1000
height = 1000

# Se crea tamaño de pantalla
r.glCreateWindow(width, height)

# Color de fondo
r.glClearColor(0, 0, 0)

# Poligono 1
r.glColor(1,1,1)
cord = [(165, 380), (185, 360), (180, 330), (207, 345) , (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]
r.glFill(cord)

# Poligono 2
r.glColor(1,1,1)
cord = [(321, 335) ,(288, 286), (339, 251), (374, 302)]
r.glFill(cord)

# Poligono 3
r.glColor(1,1,1)
cord = [(377, 249) ,(411, 197), (436, 249)]
r.glFill(cord)

# Poligono 4
r.glColor(1,1,1)
cord = [(413, 177) ,(448, 159) ,(502, 88), (553, 53), (535, 36) ,(676, 37), (660, 52), (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230),(597, 215) ,(552, 214), (517, 144) ,(466, 180)]
r.glFill(cord)

# Poligono 5
r.glColor(0,0,0)
cord = [(682, 175) ,(708, 120) ,(735, 148) ,(739, 170)]
r.glFill(cord)

r.glFinish()