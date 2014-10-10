package js.interview;

import processing.core.PApplet;

import java.awt.event.KeyEvent;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * Created by julenka on 10/6/14.
 */
public class Djikstra extends PApplet {
    static final boolean ROUND_EDGE_WEIGHTS = true;
    final int NODE_RADIUS = 10;
    final int NODE_SPACING = 100;
    final int NUM_ROWS = 5;
    final int NUM_COLS = 5;

    final int START_R = 0;
    final int START_C = 0;
    final int END_R = 4;
    final int END_C = 4;

    List<Node> nodes = new ArrayList<Node>();
    Random random = new Random();

    List<Node> cheapestPath = new ArrayList<Node>();
    List<Node> unexploredNodes = new ArrayList<Node>();

    @Override
    public void setup() {
        int node_dx = NODE_RADIUS * 2 + NODE_SPACING;
        int node_dy = node_dx;
        int x_start = NODE_SPACING;
        int y_start = NODE_SPACING;
        super.setup();
        size(NODE_SPACING * (NUM_COLS + 2), NODE_SPACING * (NUM_ROWS + 2));
        // setup nodes
        for(int r = 0; r < NUM_ROWS; r++) {
            for(int c = 0; c < NUM_COLS; c++) {
                float x = x_start + c * node_dx;
                float y =  y_start + r * node_dy;
                if(r == START_R && c == START_C) {
                    nodes.add(new Node(x, y, new Color(0,255,0)));
                } else if (r == END_R && c == END_C) {
                    nodes.add(new Node(x, y, new Color(255, 0, 0)));
                } else {
                    nodes.add(new Node(x, y));
                }

            }
        }

        // setup outgoingEdges
        for(int i = 0; i < nodes.size(); i++) {
            int r = i / NUM_COLS;
            int c = i % NUM_COLS;
            Node cur = getNode(r, c);
            if(r < NUM_ROWS - 1 && c < NUM_COLS - 1) {
                // corner
                cur.addEdge(getNode(r+1,c+1), random.nextFloat() * 100);
            }
            if(r < NUM_ROWS - 1) {
                // bottom
                cur.addEdge(getNode(r+1,c), random.nextFloat() * 100);
            }
            if(c < NUM_COLS - 1) {
                // right
                cur.addEdge(getNode(r,c+1), random.nextFloat() * 100);
            }
        }

    }

    private void reset() {
        for (Node node : nodes) {
            for(Edge edge : node.outgoingEdges) {
                edge.weight = random.nextFloat() * 100;
            }
            node.weight = Float.MAX_VALUE;
            node.explored = false;
        }
        cheapestPath.clear();
        // reset unexplored nodes?
    }

    private Node getNode(int r, int c) {
        int i = r * NUM_COLS + c;
        return nodes.get(i);
    }

    @Override
    public void draw() {
        background(0);
        // draw nodes
        for(Node n : nodes) {

            for(Edge e : n.outgoingEdges) {
                stroke(100);
                line(e.from.x, e.from.y, e.to.x, e.to.y);
                fill(255);
                text("" + Math.round(e.weight), (e.from.x + e.to.x) / 2, (e.from.y + e.to.y) / 2);
            }
            fill(n.color.r, n.color.g, n.color.b);
            ellipse(n.x, n.y, NODE_RADIUS, NODE_RADIUS);
            fill(255);
            if(n.weight < Float.MAX_VALUE) {
                text("" + Math.round(n.weight), n.x + NODE_RADIUS, n.y + NODE_RADIUS);
            }
        }

        noFill();
        Node prev = null;
        for (Node n : cheapestPath) {
            stroke(0,255, 0);
            ellipse(n.x, n.y, NODE_RADIUS, NODE_RADIUS);
            if(prev != null) {
                line(prev.x, prev.y, n.x, n.y);
            }

            prev = n;
        }
    }

    @Override
    public void keyPressed(KeyEvent e) {
        if(e.getKeyChar() == ' ') {
            print("running findPath()...");
            findPath();
        }
        if(e.getKeyChar() == 'r') {
            reset();
        }

    }

    public static void main(String[] args) {
        PApplet.main(new String[] { "js.interview.Djikstra" });
    }


    /**
     * Finds the lowest cost path between START node and END node
     */
    private void findPath() {
        // reset state
        for (Node node : nodes) {
            node.weight = Float.MAX_VALUE;
            node.explored = false;
        }
        unexploredNodes.clear();

        // initialize
        for (Node node : nodes) {
            unexploredNodes.add(node);
        }
        getNode(START_R, START_C).weight = 0;

        // Mark weights
        Node cur = findCheapestUnexploredNode();
        while(cur != null && unexploredNodes.size() > 0) {
            cur.setExplored();
            unexploredNodes.remove(cur);
            for(Edge edge : cur.outgoingEdges) {
                Node outgoing = edge.to;
                // Ignore nodes that have been explored already
                if(outgoing.explored) {
                    continue;
                }
                if(cur.weight + edge.weight < outgoing.weight) {
                    outgoing.weight = cur.weight + edge.weight;
                }
            }
            cur = findCheapestUnexploredNode();
        }

        // set cheapest path
        cheapestPath.clear();
        cur = getNode(END_R, END_C);
        if(cur.weight == Float.MAX_VALUE) {
            print("path not found!");
            return;
        }
        Node start = getNode(START_R, START_C);
        while(cur != start) {
            cheapestPath.add(cur);
            Node cheapestNode = null;
            for(Edge e: cur.incomingEdges) {
                if(e.weight + e.from.weight == cur.weight) {
                    cheapestNode = e.from;
                }
            }
            cur = cheapestNode;
        }
        cheapestPath.add(start);

    }

    private Node findCheapestUnexploredNode() {
        float cheapestValue = Float.MAX_VALUE;
        Node result = null;
        for(Node node : unexploredNodes) {
            if(node.weight < cheapestValue) {
                cheapestValue = node.weight;
                result = node;
            }
        }
        return result;

    }
}

class Color {
    int r, g, b;
    public Color() {
        this.r = 100;
        this.g = 100;
        this.b = 100;
    }
    public Color(int r, int g, int b) {
        this.r = r;
        this.g = g;
        this.b = b;
    }
}
class Node {
    float x, y, weight;
    Color color;
    List<Edge> outgoingEdges;
    List<Edge> incomingEdges;
    boolean explored;
    public Node(float x, float y) {
        this.outgoingEdges = new ArrayList<Edge>();
        this.incomingEdges = new ArrayList<Edge>();
        this.x = x;
        this.y = y;
        this.weight = Float.MAX_VALUE;
        this.color = new Color();
        this.explored = false;
    }
    public Node(float x, float y, Color c) {
        this(x, y);
        this.color = c;
    }

    public void setExplored() {
        this.explored = true;
        this.color = new Color(50,50,50);

    }

    public void addEdge(Node to, float weight) {
        Edge newEdge = new Edge(this, to, weight);
        outgoingEdges.add(newEdge);
        to.incomingEdges.add(newEdge);
    }
}

class Edge {
    float weight;
    Node from, to;
    public Edge(Node from, Node to, float weight) {
        if(Djikstra.ROUND_EDGE_WEIGHTS) {
            this.weight = Math.round(weight);
        } else {
            this.weight = weight;
        }

        this.from = from;
        this.to = to;
    }
}
