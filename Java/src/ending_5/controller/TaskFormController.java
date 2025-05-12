package ending_5.controller;

import ending_5.db.DBHelper;
import ending_5.model.Task;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;

import java.sql.SQLException;

public class TaskFormController {

    @FXML private TextField titleField;
    @FXML private TextField descriptionField;
    @FXML private TextField dueDateField;
    @FXML private Button saveButton;
    @FXML private Button cancelButton;

    // Этот метод будет вызван при нажатии кнопки "Сохранить"
    @FXML
    public void onSaveTask(MouseEvent event) {
        String title = titleField.getText();
        String description = descriptionField.getText();
        String dueDate = dueDateField.getText();

        // Проверка на пустые поля
        if (title.isEmpty() || description.isEmpty() || dueDate.isEmpty()) {
            showError("Пожалуйста, заполните все поля.");
            return;
        }

        // Создание новой задачи
        Task newTask = new Task(title, description, dueDate, false);

        try {
            // Сохранение задачи в базу данных
            DBHelper.saveTask(newTask);
            showSuccess("Задача успешно добавлена.");
        } catch (SQLException e) {
            showError("Ошибка при сохранении задачи в базу данных.");
        }
    }

    // Этот метод будет вызван при нажатии кнопки "Отменить"
    @FXML
    public void onCancel(MouseEvent event) {
        // Закрытие текущего окна (например, можно закрыть форму или вернуть в основной экран)
        // В зависимости от вашей реализации, возможно, нужно вызвать Stage.close()
    }

    // Метод для отображения сообщения об ошибке
    private void showError(String message) {
        Alert alert = new Alert(AlertType.ERROR);
        alert.setTitle("Ошибка");
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }

    // Метод для отображения сообщения об успехе
    private void showSuccess(String message) {
        Alert alert = new Alert(AlertType.INFORMATION);
        alert.setTitle("Успех");
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }
}
