package js.interview;

public class Searching {
    public static int binarySearch(int[] haystack, int needle) {
        int startIndex = 0;
        int endIndex = haystack.length;
        while(startIndex <= endIndex) {
            int middleIndex = (startIndex + endIndex) / 2;
            if(haystack[middleIndex] == needle) {
                return middleIndex;
            }
            if(haystack[middleIndex] > needle) {
                endIndex = middleIndex - 1;
            } else {
                startIndex = middleIndex + 1;
            }
        }
        return -1;
    }
}
