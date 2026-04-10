public class Main {

    public static void main(String[] args) {

        HourlyPayGrade grade = HourlyPayGrade.MASTER;

        double r = grade.rate();

        System.out.println("Grade: " + grade); //MASTER
        System.out.println("Rate: " + r); //2

        HourlyEmployee emp = new HourlyEmployee(450, grade);

        double salary = emp.calculatePay();

        System.out.println("Salary: " + salary);
    }
}


// =======================
// ENUM
// =======================
enum HourlyPayGrade {
    APPRENTICE(1.0),
    JOURNEYMAN(1.5),
    MASTER(2.0); //<-------- VALUE

    private final double rate; 

    HourlyPayGrade(double rate) {
        this.rate = rate; //<-------- VALUE
    }

    public double rate() {
        return rate;
    }
}


// =======================
// CLASS EMPLOYEE
// =======================
class HourlyEmployee {
    private int tenthsWorked;
    private HourlyPayGrade grade;

    public HourlyEmployee(int tenthsWorked, HourlyPayGrade grade) {
        this.tenthsWorked = tenthsWorked;
        this.grade = grade;
    }

    public double calculatePay() {
        int TENTHS_PER_WEEK = 400;
        double OVERTIME_RATE = 1.5;

        int straightTime = Math.min(tenthsWorked, TENTHS_PER_WEEK);
        int overTime = tenthsWorked - straightTime;

        return grade.rate() * (tenthsWorked + OVERTIME_RATE * overTime);
    }
}
