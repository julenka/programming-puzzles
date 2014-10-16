package js.interview;

/**
 * Created by julenka on 10/15/14.
 */
public class BalancedTreeNode {
    public BalancedTreeNode left, right;
    int height = 1;
    String data;
    public BalancedTreeNode(String data) {
        this.data = data;
    }
    public boolean isBalanced() {
        if(left == null && right == null) {
            return true;
        }
        int leftHeight = 0, rightHeight = 0;
        if(left != null){
            if(!left.isBalanced()) return false;
            leftHeight = left.height;
        }
        if(right != null) {
            if(!right.isBalanced()) return false;
            rightHeight = right.height;
        }
        height = Math.max(leftHeight, rightHeight) + 1;
        return Math.abs(leftHeight - rightHeight) <= 1;
    }

    /**
     * Clears all descendents of structure
     */
    public void clearDescendants() {
        if(left != null) {
            left.clearDescendants();
            left = null;
        }
        if(right != null) {
            right.clearDescendants();
            right = null;
        }
    }
}
