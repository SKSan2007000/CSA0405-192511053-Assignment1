#define _POSIX_C_SOURCE 200809L
#include <errno.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <time.h>
#include <unistd.h>

#define COUNT 1000
static void *worker(void *arg) {
    (void)arg;
    return NULL;
}
static double elapsed(struct timespec start, struct timespec end) {
    return (double)(end.tv_sec - start.tv_sec) +
           (double)(end.tv_nsec - start.tv_nsec) / 1000000000.0;
}
int main(void) {
    struct timespec start, end;
    int process_count = 0, status = 0;

    if (clock_gettime(CLOCK_MONOTONIC, &start) != 0) {
        perror("clock_gettime"); return 1;
    }
    for (int i = 0; i < COUNT; i++) {
        pid_t pid = fork();
        if (pid < 0) { perror("fork"); break; }
        if (pid == 0) _exit(0);
        if (waitpid(pid, &status, 0) < 0) { perror("waitpid"); break; }
        if (!WIFEXITED(status) || WEXITSTATUS(status) != 0) break;
        process_count++;
    }
    if (clock_gettime(CLOCK_MONOTONIC, &end) != 0) {
        perror("clock_gettime"); return 1;
    }
    double process_time = elapsed(start, end);

    pthread_t threads[COUNT];
    int thread_count = 0;
    if (clock_gettime(CLOCK_MONOTONIC, &start) != 0) {
        perror("clock_gettime"); return 1;
    }
    for (int i = 0; i < COUNT; i++) {
        int rc = pthread_create(&threads[i], NULL, worker, NULL);
        if (rc != 0) { errno = rc; perror("pthread_create"); break; }
        thread_count++;
    }
    for (int i = 0; i < thread_count; i++) {
        int rc = pthread_join(threads[i], NULL);
        if (rc != 0) { errno = rc; perror("pthread_join"); return 1; }
    }
    if (clock_gettime(CLOCK_MONOTONIC, &end) != 0) {
        perror("clock_gettime"); return 1;
    }
    double thread_time = elapsed(start, end);

    printf("Processes created and reaped: %d\n", process_count);
    printf("fork+wait total seconds: %.6f\n", process_time);
    printf("Threads created and joined: %d\n", thread_count);
    printf("pthread total seconds: %.6f\n", thread_time);
    return (process_count == COUNT && thread_count == COUNT) ? 0 : 1;
}
