from scraper.fetch import fetch_text
from agents.writer import spin_chapter
from agents.reviewer import review_chapter

def test_pipeline():
    raw = fetch_text("https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1")
    spun = spin_chapter(raw)
    reviewed = review_chapter(spun)
    assert spun and reviewed and "the" in reviewed.lower()
