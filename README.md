# NIST 800-171 Continuous Compliance Lab

Yes — that’s exactly the kind of phrasing hiring managers respond to, and it’s more impactful than the generic “OPA compliance evaluation framework” opener.

Here’s how I’d rewrite the README summary using your suggested language but keeping it polished:

---

## NIST 800-171 Policy-as-Code Compliance Framework

This project demonstrates the integration of **policy-as-code** into a **CI/CD workflow**, where every code or configuration change is automatically validated against **NIST 800-171** security controls.

### Overview

The framework uses **Open Policy Agent (OPA)** to enforce compliance rules defined in `.rego` policies. Application configuration files are evaluated automatically during the build process, ensuring that violations are detected early—before deployment.

### Implementation Highlights

* **Policy-as-Code**

  * Implemented NIST 800-171 control checks as `.rego` policies in the `opa-policies/` directory.
  * Policies cover areas such as access control, backup protection, and secure remote access.

* **Automated Compliance Evaluation**

  * Enhanced `run_opa_eval.sh` to:

    * Automatically discover all `.rego` policies.
    * Load `data/mock_app_config.json` as the default evaluation input.
    * Output a clean, column-aligned **PASS/FAIL** summary table.

* **Environment & Tooling Setup**

  * Installed OPA CLI for policy execution and `jq` for structured result parsing.
  * Set up Python dependencies (`pandas`, `jinja2`, `weasyprint`) to enable compliance reporting.

* **Current Status**

  * The CI/CD-ready evaluation pipeline is fully functional.
  * Mock configuration data intentionally triggers FAIL results to demonstrate policy enforcement.
  * The framework is ready for integration with live configurations and real-time compliance reporting.

