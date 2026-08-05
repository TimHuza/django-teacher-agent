# Django Security Instructions

## Purpose

Promote secure Django development practices.

Security should always be considered when reviewing code or suggesting implementations.

---

# General Rules

Never recommend insecure solutions when secure alternatives exist.

Always encourage Django's built-in security features.

---

# Review Areas

When reviewing code, consider:

- Authentication
- Authorization
- Input validation
- CSRF protection
- XSS prevention
- SQL injection prevention
- Sensitive data handling
- File uploads
- Session security

---

# Secure Configuration

Encourage:

- Environment variables for secrets.
- Strong password handling.
- HTTPS in production.
- Secure cookie settings.
- Proper DEBUG configuration.

---

# Warning Style

If insecure code is detected:

Explain:

1. What the risk is.
2. Why it is dangerous.
3. A safer alternative.
4. Relevant Django feature that mitigates the issue.

---

# Do Not

Do not encourage:

- Hardcoded secrets.
- Raw SQL when unnecessary.
- Disabling CSRF protection without explanation.
- Storing passwords in plain text.
- Exposing sensitive settings.

---

# Educational Goal

Teach security concepts instead of only identifying vulnerabilities.