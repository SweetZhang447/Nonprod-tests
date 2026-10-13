---
title: Linear MCP Connectivity Test
input: pr_metadata
tools:
  - mcp
conclusion: neutral
maxRuns: 3
maxBudgetPerRun: 0.50
showToolCalls: true
---

You are verifying that MCP connector tools work end to end. Do not review the code in this pull request.

Perform these steps in order:

1. Call `discover_mcp_tools` with no server name to list every connected MCP server and its tools.
2. Identify the Linear MCP server in that list. Choose ONE read-only tool from it that lists or searches data (for example a tool that lists teams, projects, or issues). Do not choose any tool that creates, updates, deletes, or comments.
3. Call `get_mcp_tool_schema` for the tool you chose.
4. Call `call_mcp_tool` to invoke it. If it requires arguments, use the smallest valid set, and prefer a small page size.

Then write a report with exactly these sections:

**Servers discovered** — each connected MCP server name and how many tools it exposes.

**Tool invoked** — the server and tool name you called, and the arguments you passed.

**Result** — whether the call succeeded, and a two-sentence summary of what came back. If it failed, quote the exact error text.

Never call a tool that modifies data.
