#define _POSIX_C_SOURCE 200809L
#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

/* Copy src to dst with read()/write(), using bufsize bytes.
   Return read() call count, or -1 on error. */
long copy_file(const char *src, const char *dst, size_t bufsize) {
    char buf[8192];
    if (bufsize == 0 || bufsize > sizeof(buf)) {
        errno = EINVAL;
        return -1;
    }

    int in = open(src, O_RDONLY);
    if (in < 0) return -1;

    int out = open(dst, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (out < 0) {
        int saved = errno;
        close(in);
        errno = saved;
        return -1;
    }

    long calls = 0;
    ssize_t n;
    for (;;) {
        do {
            n = read(in, buf, bufsize);
            calls++;
        } while (n < 0 && errno == EINTR);

        if (n == 0) break;
        if (n < 0) {
            calls = -1;
            break;
        }

        ssize_t offset = 0;
        while (offset < n) {
            ssize_t written = write(out, buf + offset, (size_t)(n - offset));
            if (written < 0 && errno == EINTR) continue;
            if (written <= 0) {
                calls = -1;
                break;
            }
            offset += written;
        }
        if (calls < 0) break;
    }

    int saved = errno;
    if (close(in) < 0 && calls >= 0) calls = -1;
    if (close(out) < 0 && calls >= 0) calls = -1;
    errno = saved;
    return calls;
}

int main(void) {
    FILE *f = fopen("records.dat", "w");
    if (!f) {
        perror("fopen");
        return 1;
    }
    for (int i = 0; i < 10000; i++) {
        if (fputc('A' + i % 26, f) == EOF) {
            perror("fputc");
            fclose(f);
            return 1;
        }
    }
    if (fclose(f) != 0) {
        perror("fclose");
        return 1;
    }

    const size_t sizes[] = {1, 512, 4096};
    int failed = 0;
    for (size_t i = 0; i < sizeof(sizes) / sizeof(sizes[0]); i++) {
        long calls = copy_file("records.dat", "copy.dat", sizes[i]);
        if (calls < 0) {
            perror("copy_file");
            failed = 1;
        } else {
            printf("buffer %4zu bytes: %5ld read() calls\n", sizes[i], calls);
        }
    }
    unlink("records.dat");
    unlink("copy.dat");
    return failed;
}
