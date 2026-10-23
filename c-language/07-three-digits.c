#include <stdio.h>

/* 输入一个三位数，分别输出百位、十位、个位 */
int main(void) {
    int a;
    scanf("%d", &a);
    int b = a / 100;
    int c = a / 10 % 10;
    int d = a % 10;
    printf("%d %d %d", b, c, d);
    return 0;
}
