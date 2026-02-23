import pytest
from unittest.mock import patch, MagicMock
from gitingest_server import ingest_repo

def test_ingest_repo_success():
    """Test successful ingestion with mocked gitingest."""
    mock_summary = "Repository: user/repo\nFiles analyzed: 5\nEstimated tokens: 100"
    mock_tree = "Directory structure:\n└── repo/\n    ├── main.py\n    └── README.md"
    mock_content = "FILE: main.py\nprint('hello')\n\nFILE: README.md\n# Title"
    
    with patch("gitingest_server.ingest") as mock_ingest:
        mock_ingest.return_value = (mock_summary, mock_tree, mock_content)
        
        result = ingest_repo(url="https://github.com/user/repo")
        
        # Verify ingest was called with correct default arguments
        mock_ingest.assert_called_once_with(
            "https://github.com/user/repo",
            branch=None,
            include_patterns=None,
            exclude_patterns=None,
            max_file_size=10 * 1024 * 1024
        )
        
        # Verify formatted output
        assert "Repository: user/repo" in result
        assert "Directory structure:" in result
        assert "FILE: main.py" in result

def test_ingest_repo_with_params():
    """Test ingestion with custom parameters."""
    mock_data = ("Summary", "Tree", "Content")
    
    with patch("gitingest_server.ingest") as mock_ingest:
        mock_ingest.return_value = mock_data
        
        ingest_repo(
            url="https://github.com/user/repo",
            branch="dev",
            include_patterns=["*.py"],
            exclude_patterns=["tests/*"],
            max_size=5000
        )
        
        # Verify ingest was called with custom arguments
        mock_ingest.assert_called_once_with(
            "https://github.com/user/repo",
            branch="dev",
            include_patterns="*.py",
            exclude_patterns="tests/*",
            max_file_size=5000
        )

def test_ingest_repo_error():
    """Test error handling when gitingest fails."""
    with patch("gitingest_server.ingest") as mock_ingest:
        mock_ingest.side_effect = Exception("Cloning failed")
        
        result = ingest_repo(url="https://github.com/invalid/repo")
        
        assert "Error: Cloning failed" in result
