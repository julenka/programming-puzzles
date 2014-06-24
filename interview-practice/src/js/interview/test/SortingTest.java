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
        ArrayList<Integer> values = TestUtils.makeRandomList(1000, false);
        TestUtils.checkSorted(Sorting.quicksortRecursive(values));
    }

    @Test
    public void testMergesort() throws Exception {
        ArrayList<Integer> values = TestUtils.makeRandomList(1000, false);
        TestUtils.checkSorted(Sorting.mergeSort(values));
    }

    @Test
    public void testQuicksortInPlace() throws Exception {
        int[] values = TestUtils.makeRandomArray(10000, false);
        Sorting.quicksortInPlace(values);
        TestUtils.checkSorted(values);
    }



}
