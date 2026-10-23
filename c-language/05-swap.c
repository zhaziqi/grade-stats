#include <stdio.h>

/* 输入两个浮点数，借助中间变量交换后输出 */
int main(void) {
    float x1, x2, c;
    scanf("%f %f", &x1, &x2);
    c = x1;
    x1 = x2;
    x2 = c;
    printf("After exchange:x1 =%.2f,x2=%.2f", x1, x2);
    return 0;
}
