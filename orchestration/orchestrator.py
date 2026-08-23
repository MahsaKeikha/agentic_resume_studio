from AGENTS import ats_agent, evidence_agent, review_agent, tailoring_agent, writing_agent
from safety.policy import authorize


def run(case: dict) -> dict:
    result = {
        "evidence": evidence_agent.run(case),
        "tailoring": tailoring_agent.run(case),
        "writing": writing_agent.run(case),
        "ats": ats_agent.run(case),
        "review": review_agent.run(case),
    }
    governance = authorize("release_resume_package", case.get("governance", {}))
    result["governance"] = governance
    result["released"] = governance["allowed"]
    return result
