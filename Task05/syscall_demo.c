#define _POSIX_C_SOURCE 200809L
#include <errno.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main(void) {
    char buffer[128];
    const char message[] = "Smart hospital system-call demonstration\n";

    if (write(STDOUT_FILENO, message, sizeof(message) - 1) < 0) {
        perror("write");
        return 1;
    }

    ssize_t n;
    do {
        n = read(STDIN_FILENO, buffer, sizeof(buffer) - 1);
    } while (n < 0 && errno == EINTR);

    if (n < 0) {
        perror("read");
        return 1;
    }
    buffer[n] = '\0';

    const char prefix[] = "Input received: ";
    if (write(STDOUT_FILENO, prefix, sizeof(prefix) - 1) < 0 ||
        write(STDOUT_FILENO, buffer, (size_t)n) < 0) {
        perror("write");
        return 1;
    }
    return 0;
}
