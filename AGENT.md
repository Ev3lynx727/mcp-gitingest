# AI Agent Integration Guide (AGENT.md)

This document is designed to guide AI Agents (LLMs/Coding Assistants) in installing and using the `mcp-gitingest` server effectively.

## Role of this Server

`mcp-gitingest` provides you with a single-step capability to ingest entire GitHub repositories. Instead of manually cloning or reading files, you can use the `ingest_repo` tool to get a full, prompt-ready context of any repository.

## Installation Guidance for Agents

If the user asks you to install this server, guide them with these steps:

1. **Prerequisite**: Ensure `uv` is installed.
2. **Setup**: Clone the repo and install dependencies:

   ```bash
   cd /home/ev3lynx/Project/local-mcp-server/mcp-gitingest
   uv build
   pip install dist/*.whl
   ```

3. **Configuration**: Add the server to the IDE's MCP config:

   ```json
   {
     "mcpServers": {
       "gitingest": {
         "command": "mcp-gitingest"
       }
     }
   }
   ```

## Tool Schema: `ingest_repo`

### Description

Ingest a GitHub repository and return a structured text digest optimized for AI agents.

### Parameters (JSON Schema)

| Name | Type | Description | Required | Default |
| --- | --- | --- | --- | --- |
| `url` | `string` | The GitHub repository URL. | **Yes** | - |
| `branch` | `string` | The specific branch to analyze. | No | Default branch |
| `include_patterns` | `array[string]` | Glob patterns for files to INCLUDE. | No | `null` (All) |
| `exclude_patterns` | `array[string]` | Glob patterns for files to EXCLUDE. | No | `null` (Defaults) |
| `max_size` | `integer` | Max file size in bytes to process. | No | `10485760` (10MB) |

### Return Value

A single `string` containing:

1. **Repository Summary**: Repo name, file count, and token estimation.
2. **Directory Structure**: A hierarchical tree view.
3. **File Contents**: Every file's content delimited by `================================================`.

## Agent Interaction Patterns

### 1. Initial Discovery

Use the tool to get the codebase structure and first pass of code.

```python
ingest_repo(url="https://github.com/user/repo")
```

### 2. Focused Analysis

If only interested in a specific language, use `include_patterns`.

```python
ingest_repo(url="...", include_patterns=["*.py", "*.go"])
```

### 3. Ignoring Noise

Exclude heavy directories to save tokens.

```python
ingest_repo(url="...", exclude_patterns=["docs/*", "tests/*", "node_modules/*"])
```

## Error Handling

- **Rate Limiting**: If you receive a "Repository Not Found" error, suggest the user provide a `GITHUB_TOKEN` environment variable.
- **Size Limits**: If a repo is too large, use `include_patterns` to ingest it in smaller, logical chunks.

---
*Optimized for AI Agents - `mcp-gitingest` version 0.1.0*
