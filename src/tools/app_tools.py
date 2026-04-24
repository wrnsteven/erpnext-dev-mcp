"""App creation and management tools."""
from mcp.server.fastmcp import FastMCP
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.executors.ssh_executor import SSHExecutor
    from src.executors.frappe_api import FrappeAPIClient

def register(mcp: FastMCP, ssh: "SSHExecutor", frappe: "FrappeAPIClient"):

    @mcp.tool()
    async def erpnext_app_list() -> str:
        """List all installed apps in the bench."""
        stdout, stderr, code = ssh.exec_bench("bench --version")
        if code != 0:
            return f"Error: {stderr}"

        # List apps
        stdout, stderr, code = ssh.exec_bench("ls -la apps/")
        if code != 0:
            return f"Error listing apps: {stderr}"
        return f"Apps in bench:\n{stdout}"

    @mcp.tool()
    async def erpnext_app_create(
        app_name: str,
        app_title: str,
        description: str = ""
    ) -> str:
        """Create a new ERPNext app scaffold.

        Args:
            app_name: Unique name for the app (snake_case, e.g., 'library_management')
            app_title: Display title for the app
            description: Optional description
        """
        # Validate app_name (snake_case only)
        if not app_name.replace("_", "").replace("-", "").isalnum():
            return "Error: app_name must be snake_case (letters, numbers, underscores only)"

        # Create app using bench
        cmd = f"bench new-app {app_name} --title '{app_title}'"
        stdout, stderr, code = ssh.exec_bench(cmd)

        if code != 0:
            return f"Error creating app: {stderr}"

        return f"App '{app_name}' created successfully!\n{stdout}"
