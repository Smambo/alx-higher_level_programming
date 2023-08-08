#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head node
 * @number: number to be inserted
 * Return: address of new node, otherwise NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;

	temp = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if ((*head) == NULL)
	{
		*head = new;
		return (new);
	} else if ((*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while (temp->next != NULL)
		{
			if (temp->next->n >= number)
			{
				new->next = temp->next;
				temp->next = new;
				return (new);
			}
			temp = temp->next;
		}
		new->next = NULL;
		temp->next = new;
		return (new);
	}
	return (NULL);
}
