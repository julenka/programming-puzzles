package js.interview;

import java.util.ArrayList;
import java.util.Arrays;

/**
 * Created by julenka on 6/19/14.
 */
public class Sorting {
    public static ArrayList<Integer> quicksortRecursive(ArrayList<Integer> values) {
        if(values.size() <= 1) {
            return values;
        }
        int pivot = values.get(0);
        ArrayList<Integer> left = new ArrayList<Integer>();
        ArrayList<Integer> right = new ArrayList<Integer>();
        for(int i = 1; i < values.size(); i++) {
            int value = values.get(i);
            if (value < pivot) {
                left.add(value);
            } else {
                right.add(value);
            }
        }
        left = quicksortRecursive(left);
        right = quicksortRecursive(right);
        ArrayList<Integer> result = new ArrayList<Integer>(left);
        result.add(pivot);
        result.addAll(right);
        return result;
    }

    public static void swap(int[] values, int index_1, int index_2) {
        int tmp = values[index_1];
        values[index_1] = values[index_2];
        values[index_2] = tmp;
    }
    public static void quicksortInPlace(int[] values) {
        quicksortInPlaceHelper(values, 0, values.length - 1 );
    }
    public static void quicksortInPlaceHelper(int[] values, int start_index, int end_index) {
        if(start_index >= end_index) {
            return;
        }
        int pivot = values[start_index];
        int less_than_ptr = start_index;
        int greater_than_ptr = end_index;
        int current_ptr = start_index + 1;
        while(current_ptr <= greater_than_ptr) {
            int current_val = values[current_ptr];
            if(current_val < pivot) {
                swap(values, less_than_ptr, current_ptr);
                less_than_ptr++;
                current_ptr++;
            } else {
                swap(values, greater_than_ptr, current_ptr);
                greater_than_ptr--;
            }

        }
        // finish
        quicksortInPlaceHelper(values, start_index, less_than_ptr - 1);
        quicksortInPlaceHelper(values, greater_than_ptr + 1, end_index);
    }
}
