interface Animal {
    void eat();
    void sleep();
}

abstract class BaseAnimal implements Animal {
    public void eat() {
        System.out.println("Eating...");
    }

    public void sleep() {
        System.out.println("Sleeping...");
    }
}

class Dog extends BaseAnimal {
}
