#include <stdio.h>

#define PI 3.14159

/* 输入半径 r，输出球的表面积 S = 4 * PI * r * r */
int main(void) {
    double r, s;
    scanf("%lf", &r);
    s = 4 * PI * r * r;
    printf("s=%.2f\n", s);
    return 0;
}
