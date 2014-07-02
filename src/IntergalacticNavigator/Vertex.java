package IntergalacticNavigator;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author bmumey + theresa
 */

import java.util.ArrayList;

public class Vertex {
    public String name;
    public int x, y;
    public boolean visited;
    public double d; // used by Dijkstra's alg
    public Vertex pred; // used by Dijkstra's alg
    public int index;
    
    // used for adjacency list representation:
    ArrayList<Vertex> neighbors;
    
    public Vertex(String name) {
        this.name = name;
    }
    
    public String toString() {
        return "(" + x + "," + y + ")";
    }
}
