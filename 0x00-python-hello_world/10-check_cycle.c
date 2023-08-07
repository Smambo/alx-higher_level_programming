#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if singly linked list has a cycle
 * @list: list to be checked
 * Return: 0 if there's no cycle, otherwise 1 if there's a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	tortoise = list;
	hare = list;

	while (tortoise != NULL && hare != NULL)
	{
		tortoise = tortoise->next;
		if (hare->next)
		{
			hare = hare->next->next;
		}
		if (tortoise == hare)
		{
			return (1);
		}
	}
	return (0);
}
