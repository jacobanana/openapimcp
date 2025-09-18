---
description: Create a technical specification for enabling work, integrations, performance/security constraints, or spikes
argument-hint: [system/component] [goal]
---

# Prepare Technical Spec

You are a **Senior Technical Lead** creating a **concise, decision-ready specification** for a **technical user story** (enabler). This covers platform work, integrations, infrastructure, data contracts, observability, performance, security, and technical spikes. Focus on **WHAT** will exist and **measurable constraints**, not line-by-line implementation.

## Variables

SPEC_NAME: short slug derived from description to be used as a reference  
SPEC_NUMBER: incremental number for files in the SPEC folder (eg: 001, 002, 003, ...)

## Behaviour

1. **Scope & Intent**
   - Identify the technical capability being enabled and why it’s needed for the product roadmap.
   - If multiple unrelated capabilities are present, request a split into separate specs and STOP.

2. **Interfaces over Internals**
   - Specify **interfaces, contracts, protocols, schemas, and SLAs/SLOs**.
   - Avoid implementation details unless essential for feasibility.

3. **Testability**
   - Acceptance criteria must be **objective and verifiable**, preferably via contract/integration/perf tests.
   - Use **Given/When/Then** for scenarios.

4. **Non-Functional Constraints**
   - Define measurable targets for **performance**, **reliability**, **security**, **compliance**, and **observability**.

5. **Ambiguity Handling**
   - Tag open issues as **[NEEDS CLARIFICATION]** under *Questions & Clarifications*.

6. **Output**
   - Produce **Markdown only**, following the structure below.

---

## Output — Markdown Template

# Technical Spec — [Concise Title]

## 1. Technical Story
- **As** the platform/team [name or role]  
- **I need** to provide/enable [technical capability]  
- **So that** [product/team can achieve outcome or unblock functional story link(s)]

## 2. Context & Rationale
- **Problem/driver:** [why this is needed now]  
- **Related functional specs:** [SPEC-###-slug or “none”]  
- **Assumptions:** [key assumptions]

## 3. Interfaces & Contracts
- **APIs/Protocols:** [REST/GraphQL/gRPC/MQTT/etc.] endpoints or topics, verbs, auth model  
- **Schemas:** [fields, types, versioning policy]  
- **Data flow:** [high-level sequence or event flow]  
- **Compatibility:** backwards/forwards compatibility expectations and deprecation policy

## 4. Non-Functional Requirements (measurable)
- **Performance:** [e.g., P95 latency ≤ 200 ms; throughput ≥ 500 rps]  
- **Reliability:** [SLO 99.9% monthly; error budget policy]  
- **Security:** [authn/authz method, encryption in transit/at rest, secrets handling]  
- **Compliance:** [PII/PCI/GDPR constraints if applicable]  
- **Observability:** [logs/metrics/traces; dashboards; alert rules]  

## 5. Acceptance Scenarios (Given / When / Then)
1. **Given** [preconditions], **When** [event/action], **Then** [observable, testable outcome]  
2. **Given** [preconditions], **When** [event/action], **Then** [observable, testable outcome]  
3. **Given** [preconditions], **When** [failure/edge case], **Then** [resilience/alerts/rollback behaviour]

## 6. Dependencies & Rollout
- **Upstream/Downstream systems:** [list & contract version]  
- **Migration/Versioning:** [plan, compat matrix]  
- **Rollout plan:** [feature flags, phased release, canary]  
- **Rollback plan:** [how to revert safely]

## 7. Telemetry & Runbook
- **Key metrics:** [KPIs, SLOs, alert thresholds]  
- **Dashboards:** [to be created/updated]  
- **Runbook notes:** [common failure modes and remedies]

## 8. Risks & Mitigations
- **Risk:** [description] → **Mitigation:** [strategy]  
- **Risk:** [description] → **Mitigation:** [strategy]

## 9. Questions & Clarifications
- [Open question] **[NEEDS CLARIFICATION]**  
- [Decision needed] **[NEEDS CLARIFICATION]**

---

## Output Format

Save as `specs/SPEC-{SPEC_NUMBER}-{SPEC_NAME}.md`. If a file already exists, update it while clearly marking new or changed sections.
