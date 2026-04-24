"""Module management tools."""
from mcp.server.fastmcp import FastMCP
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.executors.ssh_executor import SSHExecutor
    from src.executors.frappe_api import FrappeAPIClient

def register(mcp: FastMCP, ssh: "SSHExecutor", frappe: "FrappeAPIClient"):

    @mcp.tool()
    async def erpnext_module_list(app_name: str) -> str:
        """List modules in an app.

        Args:
            app_name: App name
        """
        stdout, stderr, code = ssh.exec_bench(f"ls apps/{app_name}/{app_name.replace('-', '_')}/")
        if code != 0:
            return f"Error: {stderr}"
        return f"Modules in {app_name}:\n{stdout}"
