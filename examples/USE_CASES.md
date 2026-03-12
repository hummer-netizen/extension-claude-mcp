# Use Cases

Real scenarios you can try with Claude Desktop + Webfuse MCP.

## Research & Analysis

**Competitive analysis:**
Navigate to three competitor pricing pages. Ask Claude to read each one and create a comparison table.

**Academic research:**
Open a Wikipedia article. Ask Claude to read the references section and check which links are still active.

**Job hunting:**
Open a job listing. Ask Claude to read the requirements and compare them to your resume (paste it in chat).

## Data Extraction

**Scrape a table:**
Navigate to any page with a data table. Ask Claude: "Read the table and convert it to CSV format."

**Contact collection:**
Open a company's team page. Ask Claude: "Find all email addresses and names on this page."

**Price monitoring:**
Navigate to a product page. Ask Claude to read the price and any discount info. Repeat for alternatives.

## Accessibility Testing

**Alt text audit:**
Open any website. Ask Claude: "Read the accessibility tree. Are there images without alt text?"

**Heading structure:**
Ask Claude: "Check the heading hierarchy on this page. Are there any skipped levels?"

**Keyboard navigation:**
Ask Claude to tab through the page and report which elements are focusable.

## Form Assistance

**Application forms:**
Open a long application form. Tell Claude the info to fill in. Watch it work through each field.

**Repeated submissions:**
If you need to fill the same form multiple times with different data, Claude can handle the repetition.

## Learning & Exploration

**Explain a dashboard:**
Open a complex web app. Ask Claude: "What are all the options on this settings page? Explain each one."

**Compare documentation:**
Open two framework docs in sequence. Ask Claude to compare their approaches to routing, state management, etc.

## Tips for Best Results

1. **Navigate first, then ask.** Open the right page in your Webfuse session before asking Claude to interact.
2. **Be specific about selectors.** "Read the table with class `pricing-table`" beats "read the pricing."
3. **Chain requests.** "Go to X, read Y, then go to Z and read the same thing" works in one message.
4. **Use screenshots for visual questions.** Ask Claude to `see_guiSnapshot` if layout matters.
5. **Scope DOM reads.** For large pages, ask Claude to read a specific section: "Read the element matching `.sidebar nav`."
