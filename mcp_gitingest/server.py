import logging
from typing import List, Optional
from fastmcp import FastMCP
from mcp_gitingest.services.ingestion_service import IngestionService

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-gitingest")

# Initialize server and services
mcp = FastMCP("GitIngest")
ingestion_service = IngestionService()

@mcp.tool()
def ingest_repo(
    url: str,
    branch: Optional[str] = None,
    include_patterns: Optional[List[str]] = None,
    exclude_patterns: Optional[List[str]] = None,
    max_size: Optional[int] = None,
) -> str:
    """
    Ingest a GitHub repository and return a structured text digest optimized for AI agents.

    Args:
        url: The URL of the GitHub repository (e.g., https://github.com/user/repo).
        branch: The specific branch to analyze (optional).
        include_patterns: A list of patterns to include (e.g., ["*.py", "*.md"]).
        exclude_patterns: A list of patterns to exclude (e.g., ["node_modules/*", "*.log"]).
        max_size: Maximum file size in bytes to process (optional).
    """
    try:
        return ingestion_service.ingest_repository(
            url=url,
            branch=branch,
            include_patterns=include_patterns,
            exclude_patterns=exclude_patterns,
            max_size=max_size
        )
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    mcp.run()

if __name__ == "__main__":
    main()
