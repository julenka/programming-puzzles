package js.interview.test;

import junit.framework.Assert;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Random;

/**
 * Created by julenka on 6/21/14.
 */
public class TestUtils {
    public static Random r = new Random();

    public static int[] makeRandomArray(int arraySize, boolean unique) {
        int[] values = new int[arraySize];
        HashSet<Integer> used = new HashSet<Integer>();

        for(int i = 0; i < arraySize; i++) {
            int toInsert = r.nextInt(10000);
            while(unique && used.contains(toInsert)) {
                toInsert = r.nextInt(10000);
            }
            values[i] = toInsert;
            used.add(toInsert);
        }
        return values;
    }

    public static ArrayList<Integer> makeRandomList(int arraySize, boolean unique) {
        int[] values = makeRandomArray(arraySize, unique);
        ArrayList<Integer> result = new ArrayList<Integer>();
        for(int i = 0; i < values.length; i++){
            result.add(values[i]);
        }

        return result;
    }

    public static void checkSorted(int[] result) {
        ArrayList<Integer> adapted = new ArrayList<Integer>();
        for(int i = 0; i < result.length; i++) {
            adapted.add(result[i]);
        }
        checkSorted(adapted);
    }
    public static void checkSorted(List<Integer> result) {
        if(result.size() == 0) {
            return;
        }
        int  prev = result.get(0);
        for(int i = 1; i < result.size(); i++) {
            int cur = result.get(i);
            Assert.assertTrue("i: " + i + " cur: " + cur + " prev: " + prev, cur >= prev);
            prev = cur;
        }
    }
}
