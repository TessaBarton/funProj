/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package IntergalacticNavigator;

import java.awt.Container;
import java.awt.FlowLayout;
import java.util.Random;
import javax.swing.*;

/**
 *
 * @author bmumey + theresa
 */
public class TestGraphs extends JFrame {

    /**
     * @param args the command line arguments
     */
    public static Graph g;
    public static String[] placenames = {"Tatueen","1. Ceramic Planet", "2. Balkan Nebulae", "3. Californian Cluster", "4. Downtown Base", "5. Home Base", "6. Chicago Base", "7. Drage Base", "8. Oldy Base", "9. Big Sky Base", "10. Beach Base", "11. Base Los Gatos", "12. Denver Base", "13. Lyon Base", "14. EPS 254 base","15. The sub planet","16. GreenPlanet ","17. Nissan base","18. Base-ment","19. Planet this age sucks","20. 319 w. Story","21. McGuire Rd.","22. Taylor Swift Planet","23. Planet @(*&$(*&#","24. Long tall glasses", "25. Mongol planet", "26. WinterFell", "27. Iron Islands","28. Carvahall","29. Dubrovnic", "30. Bridger Bowl", "31. A black hole", "32. Pit of death planet", " 33. Mordor", "34. out of names planet"};
    public static AsteroidBelts a;
    public static String follow;
    

    public static double effectivedistance(double x0, double y0, double x1, double y1, double R) {
        return R * Math.sqrt((x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0));
    }
    public TestGraphs()
    { super("");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Container contentPane = getContentPane();
        contentPane.setLayout(new FlowLayout());
        contentPane.isMaximumSizeSet();
        JPanel temp = new Panel();
        contentPane.add(temp);
        contentPane.add(new MapPanel());
        
        pack();
        setLocationRelativeTo(null);
        setVisible(true); 
  
        ///turn off
    }
   

    public static void main(String[] args) {
        // TODO code application logic here
        TestGraphs newgraph = new TestGraphs();
        

        // create asteroid belts
        a = new AsteroidBelts();
        a.createAsteroidBelts();
        createGraph();
//        g.printGraph();

//        // find nearest neighbors:
//        for (int i = 0; i < numVertices; i++) {
//            double lowestD = Double.MAX_VALUE;
//            int nearestNeighbor = 0;
//            for (int j = 0; j < numVertices; j++) {
//                if (i != j) {
//                    double d = distance(g.vertex[i].x, g.vertex[i].y,
//                            g.vertex[j].x, g.vertex[j].y);
//                    if (d < lowestD) {
//                        nearestNeighbor = j;
//                        lowestD = d;
//                    }
//                }
//            }
//            // add edge between i and nearestneighbor;
//            System.out.println(g.vertex[i] + " has nearest neighbor " + g.vertex[nearestNeighbor]);
//            g.weight[i][nearestNeighbor] = lowestD;
//        }
        g.createAdjacencyLists();

    }

    //System.out.println("BFS returns: " + g.breadthFirstSearch(g.vertex[0]));
    public static void createGraph() {
        //creates graph. Bugfix- need to prevent bases from being in asteroid belts
        int numVertices = 35;
        int boardsize = 1000;
        Random r = new Random();
        ///seed the random number generator to get the same graph every time

        g = new Graph(numVertices);

        for (int i = 0; i < numVertices; i++) {
            g.vertex[i] = new Vertex("Vertex " + i);
            boolean locationOK = false;
            while(locationOK == false){
            g.vertex[i].x = r.nextInt(boardsize);
            g.vertex[i].y = r.nextInt(boardsize);
            locationOK= avoidBelt(g.vertex[i].x,g.vertex[i].y);
        }
            g.vertex[i].name = placenames[i];
            g.vertex[i].index = i;
        }
    
        for (int i = 0; i < numVertices; i++) {
            for (int s = 0; s < numVertices; s++) {
                if(s!=i){
                    g.weight[i][s] = g.weight[s][i]
                                = effectivedistance(g.vertex[i].x, g.vertex[i].y, g.vertex[s].x, g.vertex[s].y,.5+r.nextDouble()*4.5);
                    
                for (int p = 0; p < 10; p++) {
                    
                    if (Graph.blockedByCircle(g.vertex[s].x, g.vertex[s].y, g.vertex[i].x, g.vertex[i].y,
                            TestGraphs.a.asteroids[p].x, TestGraphs.a.asteroids[p].y, TestGraphs.a.asteroids[p].radius)==true) {
                        // sometimes breaks if planet not blocked
                        g.weight[i][s] = g.weight[s][i] = -1.0; 
                    }
                        
                        //need to time warp distance
                        
                    }}}
                }
            

        for (int i = 0; i < numVertices; i++) {
            for (int s = 0; s < numVertices; s++) {
                System.out.println(g.weight[i][s]);
            }
        }

    }
    
    private static boolean avoidBelt(int x, int y){
        /// returns true if the given point is allowable and not in a belt
        boolean p = true;
        for( int i = 0; i < 10; i++){
            // fix this!
            if( (Graph.blockedByCircle(x, y, x+1, y+1,a.asteroids[i].x , a.asteroids[i].y,a.asteroids[i].radius ))==true){
                p= false;
            }
        }
        return p;
    }
    public static void findpath(Vertex s,Vertex f){
        g.dijkstra(s);
        g.printShortestPath(f);
        follow = ("( distance = " + String.format("%.2f", g.vertex[f.index].d) + ")");
    }
    
    public static void printAllVertexes(Vertex v) {
        g.dijkstra(v);
//        System.out.println("paths from" + v);
        for (int i = 0; i < g.vertex.length; i++) {
            System.out.println("The shortest path from " + v.name + " to " + g.vertex[i].name + " is:");
            g.printShortestPath(g.vertex[i]);
           follow = ("( distance = " + String.format("%.2f", g.vertex[i].d) + ")");
        }

    }

    

    public static double sumD(Vertex v) {
        g.dijkstra(v);
        double sum = 0;
        for (int i = 0; i < g.vertex.length; i++) {
            sum = sum + g.vertex[i].d;
        }
        return sum;
    }
}


