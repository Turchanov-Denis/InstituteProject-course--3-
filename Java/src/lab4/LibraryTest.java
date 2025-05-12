package lab4;

public class LibraryTest {
    public static void main(String[] args) {
        Library library = new Library();

        // Новые книги
        Book book1 = new Book("Мастер и Маргарита", "Михаил Булгаков", 1967);
        Book book2 = new Book("Пикник на обочине", "Аркадий и Борис Стругацкие", 1972);
        Book book3 = new Book("Мы", "Евгений Замятин", 1920);
        Book book4 = new Book("Чапаев и Пустота", "Виктор Пелевин", 1996);
        Book book5 = new Book("Герой нашего времени", "Михаил Лермонтов", 1840);

        // Добавление книг в библиотеку
        library.addBook(book1);
        library.addBook(book2);
        library.addBook(book3);
        library.addBook(book4);
        library.addBook(book5);

        System.out.println("=== Список всех книг ===");
        library.printAllBooks();
        System.out.println("\n-----------------------------");

        System.out.println("Книги Михаила Булгакова:");
        library.findBooksByAuthor("Михаил Булгаков").forEach(System.out::println);
        System.out.println("\n-----------------------------");

        System.out.println("Книги 1920 года:");
        library.findBooksByYear(1920).forEach(System.out::println);
        System.out.println("\n-----------------------------");

        System.out.println("Уникальные авторы:");
        library.printUniqueAuthors();
        System.out.println("\n-----------------------------");

        System.out.println("Статистика по авторам:");
        library.printAuthorStatistics();
        System.out.println("\n-----------------------------");

        System.out.println("=== После удаления книги ===");
        library.removeBook(book2);
        library.printAllBooks();
        System.out.println("\n-----------------------------");

        System.out.println("Статистика после удаления:");
        library.printAuthorStatistics();
    }
}
