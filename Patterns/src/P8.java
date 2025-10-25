/**
 	Code to Print the following Pattern :
 	*********
 	 *******
 	  *****
 	   ***
 	    *
*/
import java.util.Scanner;

public class P8 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the number of terms = ");
		int not=sc.nextInt();
	    printPattern(not);
	}
	static void printPattern(int not)
	{
		for(int i=1;i<=not;i++)
		{
		   for(int l=i;l>1;l--)System.out.print("  ");
		   for(int j=i;j<=not;j++) System.out.print("* ");
		   for(int m=not-i;m>=1;m--)System.out.print("* ");
		   System.out.println();
		}
	}
}
