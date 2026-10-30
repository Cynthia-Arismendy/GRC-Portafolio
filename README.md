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

## 🎓 Core Competencies
* **Compliance & Frameworks:** NIST CSF 2.0, ISO 27001, SOC 2, PCI-DSS, GDPR
* **Auditing & Analysis:** Control Mapping, Gap Analysis, Risk Remediation, Institutional Auditing
* **Technical Knowledge:** Data Management, Relational Databases (SQL), Linux Security Principles

---

## 4. Multi-List Access Verification Script (Python Fundamentals Practice)

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

