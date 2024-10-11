import java.util.ArrayList;
import java.util.StringTokenizer;
import java.util.Scanner;

public class Main {
	static int[][] graph;
	static boolean[][] visited;
	static int N,M;
	static int answer;
	
	static int[] dx = {-1,0,1,0};
	static int[] dy = {0,-1,0,1};
	
    public static void main(String[] args) {
      
    	//입력 및 초기화
    	Scanner sc = new Scanner(System.in);
    	
    	N = sc.nextInt();
    	
    	graph = new int[N+1][N+1];
 
    	
    	//그래프 정보 입력
    	for(int i=1; i<=N; i++) {
    		for(int j=1; j<=N;j++) {
    			graph[i][j] = sc.nextInt();
    		}
    	}
    	
    	int maxHeight = getMaxHeight(); // 가장 높은 곳의 높이
    	
    	
    	//dfs
    	int maxSafeZone = 1;
    	for(int h =1;h<=maxHeight;h++ ) {
    		maxSafeZone = Math.max(maxSafeZone, getSafeZone(h));
    	}
    	
    	answer = maxSafeZone;
    	System.out.print(answer);
    }

    //최대 높이 가져옴
	private static int getMaxHeight() {
		 int max = 0;
	        for (int i = 0; i < N; i++) {
	            for (int j = 0; j < N; j++) {
	                max = Math.max(max, graph[i][j]);
	            }
	        }
	        return max;
	}
	
	//높이에 따른 안전지역 개수 반환
	private static int getSafeZone(int h) {
	   	visited = new boolean[N+1][N+1];
		int safeZone=0;
		
    	for(int i =0; i<= N;i++) {
    		for(int j=1; j<=N;j++)
    		if(graph[i][j]>h&&!visited[i][j]) {
    			dfs(i,j,h);
    			safeZone++;
    		}    		
    	}
    	return safeZone;
	}

	//깊이우선탐색
	private static void dfs(int x, int y,int h) {
		// TODO Auto-generated method stub
		visited[x][y] = true;
		//주변에 높이조건만족, 상하좌우, 방문여건 만족시 dfs실행
		for(int i =0; i<4; i++) {
			int nextX = x+dx[i];
			int nextY = y+dy[i];
			if(isInsideGraph(nextX,nextY)&&graph[nextX][nextY]>h&&!visited[nextX][nextY])//벽이아니면서 상하좡
			{
				dfs(nextX,nextY,h);
			}
		}
	}
	
	//그래프를 넘어가면 false를를 반환
	private static boolean isInsideGraph(int x, int y) {
		return (x > 0 && x <= N && y > 0 && y <= N);
	}
}
