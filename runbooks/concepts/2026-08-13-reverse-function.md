## What is `reverse()`?

`reverse()` is a Django utility function (from `django.urls`) that takes the **name** of a URL pattern and gives you back the actual **URL path string** for it.

Think of it like a phone contact list: instead of remembering someone's phone number (the raw URL, like `/accounts/login/`), you just look up their name (`"users:login"`) and Django hands you the number.

```python
from django.urls import reverse

url = reverse("main:product")
# url might be "/products/"
```

In your project, [users/views.py](examples/heavyaura-shop/users/views.py#L1-L20) uses it exactly this way:

```python
from django.urls import reverse
from django.http import HttpResponseRedirect

return HttpResponseRedirect(reverse("main:product"))
```

## Why does it exist?

Without `reverse()`, developers would hardcode URLs as plain strings everywhere:

```python
return HttpResponseRedirect("/products/")
```

That's fragile. If you ever change the URL pattern in `urls.py` (say `/products/` becomes `/shop/products/`), you'd have to hunt down and fix every hardcoded string in your entire codebase — views, templates, tests, everywhere.

`reverse()` solves this by letting you refer to URLs **by name**, not by their literal path. Change the path once in `urls.py`, and every `reverse()` call automatically produces the new correct URL.

## How does it work internally?

1. Every URL pattern in `urls.py` can have a `name`:
   ```python
   path("products/", views.product_list, name="product")
   ```
2. When you call `reverse("main:product")`, Django looks through the **URL resolver** (built from all your `urlpatterns`) to find the pattern with that name.
3. It rebuilds the actual path string from that pattern, filling in any required arguments (like an ID).
4. It returns that string, e.g. `"/products/"`.

The `"main:"` prefix in `"main:product"` is a **namespace** — it tells Django "look inside the `main` app's URLs" (set up via `app_name = "main"` in that app's `urls.py`, and `include("main.urls", namespace="main")` in the project's root `urls.py`). Namespaces prevent name collisions when different apps use the same URL name (e.g., two apps both having a view named `"detail"`).

If a URL requires parameters, you pass them in:

```python
reverse("orders:detail", args=[order.id])
# or
reverse("orders:detail", kwargs={"order_id": order.id})
```

## How Django uses it

- **Views**: to build redirect URLs, as in your `login` view above (`HttpResponseRedirect(reverse(...))`).
- **Templates**: the `{% url %}` template tag is the template-language equivalent of `reverse()` — same idea, different syntax.
- **Shortcuts**: `redirect()` actually calls `reverse()` internally when you pass it a URL name instead of a raw URL.

## When to use it

- Anytime you need a URL as a Python string inside a view, form, or other Python code (not a template) — for redirects, building links in JSON responses, sending emails with links, etc.
- Use `reverse_lazy()` instead when the URL needs to be evaluated later, not immediately — commonly needed in class-based views where `urls.py` might not be fully loaded yet (e.g., `success_url = reverse_lazy("main:product")` as a class attribute).

## Common mistakes

- **Hardcoding URLs** instead of using names — defeats the whole purpose and breaks easily.
- **Forgetting the namespace** — calling `reverse("product")` when the actual registered name is `"main:product"` raises a `NoReverseMatch` error.
- **Using `reverse()` at class definition time** — for class attributes in class-based views, `urls.py` may not be loaded yet, causing errors. Use `reverse_lazy()` there instead.
- **Missing required URL arguments** — if the URL pattern needs an `id`, forgetting to pass `args`/`kwargs` also raises `NoReverseMatch`.

## Best practices

- Always give your URL patterns a `name` in `urls.py`, and use app namespaces (`app_name`) for larger projects.
- Prefer `reverse()`/`{% url %}` over hardcoded paths everywhere — in views, templates, and tests.
- Use `reverse_lazy()` in class-based view attributes evaluated at import time (like `success_url`).
