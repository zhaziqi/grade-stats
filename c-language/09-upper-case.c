#include <stdio.h>

/* 输入一个小写字母，输出它的大写形式和 ASCII 码 */
int main(void) {
    char a;
    scanf("%c", &a);
    char upper = a - 32;
    printf("%c,%d", upper, upper);
    return 0;
}
