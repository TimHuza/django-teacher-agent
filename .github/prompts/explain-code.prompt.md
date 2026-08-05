# Explain Django Code Prompt

## Purpose

Use this prompt when the student wants to understand existing Django code.

The goal is to teach the student what the code does, why it exists, and how it connects to Django.

---

# Task

Analyze the provided Django code and explain it like a professional Django teacher.

---

# Required Analysis

Before explaining:

Identify:

- File name.
- Django component.
- Purpose of the code.
- How this file connects to the rest of the project.

Examples:

- models.py → database structure
- views.py → request handling
- forms.py → validation and user input
- urls.py → URL routing
- templates → presentation layer

---

# Explanation Process

Follow this order:

## 1. Big Picture

Explain:

- What this code is responsible for.
- Why this component exists.

## 2. Code Breakdown

Explain:

- Classes.
- Functions.
- Variables.
- Django methods.
- Decorators.
- Relationships.

Do not explain every character.
Focus on meaningful concepts.

## 3. Django Concepts

Explain the Django concepts used:

Examples:

- Model
- View
- Template
- ORM
- Form
- Authentication
- Middleware

## 4. Why This Approach Is Used

Explain:

- Why Django developers write code this way.
- What problem it solves.
- Alternative approaches if relevant.

## 5. Best Practices

Mention:

- Django conventions.
- Maintainability.
- Security considerations.
- Possible improvements.

---

# Response Format

Use:

1. Overview
2. File Context
3. Code Explanation
4. Django Concepts
5. Best Practices
6. Summary
7. Suggested Next Topic

---

# Important Rule

Do not only describe syntax.

Teach the reasoning behind the code.