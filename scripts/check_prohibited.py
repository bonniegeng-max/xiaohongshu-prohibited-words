#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书「免费课程/证书」笔记 离线违禁词扫描器 — free-course-share skill

不依赖付费 API，纯离线。扫描标题/正文/标签文本，分级输出命中结果。
词库见 references/prohibited-words.md（本脚本内置一份精简可运行版，二者需保持同步）。

用法:
  python3 check_prohibited.py "标题文本" "正文文本" "标签文本"
  python3 check_prohibited.py --file 笔记终稿.md    # 从 markdown 提取并扫描

退出码: 0=无P0硬词(PASS)  1=发现P0硬词(需改)  2=运行错误
"""
import re
import sys

# ============ 离线词库（与 references/prohibited-words.md 同步维护）============
# 每个词条: (正则, 级别, 说明, 替代建议)
P0_HARD = [
    (r"白嫖", "P0", "9/12 两次实测触发'仅自己可见'软限流", "直接删，靠结果感钩子"),
    (r"0\s*元|¥\s*0|零元", "P0", "价格诱导词，封面OCR尤其敏感", "删，免费靠'登录就能学'暗示"),
    (r"免费(领取|白拿|白送|获得|获取)", "P0", "价格诱导组合", "删或改'登录就能学'"),
    (r"官方.{0,6}(免费|白嫖).{0,6}(拿证|证书|徽章)", "P0", "'免费+官方+拿证'三词连用触发营销标签", "三词拆开"),
    (r"答案.{0,4}(合集|PDF|文档).{0,4}(主页群|群|自取)", "P0", "答案+资料+主页群 导流诱导高危", "改'攻略整理成文档，主页可看'"),
    (r"免费证书|AI证书|免费课程|白嫖快乐", "P0", "营销诱导敏感标签/词", "删，保留中性词"),
    (r"LinkedIn|领英学习|领英", "P0", "外部平台名，导流站外", "只写出品方"),
    (r"微信号|vx|卫星|加V|私我|私信我", "P0", "站外导流", "不写，转化走主页简介"),
]

P1_LIMIT = [
    (r"最(好|佳|优|大|小|便宜|火|安全|强|快|全)", "P1", "极限词，虚假营销", "删或改'更/相对'"),
    (r"第一|唯一|首家|全网首发|独家|绝无仅有", "P1", "极限词", "删"),
    (r"100%|百分百|满分|根治|永久|无效退款|一次(搞定|通过)|稳赚|躺赚|秒过|闭眼入", "P1", "绝对化承诺/诱导", "删或改客观描述"),
    (r"限时(秒杀|抢购)|仅限今日|马上涨价|再不买就没了|点击领|爆单|卖爆|疯抢|亏本甩卖|跳楼价|抄底价", "P1", "价格营销诱导", "删"),
]

P2_ACCOUNT = [
    (r"初体验|第一课|入门推荐|课程分享", "P2", "Bonnie账号级禁区词", "删"),
    (r"我学了", "P2", "'我学了X'句式", "改'我整理了/我实测/我全程中文版'"),
]

def _extract_section(content, section_name):
    """从 markdown 提取指定标题段落内容（到下一个同级标题为止）"""
    lines = content.split("\n")
    result = []
    in_section = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## "):
            # 进入目标段
            in_section = (stripped[3:].strip() == section_name.lstrip("# ").strip() or
                          stripped.startswith(section_name))
            if in_section:
                continue
        elif stripped.startswith("# "):
            # 遇到更高一级标题，退出
            if in_section:
                break
        if in_section:
            result.append(line)
    return "\n".join(result).strip()

def scan(text, rules):
    """返回命中列表 [(词, 级别, 说明, 建议)]"""
    hits = []
    for pattern, level, why, suggest in rules:
        for m in re.finditer(pattern, text):
            hits.append((m.group(0), level, why, suggest))
    return hits

def main():
    args = sys.argv[1:]
    if not args:
        print("用法: check_prohibited.py '标题' '正文' '标签'  或  --file 笔记.md")
        return 2

    title, body, tags = "", "", ""
    if args[0] == "--file":
        try:
            with open(args[1], "r", encoding="utf-8") as f:
                content = f.read()
            # 只提取「## 标题」和「## 正文」两段，跳过「违禁词审查记录/checklist/发布建议」等元信息段
            # 否则审查记录里"旧版用了白嫖→已删"这类对照词会被误报
            title = _extract_section(content, "## 标题")
            body = _extract_section(content, "## 正文")
            if not title and not body:
                # 没找到标准段落，退回整篇（纯文案文件场景）
                title = body = content
        except Exception as e:
            print(f"读取失败: {e}")
            return 2
    else:
        title = args[0] if len(args) > 0 else ""
        body = args[1] if len(args) > 1 else ""
        tags = args[2] if len(args) > 2 else ""

    all_text = "\n".join([title, body, tags])
    hits_p0 = scan(all_text, P0_HARD)
    hits_p1 = scan(all_text, P1_LIMIT)
    hits_p2 = scan(all_text, P2_ACCOUNT)

    print("=" * 50)
    print("违禁词离线扫描结果")
    print("=" * 50)

    def print_hits(label, hits):
        if hits:
            print(f"\n【{label}】命中 {len(hits)} 处:")
            for word, level, why, suggest in hits:
                print(f"  - [{level}] 「{word}」 → {why}；建议：{suggest}")
        else:
            print(f"\n【{label}】未命中")

    print_hits("P0 硬词（必改，否则可能限流）", hits_p0)
    print_hits("P1 极限词/营销诱导（建议改）", hits_p1)
    print_hits("P2 账号级禁区词（建议改）", hits_p2)

    # 免费出现次数统计
    free_count = len(re.findall(r"免费", all_text))
    print(f"\n[提示] 「免费」全文出现 {free_count} 次（≥2 次建议削减到 1 次）")

    print("\n" + "=" * 50)
    if hits_p0:
        print("结论：❌ 有 P0 硬词，需修改后再发布")
        return 1
    else:
        print("结论：✅ 无 P0 硬词，可发布（P1/P2 若命中建议顺手改）")
        return 0

if __name__ == "__main__":
    sys.exit(main())
