/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
package IntergalacticNavigator;
/**
 *
 * @author Tessa
 */
package IntergalacticNavigator;

import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.JTextArea;

public class Panel extends JPanel {
     public JTextField startField, endField;
     public JTextArea directions;
     private JButton clearButton, enterButton;
     
     public Panel() {
        setLayout(new FlowLayout());

        add(new JLabel("Enter start NUMBER"));
        startField = new JTextField(5);
        //firstNameField.addActionListener(new NewTextFieldValue());
        add(startField);
        add(new JLabel("Enter end NUMBER"));
        endField = new JTextField(5);
       
        //lastNameField.addActionListener(new NewTextFieldValue());
        add(endField);
        
        clearButton = new JButton("Clear");
        clearButton.addActionListener(new ClearPressed());
        add(clearButton);
        enterButton = new JButton("Enter");
        enterButton.addActionListener(new EnterPressed());
        add(enterButton);
        directions = new JTextArea(10,25);
        add(directions);
}

public void clearFields() {
        startField.setText("");
        endField.setText("");
        directions.setText("");
}
private class ClearPressed
            implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
            clearFields();
        }
    }

    private class EnterPressed
            implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
            int startint = Integer.parseInt(startField.getText());
            int endint = Integer.parseInt(endField.getText());
            
            TestGraphs.findpath(TestGraphs.g.vertex[startint], TestGraphs.g.vertex[endint]);
            String string= "";
            for( int i = 0 ; i < Graph.dir.length; i++){
                string =string +Graph.dir[i];
            }
            directions.setLineWrap(true);
            directions.setText("Starting at : " + TestGraphs.g.vertex[startint].name+ "\n" +string +"\n"+"arrive at : " + TestGraphs.g.vertex[endint].name +"\n"+ TestGraphs.follow );
           
            
           

}
    }
}