from mcp.server.fastmcp import FastMCP
mcp = FastMCP("example-server")

@mcp.tool()
def add(a: float, b: float) -> float:
    return a + b

@mcp.tool()
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny and 25°C."

@mcp.tool()
def word_count(text: str) -> int:
    return len(text.split())

@mcp.resource("config://server-info")
def server_info() -> str:
    return "example-server v1.0 - a minimal demo MCP server"

if __name__ == "__main__":
    mcp.run(transport="stdio")