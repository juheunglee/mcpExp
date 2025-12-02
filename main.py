from mcp.server.fastmcp import FastMCP # Parameter is not strictly needed now, but good practice to keep if you add more complex params later

# Create the FastMCP instance with stdio transport
mcp = FastMCP()

# Define the tool using the @mcp.tool() decorator
@mcp.tool()
def get_weather(city: str) -> str:

   return f"{city} weather is 비가 마이와"
   
@mcp.tool()
def get_multiple(a: int , b:int) -> int:

   return f"두수의 곱곱은 {a*b} 입니다"

# The tool is automatically added to the mcp instance by the decorator
# prompt : What's the weather like in Seoul?

# Run the server if the script is executed directly
if __name__ == "__main__":
   print("Starting MCP server...")
   mcp.run(transport="stdio")
