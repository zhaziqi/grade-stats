#include <stdio.h>

/* 对比 (A+B)*C 与 A+B*C 的结果 */
int main(void) {
    int A, B, C;
    scanf("%d %d %d", &A, &B, &C);
    printf("%d %d", (A + B) * C, A + B * C);
    return 0;
}
