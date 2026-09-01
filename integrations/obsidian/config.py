from pathlib import Path
from .exceptions import ObsidianConfigError, VaultNotFoundError
import json


class ObsidianConfig:
    """Loads and validates Obsidian integration configuration."""

    def __init__(self, config_path: str | Path):
        self.config_path = Path(config_path)

        self.enabled = False
        self.vault_path: Path | None = None
        self.base_folder = "Django"

    def load(self) -> "ObsidianConfig":
        """Load configuration from the JSON file."""

        if not self.config_path.exists():
            raise ObsidianConfigError(
                f"Obsidian configuration file not found: "
                f"{self.config_path}"
            )

        try:
            with self.config_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError as exc:
            raise ObsidianConfigError("Obsidian configuration contains invalid JSON.") from exc

        self.enabled = data.get("enabled", False)

        vault_path = data.get("vault_path", "").strip()

        if vault_path:
            self.vault_path = Path(vault_path)

        self.base_folder = data.get("base_folder", "Django").strip()

        if "base_folder" in data:
            # An explicit empty string means "save directly in the vault
            # root", so it is respected as-is instead of falling back to
            # the "Django" default below.
            self.base_folder = data["base_folder"].strip()
        else:
            self.base_folder = "Django"

        if self.enabled:
            self.validate_vault()

        return self

    def validate_vault(self) -> None:
        """Validate that the configured vault exists."""

        if self.vault_path is None:
            raise ObsidianConfigError("Obsidian vault_path is not configured.")

        if not self.vault_path.exists():
            raise VaultNotFoundError(f"Obsidian vault was not found: {self.vault_path}")

        if not self.vault_path.is_dir():
            raise ObsidianConfigError(
                f"Obsidian vault path is not a directory: "
                f"{self.vault_path}"
            )