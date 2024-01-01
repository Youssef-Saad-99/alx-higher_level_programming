#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checked if list if cycled
 * @list: pointer to list to check
 * Return: 1 if cyclical, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
