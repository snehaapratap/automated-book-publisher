from scraper.fetch import fetch_text
from scraper.screenshots import take_screenshot
from agents.writer import spin_chapter
from agents.reviewer import review_chapter
from agents.human_loop import get_human_input
from versioning.db import save_version
import uuid
from dotenv import load_dotenv
load_dotenv()

def main():
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    take_screenshot(url)
    raw_text = fetch_text(url)
    
    spun = spin_chapter(raw_text)
    reviewed = review_chapter(spun)
    
    final = get_human_input(spun, reviewed)
    version_id = str(uuid.uuid4())

    save_version(final, {"version_id": version_id, "source": url})
    print(f"\n✅ Final version saved with ID: {version_id}")

if __name__ == "__main__":
    main()
