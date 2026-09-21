# mcp server with 2 tools:
# 1. add_numbers: add two numbers and return the result
# 2. generate_random_number: generate a random number within a given range

import random
from fastmcp import FastMCP

# create an instance of FastMCP with a name for the server
mcp = FastMCP("Simple Calculator Server")

# Tool 1: add two numbers
@mcp.tool
def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers and return the result.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b

# Tool 2: Generate a random number within a given range
@mcp.tool
def generate_random_number(min_value: int=1, max_value: int=100) -> int:
    """
    Generate a random number within a given range.

    Args:
        min_value (int): The minimum value of the range.
        max_value (int): The maximum value of the range.

    Returns:
        int: A random number between min_value and max_value (inclusive).
    """
    return random.randint(min_value, max_value)

# Resource: Server information
@mcp.resource("info://server")
def server_info() -> dict:
    """
    Provide information about the server.

    Returns:
        dict: A dictionary containing server information.
    """
    return {
        "server_name": mcp.name,
        "version": "1.0",
        "description": "A simple calculator server with basic arithmetic and random number generation.",
        "tools": ["add_numbers", "generate_random_number"],
        "resources": ["server_info"],
        "author": "Sumit Das",
    }

# run the server
if __name__ == "__main__":
    # running remote server on port 8000
    mcp.run(transport="http", host="0.0.0.0", port=8000)