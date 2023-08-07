#include "lists.h"

/**
 * check_cycle - checks if the linked list is containing a cycle
 * @list: linked list 
 *
 * Return: 1 success, 0 failure
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	if (!list)
		return (0);

	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
		return (1);
	}

	return (0);
}

