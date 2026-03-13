---
title: "Connect Claude to a Live Browser in 2 Minutes (Zero Code)"
description: "Add one config file to Claude Desktop and it can see, click, scroll, and read any website through Webfuse MCP. No server, no code, no headless browser."
shortTitle: "Claude Desktop + Webfuse MCP"
created: 2026-03-11
category: ai-agents
authorId: nicholas-piel
tags: ["claude", "anthropic", "mcp", "browser-automation", "webfuse", "claude-desktop", "claude-code", "cursor", "vscode", "zero-code"]
featurePriority: 0
relatedLinks:
  - text: "OpenAI Agent + Webfuse MCP"
    href: "/blog/build-an-ai-agent-that-controls-a-live-browser"
    description: "Build a custom agent with the OpenAI Agents SDK and Webfuse MCP."
  - text: "Vercel AI SDK + Webfuse MCP"
    href: "/blog/build-a-browsing-assistant-with-vercel-ai-sdk-and-webfuse"
    description: "TypeScript version for Next.js apps."
  - text: "LangChain + Webfuse MCP"
    href: "/blog/how-to-connect-langchain-to-a-live-browser-with-webfuse-mcp"
    description: "Python tutorial with LangGraph and human-in-the-loop."
  - text: "LiveKit Voice Agent + Webfuse MCP"
    href: "/blog/build-a-voice-agent-that-browses-with-livekit-and-webfuse"
    description: "Voice-controlled browser agent with LiveKit."
  - text: "Session MCP Server Docs"
    href: "https://dev.webfu.se/session-mcp-server/"
    description: "Full reference for the 13 browser tools."
  - text: "GitHub Repository"
    href: "https://github.com/hummer-netizen/extension-claude-mcp"
    description: "Config file and setup guide."
faqs:
  - question: "Do I need to run a server?"
    answer: "No. Claude Desktop connects directly to the Webfuse MCP endpoint. No server, no proxy, no infrastructure."
  - question: "Which Claude models work?"
    answer: "Any model in Claude Desktop that supports tool use. Claude Opus and Sonnet both work."
  - question: "Can I use this with Claude API instead of Desktop?"
    answer: "Yes. Use the MCP endpoint with any Anthropic SDK that supports MCP tools. The Desktop setup is just the simplest way to get started."
  - question: "What about sensitive pages?"
    answer: "The Webfuse session runs in your browser with your auth. Claude only sees what you see. You control which pages to visit."
  - question: "Does this work with Cursor and VS Code?"
    answer: "Yes. The same MCP endpoint works with any MCP client. Config examples for Claude Desktop, Cursor, and VS Code Copilot are all in the GitHub repo."
---

What if Claude could see your screen and control your browser?

Not a screenshot you paste in. Not a URL you copy. The actual live page. Clicking buttons. Filling forms. Reading content.

One config file. That's all it takes.

<TldrBox title="TL;DR">

**Add a Webfuse MCP server to Claude Desktop. Claude gets 13 browser tools.** Ask it to do anything on any website. No code. No server. Just a JSON config and a Webfuse Space.

Config: [claude_desktop_config.json](https://github.com/hummer-netizen/extension-claude-mcp/blob/main/examples/claude_desktop_config.json)

</TldrBox>

## The Setup

Open Claude Desktop settings. Go to Developer. Edit your MCP config. Add this:

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

Replace the key. Restart Claude Desktop. Done.

Claude now has 13 browser tools. Navigate, click, type, scroll, read the DOM, take screenshots, highlight text, press keys. The full set.

## What You Can Do

Open your Webfuse Space in a browser. Then just talk to Claude:

**"What's on this page?"**
Claude takes a DOM snapshot, reads the structure, and tells you.

**"Click the login button and fill in my email"**
Claude finds the button, clicks it, locates the email field, types your address.

**"Compare the prices in this table"**
Claude reads the table structure, extracts the numbers, and gives you a summary.

**"Scroll down to the FAQ section and read the first question"**
Claude scrolls, finds the section, reads the content.

You watch it happen in your browser. If Claude goes the wrong way, just tell it. Or grab the mouse and do it yourself. Claude works in your session, not in some invisible headless browser.

## Why This Matters

Every other "Claude + browser" setup needs infrastructure. A server running Puppeteer. A headless Chrome instance. Docker containers. API bridges.

This needs a config file.

Claude Desktop already supports MCP. Webfuse already exposes browser sessions as MCP tools. Put them together and you skip everything in between.

No server to maintain. No browser to provision. No credentials to sync. The session runs in YOUR browser with YOUR cookies and YOUR login state.

::ArticleSignupCta
---
heading: "Give Claude a browser"
subtitle: "Webfuse connects Claude to live web sessions via MCP. No headless browsers, no infrastructure. Try it free."
---
::

## The Co-Pilot Angle

This isn't just automation. It's collaboration.

Claude can do the tedious research: open five tabs, read through documentation, compare pricing pages, extract data from tables. You watch it work. When it finds something interesting, you take over and dive deeper.

Think of it as pair browsing. Claude handles the mechanical parts. You make the decisions.

A few things people are building with this:

- **Research workflows.** "Read these three competitor pages and summarize the differences."
- **Form filling.** "Fill in this application form with the info from my resume."
- **Data extraction.** "Go through these search results and find companies with more than 100 employees."
- **Learning.** "Walk me through the settings page and explain each option."

The browser stays yours. Claude is just really good at reading and clicking.

## Going Further

The config file is the starting point. From here:

- **Claude API.** Use the same MCP endpoint with the Anthropic SDK for programmatic access.
- **Custom tools.** Build a Webfuse extension that adds domain-specific tools on top of the 13 built-in ones.
- **Team workflows.** Share a Space link. Multiple people (and Claude) can collaborate in the same session.

Or just keep chatting with Claude Desktop. Sometimes the simplest setup is the best one.

## Source

Everything is on GitHub: [hummer-netizen/extension-claude-mcp](https://github.com/hummer-netizen/extension-claude-mcp)

There's not much to it. That's the point.

## Works with Claude Code Too

Same config, different client. If you use [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (Anthropic's terminal-based coding agent), add the same MCP server:

```bash
claude mcp add webfuse \
  --transport http \
  --url https://session-mcp.webfu.se/mcp \
  --header "Authorization: Bearer YOUR_WEBFUSE_REST_KEY"
```

Now Claude Code can browse documentation, check deployed pages, and interact with web apps — all from your terminal. Useful for debugging: "Navigate to localhost:3000 and check if the login form works."

## Works with Cursor

If you're building web apps, Cursor + Webfuse is a natural fit. Your AI coding assistant can check its own work.

Add this to `.cursor/mcp.json` in your project root:

```json
{
  "mcpServers": {
    "webfuse-session": {
      "type": "http",
      "url": "https://session-mcp.webfu.se/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_WEBFUSE_REST_KEY"
      }
    }
  }
}
```

Now Cursor's agent can navigate to your deployed app, check if the UI renders correctly, fill in forms to test validation, and read error messages from the actual page. Debug loops get shorter when the AI can see the result.

## Works with VS Code Copilot

GitHub Copilot in VS Code also supports MCP. Create `.vscode/mcp.json`:

```json
{
  "servers": {
    "webfuse-session": {
      "type": "http",
      "url": "https://session-mcp.webfu.se/mcp",
      "headers": {
        "Authorization": "${input:webfuse_api_key}"
      }
    }
  },
  "inputs": [
    {
      "type": "promptString",
      "id": "webfuse_api_key",
      "description": "Webfuse Space REST API Key",
      "password": true
    }
  ]
}
```

VS Code prompts for the key on first use and stores it securely. Same 13 tools, same live browser.

## How It Works

The magic is that there's no magic.

```
You ──────────────── Webfuse Session ──── Any Website
                          │
Claude ── MCP endpoint ───┘
```

Your browser runs through a Webfuse proxy session. That session exposes an MCP endpoint with 13 tools. Claude Desktop (or Cursor, or VS Code, or Claude Code) connects to that endpoint.

When Claude calls `act_click`, the click happens in your actual browser tab. When it calls `see_domSnapshot`, it reads the live DOM. There's no separate browser instance, no screen recording, no pixel matching. Just structured access to the page you're looking at.

The REST key scopes Claude to your Space. Multiple sessions can run simultaneously. You stay in control of what pages Claude can see.

## Use Cases

People are using this for research workflows, data extraction, accessibility audits, and form filling. See the full list: [examples/USE_CASES.md](https://github.com/hummer-netizen/extension-claude-mcp/blob/main/examples/USE_CASES.md)
