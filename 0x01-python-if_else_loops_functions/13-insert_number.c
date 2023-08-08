#include "lists.h"
#include <stddef.h>
/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **h, int num)
{
	listint_t *_node = *h, *_new;

	_new = malloc(sizeof(listint_t));
	if (_new == NULL)
		return (NULL);
	_new->n = num;

	if (_node == NULL || _node->n >= num)
	{
		_new->next = _node;
		*h = _new;
		return (_new);
	}

	while (_node && _node->next && _node->next->n < num)
		_node = _node->next;

	_new->next = _node->next;
	_node->next = _new;

	return (_new);
}
