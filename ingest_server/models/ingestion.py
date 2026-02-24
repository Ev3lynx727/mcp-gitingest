from typing import List, Optional
from pydantic import BaseModel, Field

class IngestRequest(BaseModel):
    url: str = Field(..., description="The URL of the GitHub repository")
    branch: Optional[str] = Field(None, description="The specific branch to analyze")
    include_patterns: Optional[List[str]] = Field(None, description="Patterns to include")
    exclude_patterns: Optional[List[str]] = Field(None, description="Patterns to exclude")
    max_size: Optional[int] = Field(None, description="Maximum file size in bytes")
