#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char** split_string(char*);

// Author: Ravi B
// Date: 10/23/2020

int libraryFine(int return_day, int return_month, int return_year, int due_day, int due_month, int due_year) 
{
    int fine = 0;
    if (return_year == due_year)
    {
        if (return_month == due_month)
        {
            if (return_day > due_day)
            {
                fine = 15 * (return_day - due_day);
            }
        }
        else if (return_month > due_month)
        {
            fine = 500 * (return_month - due_month);
        }
    }
    else if (return_year > due_year)
    {
        fine = 10000;
    }
    return fine;
}

int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

    char** d1M1Y1 = split_string(readline());

    char* d1_endptr;
    char* d1_str = d1M1Y1[0];
    int d1 = strtol(d1_str, &d1_endptr, 10);

    if (d1_endptr == d1_str || *d1_endptr != '\0') { exit(EXIT_FAILURE); }

    char* m1_endptr;
    char* m1_str = d1M1Y1[1];
    int m1 = strtol(m1_str, &m1_endptr, 10);

    if (m1_endptr == m1_str || *m1_endptr != '\0') { exit(EXIT_FAILURE); }

    char* y1_endptr;
    char* y1_str = d1M1Y1[2];
    int y1 = strtol(y1_str, &y1_endptr, 10);

    if (y1_endptr == y1_str || *y1_endptr != '\0') { exit(EXIT_FAILURE); }

    char** d2M2Y2 = split_string(readline());

    char* d2_endptr;
    char* d2_str = d2M2Y2[0];
    int d2 = strtol(d2_str, &d2_endptr, 10);

    if (d2_endptr == d2_str || *d2_endptr != '\0') { exit(EXIT_FAILURE); }

    char* m2_endptr;
    char* m2_str = d2M2Y2[1];
    int m2 = strtol(m2_str, &m2_endptr, 10);

    if (m2_endptr == m2_str || *m2_endptr != '\0') { exit(EXIT_FAILURE); }

    char* y2_endptr;
    char* y2_str = d2M2Y2[2];
    int y2 = strtol(y2_str, &y2_endptr, 10);

    if (y2_endptr == y2_str || *y2_endptr != '\0') { exit(EXIT_FAILURE); }

    int result = libraryFine(d1, m1, y1, d2, m2, y2);

    fprintf(fptr, "%d\n", result);

    fclose(fptr);

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) { break; }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }

        size_t new_length = alloc_length << 1;
        data = realloc(data, new_length);

        if (!data) { break; }

        alloc_length = new_length;
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';
    }

    data = realloc(data, data_length);

    return data;
}

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);
        if (!splits) {
            return splits;
        }

        splits[spaces - 1] = token;

        token = strtok(NULL, " ");
    }

    return splits;
}
