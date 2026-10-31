# Cynthia Arismendy — GRC & Cybersecurity Portfolio

> **Target Goal:** Aspiring GRC / Cybersecurity Intern | B.S. Cybersecurity Candidate (WGU) & Google Cybersecurity Professional Certificate.

---

### 🛠️ Core Focus & Learning Foundations

- **Frameworks & Standards (Practicing):** NIST CSF, ISO/IEC 27001 (A.9 Access Control), NIST SP 800-53, PCI-DSS, GDPR, SOC 2
- **Technical & Practical Skills:** Python Basics (Access Audit Logic), Risk Assessment, Incident Response Documentation, Compliance Checklists
- **Core Objective:** Seeking an entry-level internship to learn, grow, and apply foundational GRC/IAM concepts in real-world enterprise environments.

---

## 🛠️ Key Governance & Risk Projects

### 1. Internal Security Audit & Compliance Assessment
* **Project:** Botium Toys Security Audit
* **Frameworks & Standards:** NIST CSF, PCI-DSS, GDPR, SOC 2
* **Scope:** Evaluated internal IT assets, identified compliance gaps, mapped controls, and developed a prioritized remediation plan.
* 📄 **[View Audit Report PDF](./Controls_and_Compliance_Checklist.pdf)**

### 2. Incident Response & Documentation
* **Project:** Incident Handler's Journal
* **Frameworks & Standards:** NIST SP 800-61
* **Scope:** Documented an end-to-end incident response process, analyzing security logs, identifying root causes, and applying NIST containment and mitigation steps.
* 📄 **[View Incident Journal PDF](./Incident_Handler_Journal.pdf)**

### 3. Vulnerability Assessment & Risk Prioritization
* **Project:** Enterprise System Vulnerability Review
* **Frameworks & Standards:** NIST SP 800-30, CVSS Scoring
* **Scope:** Analyzed system vulnerabilities, mapped potential business impact, and developed a prioritized remediation roadmap.
* 📄 **[View Vulnerability Report PDF](./Vulnerability_Assessment_Report.pdf)**

---
### 4. Third-Party Risk Management (TPRM) Assessment
* **Project:** SaaS Vendor Security Review
* **Frameworks & Standards:** ISO 27001 (A.15 Supplier Relationships), NIST SP 800-161, SOC 2 Type II
* **Scope:** Evaluated third-party cloud vendor posture, identified MFA and data retention gaps, and documented remediation requirements.
* 📁 **[View TPRM Assessment Report](./vendor-risk-assessment/README.md)**

  
## 🎓 Core Competencies
* **Compliance & Frameworks:** NIST CSF 2.0, ISO 27001, SOC 2, PCI-DSS, GDPR
* **Auditing & Analysis:** Control Mapping, Gap Analysis, Risk Remediation, Institutional Auditing
* **Technical Knowledge:** Data Management, Relational Databases (SQL), Linux Security Principles

---

## 5. Multi-List Access Verification Script (Python Fundamentals Practice)

### 🎯 Project Purpose
As a career transitioner practicing Python fundamentals before starting my B.S. at WGU, I wrote this script to understand the logical workflows of access control reviews. In real corporate environments, access is granted to both internal employees and external third-party contractors (vendors). This project simulates verifying user access against multiple authorized identity groups.

### 🧠 Skills Practiced
- **Logical Operators:** Used the `and` operator to verify that a system user belongs to at least one trusted source.
- **Control Flow:** Practiced basic `for` loops and `if` statements to handle identity evaluation.
- **Data Hardcoding for Testing:** Manually simulated data lists to test the code's accuracy without requiring production database connections.

### 📋 How the Logic Works
The script acts as a security filter by executing the following step-by-step logic:

1. **Start:** Reads the list of accounts currently logged into the system (`current_system_users`).
2. **Check 1 (Employees):** Checks if the user exists in `active_employees`.
   - ➔ **If Yes:** Access is verified and approved.
   - ➔ **If No:** Moves to Check 2.
3. **Check 2 (Vendors):** Checks if the user exists in `active_vendors`.
   - ➔ **If Yes:** Access is verified and approved.
   - ➔ **If No (not in either list):** 🚨 **ALERT:** Flags account as an unauthorized access risk and prints an alert.

- 📁 **View Code:** [`access_verification_audit.py`](./access-control-audit/access_verification_audit.py)

### 🔮 Internship Goals & Future Learning Roadmap
As I work toward my B.S. at WGU, I am actively seeking an internship opportunity where I can learn to scale this logic in real-world environments. My target learning milestones include:

- **Automated Offboarding Triggers:** Learning how enterprise IAM systems automatically trigger audit scripts whenever an employee or contractor is offboarded from HR systems.
- **Exploring AI & Automation in SecOps:** Developing practical skills to use AI tools and automation scripts to help detect access anomalies faster and streamline incident reporting.
- **API Integration Basics:** Gaining hands-on experience connecting Python scripts to real identity platforms (such as Active Directory or Okta) to automatically flag or revoke unauthorized access.

# The Phishing Snowflake Effect: A Modern GRC Security Awareness Framework

## 🎯 Executive Summary
A gamified, behavior-driven security awareness framework designed to transform corporate culture, mitigate modern AI-driven phishing vectors, and seamlessly integrate with compliance frameworks like NIST CSF 2.0 and ISO 27001.

---

## 1. Pedagogical Micro-Learning Storyboard (60-Second Script)
* **Format:** Ultra-short, high-impact video scripts broken down into exact timestamps (0:00 to 1:00).
* **Modern Threat Vectors:** Focuses on realistic AI-generated threats, such as deepfake audio directives, deceptive QR codes, and urgent corporate benefits phishing.

---

## 2. Dynamic Employee Avatar Progression & Badging
* **Level System:** Gamified progression tracking where employees evolve from Baseline to Security Sentinel and Master of Defense.
* **Professional Validation:** Unlocks verified digital credentials and badges exportable to public professional profiles like LinkedIn.

---

## 3. Equitable Reward Architecture (On-Site & Remote Parity)
* **For On-Site Staff:** Premium parking spots, catered team lunches, **Early Friday Sign-Off Passes**, and **1 additional Paid PTO Day** for maintaining zero-click records across 2 consecutive quarters.
* **For Remote/WFA Staff:** Food delivery stipends (DoorDash/UberEats), home office technology stipends, **Total Disconnect Days**, and digital flexibility passes.

---

## 4. Viral Culture & Internal Communications
* **Pre-Campaign Engagement:** Participatory baseline surveys co-designed with Human Resources.
* **Viral Amplification:** Official corporate campaign hashtag (**`#CatchTheSnowflake`**) and automated public shoutouts/mentions in corporate Slack and Microsoft Teams channels upon module completion.
* **Peer Recognition:** Monthly community episodes highlighting safe security behaviors and peer shout-out rewards.

---

## 5. GRC Audit Mapping & Automated Evidence Collection
* **Standards Alignment:** Rigorously mapped to **NIST CSF 2.0** (Controls PR.AT-01, GV.OC-01) and **ISO/IEC 27001:2022** (Control A.7.2.2).
* **Automation:** Designed for seamless integration with automated GRC and trust platforms like **Vanta** to automatically gather timestamped compliance audit trails.

---

## 6. RACI Governance & 10-Week Execution Roadmap
* **Role Separation:** Clearly distinguishes the GRC Specialist’s strategic oversight from creative production, HR management, and IT administration.
* **Rollout Timeline:** A structured 10-week execution plan moving from initial risk assessment and stakeholder alignment to full deployment and final auditor reporting.

---

## 🛡️ 7. Third-Party Vendor Security Extension (Supply Chain Protection)
To mitigate supply chain and external vendor risks (fully aligned with ISO 27001:2022 A.7.2.2 and NIST CSF 2.0 GV.OC-01), the framework extends beyond internal staff:
* **Vendor Integration Pack:** External suppliers, contractors, and third-party vendors handling company data undergo the same 60-second micro-learning modules and behavior-based awareness tracking.
* **Compliance Pre-requisite:** Completion of security awareness verification and maintaining a clean click-record is mandatory for third-party API and system access renewals, ensuring end-to-end organizational defense.

---

### 🚀 Enterprise Implementation & Availability
The core architecture, threat vector mapping, and strategic governance model for **"The Phishing Snowflake Effect"** are outlined above. 

* **Proprietary Operational Guide:** The comprehensive, step-by-step implementation manual, metric calculators, and training assets are securely withheld to protect intellectual property.
* **Professional Engagement:** Complete access to the full implementation package and customized deployment roadmaps is available through **full-time roles, strategic security consulting, or select graduate/advanced placement opportunities**.
