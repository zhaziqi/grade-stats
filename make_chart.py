"""
make_chart.py — 把成绩数据画成图

复用 grade_stats.py 里的数据和函数，不重复写一遍逻辑（这是"模块化"的意义）。
输出：chart.png
"""
import matplotlib
matplotlib.use("Agg")          # 不弹窗口，直接存文件
import matplotlib.pyplot as plt

from grade_stats import SCORES, total_of, average_of, grade_of, distribution

# 中文显示：用系统里的微软雅黑
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

DARK = "#1A1A1A"
ACCENT = "#2F5D8A"
LIGHT = "#BFCFE0"


def main():
    # ---------- 准备数据 ----------
    names = list(SCORES.keys())
    totals = [total_of(SCORES[n]) for n in names]

    # 按总分从高到低排
    pairs = sorted(zip(names, totals), key=lambda x: x[1], reverse=True)
    names = [p[0] for p in pairs]
    totals = [p[1] for p in pairs]

    dist = distribution(SCORES)
    levels = ["A", "B", "C", "D"]
    counts = [dist[l] for l in levels]

    # ---------- 画图 ----------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2), dpi=160)
    fig.patch.set_facecolor("white")

    # 左图：总分排名
    bars = ax1.bar(names, totals, color=ACCENT, width=0.6)
    ax1.set_title("总分排名", fontsize=14, color=DARK, pad=12)
    ax1.set_ylabel("总分", fontsize=11, color=DARK)
    ax1.set_ylim(0, max(totals) * 1.18)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.tick_params(colors=DARK, labelsize=10)
    for b, v in zip(bars, totals):
        ax1.text(b.get_x() + b.get_width() / 2, v + max(totals) * 0.02,
                 str(v), ha="center", va="bottom", fontsize=10, color=DARK)

    # 右图：等级分布
    bars2 = ax2.bar(levels, counts, color=LIGHT, width=0.55, edgecolor=ACCENT, linewidth=1.2)
    ax2.set_title("平均分等级分布", fontsize=14, color=DARK, pad=12)
    ax2.set_ylabel("人数", fontsize=11, color=DARK)
    ax2.set_ylim(0, max(counts) + 1.2)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.tick_params(colors=DARK, labelsize=11)
    for b, v in zip(bars2, counts):
        ax2.text(b.get_x() + b.get_width() / 2, v + 0.12,
                 str(v), ha="center", va="bottom", fontsize=11, color=DARK)

    fig.tight_layout()
    fig.savefig("chart.png", bbox_inches="tight", facecolor="white")
    print("已生成 chart.png")

    # 顺带把统计摘要打出来，方便写 README
    print("\n统计摘要：")
    for n in names:
        avg = average_of(SCORES[n])
        print("  %s  总分 %d  平均 %.1f  等级 %s" % (n, total_of(SCORES[n]), avg, grade_of(avg)))


if __name__ == "__main__":
    main()
