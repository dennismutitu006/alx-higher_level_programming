#include "lists.h"
/***
 * insert_node - a function that inserts a number into a sorted singly linked.
 * @head: a pointer to the head of the list.
 * @number: the number that is to be inserted.
 * Return: the adrres of the new npode or null if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	
	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	new->next = node->next;
	node->next = new;
	return (new);
}
