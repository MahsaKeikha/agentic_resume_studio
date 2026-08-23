# F164 | Agentic Resume Studio | L3 Gold Standard | v1.0

A governed five-agent reference architecture for resume development across evidence extraction, role tailoring, achievement writing, ATS compatibility, editorial review, privacy, fairness, version control, provenance, and explicit user approval.

F164 is a resume-development and career-document support system. It is not a recruiter, employer, credential verifier, background-check authority, application-submission system, or autonomous representative of the candidate. It cannot fabricate or exaggerate credentials, submit applications, impersonate the candidate, alter verified employment records, disclose sensitive personal information without consent, or bypass required human review.

## Resume-development lifecycle

```text
Source Evidence
        -> Role and Job-Description Analysis
        -> Tailoring and Claim Selection
        -> Resume Writing
        -> ATS and Format Review
        -> Truthfulness, Privacy, and Fairness Review
        -> User Final Approval
        -> User-Controlled Submission
```

The workflow fails closed when required reviews are missing or when material evidence, truthfulness, job alignment, ATS, privacy, fairness, provenance, authorship, or submission-boundary issues remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Evidence Agent | Extracts employment history, education, credentials, skills, projects, publications, achievements, dates, scope, and supporting evidence | What claims are actually supported by the candidate's evidence? |
| Tailoring Agent | Maps verified experience to job requirements, role priorities, keywords, seniority, domain language, and relevant achievements | Which supported facts are most relevant to this role? |
| Writing Agent | Produces concise, achievement-oriented, human-readable resume language while preserving factual accuracy and authorship boundaries | How can verified experience be expressed clearly and persuasively without exaggeration? |
| ATS Agent | Reviews structure, headings, chronology, parsing, keywords, readability, file-format assumptions, and anti-gaming constraints | Will the resume remain machine readable without deceptive ATS tactics? |
| Review Agent | Reviews truthfulness, privacy, fairness, version history, provenance, tone, consistency, and user approval before external use | Is the resume accurate, defensible, respectful, and ready for the user's final decision? |

## Repository structure

```text
AGENTS/
├── evidence_agent.py
├── tailoring_agent.py
├── writing_agent.py
├── ats_agent.py
└── review_agent.py

SKILLS/
├── evidence_extraction.py
├── job_alignment.py
├── achievement_writing.py
├── ats_reasoning.py
└── editorial_review.py

TOOLS/
├── evidence_ledger.py
├── claim_checker.py
├── keyword_matrix.py
├── version_store.py
└── approval_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

## Evidence-first architecture

The central rule is simple: every material resume claim should be grounded in evidence supplied or confirmed by the candidate. F164 may improve wording, structure, emphasis, and relevance, but it should not improve the resume by inventing facts.

## Evidence review

The executable policy requires `evidence_reviewed`. `evidence_gap` blocks release when material employment, education, credential, skill, achievement, date, title, scope, or source evidence remains unresolved.

Evidence can include prior resumes, employment records, project notes, publications, portfolios, certificates, transcripts, performance reviews, job descriptions, contracts, public professional profiles, and user-confirmed facts.

## Employment history

Employment entries should preserve employer, role, dates, employment type where relevant, scope, responsibilities, achievements, and location only when useful and appropriate.

Approximate dates should not be silently converted into exact dates.

## Job titles

Official job titles should remain distinguishable from clarified functional titles. A functional descriptor can help readability, but it should not create a materially different seniority level or authority claim.

## Promotions

Multiple roles at one employer should preserve promotion history and chronology where that improves accuracy.

## Overlapping roles

Consulting, teaching, advisory, entrepreneurial, part-time, and full-time work can overlap legitimately. Chronology should preserve the actual relationship rather than forcing a misleading linear timeline.

## Employment gaps

F164 should not invent employment to hide gaps. Gaps can be handled through structure, chronology, project work, education, caregiving, sabbaticals, or other truthful context when the user chooses to include it.

## Education

Education entries should preserve institution, degree or credential, field, completion state, and dates where material.

An incomplete degree should not be presented as completed.

## Certifications and licenses

Certifications, licenses, registrations, and professional designations should preserve issuer, status, jurisdiction where relevant, and expiration when material.

Expired, pending, inactive, or jurisdiction-limited credentials should not be presented as unrestricted current credentials.

## Publications and patents

Publications, conference papers, books, patents, and other intellectual contributions should preserve authorship, title, venue, status, and citation detail where relevant.

Submitted, accepted, in-press, published, filed, granted, and pending are different statuses.

## Projects

Projects can demonstrate skills when they are accurately described. The resume should distinguish personal, academic, open-source, consulting, internal, client, and employer-owned projects when that distinction matters.

## Confidential work

Confidential employer or client information should not be exposed merely to strengthen a resume. Achievements can often be generalized without revealing protected information.

## Skills

Skills should reflect demonstrated ability or credible training. Keyword relevance does not justify adding a skill the candidate does not possess.

## Skill levels

Terms such as expert, advanced, proficient, working knowledge, and familiar should be used carefully. F164 should not inflate competence to satisfy a posting.

## Languages

Language proficiency should reflect the user's actual ability and should not be inferred from nationality, surname, location, or education.

## Metrics and achievements

Quantified achievements can strengthen resumes, but numbers should be supported or clearly user-confirmed.

F164 must not manufacture percentages, revenue, savings, team sizes, customer counts, performance gains, budgets, timelines, or scale.

## Attribution

A team result should not automatically become an individual achievement. Language can distinguish led, owned, contributed to, supported, collaborated on, or participated in.

## Scope

Claims about team size, budget, geography, platform scale, responsibility, reporting lines, or decision authority should remain faithful to actual scope.

## Truthfulness architecture

The executable policy requires `claim_truthfulness_reviewed`. `truthfulness_risk` blocks release when a material claim may be fabricated, exaggerated, misleading, unverifiable, or improperly attributed.

## Fabrication boundary

`fabricate_or_exaggerate_credential` is protected. F164 must not create fictional degrees, employers, titles, awards, publications, patents, certifications, skills, clients, achievements, dates, metrics, clearances, licenses, or responsibilities.

## Exaggeration

A claim can be technically based on truth while still misleading through inflated scope, seniority, causation, precision, or ownership. Review should consider the likely interpretation by a reasonable reader.

## Causation

Resume language should not claim that the candidate caused an outcome when the evidence supports only contribution or correlation.

## Numerical precision

Precise metrics can create credibility but also risk falsehood. If a number is estimated, the user should confirm whether approximate wording is appropriate.

## Awards

Awards should preserve issuer, date, category, and recipient scope when material. A team award should not become a personal award unless the candidate was individually recognized.

## Security clearances

Clearance claims can be sensitive and must be accurate. Current, inactive, eligible, interim, and historical status are not interchangeable.

## Background checks

F164 does not certify employment, education, criminal, financial, or credential history. It prepares candidate-authored materials based on evidence and user confirmation.

## Role alignment architecture

The executable policy requires `job_alignment_reviewed`. `job_alignment_gap` blocks release when material role requirement, qualification, keyword, seniority, industry, or evidence-to-requirement mapping remains unresolved.

## Job-description parsing

A job description can be decomposed into required qualifications, preferred qualifications, responsibilities, domain language, technical skills, leadership expectations, compliance requirements, and evidence signals.

## Required versus preferred

Required and preferred qualifications should not be treated as equivalent. The resume can emphasize relevant evidence without falsely claiming to satisfy every requirement.

## Seniority

Tailoring should respect actual seniority. A candidate should not be rewritten into a director, principal, manager, architect, scientist, professor, or executive if their evidence does not support that level.

## Industry translation

Experience can often be translated across industries by emphasizing transferable systems, methods, outcomes, and constraints while avoiding false claims of domain-specific expertise.

## Transferable skills

Examples include project leadership, systems thinking, controls, data analysis, AI, embedded systems, research, communication, stakeholder management, quality, product development, teaching, and operations.

## Keyword alignment

Relevant keywords can be incorporated when supported by evidence. Keyword matching is a retrieval and communication aid, not a license to add unsupported skills.

## Keyword stuffing

Excessive repetition can hurt readability and may be interpreted as manipulative. F164 should favor natural, evidence-grounded inclusion.

## Hidden keyword tactics

Invisible text, white-on-white keywords, zero-size text, concealed sections, metadata stuffing, or other deceptive ATS manipulation are outside the intended design.

## Writing architecture

Resume writing should prioritize clarity, truthfulness, relevance, evidence density, and readability.

## Achievement bullets

A useful bullet can combine action, context, method, and result. The exact pattern should vary naturally rather than making every bullet formulaic.

## Action verbs

Strong verbs should reflect actual responsibility. Led, directed, owned, designed, architected, developed, implemented, analyzed, supported, collaborated, coordinated, and contributed are not interchangeable.

## Present versus past tense

Current roles often use present tense for ongoing responsibilities and past tense for completed achievements. Past roles generally use past tense.

## Voice

The resume should sound like the candidate's professional voice rather than generic AI marketing language.

## Brevity

Concise writing should not remove technical specificity, scope, evidence, or material distinctions.

## Technical depth

Technical resumes may require tools, languages, architectures, standards, protocols, methods, hardware, algorithms, research techniques, or domain terms. These should remain understandable and relevant to the target role.

## Leadership evidence

Leadership should be shown through scope, decisions, teams, programs, mentoring, cross-functional coordination, outcomes, or ownership, not just the word leadership.

## Research resumes

Research-oriented resumes can include publications, grants, methods, experiments, collaborations, teaching, invited talks, patents, datasets, and research impact.

## Academic CV boundary

A full academic CV can require more detail than a resume. F164 should not compress away publications, teaching, grants, service, or appointments when the user needs an academic format.

## Executive resumes

Executive materials can emphasize enterprise scope, transformation, strategy, governance, budgets, teams, P&L, boards, markets, and outcomes, but only when supported by evidence.

## Career-change resumes

Career-change tailoring should emphasize transferable evidence and relevant achievements without pretending prior roles were in the target field.

## Early-career resumes

Early-career candidates can draw from education, projects, internships, research, volunteering, leadership, coursework, and portfolio evidence without inventing professional experience.

## ATS architecture

The executable policy requires `ats_format_reviewed`. `ats_integrity_gap` blocks release when material parsing, structure, heading, chronology, keyword stuffing, hidden-text, formatting, or machine-readability issues remain unresolved.

## Standard sections

Common ATS-friendly headings include Summary, Experience, Education, Skills, Projects, Certifications, Publications, and Awards.

## Parsing

Tables, text boxes, graphics, icons, columns, headers, footers, and unusual typography can parse inconsistently across systems. F164 should identify risk without claiming universal ATS behavior.

## File format

DOCX and text-based PDF are common, but employer instructions should control. F164 should not assume one format works for every ATS.

## Chronology

Dates should be consistent and machine readable. Mixed formats can create parsing ambiguity.

## Contact information

Contact information should be current and limited to what the user wants to share. Sensitive identifiers should not appear on a resume.

## Address privacy

A full street address is often unnecessary. City and region may be enough when location context is helpful.

## Links

LinkedIn, GitHub, portfolio, Google Scholar, personal sites, and other links should be current, relevant, and user approved.

## Accessibility

Readable typography, meaningful headings, adequate contrast, logical structure, and simple layout can improve accessibility for human readers and assistive technology.

## ATS myths

F164 should avoid presenting unverifiable folklore as universal truth. ATS systems vary by vendor, configuration, employer process, parsing stack, and recruiter behavior.

## Score boundaries

An ATS score from a third-party tool is an estimate, not a guarantee of interview selection.

## Privacy architecture

The executable policy requires `privacy_reviewed`. `privacy_sensitive_data_risk` blocks release when material personal, confidential, protected, third-party, reference, salary, identity, or sensitive-data issues remain unresolved.

## Sensitive identifiers

Social security numbers, national IDs, passport numbers, driver's license numbers, bank details, private addresses, authentication secrets, and similar identifiers should not appear on a resume.

## Salary history

Salary history can be sensitive and legally regulated in some jurisdictions. F164 should not include it by default.

## Age and date of birth

Birth date is generally unnecessary for a resume unless a specific lawful context requires it.

## Marital and family status

Marital status, children, pregnancy, caregiving, religion, ethnicity, sexual orientation, disability, and other protected or sensitive characteristics should not be inferred or inserted by default.

## References

Reference names, emails, phone numbers, and relationships should be shared only with appropriate consent.

## Client confidentiality

Client names and confidential engagements should not be exposed without permission. Generalized descriptions can preserve value while protecting confidentiality.

## Employer confidentiality

Internal metrics, unreleased products, source code, confidential roadmaps, security details, customer data, and proprietary methods should be handled carefully.

## Privacy versus completeness

A resume does not need to contain every true fact. The candidate controls what relevant personal information is disclosed.

## Fairness and nondiscrimination architecture

The executable policy requires `fairness_nondiscrimination_reviewed`. `fairness_discrimination_risk` blocks release when material protected-characteristic, discriminatory framing, unlawful screening, exclusion, or fairness issues remain unresolved.

## Protected characteristics

F164 should not recommend adding, removing, or manipulating information solely to discriminate against or conceal a protected characteristic for unlawful purposes.

## Name changes

Candidates can choose the professional name they use. F164 should not infer legal identity or gender from a name.

## Pronouns

Pronouns should be included only according to user preference and context.

## Disability

The system should not infer disability status or recommend disclosure without user intent.

## Employment gaps and caregiving

Career gaps should not be treated as evidence of lower ability. If the user wants to include caregiving, family leave, health leave, sabbatical, or other context, wording should remain truthful and respectful.

## Age bias

The system can help focus older experience on relevance and avoid unnecessary graduation dates where appropriate, but it should not falsify dates.

## International experience

Global experience, immigration history, citizenship, visa status, and work authorization can be sensitive. The user controls what is disclosed, subject to legitimate application requirements.

## Version architecture

The executable policy requires `version_provenance_reviewed`. `version_provenance_gap` blocks release when material source, edit, version, tailored claim, authorship, job-description, or approval provenance is incomplete.

## Master resume

A master resume can preserve the full verified evidence base. Tailored resumes should derive from it without erasing the source history.

## Tailored versions

Each tailored version should preserve target role, employer, job description or reference, date, major edits, claims added or removed, and approval state.

## Version naming

Clear names can prevent accidental submission of the wrong version.

## Change history

Material changes should be reviewable, especially changes to dates, metrics, titles, credentials, or claims.

## Rollback

A prior approved version should be recoverable when practical.

## Provenance

`version_provenance_gap` and the evidence ledger together preserve how each claim entered the resume and what source supports it.

## Authorship

AI-assisted drafting does not transfer ownership of factual claims to the system. The candidate remains responsible for reviewing and approving the content they present externally.

## User approval architecture

The executable policy requires `user_final_approval`. `authorship_submission_gap` blocks release when material user authorship, consent, final-review, submission-state, or external-use boundary remains unresolved.

## Final review

Before external use, the user should review names, dates, titles, employers, metrics, skills, education, credentials, contact details, links, and role-specific claims.

## Submission boundary

`submit_job_application` is protected. F164 can prepare a resume package but cannot autonomously submit it.

## Impersonation boundary

`impersonate_candidate_or_contact_employer` is protected. The system can draft messages, but it should not communicate externally as though it were the candidate without explicit authorized execution.

## Verified-record boundary

`alter_verified_employment_record` is protected. F164 cannot change authoritative employer, education, credential, background-check, or government records.

## Sensitive-disclosure boundary

`disclose_sensitive_personal_data_without_consent` is protected.

## Review-bypass boundary

`bypass_required_human_review` is protected. Passing automated checks does not remove the candidate's responsibility to approve external-facing content.

## Cover letters

F164 can support cover letters when they remain grounded in verified experience and user intent. A cover letter should not claim enthusiasm, relationships, achievements, or motives the user does not endorse.

## Professional summaries

Summaries should reflect evidence and target relevance rather than generic claims such as visionary leader or world-class expert unless the record supports them.

## Objective statements

Objectives can be useful in some contexts but should be specific enough to add information beyond the job title.

## Skills sections

Skills can be grouped by domain, technical area, methods, tools, leadership, or language when useful. Unsupported keyword lists should be avoided.

## Portfolio links

Portfolio content should be reviewed for confidentiality, ownership, broken links, outdated work, and consistency with the resume.

## GitHub links

GitHub repositories can provide evidence of technical ability, but private, employer-owned, security-sensitive, or low-quality repositories should not be surfaced automatically.

## LinkedIn consistency

Minor differences across resume and LinkedIn can be legitimate, but major date, title, or employer inconsistencies should be reviewed.

## Background-check consistency

Resume wording can emphasize relevant scope, but factual fields that may be verified should remain consistent with authoritative records.

## Reorganizations and acquired companies

Employer naming can preserve both historical entity and recognizable current parent when useful, for example Company A, acquired by Company B.

## Consulting and self-employment

Consulting work should preserve client confidentiality, employment structure, project dates, and actual scope. Self-employment should not be presented as employment by a client.

## Freelance work

Multiple freelance engagements can be grouped when that improves readability, provided dates and client relationships remain truthful.

## Volunteer work

Volunteer experience can demonstrate leadership and skills. It should not be misrepresented as paid employment.

## Board and advisory roles

Board, advisory, mentor, and community roles should preserve whether they were formal, informal, compensated, fiduciary, or volunteer when material.

## Teaching and speaking

Teaching, invited lectures, conference speaking, workshops, and training should preserve venue, role, subject, and status.

## Awards and recognition

Recognition should be specific enough to verify and should not imply broader prestige than the award warrants.

## Work authorization

F164 can help phrase work-authorization status based on user-confirmed facts, but it does not provide immigration legal advice.

## Legal and employment boundaries

Employment agreements, nondisclosure agreements, noncompetes, export controls, public-sector restrictions, regulated credentials, and immigration status can affect what may be disclosed or claimed.

Qualified legal or HR review may be appropriate when material.

## AI-generated wording

Generated wording should remain editable and reviewable. F164 should not introduce unsupported facts merely because they make a bullet sound stronger.

## Hallucination control

The system must never invent employers, dates, titles, responsibilities, skills, credentials, publications, awards, projects, metrics, clients, clearances, citations, or URLs.

## Claim checker

`TOOLS/claim_checker.py` can compare draft claims against the evidence ledger and flag unsupported or materially altered claims.

## Evidence ledger

`TOOLS/evidence_ledger.py` can preserve claim, source, date, confidence, user confirmation, supporting excerpt or reference, and status.

## Keyword matrix

`TOOLS/keyword_matrix.py` can map job-description terms to verified evidence, related terminology, missing evidence, and resume sections.

## Version store

`TOOLS/version_store.py` can preserve master and tailored resume versions, target roles, dates, changes, and approval state.

## Memory and state

The `memory/` layer can preserve verified claims, user preferences, role targets, approved wording, rejected wording, resume versions, and unresolved questions.

Stale or rejected claims should not silently reappear in later resumes.

## Observability

The `observability/` layer supports traceability across evidence extraction, claim selection, tailoring, writing, ATS review, privacy flags, fairness flags, versions, user approvals, and protected-action attempts.

Useful telemetry includes unsupported claims, changed metrics, title changes, date conflicts, missing evidence, ATS warnings, keyword overuse, privacy flags, confidential-information flags, and approval state.

## Required reviews

The executable policy requires all eight conditions:

```text
evidence_reviewed
claim_truthfulness_reviewed
job_alignment_reviewed
ats_format_reviewed
privacy_reviewed
fairness_nondiscrimination_reviewed
version_provenance_reviewed
user_final_approval
```

Missing any condition fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- employment, education, credentials, skills, achievements, dates, titles, scope, or source evidence remains unresolved
- a material claim may be fabricated, exaggerated, misleading, unverifiable, or improperly attributed
- role requirements, qualifications, keywords, seniority, industry context, or evidence-to-requirement mapping remains unresolved
- parsing, structure, headings, chronology, keyword stuffing, hidden text, formatting, or machine-readability issues remain unresolved
- personal, confidential, protected, third-party, salary, identity, or sensitive-data issues remain unresolved
- protected-characteristic, discriminatory framing, unlawful screening, exclusion, or fairness concerns remain unresolved
- source, edit, version, tailored claim, authorship, job-description, or approval provenance is incomplete
- user authorship, consent, final review, submission state, or external-use boundaries remain unresolved
- any required review is missing
- user final approval is missing

The system exposes blockers rather than manufacturing credentials, truthfulness, ATS compatibility, user consent, or submission authority.

## Protected actions

```text
fabricate_or_exaggerate_credential
submit_job_application
impersonate_candidate_or_contact_employer
alter_verified_employment_record
disclose_sensitive_personal_data_without_consent
bypass_required_human_review
```

These remain outside autonomous authority even after all required reviews pass.

## Human authority boundaries

F164 must not autonomously apply for jobs, communicate with employers as the candidate, accept application terms, alter verified records, make legal representations, decide what sensitive data to disclose, or present unreviewed AI-generated claims externally.

The candidate retains final authority over factual claims, wording, disclosure, target role, versions, and submission.

## Explicit failure states

```text
EVIDENCE REVIEW REQUIRED
CLAIM TRUTHFULNESS REVIEW REQUIRED
JOB ALIGNMENT REVIEW REQUIRED
ATS FORMAT REVIEW REQUIRED
PRIVACY REVIEW REQUIRED
FAIRNESS AND NONDISCRIMINATION REVIEW REQUIRED
VERSION AND PROVENANCE REVIEW REQUIRED
USER FINAL APPROVAL REQUIRED
EVIDENCE GAP
TRUTHFULNESS RISK
JOB ALIGNMENT GAP
ATS INTEGRITY GAP
PRIVACY OR SENSITIVE DATA RISK
FAIRNESS OR DISCRIMINATION RISK
VERSION OR PROVENANCE GAP
AUTHORSHIP OR SUBMISSION GAP
CREDENTIAL FABRICATION OR EXAGGERATION PROHIBITED
AUTONOMOUS JOB APPLICATION SUBMISSION PROHIBITED
CANDIDATE IMPERSONATION OR EMPLOYER CONTACT PROHIBITED
VERIFIED EMPLOYMENT RECORD ALTERATION PROHIBITED
UNAUTHORIZED SENSITIVE DATA DISCLOSURE PROHIBITED
REQUIRED HUMAN REVIEW BYPASS PROHIBITED
```

## End-to-end reference workflow

1. Collect candidate-approved source material, employment history, education, credentials, projects, publications, achievements, skills, and prior resume versions.
2. Build an evidence ledger with dates, sources, confidence, user confirmation, and unresolved discrepancies.
3. Parse the target job description into requirements, preferences, responsibilities, seniority, domain language, and relevant keywords.
4. Map each important job requirement to verified candidate evidence and explicitly mark missing evidence.
5. Select the most relevant verified achievements without inventing experience merely to increase match rate.
6. Draft concise resume content that preserves actual ownership, scope, seniority, chronology, and quantitative evidence.
7. Run claim-truthfulness checks for dates, titles, skills, metrics, credentials, employers, publications, and responsibilities.
8. Review ATS structure, headings, chronology, keyword use, file-format assumptions, and deceptive formatting risks.
9. Review privacy, confidentiality, references, protected characteristics, fairness, work-authorization wording, and sensitive disclosures.
10. Preserve version history, job-description provenance, edits, removed claims, tailored claims, and approval state.
11. Apply fail-closed governance and require explicit user final approval.
12. Keep application submission, employer communication, record alteration, sensitive disclosure, and any external representation under user control.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test evidence extraction, claim fidelity, unsupported-claim detection, job alignment, achievement writing, ATS compatibility, keyword discipline, confidentiality, privacy, fairness, chronology, versioning, provenance, and user-approval boundaries.

The behavioral verification layer includes direct governance tests and a 10-scenario held-out suite covering missing review, approved resume release, evidence gaps, truthfulness risks, job-alignment gaps, ATS-integrity gaps, privacy risks, fairness risks, version-provenance gaps, and authorship-submission gaps.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed governance, held-out scenarios, and execution of the governed five-agent resume workflow.

## Reproducibility

A reproducible resume build should preserve candidate-approved source evidence, target job description, extraction date, claim ledger, tailoring decisions, keyword map, draft version, review findings, approved edits, and final user approval state.

## Extension points

Organization-specific implementations can add governed integrations for document libraries, job-description sources, resume parsers, ATS-preview tools, portfolio systems, professional-profile systems, credential repositories, and application trackers.

Any integration capable of submitting applications, sending messages, modifying external profiles, sharing personal data, changing authoritative records, or accepting legal terms should remain behind explicit user authorization, clear previews, audit logging, and human-controlled execution.

## Example applications

Potential governed uses include master resume creation, job-specific tailoring, executive resumes, technical resumes, research resumes, academic-industry transitions, career-change resumes, early-career resumes, project-based resumes, ATS reviews, achievement rewriting, privacy reviews, evidence audits, and version management.

F164 is not an autonomous recruiter, applicant, credential verifier, background-check service, employer representative, or application-submission authority.

## Design principles

1. Ground every material resume claim in evidence supplied or confirmed by the candidate.
2. Improve wording and relevance without changing the underlying facts.
3. Never manufacture credentials, experience, achievements, metrics, seniority, authorship, or technical skills to satisfy a job description.
4. Treat ATS optimization as clarity and machine readability, not deceptive keyword or hidden-text manipulation.
5. Preserve privacy, confidentiality, fairness, and user control over sensitive disclosures.
6. Keep master and tailored versions linked through explicit provenance and version history.
7. Preserve uncertainty and ask for user confirmation rather than converting ambiguous evidence into confident claims.
8. Fail closed when evidence, truthfulness, alignment, ATS integrity, privacy, fairness, provenance, authorship, or user approval is incomplete.
9. Keep submission, external communication, record alteration, and consequential disclosure under explicit user control.

## Scope statement

F164 demonstrates a governed multi-agent architecture for resume development. It combines specialized evidence, tailoring, writing, ATS, and review agents with deterministic evidence-ledger, claim-checking, keyword, versioning, and approval tools, observability, held-out evaluation, and fail-closed governance while preserving strict user authority over factual claims, disclosures, external representation, and job-application submission.

Author: Mahsa Keikha
