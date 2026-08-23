"""Held-out governance scenarios for F164."""
from safety.policy import REQUIRED_REVIEWS, authorize


def base():
    return {key: True for key in REQUIRED_REVIEWS}


SCENARIOS = [
    ({}, False),
    (base(), True),
    (base() | {"evidence_gap": True}, False),
    (base() | {"truthfulness_risk": True}, False),
    (base() | {"job_alignment_gap": True}, False),
    (base() | {"ats_integrity_gap": True}, False),
    (base() | {"privacy_sensitive_data_risk": True}, False),
    (base() | {"fairness_discrimination_risk": True}, False),
    (base() | {"version_provenance_gap": True}, False),
    (base() | {"authorship_submission_gap": True}, False),
]


def main():
    for index, (context, expected) in enumerate(SCENARIOS, 1):
        actual = authorize("release_resume_package", context)["allowed"]
        assert actual is expected, f"scenario {index}: expected {expected}, got {actual}"
    print(f"F164 held-out governance: {len(SCENARIOS)}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
