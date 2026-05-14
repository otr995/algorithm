# 🧠 Algorithm Study

Java 기반 알고리즘 문제 풀이를 기록하는 저장소입니다.  
문제 유형별 접근 방식과 복습이 필요한 문제를 함께 관리합니다.

---

## 📌 목표

- 알고리즘 유형별 문제 해결 패턴 정리
- 다시 풀 문제와 못 푼 문제 복습 관리
- 풀이 과정, 시간 복잡도, 개선 포인트 기록
- GitHub 커밋을 통한 꾸준한 학습 기록 유지

---

## 🛠 사용 언어

- Java

---

## 📊 진행 현황

| 전체 | 한 번에 푼 문제 | 다시 풀 문제 | 못 푼 문제 |
|---|---|---|---|
| 4 | 0 | 3 | 1 |

---

## 📚 유형별 풀이 수

| 유형 | 풀이 수 |
|---|---|
| bfs-dfs | 1 |
| dp | 0 |
| stack-queue | 0 |
| greedy | 0 |
| implementation | 3 |
| sort | 0 |
| graph | 0 |


---

## 📂 폴더 구조

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

---

## ✅ 한 번에 푼 문제

| 날짜 | 유형 | 플랫폼 | 문제 | 난이도 | 비고 |
|---|---|---|---|---|---|


---

## 🔁 다시 풀 문제

| 날짜 | 유형 | 플랫폼 | 문제 | 난이도 | 비고 |
|---|---|---|---|---|---|
| 2026-04-27 | implementation | programmers | [충돌위험 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/340211) / [충돌위험 찾기.md](implementation/%EC%B6%A9%EB%8F%8C%EC%9C%84%ED%97%98%20%EC%B0%BE%EA%B8%B0.md) | Lv2 | 시뮬레이션 구현 복습 필요 |
| 2026-05-08 | implementation | programmers | [아날로그 시계](https://school.programmers.co.kr/learn/courses/30/lessons/250135) / [아날로그 시계.md](implementation/%EC%95%84%EB%82%A0%EB%A1%9C%EA%B7%B8%20%EC%8B%9C%EA%B3%84.md) | lv2 | 시계 관련 문제 나왔을 때 참고하기 좋을 듯! |
| 2026-05-14 | implementation | programmers | [수식 복원하기](https://school.programmers.co.kr/learn/courses/30/lessons/340210) / [수식 복원하기.md](implementation/%EC%88%98%EC%8B%9D%20%EB%B3%B5%EC%9B%90%ED%95%98%EA%B8%B0.md) | lv3 | 푸는 방법이 잘 보이지 않는 문제, 복잡한 생각을 잘 정리하는 능력을 올려줄 듯 |


---

## ❌ 못 푼 문제

| 날짜 | 유형 | 플랫폼 | 문제 | 난이도 | 비고 |
|---|---|---|---|---|---|
| 2026-04-29 | bfs-dfs | programmers | [수레 움직이기](https://school.programmers.co.kr/learn/courses/30/lessons/250134) / [수레 움직이기.md](bfs-dfs/%EC%88%98%EB%A0%88%20%EC%9B%80%EC%A7%81%EC%9D%B4%EA%B8%B0.md) | lv3 | bfs / dfs 기본 구조 구현에 대한 공부와 상태 및 경로에 관한 좋은 문제! |


---

## 🔖 상태 기준

| 상태 | 기준 |
|---|---|
| solved | 힌트 없이 해결 + 설명 가능 |
| retry | 힌트 참고 or 풀이 불안정 |
| failed | 스스로 해결 못함 |

---

## ✍️ 작성 규칙

문제 파일 상단에는 아래 metadata를 작성합니다.

    ---
    title: 문제 이름
    platform: programmers
    level: Lv2
    type: bfs-dfs
    status: solved
    date: 2026-04-24
    link: 문제 링크
    reason:
    ---

---

## 🔄 자동화

문제 풀이 후 아래 명령어로 README를 자동 갱신합니다.

    python scripts/generate_readme.py

---

## 🚀 진행 방식

1. 문제 풀이 후 `template.md` 기반으로 md 작성
2. 상태(status) 설정
3. 스크립트 실행 또는 GitHub Actions로 README 자동 갱신
4. commit & push
