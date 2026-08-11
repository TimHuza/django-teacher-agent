from pathlib import Path
import asyncio
import sys
from typing import List, Optional

from mcp.server import MCPServer

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from integrations.obsidian.service import ObsidianService

CONFIG_PATH = PROJECT_ROOT / "config" / "obsidian.json"

# 1. Initialize the High-Level MCPServer
mcp = MCPServer(
    "django-teacher-obsidian",
    version="1.0.0",
)

# 2. Define the tool using the high-level @mcp.tool() decorator.
# The docstrings and type hints auto-generate your tool's inputSchema.
@mcp.tool()
def save_runbook_to_obsidian(
    title: str,
    content: str,
    category: str = "Concepts",
    tags: Optional[List[str]] = None,
) -> str:
    """
    Save a Django Teacher Agent runbook as a Markdown file in the configured Obsidian vault.

    Args:
        title: Title of the runbook.
        content: Complete Markdown content of the runbook.
        category: Runbook category such as Concepts, Debugging, Security, or Architecture.
        tags: Optional Obsidian tags.
    """
    if tags is None:
        tags = []
        
    try:
        service = ObsidianService(CONFIG_PATH)
        note_path = service.save_runbook(
            title=title,
            content=content,
            category=category,
            tags=tags,
        )
        return f"Runbook successfully saved to Obsidian: {note_path}"
        
    except Exception as exc:
        # High-level framework automatically converts strings or raised errors into CallToolResult formats
        raise RuntimeError(f"Failed to save runbook to Obsidian: {exc}")


if __name__ == "__main__":
    # 3. High-level runtime uses mcp.run() directly with built-in stdio allocation
    mcp.run()