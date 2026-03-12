# Claude Desktop + Webfuse MCP

Give Claude Desktop a live browser. No code required.

Claude gets 13 browser tools via [MCP](https://modelcontextprotocol.io): navigate, click, type, scroll, read the DOM, take screenshots, read the accessibility tree, and more. Ask Claude to interact with any website in plain English.

## Quick Start

1. Copy `examples/claude_desktop_config.json` to your Claude Desktop config
2. Replace `YOUR_WEBFUSE_REST_KEY` with your [Webfuse](https://webfuse.com) Space REST key
3. Restart Claude Desktop
4. Open your Webfuse Space in a browser
5. Ask Claude to do things on the page

See [SETUP.md](SETUP.md) for the full guide.

### Verify Your Connection

```bash
pip install httpx
python examples/test_connection.py YOUR_REST_KEY
```

This lists all 13 tools — if it works here, it works in Claude Desktop.

## Also Works With

Config examples are included for multiple MCP clients:

| Client | Config File |
|--------|------------|
| Claude Desktop / Claude Code | [`examples/claude_desktop_config.json`](examples/claude_desktop_config.json) |
| VS Code (Copilot) | [`examples/vscode_mcp.json`](examples/vscode_mcp.json) |
| Cursor | [`examples/cursor_mcp.json`](examples/cursor_mcp.json) |

The endpoint is the same for all clients: `https://session-mcp.webfu.se/mcp`

## What Makes This Different

- **No code.** Just a config file. No server, no Docker, no build step.
- **Real browser.** Not headless. You see everything Claude does in your own browser tab.
- **Take over anytime.** Claude works in your browser session. Grab the mouse whenever you want.
- **Any website.** The MCP tools work on any page loaded through Webfuse — no site cooperation needed.
- **Your auth, your cookies.** The session runs with your login state. Claude doesn't need your passwords.

## The 13 Tools Claude Gets

| Category | Tool | What it does |
|----------|------|-------------|
| **See** | `see_domSnapshot` | Read the page structure (HTML) |
| | `see_guiSnapshot` | Take a screenshot |
| | `see_accessibilityTree` | Read the accessibility tree |
| | `see_textSelection` | Read highlighted text |
| **Act** | `act_click` | Click an element |
| | `act_type` | Type text into fields |
| | `act_keyPress` | Press keyboard keys (Enter, Tab, etc.) |
| | `act_scroll` | Scroll the page |
| | `act_mouseMove` | Move the mouse |
| | `act_select` | Select dropdown options |
| | `act_textSelect` | Highlight text on the page |
| **Navigate** | `navigate` | Go to a URL |
| **Wait** | `wait` | Wait for page changes |

## Guides

- [WALKTHROUGH.md](examples/WALKTHROUGH.md) — Demo conversations to try
- [USE_CASES.md](examples/USE_CASES.md) — Real scenarios by category (research, forms, accessibility)
- [SYSTEM_PROMPTS.md](examples/SYSTEM_PROMPTS.md) — Prompt templates for better results

## Blog Post

Read the full write-up: [Connect Claude to a Live Browser in 2 Minutes (Zero Code)](blog/draft.md)

## Links

- [Webfuse](https://webfuse.com) — The AI browser actuation platform
- [Session MCP Server Docs](https://dev.webfu.se/session-mcp-server/) — Full tool reference
- [Automation API Docs](https://dev.webfu.se/automation-api/) — Underlying API reference
- [Claude Desktop MCP Guide](https://docs.anthropic.com/en/docs/claude-desktop/mcp) — Anthropic's MCP docs

## License

MIT
