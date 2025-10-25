/**
 	Code to Print the following Pattern :
 	     *
 	    ***
 	   *****
 	  *******
 	 *********
 	  *******
 	   *****
 	    ***
 	     *
*/
import java.util.Scanner;
public class P9 {
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
		    for(int l=1;l<=not-i;l++) System.out.print("  ");
		    for(int m=1;m<=i;m++)System.out.print("* ");
		    for(int n=i;n>1;n--)System.out.print("* ");
		    System.out.println();
		}
		for(int i=1;i<=not;i++)
		{
			 for(int l=i;l>1;l--)System.out.print("  ");
			 for(int k=i;k<=not;k++)System.out.print("* ");
			 for(int n=not-i;n>=1;n--)System.out.print("* ");
			 System.out.println();
		}
	}
}

