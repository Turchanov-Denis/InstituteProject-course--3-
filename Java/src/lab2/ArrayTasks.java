package lab2;

import java.util.*;

public class ArrayTasks {
    // task 1
    public static String longestUniqueSubstring(String s) {
        Set<Character> set = new HashSet<>();
        int left = 0, maxLen = 0, start = 0;
        for (int right = 0; right < s.length(); right++) {
            while (set.contains(s.charAt(right))) set.remove(s.charAt(left++));
            set.add(s.charAt(right));
            if (right - left + 1 > maxLen) {
                maxLen = right - left + 1;
                start = left;
            }
        }
        return s.substring(start, start + maxLen);
    }

    // task 2
    public static int[] mergeSortedArrays(int[] arr1, int[] arr2) {
        int[] result = new int[arr1.length + arr2.length];
        int i = 0, j = 0, k = 0;
        while (i < arr1.length && j < arr2.length) result[k++] = arr1[i] < arr2[j] ? arr1[i++] : arr2[j++];
        while (i < arr1.length) result[k++] = arr1[i++];
        while (j < arr2.length) result[k++] = arr2[j++];
        return result;
    }

    // task 3
    public static int maxSubarraySum(int[] arr) {
        int maxSum = arr[0], currentSum = arr[0];
        for (int i = 1; i < arr.length; i++) {
            currentSum = Math.max(arr[i], currentSum + arr[i]);
            maxSum = Math.max(maxSum, currentSum);
        }
        return maxSum;
    }

    // task 4
    public static int[][] rotate90Clockwise(int[][] matrix) {
        int n = matrix.length;
        int[][] rotated = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                rotated[j][n - 1 - i] = matrix[i][j];
        return rotated;
    }

    // task 5
    public static int[] findPairWithSum(int[] arr, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : arr) {
            if (map.containsKey(target - num)) return new int[]{target - num, num};
            map.put(num, 1);
        }
        return null;
    }

    // task 6
    public static int sum2DArray(int[][] matrix) {
        int sum = 0;
        for (int[] row : matrix) for (int num : row) sum += num;
        return sum;
    }

    // task 7
    public static int[] maxInEachRow(int[][] matrix) {
        int[] result = new int[matrix.length];
        for (int i = 0; i < matrix.length; i++)
            result[i] = Arrays.stream(matrix[i]).max().orElse(Integer.MIN_VALUE);
        return result;
    }

    // task 8
    public static int[][] rotate90CounterClockwise(int[][] matrix) {
        int n = matrix.length;
        int[][] rotated = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                rotated[n - 1 - j][i] = matrix[i][j];
        return rotated;
    }

    public static void main(String[] args) {
        System.out.println(longestUniqueSubstring("abcabcbb"));
        System.out.println(Arrays.toString(mergeSortedArrays(new int[]{1, 3, 5}, new int[]{2, 4, 6})));
        System.out.println(maxSubarraySum(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4}));
        int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        System.out.println(Arrays.deepToString(rotate90Clockwise(matrix)));
        System.out.println(Arrays.toString(findPairWithSum(new int[]{2, 7, 11, 15}, 9)));
        System.out.println(sum2DArray(new int[][]{{1, 2, 3}, {4, 5, 6}}));
        System.out.println(Arrays.toString(maxInEachRow(new int[][]{{1, 2, 3}, {4, 5, 6}})));
        System.out.println(Arrays.deepToString(rotate90CounterClockwise(matrix)));
    }
}
