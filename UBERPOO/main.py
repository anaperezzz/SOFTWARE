from car import Car 
from account import Account 
from uberX import UberX
from user import User 

if __name__ == "__main__":
    print("Inicializando las info de los carros")
    print("Car")
    car = Car("AMS256", Account("Andres Herrera", "ASD12365", "ana.perez.carrilo77@gmail.com", "2563"))
    print(vars(car))
    print(vars(car.driver))

    print("UberX")
    uberX=UberX("KLO365", Account("Marco Lois","SGHJ1236",
    "ana.perez.carrillo77@gmail.com","7856") "Toyota", "Corolla")
    print(vars(uberX))
    print(vars(uberX.driver))

    print("User")
    user = User ("mariana Valle", "SDFG125F", "mariana@gmail.com",
    "7856")
    print (vars(user))