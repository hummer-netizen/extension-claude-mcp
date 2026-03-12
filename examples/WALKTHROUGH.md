# Demo Walkthrough

Try these conversations in Claude Desktop after connecting Webfuse MCP.

## 1. Screenshot and Explore

Open your Webfuse Space (e.g. `https://webfu.se/+your-space/`) and navigate to any website.

**You:** Take a screenshot of the current page.

**You:** What's the main heading on this page? Read the DOM to find out.

**You:** Scroll down and take another screenshot. What changed?

## 2. Search and Extract

Navigate to a search engine or shopping site.

**You:** Type "best noise cancelling headphones 2026" into the search field and press Enter.

**You:** Read the results page. What are the top 3 results?

**You:** Click on the first result and summarize what you see.

## 3. Form Filling

Navigate to any signup or contact form page.

**You:** Read the form fields on this page. What information does it need?

**You:** Fill in the name field with "Jane Doe" and the email with "jane@example.com".

## 4. Research Workflow

Open a Wikipedia article through the Webfuse session.

**You:** Navigate to https://en.wikipedia.org/wiki/Amsterdam

**You:** Read the infobox on the right side. What's the population?

**You:** Now navigate to https://en.wikipedia.org/wiki/Rotterdam and get the same info. Which city is bigger?

## 5. Accessibility Check

Navigate to any website.

**You:** Read the accessibility tree for this page. Are there any images missing alt text?

**You:** How many heading levels does this page use? Is the hierarchy correct?

## Tips

- **Be specific.** "Click the blue Submit button at the bottom" works better than "submit the form."
- **Use CSS selectors.** Claude can target elements precisely: "Click the element matching `button.primary`."
- **Chain actions.** "Navigate to google.com, search for Webfuse, and read the first result" works as one instruction.
- **Watch your browser.** Every action Claude takes is visible in your Webfuse session in real time.
