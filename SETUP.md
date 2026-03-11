# Connect Claude Desktop to a Live Browser

Three steps. No code.

## 1. Get a Webfuse REST Key

Sign up at [webfuse.com](https://webfuse.com) and create a Space. Copy the REST key from Space settings.

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

Open your Webfuse Space (the link from your Space settings). This opens a browser session.

In Claude Desktop, you'll see 13 new tools. Ask Claude anything:

- "Take a screenshot of the current page"
- "Click the Sign In button"
- "Fill in the search field with 'Amsterdam hotels' and press Enter"
- "Read the main heading on this page"
- "Scroll down and find the pricing section"

Claude sees the page. Claude controls the page. You watch it happen in your browser.

## That's It

No server. No code. No API keys to manage (beyond the REST key). Claude Desktop handles the MCP connection directly.

The 13 tools Claude gets:

| Tool | What it does |
|------|-------------|
| `see_domSnapshot` | Read the page structure |
| `see_guiSnapshot` | Take a screenshot |
| `see_accessibilityTree` | Read the accessibility tree |
| `see_textSelection` | Read highlighted text |
| `act_click` | Click an element |
| `act_type` | Type text |
| `act_keyPress` | Press keyboard keys |
| `act_scroll` | Scroll the page |
| `act_mouseMove` | Move the mouse |
| `act_select` | Select dropdown options |
| `act_textSelect` | Highlight text on the page |
| `navigate` | Go to a URL |
| `wait` | Wait for page changes |
