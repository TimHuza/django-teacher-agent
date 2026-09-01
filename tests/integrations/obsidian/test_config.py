import json

from integrations.obsidian.config import ObsidianConfig


def write_config(tmp_path, data):
    config_path = tmp_path / "obsidian.json"
    config_path.write_text(json.dumps(data), encoding="utf-8")
    return config_path


def test_default_base_folder_is_django_when_not_configured(tmp_path):
    vault_path = tmp_path / "vault"
    vault_path.mkdir()

    config_path = write_config(
        tmp_path,
        {"enabled": True, "vault_path": str(vault_path)},
    )

    config = ObsidianConfig(config_path).load()

    assert config.base_folder == "Django"


def test_empty_base_folder_saves_directly_in_vault_root(tmp_path):
    vault_path = tmp_path / "vault"
    vault_path.mkdir()

    config_path = write_config(
        tmp_path,
        {
            "enabled": True,
            "vault_path": str(vault_path),
            "base_folder": "",
        },
    )

    config = ObsidianConfig(config_path).load()

    assert config.base_folder == ""


def test_custom_base_folder_is_respected(tmp_path):
    vault_path = tmp_path / "vault"
    vault_path.mkdir()

    config_path = write_config(
        tmp_path,
        {
            "enabled": True,
            "vault_path": str(vault_path),
            "base_folder": "Notes",
        },
    )

    config = ObsidianConfig(config_path).load()

    assert config.base_folder == "Notes"