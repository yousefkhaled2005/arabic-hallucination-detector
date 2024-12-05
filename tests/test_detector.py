from src.taxonomy.classifier import HallucinationClassifier, HallucinationType
from src.evaluator.citation_verifier import ArabicCitationVerifier


def test_citation_verifier():
    verifier = ArabicCitationVerifier(valid_articles=[104, 105])
    res = verifier.verify_citations("وفق المادة 104 والمادة 999")
    assert 104 in res["valid_citations"]
    assert 999 in res["hallucinated_citations"]
    assert res["is_valid"] is False


def test_classifier():
    classifier = HallucinationClassifier()
    res = classifier.classify("نص مطابق تماما", "نص مطابق تماما للمرجع الأصلي")
    assert res["type"] == HallucinationType.NONE
