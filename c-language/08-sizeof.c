#include <stdio.h>

/* 输入 char / int / double，输出它们的值和 sizeof
 *
 * 注：原作业用的是 %zu，但 MinGW 的 printf 不支持该格式符
 *（会报 "unknown conversion type character 'z'"），
 * 所以这里改成 %lu + 强制转换为 unsigned long，效果一样。 */
int main(void) {
    char a;
    int b;
    double c;
    scanf("%c %d %lf", &a, &b, &c);
    printf("%c,%lu\n", a, (unsigned long)sizeof(a));
    printf("%d,%lu\n", b, (unsigned long)sizeof(b));
    printf("%lf,%lu", c, (unsigned long)sizeof(c));
    return 0;
}
