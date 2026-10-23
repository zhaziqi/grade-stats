"""
成绩统计小工具 (grade_stats.py)

用途：输入一批学生的成绩，自动算出总分、平均分、排名和分数段分布。

用到的知识（都在网课已学范围内）：
  - 数据类型：str / int / float
  - 列表 list：存多个分数
  - 元组 tuple：存"姓名, 总分"这种固定搭配
  - 字典 dict：姓名 -> 分数列表
  - for 循环：遍历
  - 函数 def：把重复逻辑封装起来
"""

# ============ 1. 数据区（用字典存：键是姓名，值是分数列表）============

SCORES = {
    "张三": [85, 90, 78],
    "李四": [92, 88, 95],
    "王五": [70, 65, 80],
    "赵六": [58, 62, 55],
    "钱七": [100, 98, 96],
}


# ============ 2. 基础函数 ============

def total_of(scores):
    """算一个学生的总分。scores 是一个列表。"""
    total = 0
    for s in scores:
        total = total + s
    return total


def average_of(scores):
    """算平均分。用 len() 取数量。"""
    if len(scores) == 0:
        return 0.0
    return total_of(scores) / len(scores)


def rank_list(data):
    """算排名。返回一个列表，里面每个元素是 (姓名, 总分) 的元组，按总分从高到低排好。"""
    rows = []                      # 先装进空列表
    for name in data:
        rows.append((name, total_of(data[name])))   # 元组：(姓名, 总分)

    # 冒泡排序：相邻两个比较，总分低的往后换
    n = len(rows)
    for i in range(n):
        for j in range(n - 1 - i):
            if rows[j][1] < rows[j + 1][1]:
                rows[j], rows[j + 1] = rows[j + 1], rows[j]
    return rows


def grade_of(score):
    """把分数转成等级字符串。"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"


def distribution(data):
    """统计每个等级有多少人。返回字典：等级 -> 人数。"""
    result = {"A": 0, "B": 0, "C": 0, "D": 0}
    for name in data:
        avg = average_of(data[name])
        level = grade_of(avg)
        result[level] = result[level] + 1
    return result


# ============ 3. 输出函数 ============

def print_table(data):
    """打印成绩明细表。"""
    print("=" * 46)
    print("姓名".ljust(6) + "各科成绩".ljust(20) + "总分".ljust(8) + "平均分")
    print("-" * 46)
    for name in data:
        scores = data[name]
        # 把分数列表拼成 "85/90/78" 这样的字符串
        score_text = ""
        for s in scores:
            score_text = score_text + str(s) + "/"
        score_text = score_text[:-1]      # 去掉最后一个斜杠

        total = total_of(scores)
        avg = average_of(scores)
        print(name.ljust(6) + score_text.ljust(20)
              + str(total).ljust(8) + format(avg, ".1f"))
    print("=" * 46)


def print_ranking(data):
    """打印排名。"""
    print("\n【排名】")
    rows = rank_list(data)
    position = 1
    for item in rows:
        name = item[0]
        total = item[1]
        print("  第 " + str(position) + " 名  " + name + "  总分 " + str(total))
        position = position + 1


def print_distribution(data):
    """打印分数段分布。"""
    print("\n【平均分等级分布】")
    dist = distribution(data)
    for level in ["A", "B", "C", "D"]:
        count = dist[level]
        bar = ""
        for i in range(count):
            bar = bar + "■"
        print("  " + level + " 段：" + str(count) + " 人  " + bar)


def query_student(data):
    """查询某个学生的详情。"""
    name = input("\n输入要查询的姓名（直接回车跳过）：").strip()
    if name == "":
        return
    if name in data:
        scores = data[name]
        print("  " + name + " 的成绩：" + str(scores))
        print("  总分：" + str(total_of(scores)))
        print("  平均分：" + format(average_of(scores), ".1f"))
        print("  等级：" + grade_of(average_of(scores)))
    else:
        print("  没有找到这个学生：", name)


# ============ 4. 主程序 ============

def main():
    print("\n成绩统计小工具 v1.0")
    print("共 " + str(len(SCORES)) + " 名学生\n")

    print_table(SCORES)
    print_ranking(SCORES)
    print_distribution(SCORES)
    query_student(SCORES)

    print("\n统计完成。")


if __name__ == "__main__":
    main()
