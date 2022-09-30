#include "lists.h"

/**
 * print_dlistint - prints the subsequent nodes in a doubly linked list
 * @h: the head of the node
 * Return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	int i;

	for (i = 0; h != NULL; i++)
	{
		printf("%d\n", h->n);
		h = h->next;
	}
	return (i);
}
