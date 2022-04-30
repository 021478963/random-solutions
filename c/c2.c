#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef char AirportCode[4];

typedef struct NodeTag {
  AirportCode Airport;
  struct NodeTag *Link;
} NodeType;

void insertNewFirstNode(char a[], NodeType **L);
void printList(NodeType *L);

int main() {
  NodeType *L, *n1, *n2, *n3;
  
  char a1[] = "123";
  char a2[] = "456";
  char a3[] = "789";

  strcpy(n1->Airport, a1);
  strcpy(n2->Airport, a2);
  strcpy(n3->Airport, a3);

  L = n1;
  n1->Link = n2;
  n2->Link = n3;
  n3->Link = NULL;

  printList(&L);
}

void insertNewFirstNode(char a[], NodeType **L) {

  NodeType *n;
  n = (NodeType*) malloc(sizeof(NodeType));
  strcpy(n->Airport, a);
  n->Link = NULL;

  if (*L == NULL) {
    *L = n;
  } else {
    n->Link = *L;
    *L = n;
  }
}

void printList(NodeType *L) {
  NodeType *i = L;
  while (i != NULL) {
    printf("%s\n", i->Airport);
    i = i->Link;
  }
}