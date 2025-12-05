/************************************************************************

Author: Joe Waclawski
		
History    Date         Author           Revision     
           11/8/2023    Joe Waclawski    Initial

This is a program that demonstrates how important protecting a 
shared resource between multiple threads. If this program is run without
any parameter, 2 threads will run, each accessing the shared counter variable.
The counter value in the end should be 20000000 (each thread should 
increment the count 10000000 times). But there is no protection of the 
counter variable, so the actual count is variable (i.e. != 20000000)

If this program is run with the single parameter "y", a mutex will be used to 
protect counter, and the resulting value will always be 20000000
		
Parameters: 1 - "y" to use a mutex; otherwise, no mutex is used.

************************************************************************/
#include <pthread.h>
#include <stdio.h>
#include <string.h>

static volatile int counter = 0;
pthread_mutex_t lock_counter;
int useMutex = 0;


void * mythread(void * arg)
{
	printf("%s: begin\n", (char*) arg);
	int i, localCounter=0;
        printf("%s: My localCounter = %d\n", (char *) arg, localCounter);	
	for (i=0; i<1e7; i++) 
	{
		if (useMutex) pthread_mutex_lock(&lock_counter);
		counter++;
		if (useMutex) pthread_mutex_unlock(&lock_counter);
		localCounter++;
	}	
        printf("%s: My localCounter = %d\n", (char *) arg, localCounter);	
	printf("%s: done\n", (char *) arg);
	return NULL;
}

int main (int argc, char *argv[])
{
	if (argc > 1 && strcmp(argv[1],"y") == 0) useMutex = 1;
	pthread_t p1, p2;
	printf("main: begin (counter = %d)\n", counter);
	pthread_create(&p1, NULL, mythread, (void *)"A");
	pthread_create(&p2, NULL, mythread, (void *)"B");

	pthread_join(p1, NULL);
	pthread_join(p2, NULL);
	printf("main: done with both (counter = %d) \n", counter);
	return 0;
}
