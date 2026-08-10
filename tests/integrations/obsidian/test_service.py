import json

from integrations.obsidian.service import ObsidianService


def create_config(tmp_path):
    vault_path = tmp_path / "vault"
    vault_path.mkdir()

    config_path = tmp_path / "obsidian.json"

    config = {
        "enabled": True,
        "vault_path": str(vault_path),
        "base_folder": "Django",
    }

    config_path.write_text(
        json.dumps(config),
        encoding="utf-8",
    )

    return config_path, vault_path


def test_save_runbook(tmp_path):
    config_path, vault_path = create_config(tmp_path)

    service = ObsidianService(config_path)

    note_path = service.save_runbook(
        title="Django Migrations",
        content=(
            "Django migrations track changes "
            "to the database schema."
        ),
        category="Concepts",
        tags=["django", "migrations"],
    )

    assert note_path.exists()

    expected_path = (
        vault_path
        / "Django"
        / "Concepts"
        / "Django Migrations.md"
    )

    assert note_path == expected_path

    content = note_path.read_text(encoding="utf-8")

    assert "# Django Migrations" in content
    assert "Django migrations track changes" in content
    assert "django" in content
    assert "migrations" in content


def test_save_debugging_runbook(tmp_path):
    config_path, vault_path = create_config(tmp_path)

    service = ObsidianService(config_path)

    note_path = service.save_runbook(
        title="TemplateDoesNotExist",
        content="This error usually means Django cannot find the template.",
        category="Debugging",
        tags=["django", "templates", "debugging"],
    )

    expected_path = (
        vault_path
        / "Django"
        / "Debugging"
        / "TemplateDoesNotExist.md"
    )

    assert note_path == expected_path
    assert note_path.exists()


def test_integration_is_enabled(tmp_path):
    config_path, _ = create_config(tmp_path)

    service = ObsidianService(config_path)

    assert service.enabled is True