class Main{

    public static void main(String[]
    args){
        System.out.println
        ("Inicializando...");
        System.out.println("Car....");
        Car car = new Car("AMQ123" , new
        Account("Andres Loiza",
        "ADN1235","andres1@hotmail.com",
        "12365"));
        car.passenger = 4;
        car.printDataCar();

        System.out.println("Uberx....");
        Uberx uberx = new Uberx
        ("MKL185", new Account("Maria Loyola","JKL12365",
        "maria1@hotmail.com","125478"),
        "Toyota","Corolla");
    }
}