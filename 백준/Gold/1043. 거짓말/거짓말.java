import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
    	
    	int n,m  ;
    	Scanner sc = new Scanner(System.in);    	
    	n = sc.nextInt(); //사람의 수
    	m = sc.nextInt(); //파티의 수
    	
    	//사람들 리스트 생성. 인덱스+1 이 사람번호고, 값이0 = 진실모름 , 값이 1 = 진실알음 
    	int[] peopleList = new int[n+1];
    	for(int i =0; i<=n; i++) {
    		peopleList[i] =0;	//일단 0으로 초기화
    	}
    	
    	//진실을 아는 사람 동적리스트
    	int realPeopleSize; //진실을 아는사람 수.
    	realPeopleSize = sc.nextInt(); 
    	for(int i =0; i <realPeopleSize;i++) {
    		int realPeople = sc.nextInt(); //진실을 아는사람 번호
    		peopleList[realPeople] = 1; //알고있는사람 1로 변경
    	}
    	
    	//m개 만큼의 동적배열생성
    	ArrayList<Integer>[] partyList = new ArrayList[m];
    	for (int i = 0; i < m; i++) {
    		partyList[i] = new ArrayList<Integer>();
    		int partyPeopleSize; //파티에 참여하는 사람 수
    		partyPeopleSize = sc.nextInt();
    		for(int j=0; j<partyPeopleSize;j++) {
    			int partyPeople = sc.nextInt(); //파티에 참여하는 사람 번호
    			partyList[i].add(partyPeople);
    		}
    	}
    	//한바퀴 돌면서 진실 알려짐 체크
    	
    	for(int k =0; k<m; k++) {
    	for(int i =0; i<m;i++) {
    		int sum=0;
    		for(int num: partyList[i])
    		{
    			sum += peopleList[num];
    		}
    		if(sum>0) { //한명이라도 진실을 알고 있다.
    			for(int num: partyList[i]){
        			peopleList[num]=1; //참가한 사람 모두 알게된다.
        		}
    		}
    	}
    	}
        /*for (int i = 1; i <= n; i++) {
            System.out.print(peopleList[i] + " ");
        }
        System.out.println();*/
    	
    	//두번째때 참여한 사람들리스트의 값의 합이 0 인경우 체크 => 정답
    		int answer =0;
	    	for(int i =0; i<m;i++) {
	    	int sum=0;
			for(int num: partyList[i])
			{
				sum += peopleList[num];
			}
			if(sum==0) { //아무도 모른다면				
				//System.out.println((i+1)+ "번째 파티에서 말할 수 있습니다.");
				answer++;
			}
    	}
	    	System.out.print(answer);
    }
}