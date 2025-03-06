import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
long         a,b;
        long c;
long a_b;
		Scanner sc = new Scanner(System.in);

		
		a= sc.nextLong();
		b= sc.nextLong();
		a_b = a*b;
		while(a%b!=0)
		{
			c=a%b;
			a = b;
			b = c;
		}
		System.out.println(a_b/b);
		}
	
    }