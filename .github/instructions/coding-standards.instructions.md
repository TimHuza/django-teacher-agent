# Django Coding Standards Instructions

## Purpose

Ensure generated or reviewed Django code follows consistent, readable, and maintainable standards.

---

# General Principles

Prefer:

- Readability over cleverness.
- Explicit code over implicit behavior.
- Simplicity over unnecessary complexity.

---

# Django Conventions

Follow standard Django project organization.

Keep:

- Models in models.py
- Views in views.py
- Forms in forms.py
- URLs in urls.py
- Templates organized by application

---

# Naming

Encourage descriptive names.

Examples:

Good:

- OrderCreateForm
- ProductListView
- UserProfile

Avoid vague names such as:

- Data
- Item
- Temp
- Test

---

# Functions

Functions should:

- Have a single responsibility.
- Be reasonably small.
- Have clear names.

---

# Classes

Classes should:

- Represent a clear concept.
- Be cohesive.
- Avoid unrelated responsibilities.

---

# Comments

Comments should explain:

- Why something exists.
- Important decisions.
- Non-obvious behavior.

Avoid comments that simply restate the code.

---

# Documentation

When generating code, explain:

- Where the code belongs.
- Why it belongs there.
- How it interacts with the rest of the Django project.

---

# Maintainability

Prefer solutions that:

- Are easy to understand.
- Follow Django conventions.
- Are easy to extend later.
- Minimize duplicated logic.

---

# Final Review

Before presenting code, mentally verify:

- Is it readable?
- Does it follow Django conventions?
- Is it maintainable?
- Is it secure?
- Will a beginner understand it with the accompanying explanation?