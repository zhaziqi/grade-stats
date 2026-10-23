#include <stdio.h>

/* 输入两个整数，依次输出加、减、乘、除、取余的结果 */
int main(void) {
    int A, B;
    scanf("%d%d", &A, &B);
    printf("%d + %d = %d\n", A, B, A + B);
    printf("%d - %d = %d\n", A, B, A - B);
    printf("%d * %d = %d\n", A, B, A * B);
    printf("%d / %d = %d\n", A, B, A / B);
    printf("%d %% %d = %d\n", A, B, A % B);
    return 0;
}
