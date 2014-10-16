package js.interview.test;

import js.interview.BalancedTreeNode;
import junit.framework.Assert;
import org.junit.Test;

/**
 * Created by julenka on 10/15/14.
 */
public class BalancedTreeTest {
    @Test
    public void balancedTreeTest() {
        BalancedTreeNode a = new BalancedTreeNode("a");
        BalancedTreeNode b = new BalancedTreeNode("b");
        BalancedTreeNode c = new BalancedTreeNode("c");
        BalancedTreeNode d = new BalancedTreeNode("d");
        BalancedTreeNode e = new BalancedTreeNode("e");
        BalancedTreeNode f = new BalancedTreeNode("f");
        BalancedTreeNode g = new BalancedTreeNode("g");

        Assert.assertTrue(a.isBalanced());

        // one child
        a.left = b;
        Assert.assertTrue(a.isBalanced());

        // 2 children
        b.left = c;
        Assert.assertFalse(a.isBalanced());

        a.right = d;
        d.right = e;

        Assert.assertTrue(a.isBalanced());

        e.right = f;
        Assert.assertFalse(a.isBalanced());

        c.right = g;
        Assert.assertTrue(c.isBalanced());


    }

}
