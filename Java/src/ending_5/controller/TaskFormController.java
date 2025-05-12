package ending_5.controller;

import ending_5.db.DBHelper;
import ending_5.model.Task;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.input.MouseEvent;
import javafx.event.ActionEvent;
import java.sql.SQLException;
import java.time.LocalDate;

public class TaskFormController {
    private TableView<Task> taskTable;
    private Task currentTask;
    private Task task;

    // Метод для загрузки данных задачи в форму

    public void setTaskTable(TableView<Task> taskTable) {
        this.taskTable = taskTable;
    }

    @FXML private TextField titleField;
    @FXML private TextArea descriptionField;
    @FXML private DatePicker dueDateField;
    @FXML private Button saveButton;
    @FXML private Button cancelButton;
    @FXML
    private CheckBox doneCheckBox;
    public void loadTask(Task task) {
        this.currentTask = task;
        titleField.setText(task.getTitle());
        descriptionField.setText(task.getDescription());
        dueDateField.setValue(LocalDate.parse(task.getDueDate()));
        doneCheckBox.setSelected(task.isDone());

    }
    // Этот метод будет вызван при нажатии кнопки "Сохранить"
    @FXML
    public void onSaveTask(ActionEvent event) {
        String title = titleField.getText();
        String description = descriptionField.getText();
        String dueDate = dueDateField.getValue().toString();
        boolean done = doneCheckBox.isSelected();
        // Проверка на пустые поля
        if (title.isEmpty() || description.isEmpty() || dueDate.isEmpty()) {
            showError("Пожалуйста, заполните все поля.");
            return;
        }

        // Создание новой задачи
        Task newTask = new Task(title, description, dueDate, done);

        try {
            // Сохранение задачи в базу данных
            DBHelper.saveTask(newTask);
            showSuccess("Задача успешно добавлена.");
            taskTable.setItems(DBHelper.getTasks());  // Обновляем список задач
        } catch (SQLException e) {
            showError("Ошибка при сохранении задачи в базу данных.");
        }
    }
    private void updateTask(Task task) {
        // Логика для обновления задачи
        currentTask = task;
        try {
            // Извлекаем необходимые данные из объекта Task
            String title = task.getTitle();  // Получаем заголовок задачи
            String description = task.getDescription();  // Получаем заголовок задачи
            // Вызываем статический метод для обновления задачи в базе данных
            DBHelper.updateTask(title, descriptionField.getText(),  doneCheckBox.isSelected());
            taskTable.setItems(DBHelper.getTasks());
            // Печатаем сообщение об успешном обновлении
            System.out.println("Задача обновлена: " + title);

        } catch (SQLException e) {
            // Обработка исключений
            System.out.println("Ошибка при обновлении задачи: " + e.getMessage());
        }
    }
    @FXML
    public void onDeleteTask(ActionEvent event) {
        // Получаем выбранную задачу из TableView

        if (currentTask == null) {
            showError("Выберите задачу для удаления.");
            return;
        }

        try {
            // Удаление задачи из базы данных
            DBHelper.deleteTask(currentTask.getTitle());
            // Обновление списка задач
            taskTable.setItems(DBHelper.getTasks());
            showSuccess("Задача успешно удалена.");
        } catch (SQLException e) {
            showError("Ошибка при удалении задачи.");
        }
    }
    // Этот метод будет вызван при нажатии кнопки "Отменить"
    @FXML
    public void onCancel(ActionEvent event) {
        // Закрытие текущего окна или возврат в основной экран
        // Например, если это окно, можно закрыть его так:
        // Stage stage = (Stage) cancelButton.getScene().getWindow();
        // stage.close();
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

    public void onEditTask(ActionEvent actionEvent) {
        updateTask(currentTask);
    }
}
