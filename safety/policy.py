"""Fail-closed governance for F164 Agentic Resume Studio."""

PROTECTED_ACTIONS = {
    "fabricate_or_exaggerate_credential",
    "submit_job_application",
    "impersonate_candidate_or_contact_employer",
    "alter_verified_employment_record",
    "disclose_sensitive_personal_data_without_consent",
    "bypass_required_human_review",
}

REQUIRED_REVIEWS = (
    "evidence_reviewed",
    "claim_truthfulness_reviewed",
    "job_alignment_reviewed",
    "ats_format_reviewed",
    "privacy_reviewed",
    "fairness_nondiscrimination_reviewed",
    "version_provenance_reviewed",
    "user_final_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "fabrication, submission, impersonation, record alteration, unauthorized disclosure, or review bypass is outside resume-studio authority"}
    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required resume review", "missing": missing}
    checks = {
        "evidence_gap": "material employment, education, credential, skill, achievement, date, title, scope, or source evidence remains unresolved",
        "truthfulness_risk": "material claim may be fabricated, exaggerated, misleading, unverifiable, or improperly attributed",
        "job_alignment_gap": "material role requirement, qualification, keyword, seniority, industry, or evidence-to-requirement mapping remains unresolved",
        "ats_integrity_gap": "material parsing, structure, heading, chronology, keyword stuffing, hidden-text, formatting, or machine-readability issue remains unresolved",
        "privacy_sensitive_data_risk": "material personal, confidential, protected, third-party, reference, salary, identity, or sensitive-data issue remains unresolved",
        "fairness_discrimination_risk": "material protected-characteristic, discriminatory framing, unlawful screening, exclusion, or fairness concern remains unresolved",
        "version_provenance_gap": "material source, edit, version, tailored claim, authorship, job-description, or approval provenance is incomplete",
        "authorship_submission_gap": "material user authorship, consent, final-review, submission-state, or external-use boundary remains unresolved",
    }
    blockers = [message for key, message in checks.items() if context.get(key)]
    if blockers:
        return {"allowed": False, "reason": "resume governance blocker", "blockers": blockers}
    return {"allowed": True, "reason": "resume package approved for user-controlled use after final review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS
