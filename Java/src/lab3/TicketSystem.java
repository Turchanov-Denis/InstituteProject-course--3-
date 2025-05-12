package lab3;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class TicketSystem {
    private List<Cinema> cinemas;
    private List<Session> sessions;

    public TicketSystem() {
        this.cinemas = new ArrayList<>();
        this.sessions = new ArrayList<>();
    }

    public void addCinema(Cinema cinema) {
        cinemas.add(cinema);
    }

    public void addSession(Session session) {
        sessions.add(session);
    }

    public Session findNearestSession(String movieName) {
        LocalDateTime now = LocalDateTime.now();
        Session nearestSession = null;
        for (Session session : sessions) {
            if (session.getMovieName().equals(movieName) && session.getStartTime().isAfter(now)) {
                if (nearestSession == null || session.getStartTime().isBefore(nearestSession.getStartTime())) {
                    nearestSession = session;
                }
            }
        }
        return nearestSession;
    }

    public boolean bookTicket(Session session, int row, int col) {
        return session.getHall().bookSeat(row, col);
    }

    public List<Cinema> getCinemas() {
        return cinemas;
    }
}
