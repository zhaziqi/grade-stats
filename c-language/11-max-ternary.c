#include <stdio.h>

/* 输入两个整数，用三目运算符输出较大的那个 */
int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    int max = (a > b) ? a : b;
    printf("两个整数中的最大值为:%d", max);
    return 0;
}
