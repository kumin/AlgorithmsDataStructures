package leed.code.com;

public class ReverseInteger {
    public static int reverse(int x) {
        if ((x > 2147483647) || (x < -2147483648)) return 0;
        char[] chars = String.valueOf(x).toCharArray();
        int n = chars.length;
        if (n == 1) return x;
        if (x < 0) {
            if (n == 2) return x;
            for (int i = 1; i <= n / 2; i++) {
                char tmp = chars[i];
                chars[i] = chars[n - i];
                chars[n - i] = tmp;
            }
        } else {
            for (int i = 0; i < n / 2; i++) {
                char tmp = chars[i];
                chars[i] = chars[n - i - 1];
                chars[n - i - 1] = tmp;
            }
        }
        try {
            return Integer.parseInt(String.valueOf(chars));
        } catch (NumberFormatException e) {
            return 0;
        }
    }

    public static void main(String[] args) {
        System.out.println(reverse(123));
    }
}
