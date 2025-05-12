package lab4;
import java.util.*;

public class Library {
    private List<Book> books = new ArrayList<>();
    private Set<String> authors = new HashSet<>();
    private Map<String, Integer> authorStatistics = new HashMap<>();

    public void addBook(Book book) {
        books.add(book);
        authors.add(book.getAuthor());
        authorStatistics.merge(book.getAuthor(), 1, Integer::sum);
    }

    public void removeBook(Book book) {
        if (books.remove(book)) {
            // Проверяем, есть ли еще книги этого автора
            boolean authorHasMoreBooks = books.stream()
                    .anyMatch(b -> b.getAuthor().equals(book.getAuthor()));
            
            if (!authorHasMoreBooks) {
                authors.remove(book.getAuthor());
            }
            
            authorStatistics.computeIfPresent(book.getAuthor(), (key, value) -> value > 1 ? value - 1 : null);
        }
    }

    public List<Book> findBooksByAuthor(String author) {
        List<Book> result = new ArrayList<>();
        for (Book book : books) {
            if (book.getAuthor().equals(author)) {
                result.add(book);
            }
        }
        return result;
    }

    public List<Book> findBooksByYear(int year) {
        List<Book> result = new ArrayList<>();
        for (Book book : books) {
            if (book.getYear() == year) {
                result.add(book);
            }
        }
        return result;
    }

    public void printAllBooks() {
        System.out.println("Все книги в библиотеке:");
        books.forEach(System.out::println);
    }

    public void printUniqueAuthors() {
        System.out.println("Уникальные авторы:");
        authors.forEach(System.out::println);
    }

    public void printAuthorStatistics() {
        System.out.println("Статистика по авторам:");
        authorStatistics.forEach((author, count) -> 
            System.out.println(author + ": " + count + " книг"));
    }
}
