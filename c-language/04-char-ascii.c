#include <stdio.h>

/* 输入一个字符，输出它本身和对应的 ASCII 码 */
int main(void) {
    char z;
    printf("输入一个字符:");
    scanf("%c", &z);
    printf(" %c 的 ASCII 为 %d", z, z);
    return 0;
}
