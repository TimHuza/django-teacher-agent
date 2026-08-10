import pytest

from integrations.obsidian.file_manager import ObsidianFileManager
from integrations.obsidian.exceptions import (
    NoteAlreadyExistsError,
)


def test_create_note(tmp_path):
    manager = ObsidianFileManager(tmp_path)

    note_path = manager.create_note(
        "Django/Concepts/Test Note.md",
        "# Test Note\n\nHello from Obsidian.",
    )

    assert note_path.exists()
    assert note_path.read_text(encoding="utf-8") == (
        "# Test Note\n\nHello from Obsidian."
    )


def test_create_note_creates_directories(tmp_path):
    manager = ObsidianFileManager(tmp_path)

    note_path = manager.create_note(
        "Django/Debugging/Test Error.md",
        "# Test Error",
    )

    assert note_path.exists()
    assert note_path.parent.exists()


def test_create_note_does_not_overwrite_existing_note(tmp_path):
    manager = ObsidianFileManager(tmp_path)

    manager.create_note(
        "Django/Concepts/Test Note.md",
        "# Original",
    )

    with pytest.raises(NoteAlreadyExistsError):
        manager.create_note(
            "Django/Concepts/Test Note.md",
            "# New Content",
        )


def test_path_cannot_escape_vault(tmp_path):
    manager = ObsidianFileManager(tmp_path)

    with pytest.raises(ValueError):
        manager.create_note(
            "../outside.md",
            "This should not be allowed.",
        )