from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

EXCLUDE_DIRS = {".git", "scripts", "template", ".github"}

STATUS_MAP = {
    "solved": "✅ 한 번에 푼 문제",
    "retry": "🔁 다시 풀 문제",
    "failed": "❌ 못 푼 문제",
}

TYPE_ORDER = [
    "bfs-dfs",
    "dp",
    "stack-queue",
    "greedy",
    "implementation",
    "sort",
    "graph",
]


def parse_front_matter(content):
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None

    metadata = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip()

    return metadata


def collect_problems():
    problems = []

    for md_file in ROOT.rglob("*.md"):
        relative_path = md_file.relative_to(ROOT)

        if md_file.name in {"README.md", "template.md"}:
            continue

        if any(part in EXCLUDE_DIRS for part in relative_path.parts):
            continue

        content = md_file.read_text(encoding="utf-8")
        metadata = parse_front_matter(content)

        if not metadata:
            continue

        problem = {
            "title": metadata.get("title", ""),
            "platform": metadata.get("platform", ""),
            "level": metadata.get("level", ""),
            "type": metadata.get("type", ""),
            "status": metadata.get("status", ""),
            "date": metadata.get("date", ""),
            "link": metadata.get("link", ""),
            "reason": metadata.get("reason", ""),
            "file_path": str(relative_path).replace("\\", "/"),
        }

        problems.append(problem)

    return problems


def make_problem_link(problem):
    title = problem["title"] or "문제"
    path = problem["file_path"]

    if problem["link"]:
        return f"[{title}]({problem['link']}) / [풀이]({path})"

    return f"[{title}]({path})"


def make_status_table(problems, status):
    filtered = [p for p in problems if p["status"] == status]

    filtered.sort(
        key=lambda p: (
            p["date"],
            TYPE_ORDER.index(p["type"]) if p["type"] in TYPE_ORDER else 999,
            p["title"],
        )
    )

    if not filtered:
        return "| 날짜 | 유형 | 플랫폼 | 문제 | 난이도 | 비고 |\n|---|---|---|---|---|---|\n"

    lines = [
        "| 날짜 | 유형 | 플랫폼 | 문제 | 난이도 | 비고 |",
        "|---|---|---|---|---|---|",
    ]

    for p in filtered:
        note = p["reason"] if p["reason"] else "-"
        lines.append(
            f"| {p['date']} | {p['type']} | {p['platform']} | {make_problem_link(p)} | {p['level']} | {note} |"
        )

    return "\n".join(lines) + "\n"


def make_type_summary(problems):
    counts = {type_name: 0 for type_name in TYPE_ORDER}

    for p in problems:
        problem_type = p["type"]
        if problem_type not in counts:
            counts[problem_type] = 0
        counts[problem_type] += 1

    lines = [
        "| 유형 | 풀이 수 |",
        "|---|---|",
    ]

    for type_name, count in counts.items():
        lines.append(f"| {type_name} | {count} |")

    return "\n".join(lines) + "\n"


def generate_readme(problems):
    total = len(problems)
    solved = len([p for p in problems if p["status"] == "solved"])
    retry = len([p for p in problems if p["status"] == "retry"])
    failed = len([p for p in problems if p["status"] == "failed"])

    return f"""# Algorithm Study

Java 기반 알고리즘 문제 풀이를 기록하는 저장소입니다.  
문제 유형별 접근 방식과 복습이 필요한 문제를 함께 관리합니다.

---

## 목표

- 알고리즘 유형별 문제 해결 패턴 정리
- 다시 풀 문제와 못 푼 문제 복습 관리
- 풀이 과정, 시간 복잡도, 개선 포인트 기록
- GitHub 커밋을 통한 꾸준한 학습 기록 유지

---

## 진행 현황

| 전체 | 한 번에 푼 문제 | 다시 풀 문제 | 못 푼 문제 |
|---|---|---|---|
| {total} | {solved} | {retry} | {failed} |

---

## 유형별 풀이 수

{make_type_summary(problems)}

---

## 폴더 구조

```txt
algorithm-study/
├─ README.md
├─ template.md
├─ scripts/
│  └─ generate_readme.py
├─ bfs-dfs/
├─ dp/
├─ stack-queue/
├─ greedy/
├─ implementation/
├─ sort/
└─ graph/