import java.util.Scanner;

public class LoginPage {

    // Simulated account data (in a real project, you might use a database or file)
    private static final String storedUsername = "admin";
    private static final String storedPassword = "1234";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String username, password;
        int attempts = 3;

        System.out.println("=== LOGIN PAGE ===");

        while (attempts > 0) {
            System.out.print("Enter Username: ");
            username = scanner.nextLine();

            System.out.print("Enter Password: ");
            password = scanner.nextLine();

            if (username.equals(storedUsername) && password.equals(storedPassword)) {
                System.out.println("\n Login successful! Welcome, " + username + ".");
                // You can call another method here to open a menu or dashboard
                break;
            } else {
                attempts--;
                System.out.println("\nInvalid credentials. Attempts left: " + attempts);
                if (attempts == 0) {
                    System.out.println(" Too many failed attempts. Exiting.");
                }
            }
        }

        scanner.close();
    }
}
