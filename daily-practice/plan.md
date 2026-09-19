# plan

## 第一阶段：先把 C 最基础输入输出弄熟

按这个顺序：

```text
C/luogu/B2002_hello_world.c
C/luogu/B2003_second_integer.c
C/luogu/B2004_aligned_output.c
C/luogu/B2005_character_triangle.c
C/luogu/P5703_apple_purchase.c
C/luogu/P5704_letter_conversion.c
C/luogu/P5705_reverse_number.c
C/luogu/P5710_number_properties.c
```

这一阶段主要搞懂：

```text
main
int / char
scanf
printf
if
运算符
```

这 8 道都做完，再继续。

## 第二阶段：循环、数组、字符串、函数

这里我建议暂时借 Python 那组基础题练“编程思维”，题目比较直观：

```text
Python/practice/01_even_numbers.py
Python/practice/02_prime_numbers.py
Python/practice/04_reverse_input.py
Python/practice/05_character_classification.py
Python/practice/09_count_character_types.py
Python/practice/12_sort_ten_numbers.py
Python/practice/13_matrix_diagonal_sum.py
Python/practice/14_swap_two_values.py
Python/practice/19_guess_number.py
Python/practice/03_factorial.py
Python/practice/06_perfect_number.py
Python/practice/07_prime_factorization.py
Python/practice/08_fibonacci.py
```

做到这里，你应该开始理解：

```text
for / while
列表 / 数组
字符串
函数
递归
```

## 第三阶段：回来认真学 C

然后做：

```text
C/practice/06_goldbach_conjecture.c
C/practice/09_count_substring_occurrences.c
C/practice/18_saddle_point.c
C/practice/10_hanoi.c
```

接下来进入 C 最重要的一关——**指针**：

```text
C/practice/01_pointer_increment.c
C/practice/11_null_pointer.c
C/practice/03_double_pointer_and_2d_array.c
C/practice/02_dynamic_memory.c
C/practice/16_dynamic_string_concat.c
```

再学结构体：

```text
C/practice/13_struct_io.c
C/practice/14_struct_pointer_max_age.c
C/practice/15_modify_struct_by_pointer.c
C/practice/17_typedef.c
```

最后补：

```text
C/practice/07_compare_and_swap_strings.c
C/practice/08_file_append_and_read.c
C/practice/12_josephus.c
C/practice/04_function_pointer.c
C/practice/05_function_pointer_series_sum.c
```

其中**函数指针放最后**，现在完全不用急。

## 第四阶段：数据结构

严格建议按：

```text
01_sequential_list.c
↓
02_linked_list.c
↓
03_stack.c
↓
04_queue.c
↓
05_binary_tree_preorder.c
↓
06_binary_tree_depth.c
↓
08_graph_dfs.c
```

做到这里，已经算正式进入数据结构了。

然后再做：

```text
13_huffman_tree.c
07_threaded_binary_tree.c
09_dijkstra.c
10_floyd.c
11_prim_mst.c
12_kruskal_mst.c
```

`线索二叉树` 其实不急，甚至可以最后再学。

## 第五阶段：真正开始刷算法 OJ

我建议算法目录不要按照文件名排序，而是：

```text
P2249 查找
↓
P1443 马的遍历
↓
connected_components
↓
P1162 填涂颜色
↓
P1141 01迷宫
↓
P1331 海战
↓
P2895 Meteor Shower
↓
P1216 数字三角形
↓
P1002 过河卒
↓
P1025 数的划分
↓
P1873 砍树
↓
P1182 数列分段
↓
P2678 跳石头
```

大致对应：

```text
二分查找
→ BFS
→ 连通块
→ 更复杂 BFS
→ DP
→ 二分答案
```

## LeetCode 放什么时候？

等你完成第二、三阶段以后再碰。

推荐顺序：

```text
0014 最长公共前缀
0387 第一个唯一字符
0392 判断子序列
0118 杨辉三角
0151 反转字符串中的单词
interview_0101 判定字符是否唯一
1047 删除相邻重复项
0860 柠檬水找零
```