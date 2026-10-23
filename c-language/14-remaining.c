#include <stdio.h>

/* 输入 N、K、M，计算 N - K * M */
int main(void) {
    int N, K, M, sum;
    scanf("%d %d %d", &N, &K, &M);
    sum = N - (K * M);
    printf("%d", sum);
    return 0;
}
