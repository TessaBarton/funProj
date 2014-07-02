/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package IntergalacticNavigator;
import java.util.Random;

/**
 *
 * @author Tessa
 */
public class AsteroidBelts {
      public Asteroids[] asteroids;
      public int width,height,maxradius;
      
      
      public void createAsteroidBelts(){
        /// creates list of 10 random asteroid belts with radius r; x and y
        asteroids = new Asteroids[10];
        Random rnd = new Random();
        
        // numbers need to be changed if size increases. when.
        width = 980;
        height= 980;
        maxradius = 50;
        ///should be 50
 

        for(int i = 0 ; i < 10; i ++){
            /// Should be 1000 fix later
            asteroids[i] = new Asteroids(Integer.toString(i));
            asteroids[i].x = 10 + rnd.nextInt(width);
            asteroids[i].y =  10 + rnd.nextInt(height);
            asteroids[i].radius = (maxradius + rnd.nextInt(maxradius));
            
        }
    }
    
}
