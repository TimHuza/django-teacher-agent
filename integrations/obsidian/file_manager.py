from pathlib import Path

from .exceptions import (
    NoteAlreadyExistsError,
    NoteCreationError,
)


class ObsidianFileManager:
    """Handles filesystem operations inside an Obsidian vault."""

    def __init__(self, vault_path: Path):
        self.vault_path = vault_path.resolve()

    def create_directory(self, relative_path: str | Path) -> Path:
        """Create a directory inside the Obsidian vault."""

        directory = self._safe_path(relative_path)

        directory.mkdir(parents=True, exist_ok=True)

        return directory

    def create_note(
        self,
        relative_path: str | Path,
        content: str,
    ) -> Path:
        """
        Create a Markdown note inside the Obsidian vault.

        Raises:
            NoteAlreadyExistsError:
                If the note already exists.
            NoteCreationError:
                If the note cannot be created.
        """

        note_path = self._safe_path(relative_path)

        if note_path.exists():
            raise NoteAlreadyExistsError(
                f"Note already exists: {note_path}"
            )

        try:
            note_path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            note_path.write_text(
                content,
                encoding="utf-8",
            )

        except OSError as exc:
            raise NoteCreationError(
                f"Could not create note: {note_path}"
            ) from exc

        return note_path

    def note_exists(
        self,
        relative_path: str | Path,
    ) -> bool:
        """Check whether a note exists."""

        note_path = self._safe_path(relative_path)

        return note_path.exists()

    def _safe_path(
        self,
        relative_path: str | Path,
    ) -> Path:
        """
        Resolve a path and make sure it stays inside the vault.
        """

        target = (self.vault_path / relative_path).resolve()

        try:
            target.relative_to(self.vault_path)
        except ValueError as exc:
            raise ValueError(
                "Path is outside of the configured Obsidian vault."
            ) from exc

        return target