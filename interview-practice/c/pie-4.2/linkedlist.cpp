#include "linkedlist.h"

void create(LinkedList* lst) {
    lst->head = NULL;
    lst->tail = NULL;
}

void create(Element* elem, int value) {
    elem->value = value;
    elem->next = NULL;
}

void print(LinkedList* lst) {
    Element* cur = lst->head;
    printf("[");
    while(cur) {
        printf("%d, ", cur->value);
        cur = cur->next;
    }
    printf("]");
    if(lst->head) {
        printf("; head: %d, tail: %d\n", lst->head->value, lst->tail->value);    
    }
    
    printf("\n");
}

void destroy(LinkedList* lst) {
    if(lst == NULL) {
        ERROR("tried to delete null list");
    }

    Element* cur = lst->head;
    Element* tmp;
    while(cur) {
        tmp = cur;
        cur = cur->next;
        delete tmp;
    }

    // finally, set the head and tail to null
    lst->head = NULL;
    lst->tail = NULL;
}

bool append(LinkedList* lst, int data) {
    if(lst == NULL) {
        ERROR("trying to append to empty list");
    }
    Element* elem = (Element*)malloc(sizeof(Element));
    create(elem, data);

    if(!elem) {
        ERROR("error allocating element in append");
        return false;
    }
    // empty list special case
    if(lst->head == NULL) {
        lst->head = elem;
        lst->tail = elem;
        return true;
    }
    lst->tail->next = elem;
    lst->tail = elem;
    // elem next is already NULL
    return true;
}

Element* elementAt(LinkedList* lst, int index) {
    if(lst == NULL) {
        ERROR("list is null");
        return NULL;
    }
    if(index < 0) {
        ERROR("index less than 0");
        return NULL;
    }
    int i = 0;
    Element* cur = lst->head;
    while(i < index && cur) {
        cur = cur->next;
        i++;
    }
    return cur;
}

bool remove(LinkedList* lst, Element* elem) {
    if(lst == NULL) {
        ERROR("lst is null");
        return false;
    }

    Element* prev = NULL;
    Element* cur = lst->head;
    while(cur && cur != elem){
        prev = cur;
        cur = cur->next;
    }
    if(cur == NULL) {
        ERROR("remove() called but element not found in list");
        return false;
    }

    // If element is first
    if(cur == lst->head) {
        lst->head = cur->next;
    }
    // If element is last
    if(cur == lst->tail) {
        lst->tail = prev;
    }
    if(prev != NULL) {
        prev->next = cur->next;
    }
    return true;
}

bool insertAfter(LinkedList* lst, Element* elem, int data) {
    if(lst == NULL) {
        ERROR("lst is null");
        return false;
    }

    Element* cur = lst->head;

    while(cur && cur != elem) {
        cur = cur->next;
    }
    if(cur == NULL) {
        ERROR("insertAfter() called but element not found in list");
    }

    Element* new_elem = (Element*)malloc(sizeof(Element));
    if(!new_elem) {
        ERROR("malloc(Element) failed");
    }
    create(new_elem, data);
    if(cur == lst->head) {
        lst->head = new_elem;
    }
    if(cur == lst->tail) {
        lst->tail = new_elem;
    }
    Element* tmp = cur;
    new_elem->next = cur->next;
    cur->next = new_elem;
}

#define CHECK_ELEMENT(el, i) do { if(el == NULL) { ERROR("elementAt(" << i << ") returned NULL"); exit(1);} } while(0)
int main() {
    LinkedList lst;
    int i;
    printf("creating list...\n");
    create(&lst);
    print(&lst);

    for(i = 0; i < 10; i++) {
        printf("appending %d...\n", i);
        if(!append(&lst, i)){
            ERROR("failed to append to list");
            exit(1);
        }
    }

    print(&lst);

    // TODO: try appending to uninitialized list

    // Testing elementAt
    for(i = 0; i < 10; i++) {
        Element* el = elementAt(&lst, i);
        CHECK_ELEMENT(el, i);
        printf("lst.elementAt(%d) returned %d\n", i, el->value);
    }

    // Testing remove
    // remove from end
    Element* el = elementAt(&lst, 9);
    CHECK_ELEMENT(el, 9);
    remove(&lst, el);
    printf("after removing @ index 9: ");
    print(&lst);

    for(i = 0; i < 9; i++) {
        el = elementAt(&lst, 0);
        CHECK_ELEMENT(el, 0);
        if(remove(&lst, el)) {
            printf("after removing @ index 0: ");
            print(&lst);        
        }
    }

    for(i = 0; i < 10; i++) {
        append(&lst, i);
    }

    for(i = 9; i >= 0; i--) {
        el = elementAt(&lst, i);
        CHECK_ELEMENT(el, i);
        int to_insert = i * 2;
        printf("inserting %d after %d: ", to_insert, i);
        insertAfter(&lst, el, to_insert);
        print(&lst);
    }

    printf("destroying...\n");
    destroy(&lst);
    print(&lst);
    return 0;
}