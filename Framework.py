# Autor: Pablo Escobar
# Date: 30/01/2023
# Descripcion: Clase Framework que contiene los metodos para resolver el laberinto (AI Framework)
class Framework:
    def __init__(self, initial, goal, pixels):
        self.initial = initial
        self.goal = goal
        self.pixels = pixels
        self.visited = []
        self.frontera = []
        self.pCost = {}
        self.shortestPath = []

        self.pixel = self.initial

    def actions(self, state):
        x, y = state[0], state[1]
        actions = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        value = [a for a in actions if self.is_valid_state(a)]
        return value

    def result(self, state, action):
        self.stepTest(action,state)
        self.visited.append(action)
        self.frontera.append(action)

    def stepTest(self, action,state):
        self.pCost[action] = state

    def goalTest(self):

        return self.pixel in self.goal

    def step_cost(self, state, action):
       self.pCost[action] = state

    def path_cost(self, states, actions):
        cost = 0
        for i in range(len(states) - 1):
            cost += self.step_cost(states[i], actions[i], states[i+1])
        return cost
    
    def pathTest(self):
        self.shortestPath = []
        while self.pixel != self.initial:
            self.shortestPath.append(self.pixel)
            self.pixel = self.pCost[self.pixel]
        self.shortestPath.append(self.initial)
        return self.shortestPath[::-1]

    def is_valid_state(self, state):
        valid = False
        x, y = state[0], state[1]
        if 0 <= x < self.pixels.size[0] and 0 <= y < self.pixels.size[1]:
            array =self.pixels.getpixel((x,y))
            r,g,b =  array[0],array[1],array[2]
            if r != 0 or g != 0 or b != 0:
                valid = True
        return valid

    def heuristic(self,node, goal):
        x1, y1 = node
        x2, y2 = self.goal[1]
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5



        

    