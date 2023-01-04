#ifndef _LISTS_H
#define _LISTS_H

#include <stdlib>

/**
* struct listint_s - singly linked list
* @n: integer
* @next: points to the next node
*
* Description: singly list node structure
*/

typedef struct listint_s
{
	int n;
	struct listint_s *next;
}listint t;

size_t print_listint(const lstint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif
