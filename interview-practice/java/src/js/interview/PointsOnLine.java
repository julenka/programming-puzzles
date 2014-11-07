package js.interview;

import processing.core.PApplet;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class PointsOnLine extends PApplet {
    final int MIN_X = -200;
    final int MIN_Y = -200;
    final int MAX_X = 200;
    final int MAX_Y = 200;
    final int N_POINTS = 500;
    final int POINT_RADIUS=5;

    private Point[] points = new Point[N_POINTS];
    private float m = 1;
    private float b = 1;
    Random random = new Random();

    private void setupPoints() {
        for(int i = 0; i < N_POINTS; i++) {
            points[i] = new Point(random.nextInt(width) + MIN_X, random.nextInt(height) + MIN_Y);
        }
    }

    private void findMostCollinearPoints() {
        HashMap<String,Integer> lineCount = new HashMap<String, Integer>();
        // for each pair of points, find m, b in y = mx + b
        for(int i = 0; i < N_POINTS; i++) {
            for(int j = i+1; j < N_POINTS; j++) {
                // compute m, b
                Point p1 = points[i];
                Point p2 = points[j];

                double m =
                        Math.round((p2.y - p1.y)/(p2.x - p1.x) * 1000) / 1000.0;
                // y = mx + b
                // b = y - mx
                double b = Math.round( (p2.y - m * p2.x) * 100 ) / 100.0;
                System.out.println(m + ", " + b);
                String key = m + "," + b;
                if (!lineCount.containsKey(key)) {
                    lineCount.put(key, 0);
                }
                int count = lineCount.get(key);
                lineCount.put(key, count + 1);
            }
        }
        // round to 100th
        // hashmap [m,b]->count
        int maxCount = 0;
        for(Map.Entry<String,Integer> entry: lineCount.entrySet()) {
            if(entry.getValue() > maxCount) {
                maxCount = entry.getValue();
                String[] mb = entry.getKey().split(",");
                m = Float.parseFloat(mb[0]);
                b = Float.parseFloat(mb[1]);
            }

        }
        System.out.println("m: " + m +  ", b: " + b + " count: " + maxCount);
        // find m,b with largest value
        // draw line

    }

    public void setup() {
        size(MAX_X - MIN_X, MAX_Y - MIN_Y);
        setupPoints();
        findMostCollinearPoints();
    }
    public void draw() {
        background(0);
        drawAxes();
        drawPoints();
        drawLine();
    }

    private void drawLine() {
        stroke(0, 255, 0);
        line(MIN_X + width / 2, m * MIN_X + b + height / 2, MAX_X + width / 2, m * MAX_X + b + height / 2);
    }
    private void drawPoints() {
        noFill();
        for(int i = 0; i < N_POINTS; i++) {
            Point p = points[i];
            ellipse(p.x + width/2, p.y + height/2, POINT_RADIUS, POINT_RADIUS);
        }
    }

    private void drawAxes() {
        stroke(255);
        line(0,height/2,width,height/2);
        line(width/2,0,width/2,height);
    }


    public static void main(String[] args) {
        PApplet.main(new String[]{"js.interview.PointsOnLine"});
    }
}

class Point {
    public float x;
    public float y;
    public Point(float x, float y) {
        this.x = x;
        this.y = y;
    }
}
