## What is ORM?

### 1. Big Picture

When you build a Django app, you need to store data somewhere — usually in a database. But databases speak their own language: **SQL** (Structured Query Language). Python doesn't understand SQL natively, and writing raw SQL everywhere in a Python project is messy and error-prone.

**ORM (Object-Relational Mapper)** is the tool that solves this problem. It lets you talk to the database using **Python code** instead of SQL.

### 2. Simple Definition

**ORM = Object-Relational Mapping.**

It's a technique (and Django has one built in) that maps:

- A **Python class** → a **database table**
- A **class attribute** (field) → a **table column**
- An **instance of that class** (an object) → a **row** in that table

### 3. Real-World Analogy

Imagine a filing cabinet (the database) full of paper forms written in a language you don't speak. An ORM is like a translator who stands next to the cabinet. Instead of learning that language, you just say in plain English: *"Give me the form for student #5"*, and the translator fetches it, converts it into a document you understand (a Python object), and hands it to you.

### 4. Django Example

```python
# models.py
class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField()
```

This Python class becomes a database table called `Student` with two columns: `name` and `grade`.

To get all students with grade 7, instead of writing SQL like:

```sql
SELECT * FROM student WHERE grade = 7;
```

You write Python:

```python
Student.objects.filter(grade=7)
```

Django's ORM converts that Python code into SQL behind the scenes, sends it to the database, and returns the results as Python `Student` objects.

### 5. Code Breakdown

- `Student` — a Django **model**, which represents the table.
- `models.CharField`, `models.IntegerField` — Django **field types**, which represent columns and their data types.
- `Student.objects` — the **manager**, your entry point for querying the table.
- `.filter(grade=7)` — a **QuerySet** method that builds and runs the equivalent SQL query.

### 6. Django Connection

The ORM lives at the **Model** layer in Django's MVT (Model-View-Template) architecture. Views ask models for data, models use the ORM to talk to the database, and the results flow back up to your templates.

### 7. Why This Approach Is Used

- You write **Python everywhere**, not a mix of Python and SQL.
- Django handles differences between database engines (SQLite, PostgreSQL, MySQL) for you — same Python code works on any of them.
- It helps prevent **SQL injection** attacks, because the ORM safely builds queries instead of you concatenating raw strings.
- Changes to your models can be tracked and applied to the database through **migrations**.

### 8. Best Practices

- Prefer ORM queries (`filter`, `get`, `exclude`, etc.) over raw SQL whenever possible — it's safer and more maintainable.
- Only drop to raw SQL for complex queries the ORM genuinely can't express well.
- Always run `makemigrations` and `migrate` after changing a model, so the database schema stays in sync with your Python code.

### 9. Common Mistakes (Beginner Watch-Outs)

- Forgetting that `Student.objects.filter(...)` returns a **QuerySet** (like a list of objects), not a single object — use `.get()` when you expect exactly one result.
- Editing the database directly and forgetting to update the model (or vice versa) — this causes mismatches Django won't know about.

---

Does this make sense so far? A great next concept to explore would be **QuerySets** in more depth, or **Migrations** — since those are the two ideas ORM connects to most closely. Want to dive into either one?
