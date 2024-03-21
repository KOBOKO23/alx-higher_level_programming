#include "lists.h"

/**
 * print_dlistint - prints all the elemts of a doubly linked list
 * @h: pointer to the head
 *
 * Return: number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t i = 0;

	/* while we have a pointer to the list */
	while (h != NULL)
	{
		printf("%d\n", h->n);
		i++;
		h = h->next;
	}
	return (i);
}
