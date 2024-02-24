#include <stdio.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>


/**
 * main - Creates five zombie processes.
 *
 * Return: EXIT_SUCCESS.
 */
int main(void)
{
	pid_t pid;
	int count = 0;

	while (count < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			count++;
		}
		else
			exit(0);
	}

	while (1)
	{
		sleep(1);
	}
	return (0);

	return (EXIT_SUCCESS);
}
