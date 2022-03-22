from kandinsky import *
from ion import *
from time import sleep

input_layer = [ 0 for i in range(1024)]
weights = [ 1 for i in range(1024)]
x1 = 0
y1 = 0

select = ["Rectangle", "Others   ", 0]

def matrix_multiply(x,y):
    sum_ = 0
    for i in range (len(x)):
        sum_ += x[i]*y[i]
    return sum_
def setup():
    global x1, y1
    draw_string("Perceptron", 110, 5)
    fill_rect(10,30,300,2,"black")
    # input layer
    draw_string("Input layer", 95, 40)
    fill_rect(9,44,66,66,"black")
    fill_rect(10,45,64,64,"white")
    draw_string("label : ", 95, 60)
    draw_string("result : ", 95, 80)
    # weights visualisation
    draw_string("Weights visualisation", 95, 130) 
    fill_rect(9,134,66,66,"black")
    fill_rect(10,135,64,64,"white")
    draw_weight()

def draw_weight():
    global weights
    for i in range(1024):
        fill_rect(10+(i%32)*2,135+(i//32)*2,2,2,color(150-int(weights[i]*50),20,150))

def neuron():
    global input_layer, weights
    if matrix_multiply(input_layer, weights) > 9:
        return "Rectangle"
    else:
        return "Others   "

def main():
    global x1, y1, select, input_layer
    setup()
    while True:
        sleep(0.02)
        if keydown(KEY_UP):
            if keydown(KEY_SHIFT):
                select[2] = 1
                draw_string("Others   ",180,60)
            elif y1 > 0:
                y1 -= 1
        if keydown(KEY_DOWN):
            if keydown(KEY_SHIFT):
                select[2] = 0
                draw_string("Rectangle",180,60)
            elif y1 < 32:
                y1 += 1
        if keydown(KEY_LEFT):
            if x1 > 0:
                x1 -= 1
        if keydown(KEY_RIGHT):
            if x1 < 32:
                x1 += 1
        if keydown(KEY_OK):
            fill_rect(10+x1*2,45+y1*2,2,2,"black")
            input_layer[y1*x1] = 1
        if keydown(KEY_EXE):
            result = neuron()
            draw_string(result, 180, 80)
            if result == "Rectangle" and select[select[2]] == "Others   ":
                for i in range(1024):
                    weights[i] -= input_layer[i]
                draw_weight()
            elif result == "Others   " and select[select[2]] == "Rectangle":
                for i in range(1024):
                    weights[i] += input_layer[i]
                draw_weight()
        if keydown(KEY_BACKSPACE):
            draw_string("          ", 170, 80)
            fill_rect(10,45,64,64,"white")
            input_layer = [ 0 for i in range(1024)]