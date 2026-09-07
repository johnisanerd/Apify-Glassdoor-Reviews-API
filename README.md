# 🏢 Glassdoor Reviews API: Employer Reviews to Structured JSON

> The most efficient, reliable, and developer-friendly way to use the Glassdoor Reviews API.

**Actor page:** [apify.com/johnvc/glassdoor-reviews-api](https://apify.com/johnvc/glassdoor-reviews-api?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/glassdoor-reviews-api/input-schema](https://apify.com/johnvc/glassdoor-reviews-api/input-schema?fpr=9n7kx3)

Give it one or more Glassdoor company review URLs and it returns that employer's reviews as clean JSON: one row per review with the overall star rating, per-category ratings, pros and cons, employment type and status, review dates, and review URLs. It is built API-first and MCP-ready, so you can call it from Python or drive it as a tool from an AI agent.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Glassdoor-Reviews-API.git
   cd Apify-Glassdoor-Reviews-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python glassdoor-reviews-api-example.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python glassdoor-reviews-api-example.py
```

## Why Use This Glassdoor Reviews API?

**A URL in, structured data out.** You never touch collection infrastructure. Paste one or more Glassdoor company review URLs and get flat, predictable fields you can load straight into a sheet, a database, or a BI tool.

**Batch many employers at once.** Pass up to 100 company URLs in a single run, each capped independently, so one call can cover a whole peer set.

**Pay per review.** Billing is per review returned, with no per-run setup fee, so you only pay for what is delivered, and `maxReviewsPerCompany` lets you cap both volume and cost.

**Analysis-ready category ratings.** Alongside the overall star rating, every review carries per-category scores for career opportunities, compensation and benefits, culture and values, work-life balance, senior leadership, and diversity and inclusion, so you can chart employee sentiment by theme.

**Reliable and predictable.** Every review comes back with the same field shape, and a URL that cannot be collected returns a clear error row instead of failing the whole run.

**MCP-ready.** Call it as a tool from Claude, Cursor, and other AI agents (see the install sections below).

## Features

### Core Capabilities
- Collect reviews for one company or a batch of employers from Glassdoor company review URLs
- Overall star rating plus six per-category ratings on every review
- Reviewer pros, cons, and one-line headline
- Employment type and status, publish date, and a direct link to each review

### Data Quality
- One consistent JSON row per review, every time
- A plain-language `summary` field on every row for quick scanning and AI use
- A clear error row for a URL that cannot be collected, so one bad link never sinks the batch
- Sub-ratings a reviewer did not rate are omitted rather than returned as a zero

## Usage Examples

### Reviews for one company
```json
{
  "companyUrls": ["https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm"],
  "maxReviewsPerCompany": 5,
  "days": 30
}
```

### Several companies, capped and window-limited
```json
{
  "companyUrls": [
    "https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm",
    "https://www.glassdoor.com/Reviews/Microsoft-Reviews-E1651.htm"
  ],
  "maxReviewsPerCompany": 200,
  "days": 90
}
```

A company Overview URL is also accepted. URLs that are not Glassdoor company URLs are skipped. The API returns one row per review.

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `companyUrls` | `list[str]` | Yes | - | One or more Glassdoor company review URLs, e.g. `https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm`. Overview URLs are also accepted. Up to 100 per run. |
| `maxReviewsPerCompany` | `int` | No | `100` | Maximum reviews to return per company (1 to 1000). Caps cost and volume; each company is capped independently. |
| `days` | `int` | No | `30` | How many days of reviews to collect, for example 30 for the last month. |

## Output Format

Each review is returned as one JSON row:

```json
{
  "result_type": "review",
  "companyName": "Google",
  "overallRating": 4,
  "ratingCareerOpportunities": 4,
  "ratingCompensationBenefits": 5,
  "ratingCultureValues": 4,
  "ratingWorkLife": 4,
  "ratingSeniorLeadership": 3,
  "ratingDiversityInclusion": 4,
  "reviewSummary": "Great company with no notable downsides",
  "pros": "Great company to be at",
  "cons": "No cons that i can think",
  "employmentStatus": "CONTRACT",
  "employmentType": "Former employee",
  "datePublished": "2026-07-05T00:00:00.000Z",
  "helpfulCount": 0,
  "reviewId": "104656922",
  "reviewUrl": "https://www.glassdoor.com/Reviews/Google-Reviews-E9079-RVW104656922.htm",
  "companyUrl": "https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm",
  "summary": "4-star review from Former employee: liked \"Great company to be at\", noted \"No cons that i can think\"."
}
```

**Two dataset views** ship with the Actor. The **Overview** view (`companyName`, `overallRating`, `employmentType`, `employmentStatus`, `datePublished`, `reviewUrl`, `summary`) is a quick reading list. The **Ratings Breakdown** view (`overallRating` plus the six per-category ratings) is for analysis by category. Sub-ratings a reviewer did not rate are omitted rather than returned as a zero.

---

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Glassdoor Reviews API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/glassdoor-reviews-api"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Glassdoor Reviews API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

---

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/glassdoor-reviews-api"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/glassdoor-reviews-api" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Glassdoor Reviews API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

---

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/glassdoor-reviews-api`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/glassdoor-reviews-api`, using OAuth when prompted.
5. Ask Claude to run the Glassdoor Reviews API.

Open Claude on the web: https://claude.ai/referral/uIlpa7nPLg

---

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/glassdoor-reviews-api"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/glassdoor-reviews-api",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Glassdoor Reviews API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

---

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/glassdoor-reviews-api`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

## Use it from n8n

There is a free, ready-made n8n template built on this API: [Log weekly Glassdoor reviews to Google Sheets](https://n8n.io/workflows/17480-log-weekly-glassdoor-reviews-to-google-sheets-using-apify/). It runs on a weekly schedule and appends one row per review, with the star rating, pros, cons, and per-category ratings, to a sheet you pick. It uses the official Apify node, so it works on n8n Cloud with a live preview.

Self-hosting n8n? There is also a dedicated community node: [`n8n-nodes-glassdoor-reviews-api`](https://www.npmjs.com/package/n8n-nodes-glassdoor-reviews-api) on npm.

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Glassdoor Reviews API to power your employer-brand monitoring, people analytics, and employee sentiment research with reliable, structured results.*

Last Updated: 2026.09.07
