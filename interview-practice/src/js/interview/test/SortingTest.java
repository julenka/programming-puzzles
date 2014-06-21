package js.interview.test;

import js.interview.Sorting;
import org.junit.Test;

import java.util.*;

/**
 * Created by julenka on 6/18/14.
 */
public class SortingTest {

    @Test
    public void testQuicksortRecursive() throws Exception {
        ArrayList<Integer> values = new ArrayList<Integer>();
        for(int i = 0; i < 1000; i++) {
            values.add(TestUtils.r.nextInt(10000));
        }
        ArrayList<Integer> result = Sorting.quicksortRecursive(values);
        TestUtils.checkSorted(result);
    }


    @Test
    public void testQuicksortInPlace() throws Exception {
        int[] values = TestUtils.makeRandomArray(10000, false);
        Sorting.quicksortInPlace(values);
        TestUtils.checkSorted(values);
    }



}
