# Autor: Pablo Escobar
# Date: 30/01/2023
# Descripcion: Programa que resuelve un laberinto graph search
import sys
import numpy as np
from PIL import Image as im
from PIL import ImageEnhance as imEnh
import Framework
import heapq

imagen = "lab2.png"

def criteria(problem, algorithm):
    if algorithm == "BFS":
        return problem.frontera.pop(0)
    elif algorithm == "DFS":
        return problem.frontera.pop(-1)
    elif algorithm == "a*":
        index = min(range(len(problem.frontera)), key=lambda x: problem.pCost[problem.frontera[x]])
        return problem.frontera.pop(index)
        


def graph_search(problem,algorithm):
    problem.pCost[problem.initial] = None
    problem.frontera.append(problem.initial)
    problem.visited.append(problem.initial)
    while problem.frontera:       
        problem.pixel = criteria(problem, algorithm)
        if problem.goalTest():
            print("Goal Found")
            return problem.pathTest()
        for a in problem.actions(problem.pixel):
            if a not in problem.visited:
                problem.result(problem.pixel, a)
                problem.pixels.putpixel(a,(136, 183, 221))




def check_distance(coord1, coord2, threshold):
    x1, y1 = coord1
    x2, y2 = coord2
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    if distance <= threshold:
        return True
    else:
        return False

def start(algorithm):
    img = im.open(imagen)
    sz = (200,200) 
    if img.size[0] > 120 or img.size[1] > 120:
        img.thumbnail(sz, im.ANTIALIAS)
        sz = (img.size[0] , img.size[1])
        imEnh.Contrast(img).enhance(3)

    RGB_FLAG = [False, False, False]
    Green_Pixels = []
    red_pixels = []
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pixel = img.getpixel((x,y))
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            if b<50 and g<50 and r<50:
                img.putpixel((x,y),(0,0,0))
            elif b>50 and g>50 and r>50:
                img.putpixel((x,y),(255,255,255))
            elif r>200 and g<50 and b<50:
                if not RGB_FLAG[0]:
                    RGB_FLAG[0] = True
                    img.putpixel((x,y),(255,0,0))
                    red_pixels.append((x,y))
                else:
                    img.putpixel((x,y),(255,255,255))
            elif g>100 and r<100 and b<100:

                if not RGB_FLAG[1]:
                    RGB_FLAG[1] = True
                    img.putpixel((x,y),(0,255,0))
                    Green_Pixels.append((x,y))
                else:
                    img.putpixel((x,y),(255,255,255))
                if not check_distance((x,y),Green_Pixels[len(Green_Pixels)-1],20):
                    RGB_FLAG[1] = False
            else:
                img.putpixel((x,y),(0,0,0))
    initial = red_pixels[0]
    goal = Green_Pixels

    problem = Framework.Framework(initial, goal, img)

    path = graph_search(problem,algorithm)



    if path:
        path.pop()
        for pixel in path:
            img.putpixel(pixel,(0,0,255))
    for pixel in Green_Pixels:
        img.putpixel(pixel,(0,255,0))

    img.putpixel(initial,(255,0,0))

    # save the image to a file
    if algorithm=="a*":
        algorithm = "a_star"
    img.save(f"GENERATED_SOLUTION_{imagen.split('.')[0]}_{algorithm}.png")


algorithms = ["BFS", "DFS", "a*"]
for algorithm in algorithms:
    start(algorithm)