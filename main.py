from scraper.fetch import fetch_text
from scraper.screenshots import take_screenshot
from agents.writer import spin_chapter
from agents.reviewer import review_chapter
from agents.human_loop import get_human_input
from versioning.db import save_version
import uuid
import os

from dotenv import load_dotenv
load_dotenv()

def write_to_file(filename, content):
    os.makedirs("data/processed", exist_ok=True)
    with open(f"data/processed/{filename}", "w", encoding="utf-8") as f:
        f.write(content)

def main():
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    take_screenshot(url)
    raw_text = fetch_text(url)

    spun = spin_chapter(raw_text)
    write_to_file("spun_version.txt", spun)

    reviewed = review_chapter(spun)
    write_to_file("reviewed_version.txt", reviewed)

    final = get_human_input(spun, reviewed)
    write_to_file("final_version.txt", final)

    version_id = str(uuid.uuid4())
    save_version(final, {"version_id": version_id, "source": url})
    
    print(f"\n✅ Final version saved with ID: {version_id}")

if __name__ == "__main__":
    main()
