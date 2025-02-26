import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String playerName;
        int[] playerInitialCount = new int[26];
        int threshold = 5;
        int printedCount = 0;
        
        for (int i = 0; i < playerInitialCount.length; i++) {
            playerInitialCount[i] = 0;
        }
        int numPlayers = sc.nextInt();

        for (int i = 0; i < numPlayers; i++) {
            playerName = sc.next();
            char initial = playerName.charAt(0);
            int index = initial - 'a';
            playerInitialCount[index]++;
            
            if (playerInitialCount[index] == threshold) {
                printedCount++;
            }
        }
        for(int i=0; i<playerInitialCount.length;i++) {
        	if(playerInitialCount[i]>=5) {
        		System.out.print((char)(i+'a'));
        	}
        }

        if (printedCount == 0) {
            System.out.print("PREDAJA");
        }
    }
}
