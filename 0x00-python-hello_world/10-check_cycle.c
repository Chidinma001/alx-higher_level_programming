#include "lists.h"

/**
 * check_cycle - fuc
 * @list: param
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *a_ptr, *b_ptr;

	if (list == NULL || list->next == NULL)
		return (0);

	a_ptr = list->next;
	b_ptr = list->next->next;

	while (a_ptr && b_ptr && b_ptr->next)
	{
		if (a_ptr == b_ptr)
			return (1);

		a_ptr = a_ptr->next;
		b_ptr = b_ptr->next->next;
	}
	return (0);
}
