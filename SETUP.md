# Connect Claude Desktop to a Live Browser

Three steps. No code.

## 1. Get a Webfuse REST Key

Sign up at [webfuse.com](https://webfuse.com) and create a Space. Go to **Settings → API Keys** and generate a REST key (starts with `rk_`).

Make sure the **Automation** app is enabled on your Space (open a Session, go to Apps tab, install "Automation", then restart the session).

## 2. Configure Claude Desktop

Open Claude Desktop settings → Developer → Edit Config. Paste this:

```json
{
  "mcpServers": {
    "webfuse": {
      "url": "https://session-mcp.webfu.se/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_WEBFUSE_REST_KEY"
      }
    }
  }
}
```

Replace `YOUR_WEBFUSE_REST_KEY` with your key. Restart Claude Desktop.

## 3. Start Browsing

Open your Webfuse Space (the link from your Space settings, e.g. `https://webfu.se/+your-space/`). This opens a browser session.

In Claude Desktop, you'll see 13 new tools available. Ask Claude anything:

- "Take a screenshot of the current page"
- "Click the Sign In button"
- "Fill in the search field with 'Amsterdam hotels' and press Enter"
- "Read the main heading on this page"
- "Scroll down and find the pricing section"
- "Read the accessibility tree and check for missing alt text"

Claude sees the page. Claude controls the page. You watch it happen live in your browser.

## That's It

No server to run. No code to write. No API keys to manage beyond the REST key. Claude Desktop handles the MCP connection directly.

## Troubleshooting

### "No tools available" in Claude Desktop

- Make sure you restarted Claude Desktop after editing the config
- Check the config file is valid JSON (no trailing commas)
- Verify the REST key is correct and starts with `rk_`

### Tools fail with "no active session"

- Open your Webfuse Space URL in a browser to start a session
- The MCP tools only work when there's an active browser session
- If the session timed out, refresh the page to start a new one

### Claude can't find elements on the page

- Ask Claude to take a `see_domSnapshot` first to understand the page structure
- Use CSS selectors for precision: "Click the element matching `button.submit`"
- For elements inside iframes, Claude can use cross-frame selectors (Webfuse-exclusive feature)

### Claude Desktop config file location

| OS | Path |
|----|------|
| macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Windows | `%APPDATA%\Claude\claude_desktop_config.json` |
| Linux | `~/.config/Claude/claude_desktop_config.json` |

## The 13 Tools

| Tool | What it does |
|------|-------------|
| `see_domSnapshot` | Read the page structure (HTML) |
| `see_guiSnapshot` | Take a screenshot |
| `see_accessibilityTree` | Read the accessibility tree |
| `see_textSelection` | Read highlighted text |
| `act_click` | Click an element |
| `act_type` | Type text into fields |
| `act_keyPress` | Press keyboard keys |
| `act_scroll` | Scroll the page |
| `act_mouseMove` | Move the mouse |
| `act_select` | Select dropdown options |
| `act_textSelect` | Highlight text on the page |
| `navigate` | Go to a URL |
| `wait` | Wait for page changes |

## Next Steps

- Try the [walkthrough examples](examples/WALKTHROUGH.md) for demo conversations
- Read the [Session MCP Server docs](https://dev.webfu.se/session-mcp-server/) for advanced usage
- Build a [custom Webfuse extension](https://dev.webfu.se/extensions/) to add domain-specific tools
