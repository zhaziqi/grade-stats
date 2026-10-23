#include <stdio.h>

/* 输入两个整数，输出它们的和与积 */
int main(void) {
    int x, y;
    printf("请输入两个整数。\n");
    printf("整数x：整数y：");
    scanf("%d%d", &x, &y);
    printf("它们的和是%d，积是%d。\n", x + y, x * y);
    return 0;
}
