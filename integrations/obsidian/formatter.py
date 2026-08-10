from datetime import date


class ObsidianFormatter:
    """Formats runbooks as Obsidian-compatible Markdown."""

    @staticmethod
    def format_runbook(
        title: str,
        content: str,
        category: str,
        tags: list[str] | None = None,
    ) -> str:
        """
        Convert a runbook into Markdown with YAML frontmatter.
        """

        tags = tags or []

        tag_lines = "\n".join(f"  - {tag}" for tag in tags)

        if not tag_lines:
            tag_lines = "  - django"

        return f"""---
title: "{title}"
type: runbook
category: "{category}"
created: {date.today().isoformat()}
tags:
{tag_lines}
---

# {title}

{content.strip()}
"""