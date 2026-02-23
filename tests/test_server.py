import pytest
from unittest.mock import patch, MagicMock
from mcp_gitingest.server import ingest_repo

def test_ingest_repo_success():
    """Test successful ingestion with mocked service."""
    mock_result = "Mocked result"
    
    with patch("mcp_gitingest.server.ingestion_service") as mock_service:
        mock_service.ingest_repository.return_value = mock_result
        
        result = ingest_repo(url="https://github.com/user/repo")
        
        # Verify service was called with correct arguments
        mock_service.ingest_repository.assert_called_once_with(
            url="https://github.com/user/repo",
            branch=None,
            include_patterns=None,
            exclude_patterns=None,
            max_size=None
        )
        
        assert result == mock_result

def test_ingest_repo_error():
    """Test error handling when service fails."""
    with patch("mcp_gitingest.server.ingestion_service") as mock_service:
        mock_service.ingest_repository.side_effect = Exception("Service failed")
        
        result = ingest_repo(url="https://github.com/invalid/repo")
        
        assert "Error: Service failed" in result
