from orchestration.orchestrator import run
from safety.policy import PROTECTED_ACTIONS, REQUIRED_REVIEWS, authorize


def approved_context():
    return {key: True for key in REQUIRED_REVIEWS}


def test_orchestrator_runs_five_agents_and_fails_closed():
    result = run({})
    for key in ("evidence", "tailoring", "writing", "ats", "review"):
        assert key in result
    assert result["released"] is False


def test_missing_reviews_fail_closed():
    result = authorize("release_resume_package", {})
    assert result["allowed"] is False
    assert len(result["missing"]) == 8


def test_reviewed_package_can_release():
    assert authorize("release_resume_package", approved_context())["allowed"] is True


def test_evidence_gap_blocks():
    assert authorize("release_resume_package", approved_context() | {"evidence_gap": True})["allowed"] is False


def test_truthfulness_risk_blocks():
    assert authorize("release_resume_package", approved_context() | {"truthfulness_risk": True})["allowed"] is False


def test_ats_integrity_gap_blocks():
    assert authorize("release_resume_package", approved_context() | {"ats_integrity_gap": True})["allowed"] is False


def test_privacy_risk_blocks():
    assert authorize("release_resume_package", approved_context() | {"privacy_sensitive_data_risk": True})["allowed"] is False


def test_protected_actions_never_autonomously_release():
    for action in PROTECTED_ACTIONS:
        assert authorize(action, approved_context())["allowed"] is False
