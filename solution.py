"""3부처 보도자료 키워드 검색 도구.

사용법: python solution.py 호우
"""
import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "보도자료데이터.json"


def main():
    if len(sys.argv) != 2 or not sys.argv[1].strip():
        print("사용법: python solution.py <키워드>")
        raise SystemExit(1)
    keyword = sys.argv[1].strip()
    articles = json.loads(DATA.read_text(encoding="utf-8"))
    result = [
        a for a in articles
        if keyword.casefold() in (a.get("부처", "") + "\n" + a.get("제목", "") + "\n" + a.get("본문", "")).casefold()
    ]
    safe_keyword = "_".join(keyword.split())
    output = HERE / f"결과_{safe_keyword}.csv"
    with output.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["번호", "부처", "제목", "본문"])
        writer.writerows([[a.get("번호", ""), a.get("부처", ""), a.get("제목", ""), a.get("본문", "")] for a in result])
    print(f"결과 {len(result)}건")
    print(f"저장: {output.name}")


if __name__ == "__main__":
    main()
