#include "stack.h"

void create(Element** stack) {
    *stack = NULL;
}

void print(Element* stack) {
    Element* cur = stack;
    printf("[");
    while(cur) {
        printf("%d, ", cur->value);
        cur = cur->next;
    }
    printf("]\n");
}

bool push(Element** head, int value) {
    // add the element to the front of the list
    Element* newEl = (Element*) malloc(sizeof(Element));
    if(!newEl) return false;
    newEl->value = value;
    newEl->next = *head;
    *head = newEl;
    return true;
}

bool pop(Element** head, int* result) {
    // remove first element from linked list
    if(!(*head)) return false;
    *result = (*head)->value;
    Element* deleteMe = *head;
    *head = deleteMe->next;
    delete deleteMe;
    return true;
}

void destroy(Element** head) {
    while(*head) {
        Element* deleteMe = *head;    
        *head = deleteMe->next;
        delete deleteMe;
    }
}

int main() {
    Element* stack;
    int i, pop_result;
    printf("creating stack...\n");
    create(&stack);
    print(stack);

    for(i = 0; i < 10; i++) {
        printf("pushing %d...\n", i);
        if(!push(&stack, i)){
            printf("error pushing onto stack!\n");
            return 1;
        }
    }

    for(i = 0; i < 10; i++) {
        printf("popping...");
        if(!pop(&stack, &pop_result)){
            printf("error popping from stack!\n");
            return 1;
        }
        printf("pop result: %d. \n", pop_result);
    }
    print(stack);
    if(!pop(&stack, &pop_result)) {
        printf("pop returned false for empty list. Good.\n");
    } else {
        printf("pop didn't return false. Bad.\n");
        return 1;
    }

    for(i = 0; i < 10; i++) {
        printf("pushing %d...\n", i);
        if(!push(&stack, i)){
            printf("error pushing onto stack!\n");
            return 1;
        }
    }

    printf("destroying...\n");
    destroy(&stack);
    print(stack);
    return 0;
}