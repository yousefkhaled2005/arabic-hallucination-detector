import re
from typing import Dict, List


class ArabicCitationVerifier:
    """Verifies whether cited legal articles or statute numbers actually exist."""

    ARTICLE_REGEX = re.compile(r"المادة\s+(?:رقم\s+)?([\d]+)")

    def __init__(self, valid_articles: List[int] = None):
        self.valid_articles = set(valid_articles or [104, 105, 106, 120, 125, 130])

    def verify_citations(self, text: str) -> Dict[str, List[int]]:
        found_articles = [int(m) for m in self.ARTICLE_REGEX.findall(text)]
        hallucinated = [a for a in found_articles if a not in self.valid_articles]
        valid = [a for a in found_articles if a in self.valid_articles]

        return {
            "valid_citations": valid,
            "hallucinated_citations": hallucinated,
            "is_valid": len(hallucinated) == 0
        }
