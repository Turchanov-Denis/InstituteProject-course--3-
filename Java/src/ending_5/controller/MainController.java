package ending_5.controller;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;  // Добавлен импорт
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.TableRow;
import javafx.scene.control.TableView;
import javafx.scene.control.TableColumn;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.input.MouseEvent;
import javafx.stage.Stage;
import ending_5.model.Task;
import ending_5.db.DBHelper;

import java.io.IOException;
import java.sql.SQLException;

public class MainController {

    @FXML private TableView<Task> taskTable;
    @FXML private TableColumn<Task, String> titleColumn;
    @FXML private TableColumn<Task, String> descriptionColumn;
    @FXML private TableColumn<Task, String> dateColumn;

    public void initialize() {
        // Настройка колонок таблицы
        titleColumn.setCellValueFactory(new PropertyValueFactory<>("title"));
        descriptionColumn.setCellValueFactory(new PropertyValueFactory<>("description"));
        dateColumn.setCellValueFactory(new PropertyValueFactory<>("dueDate"));

        // Загрузка данных и настройка таблицы
        try {
            taskTable.setItems(DBHelper.getTasks());
        } catch (SQLException e) {
            showError("Ошибка при загрузке задач.");
        }

        // Изменение цвета строк в зависимости от выполнения задачи
        taskTable.setRowFactory(tv -> {
            TableRow<Task> row = new TableRow<>();
            row.itemProperty().addListener((obs, oldItem, newItem) -> {
                if (newItem != null) {
                    // Если задача выполнена, строка зеленая, если нет - красная
                    row.setStyle(newItem.isDone() ? "-fx-background-color: lightgreen;" : "-fx-background-color: lightcoral;");
                }
            });
            return row;
        });
        taskTable.setOnMouseClicked(event -> {
            if (event.getClickCount() == 2) { // Проверка на двойной клик
                Task selectedTask = taskTable.getSelectionModel().getSelectedItem();
                if (selectedTask != null) {
                    openTask(selectedTask); // Открываем задачу
                }
            }
        });
    }
    private void openTask(Task task) {
        try {
            // Открытие окна редактирования задачи
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/view/task_form1.fxml"));
            Scene scene = new Scene(loader.load());
            Stage stage = new Stage();
            stage.setScene(scene);
            stage.setTitle("Редактирование задачи");

            // Передаем задачу в новое окно
            TaskFormController controller = loader.getController();
            controller.setTaskTable(taskTable);
            controller.loadTask(task); // Передаем задачу в контроллер
            stage.show();


        } catch (IOException e) {
            showError("Ошибка при открытии окна редактирования.");
        }
    }
    @FXML
    public void onAddTask(MouseEvent event) throws IOException {
        // Открытие окна добавления задачи
        FXMLLoader loader = new FXMLLoader(getClass().getResource("/view/task_form.fxml"));
        Scene scene = new Scene(loader.load());
        Stage stage = new Stage();
        stage.setScene(scene);
        TaskFormController taskFormController = loader.getController();

        // Передаем taskTable для обновления после добавления задачи
        taskFormController.setTaskTable(taskTable);

        stage.setTitle("Добавить задачу");
        stage.show();

    }

    private void showError(String message) {
        Alert alert = new Alert(AlertType.ERROR);
        alert.setTitle("Ошибка");
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }


}
