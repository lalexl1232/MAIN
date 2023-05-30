#include <stdio.h>
#include <mm_malloc.h>



int main(void){
    FILE *in;
    if ((in = fopen("lab4.dat", "r")) == NULL){
        printf("File not open");
    }
    int n , m, i, j, *x, *s, k, min, **a;
    printf("Enter n:\n");
    scanf("%d", &n);
    printf("Enter m:\n");
    scanf("%d", &m);
    x = (int*) malloc(m*sizeof(int));
    s = (int*) malloc(n*sizeof(int));
    a = (int**) malloc(n*sizeof(int*));
    for (int i = 0; i < n; i++) {
        a[i] = (int*) malloc(m*sizeof(int));
        for (int j = 0; j < m; j++) {
            fscanf(in, "%d", &a[i][j]);
        }
    }
    printf("Matrix A===========\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++)
            printf("5%d", a[i][j]);
        printf("\n");
    }

}