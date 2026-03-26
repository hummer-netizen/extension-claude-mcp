#!/usr/bin/env python3
"""
Quick test: verify your Webfuse MCP connection works.

Usage:
  pip install httpx
  python test_connection.py YOUR_REST_KEY

If successful, you'll see the list of 13 available tools.
"""

import sys
import httpx
import json

if len(sys.argv) < 2:
    print("Usage: python test_connection.py <WEBFUSE_REST_KEY>")
    sys.exit(1)

REST_KEY = sys.argv[1]
MCP_URL = "https://session-mcp.webfu.se/mcp"

headers = {
    "Authorization": f"Bearer {REST_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream",
}


def parse_response(resp):
    """Parse JSON from either direct JSON or SSE response."""
    content_type = resp.headers.get("content-type", "")
    if "text/event-stream" in content_type:
        for line in resp.text.splitlines():
            if line.startswith("data: "):
                return json.loads(line[6:])
        raise ValueError("No data line found in SSE response")
    return resp.json()


print(f"Connecting to {MCP_URL}...")

# Step 1: Initialize
resp = httpx.post(MCP_URL, json={
    "jsonrpc": "2.0",
    "id": 0,
    "method": "initialize",
    "params": {
        "protocolVersion": "2025-03-26",
        "capabilities": {},
        "clientInfo": {"name": "connection-test", "version": "1.0"},
    },
}, headers=headers, timeout=15)

if resp.status_code != 200:
    print(f"❌ Initialize failed: HTTP {resp.status_code}")
    print(resp.text[:200])
    sys.exit(1)

data = parse_response(resp)
session_id = resp.headers.get("mcp-session-id", "")
if session_id:
    headers["mcp-session-id"] = session_id

print(f"✅ Connected (session: {session_id[:16]}...)")

# Step 2: Send initialized notification
httpx.post(MCP_URL, json={
    "jsonrpc": "2.0",
    "method": "notifications/initialized",
}, headers=headers, timeout=10)

# Step 3: List tools
resp = httpx.post(MCP_URL, json={
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list",
    "params": {},
}, headers=headers, timeout=15)

data = parse_response(resp)
tools = data.get("result", {}).get("tools", [])

if tools:
    print(f"\n✅ Found {len(tools)} tools:\n")
    for t in tools:
        print(f"  • {t['name']}: {t.get('description', '')[:60]}")
    print(f"\n🎉 Everything works! Claude Desktop will see these same {len(tools)} tools.")
else:
    print("❌ No tools found. Check that:")
    print("   - The Automation app is enabled on your Space")
    print("   - You restarted the Session after enabling it")
    print(f"\nRaw response: {json.dumps(data, indent=2)[:500]}")
