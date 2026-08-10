from integrations.obsidian.formatter import ObsidianFormatter


def test_format_runbook():
    content = ObsidianFormatter.format_runbook(
        title="Django Migrations",
        content="Django migrations track changes to the database schema.",
        category="Concepts",
        tags=["django", "migrations"],
    )

    assert "# Django Migrations" in content
    assert "Django migrations track changes" in content
    assert 'type: runbook' in content
    assert 'category: "Concepts"' in content
    assert "- django" in content
    assert "- migrations" in content