import logging
from typing import List, Optional
from fastmcp import FastMCP
from gitingest import ingest

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-gitingest")

# Create FastMCP server
mcp = FastMCP("GitIngest")

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
    logger.info(f"Ingesting repository: {url} (branch: {branch})")
    try:
        # Construct parameters for gitingest.ingest
        # Note: ingest returns (summary, tree, content)
        summary, tree, content = ingest(
            url,
            branch=branch,
            include_patterns=",".join(include_patterns) if include_patterns else None,
            exclude_patterns=",".join(exclude_patterns) if exclude_patterns else None,
            max_file_size=max_size if max_size else 10 * 1024 * 1024, # Default to 10MB if not specified
        )
        
        # Combine the results into a single formatted string as recommended by gitingest
        full_context = f"{summary}\n\n{tree}\n\n{content}"
        return full_context
    except Exception as e:
        logger.error(f"Error ingesting repository {url}: {str(e)}")
        return f"Error: {str(e)}"

def main():
    mcp.run()

if __name__ == "__main__":
    main()
