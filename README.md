# Claude Desktop + Webfuse MCP

Connect Claude Desktop to a live browser session. No code required.

Claude gets 13 browser tools via MCP: navigate, click, type, scroll, read the DOM, take screenshots, and more. Ask Claude to interact with any website in plain English.

## Quick Start

1. Copy `examples/claude_desktop_config.json` to your Claude Desktop config
2. Replace `YOUR_WEBFUSE_REST_KEY` with your [Webfuse](https://webfuse.com) Space REST key
3. Restart Claude Desktop
4. Open your Webfuse Space in a browser
5. Ask Claude to do things on the page

See [SETUP.md](SETUP.md) for the full guide.

## What Makes This Different

- **No code.** Just a config file.
- **Real browser.** Not headless. You see everything Claude does.
- **Take over anytime.** Claude works in your browser session. Grab the mouse whenever you want.
- **Any website.** The MCP tools work on any page loaded through Webfuse.

## Blog Post

Read the full write-up: [Connect Claude Desktop to a Live Browser](/blog/connect-claude-to-a-live-browser-with-webfuse-mcp)

## Links

- [Webfuse](https://webfuse.com) — The browser actuation platform
- [Session MCP Server Docs](https://dev.webfu.se/session-mcp-server/) — Full tool reference
- [Claude Desktop MCP Guide](https://docs.anthropic.com/en/docs/claude-desktop/mcp) — Anthropic's MCP docs
