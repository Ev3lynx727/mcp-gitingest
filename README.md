# GitIngest MCP Server

*An MCP gateway that turns any Git repository into an AI-ready digest.*

---

## 🏛️ Architectural Vibe

This codebase carries a **quiet, focused energy**. It is small, deliberate, and respects its boundaries.

```
vibe score: 85/100
modules: 2 (115 LOC)
coupling: minimal
ghosts: none
```

### The Modules

| Module | Lines | Role | Stability |
|--------|-------|------|-----------|
| `gitingest_server.py` | ~80 | Core server | I = 0.0 (stable) |
| `tests/test_server.py` | ~35 | Test suite | I = 1.0 (leaf) |

There are no god modules. No circular dependencies. No architectural hauntings.

### Energy Flow

```
tests.test_server ──┐
                    ▼
          gitingest_server (stable utility layer)
```

`gitingest_server` is a **stable utility** — it exports a single tool and imports nothing from the project itself. It stands alone, ready to be consumed. This is ideal.

`tests.test_server` is a **leaf node** — it reaches outward but is not depended upon. In a healthy system, leaves should be numerous and this one is perfectly placed.

---

## 📡 What This Does

`mcp-gitingest` is a specialized Model Context Protocol (MCP) server that wraps the `gitingest` library. It lets AI agents and LLMs fetch, clean, and format entire codebases into structured text with a single tool call.

Instead of juggling git commands and file parsing, an agent simply says: *"Ingest this repository"* — and receives a prompt-ready digest: summary, tree, and content.

---

## ✨ Features

- **Prompt-Ready Digests** — structured output designed for LLM context
- **Selective Ingestion** — glob patterns to include/exclude files
- **Branch Support** — target any branch or tag
- **Token Efficiency** — summary includes token estimates

---

## 🤖 AI Agent Guide

For detailed agent interaction patterns, see **[AGENT.md](./AGENT.md)**.

---

## 🔧 The Tool: `ingest_repo`

The sole exposure point of this server.

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `url` | `string` | **Required**. GitHub/Git repository URL. |
| `branch` | `string` | Optional. Branch to analyze. |
| `include_patterns` | `list[string]` | Optional. Glob patterns to include (e.g. `["*.py", "*.md"]`). |
| `exclude_patterns` | `list[string]` | Optional. Glob patterns to exclude. |
| `max_size` | `number` | Optional. Max file size in bytes (default: 10MB). |

---

## 🧱 Architecture

Built with **FastMCP** (Python) for robust MCP communication.

```mermaid
graph LR
    IDE[AI Agentic IDE] -- Tool Call (ingest_repo) --> MCP[mcp-gitingest Server]
    MCP -- Python API --> GI[gitingest Library]
    GI -- Clone/Read --> Git[GitHub/Git Repository]
    Git -- Raw Files --> GI
    GI -- Structured Digest --> MCP
    MCP -- Tool Result --> IDE
```

**Layers:**
1. **Transport:** FastMCP (MCP protocol)
2. **Server:** `gitingest_server.py` (tool orchestration)
3. **Core:** `gitingest` library (ingestion logic)
4. **Source:** Git repository (input)

---

## 📦 Packaging

This project is structured as a Python package with `hatchling` build backend.

```toml
[project]
name = "mcp-gitingest"
version = "0.1.0"
dependencies = ["fastmcp>=3.0.2", "gitingest>=0.3.1"]

[project.scripts]
mcp-gitingest = "gitingest_server:main"
```

Entry point: `mcp-gitingest` runs the server directly.

---

## 🚀 Installation & Setup

### Prerequisites

- [uv](https://github.com/astral-sh/uv) installed

### From Source

```bash
cd /home/ev3lynx/Project/local-mcp-server/mcp-gitingest
uv sync
```

Run the server:

```bash
uv run python gitingest_server.py
```

Or use the installed entry point (after `uv pip install -e .`):

```bash
mcp-gitingest
```

### Wheel Install

```bash
pip install dist/mcp_gitingest-0.1.0-py3-none-any.whl
mcp-gitingest
```

---

## 🖥️ IDE Integration

Add to your MCP configuration (Claude Desktop, Cursor, etc.):

```json
{
  "mcpServers": {
    "gitingest": {
      "command": "uv",
      "args": [
        "--directory",
        "/home/ev3lynx/Project/local-mcp-server/mcp-gitingest",
        "run",
        "python",
        "gitingest_server.py"
      ]
    }
  }
}
```

Restart your IDE. The `ingest_repo` tool will appear.

---

## 🛠️ Development

### Run in dev mode

```bash
uv run python gitingest_server.py
```

### Test with MCP Inspector

```bash
npx @modelcontextprotocol/inspector uv run python gitingest_server.py
```

### Run unit tests

```bash
uv run pytest tests/
```

---

## 🔮 Architectural Roadmap

The current single-file design is **intentionally minimal**. It will remain this way until complexity grows.

### When to Split

If `gitingest_server.py` exceeds ~200 lines or you add a second tool, refactor into:

```
mcp_gitingest/
├── server.py      # FastMCP setup, tool registration
├── ingest.py      # Core ingestion logic
├── models.py      # Pydantic schemas (if needed)
└── exceptions.py  # Custom error types
```

**Trigger conditions:**
- More than one tool exposed
- Business logic beyond simple parameter mapping
- Need for internal caching or state

Until then: keep it small. Keep it quiet.

---

## 📊 Health Metrics

| Metric | Current | Target |
|--------|---------|--------|
| Vibe Score | 85/100 | >80 |
| Coupling | Minimal | Minimal |
| Test Coverage | 100% | >90% |
| Cyclomatic Complexity | ~4 | <10 |
| Lines per Function | ~30 | <50 |

All green. No action required.

---

## 📄 License

(Add your license here if applicable)

---

*Maintained with ghostclaw awareness.*
