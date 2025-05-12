package lab3;

import java.time.LocalDateTime;

public class TestData {

    public static void initializeData(TicketSystem ticketSystem) {
        Cinema cinema1 = new Cinema("Cinema 1");
        Cinema cinema2 = new Cinema("Cinema 2");

        Hall hall1 = new Hall("Hall 1", 5, 10);
        Hall hall2 = new Hall("Hall 2", 6, 8);
        Hall hall3 = new Hall("Hall 3", 4, 12);

        cinema1.addHall(hall1);
        cinema1.addHall(hall2);
        cinema2.addHall(hall3);

        ticketSystem.addCinema(cinema1);
        ticketSystem.addCinema(cinema2);

        LocalDateTime now = LocalDateTime.now();
        Session session1 = new Session("Movie 1", now.plusHours(1), 120, hall1);
        Session session2 = new Session("Movie 2", now.plusHours(2), 90, hall2);
        Session session3 = new Session("Movie 3", now.plusHours(3), 150, hall3);

        ticketSystem.addSession(session1);
        ticketSystem.addSession(session2);
        ticketSystem.addSession(session3);

        System.out.println("Базовые данные успешно загружены.");
    }
}
