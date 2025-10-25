/**
 	Code to Print the following Pattern :
 	     *
 	    ***
 	   *****
 	  *******
 	 *********
*/
import java.util.Scanner;
public class P7 {
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
			for(int l=not-i;l>=1;l--)System.out.print("  ");
		    for(int m=1;m<=i;m++) System.out.print("* ");
		    for(int n=1;n<=i-1;n++ )System.out.print("* ");
		    System.out.println();
		}
	}
}
