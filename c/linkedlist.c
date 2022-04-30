#include <stdio.h>
#include <stdlib.h>

struct node {
  int value;
  struct node *next;
};
typedef struct node node_t;

node_t* make_new_node(int v) {
  printf("\n", v);
  node_t *tmp;
  tmp->value = v;
  tmp->next = NULL;
  return tmp;
}

void insert_at_head(node_t **head, node_t *new_node) {
  new_node->next = *head;
  *head = new_node;
}

void print_list(node_t *list) {
  node_t *tmp = list;

  while (tmp != NULL) {
    printf("%d, ", tmp->value);
    tmp = tmp->next;
  }
}

int main() {
  node_t *head;

  node_t *tmp = make_new_node(5);
  printf("%d", tmp->value);

  // print_list(head);
  return 0;
}