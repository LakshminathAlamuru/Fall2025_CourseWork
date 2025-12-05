#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

int total = 0, done = 0;

sem_t s1, s2; 
void sum(int n) {
	for (int i = 1; i <= n; i++) {
		sem_wait(&s1);
		total += i;
		printf("worker: processed i = %d\n", i);
		sem_post(&s2);
	}
}

void finish() {
	sem_wait(&s1);
	done = 1;
	sem_post(&s2);
	printf("worker done\n");
}

void* worker(void* arg) {
	int num = *(int*)arg;
	printf("worker: received n = %d\n", num);
	sum(num);
	finish();
		return NULL;
}

void thr_wait() {
	while (1) {
		sem_wait(&s2);
		if (done == 1) {
			break;
		}
		printf("main: running total = %d\n", total);
		sem_post(&s1);
	}
}

int main(int argc, char* argv[]) {
	printf("main: begin\n");
	sem_init(&s1, 0, 1);
	sem_init(&s2, 0, 0);
	int param = 3;
	pthread_t t;
	pthread_create(&t, NULL, worker, (void*)&param);
	thr_wait();
	printf("main: outcome = %d\n", total);
	printf("main: end\n"); 
}

