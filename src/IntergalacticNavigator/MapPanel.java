/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package IntergalacticNavigator;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseListener;



/**
 *
 * @author Tessa
 */
public class MapPanel extends JPanel {
    private int width = 1000;
    private int height = 1000;
    
    public JTextField startField, endField;
;
    //private TicTacToe tttGame;

    // TTT board data:
    private char[][] board;

    /**
     * Constructor for objects of class MondrianFrame
     */
    public MapPanel() {
        
        setPreferredSize(new Dimension(width, height));

        // initialize the board:
        board = new char[width][height]; // initialize board

        for (int i = 0; i < width; i++) {
            for (int j = 0; j < height; j++) {
                board[i][j] = ' '; // blank char
            }
        }
    }
    

    public void paint(Graphics g) {
        g.setColor(Color.BLACK);
        g.fillRect(0, 0, width, height);
//paint asteroid field
        g.setColor(Color.RED);
        try{
        for(int i = 0; i<10; i++){
        
        int temp = TestGraphs.a.asteroids[i].radius;
        // sometimes throws out of bounds error when out of bounds oh well . program still runs
        g.drawOval(TestGraphs.a.asteroids[i].x -temp, TestGraphs.a.asteroids[i].y-temp, 2*TestGraphs.a.asteroids[i].radius, 2*TestGraphs.a.asteroids[i].radius);
        }
        }
        catch (NullPointerException e){
            System.err.println("FileNotFoundException: " + e.getMessage());
    throw new NullPointerException();
        }
                

        
        //print edges
         Font f = new Font("Courier", Font.PLAIN, 10);
        g.setFont(f);
        int counter = 0;
        int edgecounter = 0;
        g.setColor(Color.DARK_GRAY);
        for(int q= 0; q< TestGraphs.g.vertex.length;q++){
            for(int r= 0; r< TestGraphs.g.vertex.length;r++){
                if(TestGraphs.g.weight[q][r] <= 0||TestGraphs.g.weight[r][q] <=0 ){
                    counter ++;
                }else{
                    edgecounter++;
                    g.drawLine(TestGraphs.g.vertex[q].x, TestGraphs.g.vertex[q].y,TestGraphs.g.vertex[r].x, TestGraphs.g.vertex[r].y) ;
                }
            }
        }
//        System.out.println(counter);
//        System.out.println(edgecounter);
        //print bases
        g.setColor(Color.YELLOW);
        for(int i = 0; i<TestGraphs.g.vertex.length; i++){
        int temp = 2;
        g.drawOval(TestGraphs.g.vertex[i].x, TestGraphs.g.vertex[i].y, 2*temp, 2*temp);
        g.drawString(TestGraphs.g.vertex[i].name, TestGraphs.g.vertex[i].x, TestGraphs.g.vertex[i].y-3);
        }
        

        
        

       
        FontMetrics fm = g.getFontMetrics();

        int a = fm.getAscent();
        int h = fm.getHeight();

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
               
               
            }
        }
    }
   
    

    public void printBoard() 
    {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(" " + board[i][j]);
            }
            System.out.println();
        }
    }
 
    
}
