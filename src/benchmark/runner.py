"""
Harness for running evaluation suite on Arabic test queries.
"""
import json
from pathlib import Path
from src.taxonomy.classifier import HallucinationClassifier
from src.evaluator.citation_verifier import ArabicCitationVerifier


def run_benchmark():
    verifier = ArabicCitationVerifier()
    classifier = HallucinationClassifier()

    sample_cases = [
        {
            "query": "ما هي المادة الحاكمة لعقد العمل المحدد؟",
            "model_output": "تنص المادة رقم 104 على انتهاء العقد بانقضاء مدته.",
            "reference": "المادة رقم 104 تنظم انقضاء عقد العمل المحدد بانتهاء مدته."
        },
        {
            "query": "ما حكم إنهاء العقد غير محدد المدة؟",
            "model_output": "تنص المادة رقم 999 على تعويض فوري قدره خمس سنوات راتب.",
            "reference": "المادة رقم 106 تنظم أحكام الإشعار والتعويض."
        }
    ]

    print("================ ARABIC HALLUCINATION BENCHMARK ================")
    for idx, case in enumerate(sample_cases, 1):
        cit_check = verifier.verify_citations(case["model_output"])
        h_check = classifier.classify(case["model_output"], case["reference"])
        print(f"\nCase #{idx}: {case['query']}")
        print(f"  - Citation Valid: {cit_check['is_valid']} (Hallucinated: {cit_check['hallucinated_citations']})")
        print(f"  - Error Category: {h_check['type']}")
    print("\n================================================================")


if __name__ == "__main__":
    run_benchmark()
