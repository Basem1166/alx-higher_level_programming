#include <stdlib.h>
#include "lists.h"

/**
  * check_cycle - checks to see if a cycle exists
  * @list: linked list
  * Return: 0 if no cylcle , 1 if ther is a cycle
  */

int check_cycle(listint_t *list)
{
	listint_t p1, p2;

	if (!list || !(list->next))
		return (0);

	p1 = list->next;
	p2 = list->next->next;

	while (p1 && p2 && p2->next)
	{
		if (p1 == p2)
			return (1);
		p1 = p1->next;
		p2 = p2->next->next;
	}
	return (0);
}
