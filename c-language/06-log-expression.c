#include <stdio.h>
#include <math.h>

/* 输入 x，计算 log10(|sin(x) - cos(x/2) + sqrt(x + 168)|) */
int main(void) {
    double x, a;
    scanf("%lf", &x);
    a = log10(fabs(sin(x) - cos(x / 2) + sqrt(x + 168)));
    printf("%.4f", a);
    return 0;
}
