#include <stdio.h>
#include<stdlib.h>
#include<string.h>
int yes_no(char* arr, int len);
int main() {
	char s[51];
	int n,i,len;
	scanf("%d", &n);
	for (i = 0;i < n;i++){
		scanf("%s", s);
		len = strlen(s);
		if (yes_no(s,len) == 0) printf("NO\n");
		
		else printf("YES\n"); 
		
	}

	return 0;
}
int yes_no(char* arr, int len)
{
	int open, close;
	open = close = 0;
	for (int i = 0;i < len;i++){
		if (arr[i] == '(')open++;
		else if (arr[i] == ')')open--;
		
		if (open < 0)return 0;
	}
	if (open == 0) return 1;
	
	return 0;
}
