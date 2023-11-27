import java.util.Random;
import java.util.Scanner;

public class GuessingGame {
    public static void main(String[] args) {
        Random random = new Random();
        int randomNumber = random.nextInt(100) + 1;
        int attempts = 0;

        Scanner scanner = new Scanner(System.in);
        System.out.println("Welcome to the Guessing Game!");

        int guess;
        do {
            System.out.print("Enter your guess (between 1 and 100): ");
            guess = scanner.nextInt();
            attempts++;

            if (guess > randomNumber) {
                System.out.println("Too high!");
            } else if (guess < randomNumber) {
                System.out.println("Too low!");
            } else {
                System.out.println("Congratulations! You guessed the number correctly.");
                System.out.println("Number of attempts: " + attempts);
            }
        } while (guess != randomNumber);

        scanner.close();
    }
}