"""Main entry point for ERPNext Dev MCP Server."""
import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

from src.config import Config
from src.executors.ssh_executor import SSHExecutor
from src.executors.frappe_api import FrappeAPIClient
from src.tools import app_tools, module_tools, doctype_tools, field_tools, workspace_tools

load_dotenv()

def main():
    config = Config.from_env()

    mcp = FastMCP("erpnext-dev-mcp")

    # Initialize executors
    ssh = SSHExecutor(config)
    frappe = FrappeAPIClient(config)

    # Register tools
    app_tools.register(mcp, ssh, frappe)
    module_tools.register(mcp, ssh, frappe)
    doctype_tools.register(mcp, ssh, frappe)
    field_tools.register(mcp, frappe)
    workspace_tools.register(mcp, frappe)

    mcp.run()

if __name__ == "__main__":
    main()
