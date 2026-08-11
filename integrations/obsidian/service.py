from .config import ObsidianConfig
from .file_manager import ObsidianFileManager
from .formatter import ObsidianFormatter
from pathlib import Path


class ObsidianService:
    """High-level service for saving notes to Obsidian."""

    def __init__(self, config_path: str | Path):
        self.config = ObsidianConfig(config_path).load()

        self.file_manager: ObsidianFileManager | None = None

        if self.config.enabled and self.config.vault_path:
            self.file_manager = ObsidianFileManager(
                self.config.vault_path
            )

    @property
    def enabled(self) -> bool:
        """Return whether Obsidian integration is enabled."""

        return self.config.enabled

    def save_runbook(
        self,
        title: str,
        content: str,
        category: str = "Concepts",
        tags: list[str] | None = None,
    ) -> Path:
        """
        Save a runbook to the configured Obsidian vault.
        """

        if not self.enabled:
            raise RuntimeError(
                "Obsidian integration is disabled."
            )

        if self.file_manager is None:
            raise RuntimeError(
                "Obsidian file manager is not initialized."
            )

        safe_title = self._sanitize_filename(title)

        category_folder = self._sanitize_folder_name(category)

        relative_path = (
            Path(self.config.base_folder)
            / category_folder
            / f"{safe_title}.md"
        )

        markdown = ObsidianFormatter.format_runbook(
            title=title,
            content=content,
            category=category,
            tags=tags,
        )

        return self.file_manager.create_note(
            relative_path=relative_path,
            content=markdown,
        )

    @staticmethod
    def _sanitize_filename(filename: str) -> str:
        """Make a string safe to use as a Windows filename."""

        invalid_characters = '<>:"/\\|?*'

        for character in invalid_characters:
            filename = filename.replace(character, "")

        filename = filename.strip().rstrip(".")

        if not filename:
            filename = "Untitled Runbook"

        return filename

    @staticmethod
    def _sanitize_folder_name(folder_name: str) -> str:
        """Make a folder name safe for the filesystem."""

        invalid_characters = '<>:"/\\|?*'

        for character in invalid_characters:
            folder_name = folder_name.replace(character, "")

        folder_name = folder_name.strip().rstrip(".")

        if not folder_name:
            folder_name = "Other"

        return folder_name