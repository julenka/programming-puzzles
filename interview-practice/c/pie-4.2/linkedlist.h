
#include <stdlib.h>
#include <stdio.h>
#include <iostream>

#define ERROR(message) do { std::cerr << "ERROR:" << message << std::endl;} while(0)

typedef struct Element {
    struct Element* next;
    int value;
} Element;

typedef struct LinkedList {
    Element* head;
    Element* tail;
} LinkedList;

// Initialize an element with given value
void create(Element* elem, int value);

// Create an empty linked list
// Both the head and tail are NULL
void create(LinkedList* lst);

// Append a value to the end of the linked list
// Return true if success
bool append(LinkedList* lst, int data);

// Returns the element at index index
// if index is invalid, returns null
Element* elementAt(LinkedList* lst, int index);

// Removes elem from lst
// Returns true if success, false if element not found
bool remove(LinkedList* lst, Element* elem);

// inserts a new node after elem with data data
// returns true if success, false if element not found
bool insertAfter(LinkedList* lst, Element* elem, int data);

// print the contents of the list
void print(Element* head);

// Destroys all elements in the list, freeing them
void destroy(LinkedList* lst);

