package com.example;

/**
 * Hello world!
 */
public final class App {
    private App() {
    }

    /**
     * Says hello to the world.
     * @param args The arguments of the program.
     */
    public static void main(String[] args) {

        // Create a new highway
        Highway highway = new Highway("Highway 1", 2);

        // Create a new car
        Car car1 = new Car("Car 1");
        car1.setSpeed(100);
        car1.setDirection(90);

        Car car2 = new Car("Car 2");
        car2.setSpeed(200);
        car2.setDirection(180);

        // Add the car to the highway
        highway.addCar(car1);
        highway.addCar(car2);

        // Print the state of the highway
        highway.printState();
    }
}
