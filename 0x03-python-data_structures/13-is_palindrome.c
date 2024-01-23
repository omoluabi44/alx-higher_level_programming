#include "lists.h"
/**
 *is_palindrome - this check for palindrome in a singly linked list
 *@head: the param received
 *Return: true if is palindrom and return false if not
 */
void reversed(listint_t **head);

int is_palindrome(listint_t **head)
{
	listint_t *second_List = NULL;
	listint_t *fast_ptr = *head;
	listint_t*slow_ptr = *head;
	/**listint_t *temp = *head*/

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		fast_ptr = fast_ptr->next->next;
		if (fast_ptr->next == NULL)
		{
			second_List = slow_ptr->next->next;
			break;
		}
		if (fast_ptr == NULL)
		{
			second_List = slow_ptr->next;
			break;
		}
		slow_ptr = slow_ptr->next;
	}
        /**slow_ptr->next = NULL;*/
	reversed(&second_List);

	while (*head != NULL && second_List != NULL)
	{
		if ((*head)->n != second_List->n)
			return (0);

		*head = (*head)->next;
		second_List = second_List->next;
	}

	return (1);
}

void reversed(listint_t **head)
{
	listint_t  *prev = NULL;
	listint_t *next_one = NULL;
	listint_t *current = *head;

	while ( current != NULL)
	{
		next_one = current->next;
		current->next = prev;
		prev = current;
		current = next_one;
	}
	*head = prev;
}
