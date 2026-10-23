#include <stdio.h>
#include <math.h>

/* 输入 x、y，输出 sqrt(x*x + y*y) */
int main(void) {
    double x, y, z;
    scanf("%lf%lf", &x, &y);
    z = sqrt(x * x + y * y);
    printf("%.1f\n", z);
    return 0;
}
