import os

# Укажите путь, где хотите создать проект
base_path = r"C:\Users\Firo\Desktop\junk\InstituteProject-course--3-\Java\src\5_ending"

# Определите структуру папок и файлов
folders = [
    os.path.join(base_path, "DailyPlanner"), 
    os.path.join(base_path, "DailyPlanner/controller"), 
    os.path.join(base_path, "DailyPlanner/model"), 
    os.path.join(base_path, "DailyPlanner/db"), 
    os.path.join(base_path, "DailyPlanner/view")
]

# Создайте папки
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Содержимое файлов (как в предыдущем ответе)
files = {
    "DailyPlanner/Main.java": """import javafx.application.Application;
import javafx.scene.Scene;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;

public class Main extends Application {
    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("/view/main.fxml"));
        Scene scene = new Scene(loader.load());
        primaryStage.setScene(scene);
        primaryStage.setTitle("Электронный ежедневник");
        primaryStage.show();
    }
}
""",
    "DailyPlanner/controller/MainController.java": """package controller;

import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.TableView;
import javafx.scene.control.TableColumn;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.input.MouseEvent;
import model.Task;
import db.DBHelper;

import java.sql.SQLException;

public class MainController {

    @FXML private TableView<Task> taskTable;
    @FXML private TableColumn<Task, String> titleColumn;
    @FXML private TableColumn<Task, String> descriptionColumn;
    @FXML private TableColumn<Task, String> dateColumn;

    public void initialize() {
        titleColumn.setCellValueFactory(new PropertyValueFactory<>("title"));
        descriptionColumn.setCellValueFactory(new PropertyValueFactory<>("description"));
        dateColumn.setCellValueFactory(new PropertyValueFactory<>("dueDate"));

        try {
            taskTable.setItems(DBHelper.getTasks());
        } catch (SQLException e) {
            showError("Ошибка при загрузке задач.");
        }
    }

    @FXML
    public void onAddTask(MouseEvent event) throws Exception {
        // Открытие окна добавления задачи
        // Для этого создадим второе окно TaskForm.fxml
    }

    private void showError(String message) {
        Alert alert = new Alert(AlertType.ERROR);
        alert.setTitle("Ошибка");
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }
}
""",
    "DailyPlanner/controller/TaskFormController.java": """package controller;

import javafx.fxml.FXML;
import javafx.scene.control.TextField;
import javafx.scene.control.TextArea;
import javafx.scene.control.DatePicker;
import javafx.scene.control.CheckBox;
import model.Task;
import db.DBHelper;

import java.sql.SQLException;

public class TaskFormController {

    @FXML private TextField titleField;
    @FXML private TextArea descriptionField;
    @FXML private DatePicker dueDateField;
    @FXML private CheckBox doneCheckBox;

    public void onSave() {
        String title = titleField.getText();
        String description = descriptionField.getText();
        String dueDate = dueDateField.getValue().toString();
        boolean isDone = doneCheckBox.isSelected();

        Task task = new Task(title, description, dueDate, isDone);

        try {
            DBHelper.saveTask(task);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
""",
    "DailyPlanner/model/Task.java": """package model;

public class Task {

    private String title;
    private String description;
    private String dueDate;
    private boolean isDone;

    public Task(String title, String description, String dueDate, boolean isDone) {
        this.title = title;
        this.description = description;
        this.dueDate = dueDate;
        this.isDone = isDone;
    }

    // Геттеры и сеттеры для всех полей
}
""",
    "DailyPlanner/db/DBHelper.java": """package db;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import model.Task;

import java.sql.*;

public class DBHelper {

    private static final String URL = "jdbc:sqlite:tasks.db";

    public static ObservableList<Task> getTasks() throws SQLException {
        ObservableList<Task> tasks = FXCollections.observableArrayList();
        try (Connection conn = DriverManager.getConnection(URL);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery("SELECT * FROM Tasks")) {

            while (rs.next()) {
                Task task = new Task(
                        rs.getString("title"),
                        rs.getString("description"),
                        rs.getString("due_date"),
                        rs.getBoolean("is_done")
                );
                tasks.add(task);
            }
        }
        return tasks;
    }

    public static void saveTask(Task task) throws SQLException {
        String query = "INSERT INTO Tasks (title, description, due_date, is_done) VALUES (?, ?, ?, ?)";
        try (Connection conn = DriverManager.getConnection(URL);
             PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setString(1, task.getTitle());
            stmt.setString(2, task.getDescription());
            stmt.setString(3, task.getDueDate());
            stmt.setBoolean(4, task.isDone());
            stmt.executeUpdate();
        }
    }
}
""",
    "DailyPlanner/view/main.fxml": """<?xml version="1.0" encoding="UTF-8"?>
<?import javafx.scene.control.TableView?>
<?import javafx.scene.control.TableColumn?>
<?import javafx.scene.layout.VBox?>
<?import javafx.scene.control.Button?>

<VBox xmlns:fx="http://javafx.com/fxml" fx:controller="controller.MainController">
    <TableView fx:id="taskTable">
        <columns>
            <TableColumn fx:id="titleColumn" text="Задача"/>
            <TableColumn fx:id="descriptionColumn" text="Описание"/>
            <TableColumn fx:id="dateColumn" text="Дата"/>
        </columns>
    </TableView>
    <Button text="Добавить задачу" onMouseClicked="#onAddTask"/>
</VBox>
""",
    "DailyPlanner/view/task_form.fxml": """<?xml version="1.0" encoding="UTF-8"?>
<?import javafx.scene.layout.VBox?>
<?import javafx.scene.control.TextField?>
<?import javafx.scene.control.TextArea?>
<?import javafx.scene.control.DatePicker?>
<?import javafx.scene.control.CheckBox?>
<?import javafx.scene.control.Button?>

<VBox xmlns:fx="http://javafx.com/fxml" fx:controller="controller.TaskFormController">
    <TextField fx:id="titleField" promptText="Название задачи"/>
    <TextArea fx:id="descriptionField" promptText="Описание задачи"/>
    <DatePicker fx:id="dueDateField"/>
    <CheckBox fx:id="doneCheckBox" text="Задача выполнена"/>
    <Button text="Сохранить" onAction="#onSave"/>
</VBox>
"""
}

# Создание файлов с соответствующим содержанием
for file_path, content in files.items():
    full_path = os.path.join(base_path, file_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Проект и файлы успешно созданы!")
