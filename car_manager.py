from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.penup()
            y_cor = random.randrange(-200, 200, 20)
            if self.all_cars:
                while self.all_cars[-1].ycor() == y_cor:
                    y_cor = random.randrange(-200, 200, 20)
            new_car.goto(300, y_cor)
            new_car.shapesize(stretch_wid=0.8, stretch_len=2)
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def cleanup_cars(self):
        for car in self.all_cars[:]:
            if car.xcor() < -320:
                car.hideturtle()
                self.all_cars.remove(car)