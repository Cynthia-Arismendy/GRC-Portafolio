# Third-Party Risk Management (TPRM) — Vendor Assessment

## Overview
Simulated vendor risk evaluation for a third-party SaaS cloud provider ("CloudVendor Inc.") hosting internal business data. The objective of this review was to identify compliance gaps against standard security baseline requirements before contract execution.

## Assessment Scope & Standards
- Vendor: CloudVendor Inc. (Cloud Storage Provider)
- Data Classification: Confidential / Internal
- Standards Applied: ISO/IEC 27001 (A.15 Supplier Relationships), NIST SP 800-161, SOC 2 Type II

## Control Review & Findings

| Control Area | Security Requirement | Vendor Status | Risk Finding & Recommendation |
| :--- | :--- | :--- | :--- |
| Data Encryption | Encryption at rest (AES-256) and in transit (TLS 1.3) | Compliant | Meets baseline security standards. |
| Access Control | Mandatory Multi-Factor Authentication (MFA) | Gap Identified | MFA is currently optional for administrative accounts. **Rec:** Require mandatory MFA prior to onboarding. |
| Audit Logs | Annual SOC 2 Type II report availability | Compliant | SOC 2 Type II report provided without material exceptions. |
| Offboarding | Data destruction SLA upon contract termination | Gap Identified | No SLA specified for post-termination data deletion. **Rec:** Insert a mandatory 30-day data destruction clause in the agreement. |

## Practical Takeaways & Internship Focus
This exercise helped me understand how security teams review vendor risks using SOC reports and security questionnaires rather than code alone. As an intern, I aim to learn how enterprise teams use TPRM tooling (such as Vanta or ServiceNow) to manage vendor assessments at scale.
