package js.test;

import js.interview.Searching;
import junit.framework.Assert;
import org.junit.Test;

import java.util.Arrays;

/**
 * Created by julenka on 6/21/14.
 */
public class SearchingTest {
    @Test
    public void testBinarySearch() throws Exception {
        int[] values = TestUtils.makeRandomArray(1000, true);
        Arrays.sort(values);

        int binarySearchResult = Searching.binarySearch(values, -1);

        Assert.assertEquals(binarySearchResult, -1);
        for(int i = 0; i < values.length; i++) {
            binarySearchResult = Searching.binarySearch(values, values[i]);
            Assert.assertEquals(i, binarySearchResult);
        }
    }
}
