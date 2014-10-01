#include <stdio.h>
#include <stdlib.h>

/**
 * Receives parameters that define the required alignment and the 
 * number of bytes to allocate. It returns a pointer aligned to 
 * alignment and pointing to size bytes.
 * 
 * ASSUMPTIONS: alignment >= 4
**/
void *alignedMalloc(unsigned int alignment, unsigned int size)
{
    printf("alignedMalloc(%d,%d)\n", alignment, size);
    // allocate sizeof(unsigned int) + alignment bytes
    char *result = (char *)malloc(sizeof(unsigned int) + alignment + size);
    // if result % alignment = 0, we will offset alignment bits
    unsigned int offset = alignment - ( (long)result % alignment );
    printf("result ptr is %ld offset is %d\n", (long)result, offset);
    // Offset the result by offset bytes, but stop just enough before to store the offset for later
    unsigned int *offsetPtr = (unsigned int*) (result + offset - sizeof(unsigned int));
    // And store the offset here
    *offsetPtr = offset;
    printf("offset at %ld is %d\n", (long)offsetPtr,*offsetPtr);
    // return aligned pointer
    return (void *)(result + offset);
}

/**
 *  The second receives the pointer returned from alignedMalloc and frees all 
 * memory allocated in alignedMalloc
 */
void alignedFree(void *p)
{
    printf("alignedFree()\n");
    // We stored the offset just before our actual data...
    unsigned int* offsetPtr = (unsigned int*) (p - sizeof(unsigned int));
    unsigned int offset = *offsetPtr;
    
    printf("offset at %ld is %d\n", (long)(p - sizeof(unsigned int)),offset);
    // Go back to our original pointer by going back offset bytes
    void *originalPtr = p - offset;
    // and free the pointer
    free(originalPtr);
}

int main() {
    for(int i = 0; i < 100; i++){
        unsigned int alignment = rand();
        unsigned int size =rand();
        char *buf = alignedMalloc(alignment,size);
        alignedFree(buf);    
    }
    
    printf("done\n");
    return 0;
}