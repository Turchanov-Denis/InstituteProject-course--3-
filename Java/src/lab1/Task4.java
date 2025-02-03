import java.util.Scanner;

public class Task4 {
    public static void main(String[] args) {
        System.out.println("Формат ввода\n" +
                "На первой строке вводится количество дорог.\n" +
                "Затем для каждой дороги вводится (на отдельных строках) количество\n" +
                "туннелей и высота каждого туннеля (точнее, максимально допустимая высота\n" +
                "грузовика) в сантиметрах.");
        Scanner scanner = new Scanner(System.in);
        int roadsCount = scanner.nextInt();
        int bestRoad = 0;
        int maxMinHeight = 0;

        for (int i = 1; i <= roadsCount; i++) {
            int tunnelsCount = scanner.nextInt();
            int minHeight = Integer.MAX_VALUE;

            for (int j = 0; j < tunnelsCount; j++) {
                int tunnelHeight = scanner.nextInt();
                if (tunnelHeight < minHeight) {
                    minHeight = tunnelHeight;
                }
            }

            if (minHeight > maxMinHeight) {
                maxMinHeight = minHeight;
                bestRoad = i;
            }
        }

        System.out.println(bestRoad + " " + maxMinHeight);
    }
}
