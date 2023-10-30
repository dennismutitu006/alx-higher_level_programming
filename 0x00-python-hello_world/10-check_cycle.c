#include "lists.h"

/**
 * check_cycle -this function will check if a linked list ontains a cycle
 * @list: the linked lists to check
 *
 * Return:1 if true and 0 if false
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
