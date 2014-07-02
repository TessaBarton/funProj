/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package IntergalacticNavigator;

/**
 *
 * @author Tessa
 */
public class Asteroids {
 
    public int x, y;
    public int radius;
    public String name;
 
    public int index;
    
    public Asteroids(String name) {
        this.name = name;
        this.radius = 0;
        this.x = 0;
        this.y = 0;
    }
    public String toString() {
        return "(" + x + "," + y + ")";
    }
}


