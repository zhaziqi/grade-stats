# C 语言练习（大一上 · 程序设计基础）

课程：程序设计基础（C语言）· 丽水学院 · 2026 级
内容：课堂作业与上机练习，每次 2 题，共 14 题。

## 题目清单

| # | 文件 | 题目 | 考察点 |
|---|---|---|---|
| 01 | `01-sphere-area.c` | 球表面积 | 宏定义、浮点运算、`scanf/printf` |
| 02 | `02-distance.c` | 两点间距离 | `math.h`、`sqrt` |
| 03 | `03-sum-product.c` | 两数之和与积 | 整型输入输出、中文提示 |
| 04 | `04-char-ascii.c` | 字符的 ASCII 码 | `char` 与整型的转换 |
| 05 | `05-swap.c` | 交换两个数 | 借助中间变量 |
| 06 | `06-log-expression.c` | 数学表达式求值 | `log10/fabs/sin/cos/sqrt` 组合 |
| 07 | `07-three-digits.c` | 三位数拆位 | 整除与取余 |
| 08 | `08-sizeof.c` | 三种类型的字节数 | `sizeof` 与格式符 |
| 09 | `09-upper-case.c` | 小写转大写 | ASCII 码差值 32 |
| 10 | `10-operator-precedence.c` | 运算符优先级 | `()` 的作用 |
| 11 | `11-max-ternary.c` | 三目运算符取最大值 | `?:` |
| 12 | `12-weekday.c` | 星期推算 | 取余 + 偏移 |
| 13 | `13-arithmetic.c` | 四则运算与取余 | 五种运算符、`%%` 转义 |
| 14 | `14-remaining.c` | 剩余数量计算 | 混合运算 |

## 怎么编译运行

用 gcc（示例为 Dev-C++ 自带的 MinGW）：

```bash
gcc -std=c11 -Wall 01-sphere-area.c -o 01-sphere-area
./01-sphere-area
```

Windows 下：

```bash
gcc -std=c11 -Wall 01-sphere-area.c -o 01-sphere-area.exe
01-sphere-area.exe
```

## 说明

- 代码按作业原逻辑还原，只修正了排版与笔误；每题都通过了 `gcc -std=c11 -Wall` 编译（零警告）。
- 第 08 题原用 `%zu`，MinGW 的 printf 不支持，改成了 `%lu + 强制转换`，并在文件里注明了原因。
- 这些题目都只用到「变量、输入输出、运算符」，还没有涉及循环和数组——下一个阶段会把它们改写进去。
