# Lab01
# Graficas por computadora 
# Esteban Aldana Guerra 20591

import struct


# 1 byte
def char(c):
    return struct.pack('=c', c.encode('ascii'))

# 2 bytes
def word(c):
    return struct.pack('=h', c)

# 4 bytes 
def dword(c):
    return struct.pack('=l', c)


# funcion de color
def color(r, g, b):
    return bytes([b, g, r])


class Render(object):
    def __init__(self):
        self.framebuffer = []     

    def glInit(self):
        pass

    # Se crea ventana
    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        
    # Se crea espacio de trabajo
    def glViewport(self, x, y, width, height):
        self.posXV = x
        self.posYV = y
        self.viewpWidth = width
        self.viewpHeight = height

    # Llena mapa de bits de un solo color
    def glClear(self):
        self.framebuffer = [
            [color(0, 0, 0) for x in range(self.width)]
            for y in range(self.height)
        ]

    # Cambia el color con el que funciona glClear
    def glClearColor(self, r, g, b):
        r = round(r*255)
        g = round(g*255)
        b = round(b*255)

        self.framebuffer = [
            [color(r, g, b) for x in range(self.width)]
            for y in range(self.height)
        ]

    # Cambiar colo de glVertex
    def glColor(self, r, g, b):
        r = round(r*255)
        g = round(g*255)
        b = round(b*255)
        self.color = color(r, g, b)

    # Se obtiene coordenada en x
    def glCordX(self, x):
        return round((x+1)*(self.viewpWidth/2)+self.posXV)

    # se obtiene coordenada en y
    def glCordY(self, y):
        return round((y+1)*(self.viewpHeight/2)+self.posYV)

    def point(self, x, y):
        self.framebuffer[y][x] = self.color

    def vertex(self, x, y):
        self.point(x, y)   
    
    # se debija la linea
    def line(self, x0, y0, x1, y1):
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        steep = dy > dx

        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        offset = 0
        threshold = dx
        y = y0
        inc = 1 if y1 > y0 else -1

        for x in range(x0, x1):
            if steep:
                self.point(y, x)
                if self.puntos.get(x) == None:
                    self.puntos[x] = []

                self.puntos[x] += [y]
            else:
                self.point(x, y)
                if self.puntos.get(y) == None:
                    self.puntos[y] = []

                self.puntos[y] += [x]

            offset += 2 * dy
            if offset >= threshold:
                y += inc
                threshold += 2 * dx

    
    # Esta parte de codigo eesta basada en esta pagina
    # https://handwiki.org/wiki/Even%E2%80%93odd_rule 
    def glFit(self, x, y, points):
        num = len(points)
        i = 0 
        j = num -1
        c = False

        for i in range(num):
            if ((points[i][1] >y) !=(points[j][1] >y )) and (x < points[i][0] + (points[j][0] - points[i][0]) * (y - points[i][1])/(points[j][1] - points[i][1])):
                c = not c
            j = i 
        return c

    def glFill(self, points):
        for x in range(self.width):
            for y in range(self.height):
                if(self.glFit(x,y,points)):
                    self.point(x, y)


              
    # Se escribe el archivo
    def glFinish(self, filename='output.bmp'):
        f = open(filename, 'bw')

        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        # image header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        # pixel data
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])

        f.close()