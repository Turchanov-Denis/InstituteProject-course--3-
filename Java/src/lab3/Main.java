package lab3;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class Main {
    private static final DateTimeFormatter DATE_TIME_FORMATTER = DateTimeFormatter.ofPattern("dd.MM.yyyy HH:mm");
    private static TicketSystem ticketSystem = new TicketSystem();
    private static Scanner scanner = new Scanner(System.in);

    private static String currentUserRole = null;

    public static void main(String[] args) {

        TestData.initializeData(ticketSystem);
        
        while (true) {
            if (currentUserRole == null) {
                System.out.println("1. Войти");
                System.out.println("2. Выход");
            } else if (currentUserRole.equals("admin")) {
                System.out.println("1. Добавить кинотеатр");
                System.out.println("2. Добавить зал");
                System.out.println("3. Создать сеанс");
                System.out.println("4. Выйти");
            } else if (currentUserRole.equals("user")) {
                System.out.println("1. Найти ближайший сеанс");
                System.out.println("2. Купить билет");
                System.out.println("3. Выйти");
            }

            int choice = scanner.nextInt();
            scanner.nextLine();

            if (currentUserRole == null) {
                switch (choice) {
                    case 1:
                        login();
                        break;
                    case 2:
                        return;
                    default:
                        System.out.println("Неверный выбор.");
                }
            } else if (currentUserRole.equals("admin")) {
                switch (choice) {
                    case 1:
                        addCinema();
                        break;
                    case 2:
                        addHall();
                        break;
                    case 3:
                        createSession();
                        break;
                    case 4:
                        currentUserRole = null;
                        System.out.println("Выход выполнен.");
                        break;
                    default:
                        System.out.println("Неверный выбор.");
                }
            } else if (currentUserRole.equals("user")) {
                switch (choice) {
                    case 1:
                        findNearestSession();
                        break;
                    case 2:
                        buyTicket();
                        break;
                    case 3:
                        currentUserRole = null;
                        System.out.println("Выход выполнен.");
                        break;
                    default:
                        System.out.println("Неверный выбор.");
                }
            }
        }
    }

    private static void login() {
        System.out.println("Выберите роль:");
        System.out.println("1. Администратор");
        System.out.println("2. Пользователь");
        int roleChoice = scanner.nextInt();
        scanner.nextLine();

        System.out.println("Введите логин:");
        String username = scanner.nextLine();
        System.out.println("Введите пароль:");
        String password = scanner.nextLine();

        Auth auth = new Auth();
        if (roleChoice == 1 && auth.login(username, password)) {
            currentUserRole = "admin";
            System.out.println("Авторизация администратора успешна.");
        } else if (roleChoice == 2) {
            currentUserRole = "user";
            System.out.println("Авторизация пользователя успешна.");
        } else {
            System.out.println("Ошибка авторизации. Проверьте логин и пароль.");
        }
    }

    private static void addCinema() {
        System.out.println("Введите название кинотеатра:");
        String cinemaName = scanner.nextLine();
        Cinema cinema = new Cinema(cinemaName);
        ticketSystem.addCinema(cinema);
        System.out.println("Кинотеатр добавлен.");
    }

    private static void addHall() {
        System.out.println("Введите название кинотеатра:");
        String cinemaNameForHall = scanner.nextLine();
        Cinema selectedCinema = ticketSystem.getCinemas().stream()
                .filter(c -> c.getName().equals(cinemaNameForHall))
                .findFirst()
                .orElse(null);
        if (selectedCinema != null) {
            System.out.println("Введите название зала:");
            String hallName = scanner.nextLine();
            System.out.println("Введите количество рядов:");
            int rows = scanner.nextInt();
            System.out.println("Введите количество мест в ряду:");
            int cols = scanner.nextInt();
            Hall hall = new Hall(hallName, rows, cols);
            selectedCinema.addHall(hall);
            System.out.println("Зал добавлен.");
        } else {
            System.out.println("Кинотеатр не найден.");
        }
    }

    private static void createSession() {
        System.out.println("Введите название фильма:");
        String movieName = scanner.nextLine();

        System.out.println("Введите дату и время начала (дд.мм.гггг чч:мм):");
        String dateTimeInput = scanner.nextLine();
        LocalDateTime startTime = null;

        try {
            startTime = LocalDateTime.parse(dateTimeInput, DATE_TIME_FORMATTER);
        } catch (Exception e) {
            System.out.println("Ошибка: Неверный формат даты и времени. Используйте формат дд.мм.гггг чч:мм.");
            return;
        }

        System.out.println("Введите продолжительность (в минутах):");
        int duration = scanner.nextInt();
        scanner.nextLine();

        System.out.println("Введите название кинотеатра:");
        String cinemaNameForSession = scanner.nextLine();
        System.out.println("Введите название зала:");
        String hallNameForSession = scanner.nextLine();

        Cinema cinemaForSession = ticketSystem.getCinemas().stream()
                .filter(c -> c.getName().equals(cinemaNameForSession))
                .findFirst()
                .orElse(null);

        if (cinemaForSession != null) {
            Hall hallForSession = cinemaForSession.getHalls().stream()
                    .filter(h -> h.getName().equals(hallNameForSession))
                    .findFirst()
                    .orElse(null);

            if (hallForSession != null) {
                Session session = new Session(movieName, startTime, duration, hallForSession);
                ticketSystem.addSession(session);
                System.out.println("Сеанс создан.");
            } else {
                System.out.println("Зал не найден.");
            }
        } else {
            System.out.println("Кинотеатр не найден.");
        }
    }

    private static void findNearestSession() {
        System.out.println("Введите название фильма:");
        String movieName = scanner.nextLine();
        Session nearestSession = ticketSystem.findNearestSession(movieName);
        if (nearestSession != null) {
            System.out.println("Ближайший сеанс: " + nearestSession.getStartTime().format(DATE_TIME_FORMATTER) + " в зале " + nearestSession.getHall().getName());
        } else {
            System.out.println("Сеансы не найдены.");
        }
    }

    private static void buyTicket() {
        System.out.println("Введите название фильма:");
        String movieNameForTicket = scanner.nextLine();
        Session sessionForTicket = ticketSystem.findNearestSession(movieNameForTicket);
        if (sessionForTicket != null) {
            System.out.println("План зала:");
            sessionForTicket.getHall().printSeats();
            System.out.println("Введите ряд и место:");
            int row = scanner.nextInt();
            int col = scanner.nextInt();
            if (ticketSystem.bookTicket(sessionForTicket, row, col)) {
                System.out.println("Билет куплен.");
            } else {
                System.out.println("Место уже занято или не существует.");
            }
        } else {
            System.out.println("Сеансы не найдены.");
        }
    }
}
