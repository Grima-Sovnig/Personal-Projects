// Project 3 for 3300-002 by Gabriel Snider
// 4/11/22

package net.codejava;

import java.sql.*;


// Main Class
public class project3 
{
	
	//executeStatement allows the user to perform operations on the database. It has a catch if there is a error completing the statement.
		 public static void executeStatement(String sql) {
			 
		        ResultSet results;
		        
		        try (Statement stmt = conn.createStatement();) {
		        	
		            results = stmt.executeQuery(sql);
		            printResults(results);
		            
		        }
		        catch (Exception e) {
		        	
		            System.out.println("\nUnable to perform SQL statement on database.\n");
		        }
		    }
		 
		 //executeUpdate lets the user add, delete or modify existing tuples in the database.
		    public static void executeUpdate(String sql) {
		    	
		        try (Statement stmt = conn.createStatement();) {
		        	
		            stmt.executeUpdate(sql);
		        }
		        catch (Exception e) {
		        	
		            System.out.println("\nUnable to perform update query on database.\n");
		            
		        }
		    }
		    
		    ////printResults presents the user of this program with a readable and organized view of the statements.
		    private static void printResults(ResultSet results) {
		    	
		        try {
		        	
		            ResultSetMetaData rsmd = results.getMetaData();
		            int numCols = rsmd.getColumnCount();
		            
		            while (results.next()) {
		            	
		                for (int i = 1; i <= numCols; i++) {
		                	
		                    if (i > 1) System.out.print(",  ");
		                    
		                    String columnValue = results.getString(i);
		                    System.out.print(columnValue + " " + rsmd.getColumnName(i));
		                }
		                
		                System.out.println("");
		            }
		        }
		        catch (Exception e) {
		        	
		            System.out.println("Unable to print results!");
		            
		        }
		    }
	
	static Connection conn;
	public static void main(String[] args) {
		
		boolean connect = false;
		Keyboard kb = Keyboard.getKeyboard();
		
		// Gets the username and password for the user and validates their connection to the database.
		while(!connect) {
			try {
				String username, password;
				username = kb.readString("Enter Username: ");
				password = kb.readString("Enter Password: ");
				
				conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/university" , username, password);
				System.out.println("Connection Successful!");
				connect = true;
				
			}catch(SQLException e){
	
				System.out.println("Unable to connect, please check Username or Password.");
				
			}
		}
		
		//This portion of the code presents the user with a simple and easy to read command line interface to operate the program.
		boolean menu = false;
		
		while(!menu) {
			
			int userInput;
		
			System.out.println("\nMenu: ");
			System.out.println("1. Update Database (Add or Delete tuples from the Database");
			System.out.println("2. View Database");
			System.out.println("3. Exit.");
			
			userInput = kb.readInt("\nOption: ");
			
			switch(userInput) {
			
			case 1:
				
				//Case 1 asks the user for the query that want to execute that adds or delete from the database.
				String userUpdate = kb.readString("Please provide your Update SQL Query here: ");
				executeUpdate(userUpdate);
				break;
				
			case 2:
				
				//Case 2 asks the user for a query to view items from the database with.
				String userView = kb.readString("Please provide your Selection or View SQL Query here: ");
				executeStatement(userView);
				break;
				
			case 3:
				
				//Case 3 is the exit condition for this switch statement. Allows the user to exit the program.
				menu = true;
				break;
				
			default:
				//This default case is here to make sure the input the user is giving the program actually is valid.
				System.out.println("Invalid Input, Please try again!");
				break;
				
			}
		} 
		
	}
}


