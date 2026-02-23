import pytest
from unittest.mock import patch
from mcp_gitingest.services.ingestion_service import IngestionService

def test_service_ingest_success():
    service = IngestionService()
    mock_data = ("Summary", "Tree", "Content")

    with patch("mcp_gitingest.services.ingestion_service.ingest") as mock_ingest:
        mock_ingest.return_value = mock_data

        result = service.ingest_repository(url="https://github.com/user/repo")

        mock_ingest.assert_called_once()
        assert "Summary" in result
        assert "Tree" in result
        assert "Content" in result

def test_service_ingest_custom_params():
    service = IngestionService(default_max_size=1000)
    mock_data = ("S", "T", "C")

    with patch("mcp_gitingest.services.ingestion_service.ingest") as mock_ingest:
        mock_ingest.return_value = mock_data

        service.ingest_repository(
            url="https://github.com/user/repo",
            max_size=500,
            include_patterns=["*.py"]
        )

        mock_ingest.assert_called_once_with(
            "https://github.com/user/repo",
            branch=None,
            include_patterns="*.py",
            exclude_patterns=None,
            max_file_size=500
        )
