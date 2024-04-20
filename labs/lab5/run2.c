#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(int argc, char ** argv)
{
    pid_t child;
    int exitStatus;

    // at least, there should be 3 arguments
    // 2 for the first command, and the rest for the second command
    if (argc < 4) {
        fprintf(stderr, "Usage: %s cmd1 cmd1_arg cmd2 [cmd2_args ..]\n", argv[0]);
        return 1;
    }
    //spliting into two processes
    child = fork();
    if(child<0)
    {
        perror("fork()");
        return -1;
    }
    else if (child==0)
    {
        execlp(argv[1], argv[1], argv[2], NULL);
        perror("execvp()");//if excevp fails
        return -1;
    }
    else if (child!=0)
    {
        //wait for first child to finish 
        wait(&exitStatus);
        //printinf of status for child 1
        printf("exited=%d exitstatus=%d\n", WIFEXITED(exitStatus), WEXITSTATUS(exitStatus));

        child = fork();
        if (child==0) //second child
        {
            execvp(argv[3], &argv[3]);
            perror("execlp()");//if excelp fails
            return -1;
        }
        else if (child!=0)
        {            
            // wait for second child to finish 
            wait(&exitStatus);
            //printinf of status for child 2 
            printf("exited=%d exitstatus=%d\n", WIFEXITED(exitStatus), WEXITSTATUS(exitStatus));
        }
    }
    // TODO
    return 0;
}
