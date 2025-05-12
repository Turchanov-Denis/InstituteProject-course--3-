package ending_5.db;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import ending_5.model.Task;

import java.io.File;
import java.sql.*;

public class DBHelper {

    private static final String URL = "jdbc:sqlite:C:/Users/Firo/Desktop/junk/InstituteProject-course--3-/Java/src/ending_5/db/tasks.db";
    static {
        try {
            // Загрузка драйвера JDBC
            Class.forName("org.sqlite.JDBC");
        } catch (ClassNotFoundException e) {
            System.out.println("Драйвер SQLite не найден");
        }
    }
    // Метод для создания базы данных, если она не существует
    private static void createDatabaseIfNotExists() {
        File dbFile = new File("C:/Users/Firo/Desktop/junk/InstituteProject-course--3-/Java/src/ending_5/db/tasks.db");
        if (!dbFile.exists()) {
            try {
                // Пытаемся подключиться, если файл базы данных не существует, он будет создан
                try (Connection conn = DriverManager.getConnection(URL)) {
                    System.out.println("База данных создана");
                }
            } catch (SQLException e) {
                System.out.println("Ошибка при создании базы данных: " + e.getMessage());
            }
        }
    }

    // Метод для создания таблицы (если она не существует)
    private static void createTableIfNotExists() throws SQLException {
        createDatabaseIfNotExists(); // Убедитесь, что база данных существует
        String createTableQuery = "CREATE TABLE IF NOT EXISTS Tasks (" +
                "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                "title TEXT NOT NULL, " +
                "description TEXT, " +
                "due_date TEXT, " +
                "is_done BOOLEAN)";

        try (Connection conn = DriverManager.getConnection(URL);
             Statement stmt = conn.createStatement()) {
            stmt.execute(createTableQuery);
        }
    }

    // Метод для получения всех задач
    public static ObservableList<Task> getTasks() throws SQLException {
        ObservableList<Task> tasks = FXCollections.observableArrayList();
        createTableIfNotExists();  // Убедитесь, что таблица существует

        String query = "SELECT * FROM Tasks";
        try (Connection conn = DriverManager.getConnection(URL);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(query)) {

            while (rs.next()) {
                Task task = new Task(
                        rs.getString("title"),
                        rs.getString("description"),
                        rs.getString("due_date"),
                        rs.getBoolean("is_done")
                );
                tasks.add(task);
            }
        } catch (SQLException e) {
            throw new SQLException("Ошибка при загрузке задач: " + e.getMessage());
        }
        return tasks;
    }

    // Метод для сохранения новой задачи в базе данных
    public static void saveTask(Task task) throws SQLException {
        createTableIfNotExists();  // Убедитесь, что таблица существует

        String query = "INSERT INTO Tasks (title, description, due_date, is_done) VALUES (?, ?, ?, ?)";
        try (Connection conn = DriverManager.getConnection(URL);
             PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setString(1, task.getTitle());
            stmt.setString(2, task.getDescription());
            stmt.setString(3, task.getDueDate());
            stmt.setBoolean(4, task.isDone());
            stmt.executeUpdate();
        } catch (SQLException e) {
            throw new SQLException("Ошибка при добавлении задачи: " + e.getMessage());
        }
    }

    // Метод для обновления статуса задачи
    public static void updateTask(String title, String description, boolean isDone) throws SQLException {
        String query = "UPDATE Tasks SET is_done = ?, description = ? WHERE title = ?";
        try (Connection conn = DriverManager.getConnection(URL);
             PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setBoolean(1, isDone);
            stmt.setString(2, description);
            stmt.setString(3, title);
            stmt.executeUpdate();
        } catch (SQLException e) {
            throw new SQLException("Ошибка при обновлении статуса задачи: " + e.getMessage());
        }
    }

    // Метод для удаления задачи
    public static void deleteTask(String title) throws SQLException {
        String query = "DELETE FROM Tasks WHERE title = ?";
        try (Connection conn = DriverManager.getConnection(URL);
             PreparedStatement stmt = conn.prepareStatement(query)) {

            // Устанавливаем значение параметра title
            stmt.setString(1, title);

            // Выполняем запрос на удаление
            stmt.executeUpdate();
        } catch (SQLException e) {
            throw new SQLException("Ошибка при удалении задачи: " + e.getMessage());
        }
    }
}
