#include <stdlib.h>
#include <stdio.h>

typedef struct Element {
    struct Element* next;
    int value;
} Element;

void create(Element* stack);
bool push(Element** head, int value);
bool pop(Element** head, int* result);
void destroy(Element** head);
void print(Element* head);
