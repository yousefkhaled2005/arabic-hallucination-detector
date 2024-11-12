from typing import Dict, List
from enum import Enum


class HallucinationType(str, Enum):
    NONE = "none"
    FACTUAL_INVENTION = "level_1_factual_invention"
    CONTRADICTION = "level_2_source_contradiction"
    LINGUISTIC_DISTORTION = "level_3_linguistic_distortion"


class HallucinationClassifier:
    """Categorizes model discrepancies based on the 3-tier Arabic error taxonomy."""

    @staticmethod
    def classify(claim: str, reference: str) -> Dict[str, str]:
        if not reference:
            return {"type": HallucinationType.NONE, "confidence": 1.0}

        # Substring / semantic heuristic check
        words_claim = set(claim.split())
        words_ref = set(reference.split())
        overlap = len(words_claim.intersection(words_ref)) / max(len(words_claim), 1)

        if overlap < 0.2:
            return {
                "type": HallucinationType.FACTUAL_INVENTION,
                "confidence": round(1.0 - overlap, 2),
                "explanation": "Claim introduces unsubstantiated entities not found in reference knowledge."
            }
        elif "لا يجوز" in claim and "يجوز" in reference and "لا يجوز" not in reference:
            return {
                "type": HallucinationType.CONTRADICTION,
                "confidence": 0.95,
                "explanation": "Claim directly inverts modal polarity (legal prohibition vs allowance)."
            }
        
        return {
            "type": HallucinationType.NONE,
            "confidence": round(overlap, 2),
            "explanation": "Grounding verification passed."
        }
