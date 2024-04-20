#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* print out an error message and exit */
void my_error(char *s)
{
    perror(s);
    exit(1);
}

/* Concatnate two strings.
 * Dynamically allocate space for the result.
 * Return the address of the result.
*/
char *my_strcat(char *s1, char *s2)
{
    // TODO 
    int length1 = strlen(s1);
    int length2 = strlen(s2);
    //include 1 for null at end
    int lengthFull = length1+length2+1;
    char* toReturn = (char*) malloc(sizeof(char)*lengthFull);
    if (toReturn == NULL)
    {
        my_error("Malloc Failed");
    }
    strcpy(toReturn, s1);
    strcat(toReturn, s2);
    return toReturn;
}

int main(int argc, char *argv[])
{
    //free call is in main

    char *s;

    s = my_strcat("", argv[0]);

    for (int i = 1; i < argc; i ++) {
        char* temp = s;
        s = my_strcat(s, argv[i]);
        free(temp);
    }

    printf("%s\n", s);
    free(s);
    return 0;
}