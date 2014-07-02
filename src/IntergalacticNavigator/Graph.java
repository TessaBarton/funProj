package IntergalacticNavigator;

import java.util.ArrayList;
import java.util.Iterator;
import java.math.*;


/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author bmumey + theresa
 */
public class Graph {

    public Vertex[] vertex;
    public static String[] dir;
    public static ArrayList<Vertex> path;


    public double[][] weight; // weight[i][j] >= 0.0 indicates an edge

    public Graph(int numVertices) {
        vertex = new Vertex[numVertices];
        weight = new double[numVertices][numVertices];
        for (int i = 0; i < numVertices; i++) {
            for (int j = 0; j < numVertices; j++) {
                weight[i][j] = -1.0; // no edge
            }
        }
   
    }
    
    /// vertex operations

    public void createAdjacencyLists() {
        for (int i = 0; i < vertex.length; i++) {
            vertex[i].neighbors = new ArrayList<Vertex>();
            for (int j = 0; j < vertex.length; j++) {
                if (j != i && weight[i][j] > 0.0) {
                    vertex[i].neighbors.add(vertex[j]);
                }
            }
        }
    }

    public void printGraph() {
        System.out.println("Vertices:");
        for (int i = 0; i < vertex.length; i++) {
            System.out.println(i + ": " + vertex[i]);
        }
        System.out.println("Edges:");
        for (int i = 0; i < vertex.length; i++) {
            System.out.print(vertex[i].name + " neighbors:");
            for (int j = 0; j < vertex.length; j++) {
                if (j != i && weight[i][j] > 0.0) {
                    System.out.print(" " + vertex[j] + "w:" + String.format("%.2f", weight[i][j]));
                }
            }
            System.out.println();
        }
    }

    ArrayList<Vertex> breadthFirstSearch(Vertex source) {

        ArrayList<Vertex> queue = new ArrayList<Vertex>();
        ArrayList<Vertex> visited = new ArrayList<Vertex>();

        // mark all vertices as not visited:
        for (int i = 0; i < vertex.length; i++) {
            vertex[i].visited = false;
        }
        source.visited = true;
        queue.add(source);
        while (!queue.isEmpty()) {
            Vertex head = queue.remove(0);
            visited.add(head);
            for (Iterator<Vertex> iter = head.neighbors.iterator(); iter.hasNext();) {
                Vertex neighbor = iter.next();
                if (! neighbor.visited) {
                    neighbor.visited = true;
                    queue.add(neighbor);
                }
            }
        }

        return visited;
    }
    
    // Dijkstra's algorithm:
    public void dijkstra(Vertex source) {
        ArrayList<Vertex> VminusS = new ArrayList<Vertex>();
        for (int i = 0; i < vertex.length; i++) {
            vertex[i].d = Double.MAX_VALUE; // + infinity
            vertex[i].pred = null;
            VminusS.add(vertex[i]);
        }
        source.d = 0.0;
        while (! VminusS.isEmpty()) {
            Vertex smallestDVertex = null;
            for (Iterator<Vertex> iter = VminusS.iterator(); iter.hasNext();) {
                Vertex current = iter.next();
                if (smallestDVertex == null || current.d < smallestDVertex.d) {
                    smallestDVertex = current;
                }
            }
            for (Iterator<Vertex> iter = smallestDVertex.neighbors.iterator(); iter.hasNext();) {
                Vertex neighbor = iter.next();
                double edgeWt = weight[smallestDVertex.index][neighbor.index];
                if (smallestDVertex.d + edgeWt < neighbor.d) {
                    neighbor.d = smallestDVertex.d + edgeWt;
                    neighbor.pred = smallestDVertex;
                }
            }
            VminusS.remove(smallestDVertex);
        }
//        System.out.println("Dijsktra's algorithm finished for source vertex " + source);
    }
    
    public void printShortestPath(Vertex destination) {
        path = new ArrayList<Vertex>();
        Vertex cur = destination;
        while (cur != null) {
            path.add(0, cur);
            cur = cur.pred;
        }
        dir = new String[path.size()];
        for(int i =0; i < path.size();i++){
            if(i != (path.size()-1)){
       double bearing = computeBearing(path.get(i).x,path.get(i).y,path.get(i+1).x,path.get(i+1).y);
       System.out.println(bearing);
     String temp = String.valueOf(bearing);
     System.out.println(temp);
        dir[i] = ( path.get(i).name+"at bearing"+temp+"\n");}
            else{
                 dir[i] = ( path.get(i).name +"\n");}
            }
        
        
    }
    
    public static boolean blockedByCircle(double x1, double y1,
            double x2, double y2,
            double x3, double y3, double r) {
        // line goes from (x1, y1) to (x2, y2)
        // circle is centered at (x3, y3) with radius r
        double t = 0.0;
        if (x1 != x2 || y1 != y2) {
            t = ((x2 - x1) * (x3 - x1) + (y2 - y1) * (y3 - y1)) / ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
        }else{
            return false;
        }

        if (t > 1) {
            t = 1.0;
        }
        if (t < 0) {
            t = 0.0;
        }
        // find closest point (x,y)
        double x = x1 + t * (x2 - x1);
        double y = y1 + t * (y2 - y1);

        double distSq = (x - x3) * (x - x3) + (y - y3) * (y - y3);
        return (distSq <= r * r);
        // if distance from xy to point center of circle is less than or equal to r, the line seg goes
        /// through the circle and the program returns true.

    }

    public static double computeBearing(double x1, double y1, double x2, double y2) {
        // computes the bearing to (x2, y2) from (x1, y1)

        double length = Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
        double angleRadians = Math.acos((y2 - y1) / length); // in radians
        double angleDegrees = Math.toDegrees(angleRadians);

        if (x2 > x1) {
            return angleDegrees;
        }
        return (360 - angleDegrees);
    }    
}
