#include <stdio.h>

int main() {
	int num = 1;
	int numList[100];
	int count = 0;

	//Continue to take in Integers Until -1 is Inputted
	while(num != -1) {
		printf("Please Enter a Number (Enter '-1' to Quit): ");
		scanf("%d", &num);
		if(num != -1) {
			numList[count] = num;
			count++;
		}
	}

	/************************************************************/
	/* Opens/Creates "results.txt" and Records "stdout" Into It */
	/************************************************************/

	freopen("results.txt", "w", stdout);

	/************************************************************/
	/************************************************************/

	//Output that is recorded into "results.txt"
	if(count < 5) 
		printf("Brah... Not Enough Numbers!\n");

	else
		for(int i = 0; i < count; i++)	printf("%d\n", numList[i]);

	return 0;
}
