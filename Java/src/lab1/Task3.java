import java.util.Scanner;

public class Task3 {
    public static void main(String[] args) {
        System.out.println(
                "Сначала вводятся два числа: координаты клада по оси икс (запад-восток) и\n" +
                "игрек (юг-север). Затем следует некоторое количество указаний карты.\n" +
                "Каждое указание карты состоит из двух строк. Первая строка содержит слово\n" +
                "«север», «юг», «запад» или «восток», вторая — натуральное число,\n" +
                "количество шагов, которое нужно пройти в данном направлении.\n" +
                "Заключительное указание карты состоит только из одной строки,\n" +
                "содержащей слово «стоп».\n" +
                "Программа выводит минимальное количество указаний карты, которое\n" +
                "нужно выполнить, чтобы прийти к кладу. Гарантируется, что карта приводит\n" +
                "к кладу.\n" +
                "my mind blowing....................");
        Scanner scanner = new Scanner(System.in);

        int targetX = scanner.nextInt();
        int targetY = scanner.nextInt();
        scanner.nextLine();

        int x = 0, y = 0, steps = 0;

        while (true) {
            String direction = scanner.nextLine();
            if (direction.equals("стоп")) break;

            int distance = scanner.nextInt();
            scanner.nextLine();

            switch (direction) {
                case "север": y += distance; break;
                case "юг": y -= distance; break;
                case "восток": x += distance; break;
                case "запад": x -= distance; break;
            }

            steps++;
            if (x == targetX && y == targetY) {
                System.out.println(steps);
                break;
            }
        }

        scanner.close();
    }
}
