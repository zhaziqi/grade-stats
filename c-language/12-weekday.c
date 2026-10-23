#include <stdio.h>

/* 输入天数 D，按 (D + 2 - 1) % 7 + 1 推算星期几 */
int main(void) {
    int D;
    scanf("%d", &D);
    printf("%d", (D + 2 - 1) % 7 + 1);
    return 0;
}
