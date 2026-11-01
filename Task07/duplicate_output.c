#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/* Intentionally demonstrates duplicated buffered output:
   do not fflush before fork; child uses exit(), which flushes its copy. */
int main(void) {
    printf("shell: running job 2\n"); /* remains in stdout buffer when redirected */
    pid_t pid = fork();
    if (pid < 0) {
        perror("fork");
        return 1;
    }
    if (pid == 0) exit(3);
    int status;
    if (waitpid(pid, &status, 0) < 0) {
        perror("waitpid");
        return 1;
    }
    printf("parent collected status %d\n", WEXITSTATUS(status));
    return 0;
}
