package lab3;

import java.time.LocalDateTime;

public class Session {
    private String movieName;
    private LocalDateTime startTime;
    private Hall hall;

    public Session(String movieName, LocalDateTime startTime, int duration, Hall hall) {
        this.movieName = movieName;
        this.startTime = startTime;
        this.hall = hall;
    }

    public String getMovieName() {
        return movieName;
    }

    public LocalDateTime getStartTime() {
        return startTime;
    }

    public Hall getHall() {
        return hall;
    }
}
