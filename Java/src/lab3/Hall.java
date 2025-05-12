package lab3;

public class Hall {
    private String name;
    private int rows;
    private int cols;
    private boolean[][] seats;

    public Hall(String name, int rows, int cols) {
        this.name = name;
        this.rows = rows;
        this.cols = cols;
        this.seats = new boolean[rows][cols];
    }

    public boolean bookSeat(int row, int col) {
        if (row >= 0 && row < rows && col >= 0 && col < cols && !seats[row][col]) {
            seats[row][col] = true;
            return true;
        }
        return false;
    }

    public void printSeats() {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print(seats[i][j] ? "[X]" : "[ ]");
            }
            System.out.println();
        }
    }

    public String getName() {
        return name;
    }
}
