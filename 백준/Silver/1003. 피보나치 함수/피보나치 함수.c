#include<stdio.h>



int main(void)
{
	int n;
	int i;
	int num;
	int ze[41];
	int one[41];

	ze[0] = 1;
	ze[1] = 0;
	one[0] = 0;
	one[1] = 1;

	for (i = 2; i < 41; i++)
	{
		ze[i] = ze[i - 1] + ze[i - 2];
		one[i] = one[i - 1] + one[i - 2];
	}


	scanf("%d", &n);
	for (i = 0; i < n; i++)
	{
		scanf("%d", &num);
		printf("%d %d\n", ze[num], one[num]);
	}


}

