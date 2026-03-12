# System Prompt Tips for Claude Desktop + Webfuse

Claude Desktop doesn't expose a system prompt field, but you can influence behavior through your first message or a Claude Project. Here are tested prompts that work well.

## Starter Prompt (paste as your first message)

```
I have Webfuse MCP tools connected. When I ask you to interact with web pages:

1. Always start with see_domSnapshot using a targeted CSS selector (not 'body')
2. Good selectors: '.infobox', 'main', 'h1', '#content', 'table'
3. When clicking, use CSS selectors from the DOM snapshot
4. Keep responses concise — summarize what you see, don't dump raw HTML
5. If a page is large, read sections one at a time

My Webfuse session is open. Let's start.
```

## For Research Tasks

```
You have browser tools via Webfuse MCP. I want you to research topics by:
1. Navigating to relevant pages (Wikipedia is a good starting point)
2. Reading specific sections with targeted CSS selectors
3. Extracting key data points
4. Presenting findings in a structured format

When reading pages, use selectors like '.infobox' or '.mw-parser-output > p:first-of-type' 
to avoid huge DOM dumps. Compare data across pages when asked.
```

## For Form Filling

```
You have browser tools via Webfuse MCP. I'll ask you to fill in web forms.
Steps:
1. Use see_domSnapshot to find all form fields
2. Confirm what fields exist before filling
3. Use act_type for text fields, act_click for checkboxes/buttons, act_select for dropdowns
4. After filling, take a see_guiSnapshot so I can verify before submitting
```

## For Accessibility Audits

```
You have browser tools via Webfuse MCP. Run an accessibility check:
1. Use see_accessibilityTree to read the page's semantic structure
2. Check for: missing alt text, heading hierarchy issues, form labels, ARIA attributes
3. Report findings as a prioritized list (critical → warning → info)
4. Suggest specific fixes for each issue
```

## Key Tips

- **Session ID:** Claude will ask for it. Find it in your Webfuse session URL — the path segment after the hostname (e.g. `sGpUNaFXihCSxCUfb3zezgaCw`).
- **Targeted selectors beat broad ones.** `.infobox` → 2KB. `body` → 500KB. Claude works better with focused context.
- **Chain commands.** "Navigate to X, read the infobox, then go to Y and compare" works in one message.
- **The 3-minute limit.** MCP connections close after 3 minutes of inactivity. If Claude's tools stop working, just send a new message — it reconnects automatically.
- **Large pages overflow context.** If Claude struggles, ask it to read smaller sections: "Read just the first paragraph" or "Read the table with class 'pricing'."
