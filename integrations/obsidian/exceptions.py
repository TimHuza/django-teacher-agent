class ObsidianError(Exception):
    """Base exception for Obsidian integration errors."""


class ObsidianConfigError(ObsidianError):
    """Raised when the Obsidian configuration is invalid."""


class VaultNotFoundError(ObsidianError):
    """Raised when the configured Obsidian vault cannot be found."""


class NoteAlreadyExistsError(ObsidianError):
    """Raised when attempting to create a note that already exists."""


class NoteCreationError(ObsidianError):
    """Raised when a note cannot be created."""