import logging
from typing import List, Optional, Tuple
from gitingest import ingest

logger = logging.getLogger("mcp-gitingest.services.ingestion")

class IngestionService:
    """
    Service responsible for interacting with the gitingest library.
    """

    def __init__(self, default_max_size: int = 10 * 1024 * 1024):
        self.default_max_size = default_max_size

    def ingest_repository(
        self,
        url: str,
        branch: Optional[str] = None,
        include_patterns: Optional[List[str]] = None,
        exclude_patterns: Optional[List[str]] = None,
        max_size: Optional[int] = None,
    ) -> str:
        """
        Ingest a repository and return a formatted digest.
        """
        logger.info(f"Ingesting repository: {url} (branch: {branch})")

        # Prepare patterns
        include_str = ",".join(include_patterns) if include_patterns else None
        exclude_str = ",".join(exclude_patterns) if exclude_patterns else None
        limit_size = max_size if max_size is not None else self.default_max_size

        try:
            summary, tree, content = ingest(
                url,
                branch=branch,
                include_patterns=include_str,
                exclude_patterns=exclude_str,
                max_file_size=limit_size,
            )
            return self._format_response(summary, tree, content)
        except Exception as e:
            logger.error(f"Failed to ingest repository {url}: {str(e)}")
            raise

    def _format_response(self, summary: str, tree: str, content: str) -> str:
        """
        Formats the gitingest output into a single string.
        """
        return f"{summary}\n\n{tree}\n\n{content}"
