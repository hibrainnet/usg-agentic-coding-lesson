import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
from rich import box
from datetime import datetime

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
}

RSS_URL = "https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko"


def fetch_top_stories(max_items: int = 20) -> list[dict]:
    response = requests.get(RSS_URL, headers=HEADERS, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "lxml-xml")
    items = soup.find_all("item")[:max_items]

    stories = []
    for item in items:
        title = item.find("title")
        source = item.find("source")
        pub_date = item.find("pubDate")

        stories.append({
            "title": title.get_text(strip=True) if title else "N/A",
            "source": source.get_text(strip=True) if source else "N/A",
            "published": _format_date(pub_date.get_text(strip=True)) if pub_date else "N/A",
        })

    return stories


def _format_date(raw: str) -> str:
    try:
        dt = datetime.strptime(raw, "%a, %d %b %Y %H:%M:%S %Z")
        return dt.strftime("%Y-%m-%d %H:%M")
    except ValueError:
        return raw


def display_table(stories: list[dict]) -> None:
    console = Console()

    table = Table(
        title=f"Google News - Top Stories ({datetime.now().strftime('%Y-%m-%d %H:%M')})",
        box=box.ROUNDED,
        show_lines=True,
        header_style="bold cyan",
    )

    table.add_column("#", style="dim", width=4, justify="right")
    table.add_column("제목", min_width=50)
    table.add_column("출처", style="green", width=20)
    table.add_column("게재 시간", style="yellow", width=16, justify="center")

    for i, story in enumerate(stories, start=1):
        table.add_row(
            str(i),
            story["title"],
            story["source"],
            story["published"],
        )

    console.print(table)


def main():
    print("Google News Top Stories 수집 중...")
    stories = fetch_top_stories(max_items=20)
    display_table(stories)


if __name__ == "__main__":
    main()
