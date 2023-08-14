#include "lists.h"

/**
 * reverse_listint - reversing the   linked list
 * @h: address of the first node in the list
 *
 * Return: pointer
 */
void reverse_listint(listint_t **h)
{
	listint_t *_prev = NULL;
	listint_t *_current = *h;
	listint_t *_next = NULL;

	while (_current)
	{
		_next = _current->next;
		_current->next = _prev;
		_prev = _current;
		_current = _next;
	}

	*h = _prev;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @h: address of address of the linked list
 *
 * Return: 1 success, 0 failure
 */
int is_palindrome(listint_t **h)
{
	listint_t *_slow = *h, *_fast = *h, *_temp = *h, *_dup = NULL;

	if (*h == NULL || (*h)->next == NULL)
		return (1);

	while (1)
	{
		_fast = _fast->next->next;
		if (!_fast)
		{
			_dup = _slow->next;
			break;
		}
		if (!_fast->next)
		{
			_dup = _slow->next->next;
			break;
		}
		_slow = _slow->next;
	}

	reverse_listint(&_dup);

	while (_dup && _temp)
	{
		if (_temp->n == _dup->n)
		{
			_dup = _dup->next;
			_temp = _temp->next;
		}
		else
			return (0);
	}

	if (!_dup)
		return (1);

	return (0);
}
