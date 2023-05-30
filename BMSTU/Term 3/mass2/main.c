#include <stdio.h>
#include <alloca.h>

int  main() {
    int i, n, k, p, *x;
    n = 20;
    x = (int*) alloca(n* sizeof(int)); // выделили память для массива длиной н, каждый элемент, которого инт
    FILE *in;
    if((in = fopen("pk.txt", "r")) == NULL){
        printf("\n fail doesnt open");
    }
    for (int j = 0; j < n; j++) {
        fscanf(in, "%d", &x[j]);
    }
    fclose(in);
    printf("\nИсходный массив:\n");
    for (i = 0; i < n; i++)
        printf("%d", x[i]); // мы не ставим здесь & потому что мы сами ничего не вводим, выводит всё сам комп
    p = 1; k =0;
    for (i = 0; i < n; i++)
        if (x[i] < 0) { // меньше нуля так как в задание просят найти произведение отрицательных чисел
            k++;   // считает количество к++ типо плюс один и так далее
            p *= x[i];  // прсто произведение всех членов
        }
    printf("\n s=%d \n k=%d" ,p,k);
}
