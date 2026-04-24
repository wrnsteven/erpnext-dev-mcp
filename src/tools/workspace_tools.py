"""Workspace creation tools."""
from mcp.server.fastmcp import FastMCP
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.executors.frappe_api import FrappeAPIClient

def register(mcp: FastMCP, frappe: "FrappeAPIClient"):

    @mcp.tool()
    async def erpnext_workspace_create(
        name: str,
        label: str,
        icon: str = "fa fa-star"
    ) -> str:
        """Create a new Workspace.

        Args:
            name: Workspace name (snake_case)
            label: Display label
            icon: Font Awesome icon class
        """
        try:
            doc = await frappe.create_doc("Workspace", {
                "doctype": "Workspace",
                "name": name,
                "label": label,
                "icon": icon,
                "public": 1,
            })
            return f"Workspace '{label}' created successfully!\nName: {doc.get('name')}"
        except Exception as e:
            return f"Error: {str(e)}"

    @mcp.tool()
    async def erpnext_workspace_list() -> str:
        """List all workspaces."""
        try:
            workspaces = await frappe.list_docs("Workspace")
            names = [w["name"] for w in workspaces]
            return f"Workspaces:\n" + "\n".join(names)
        except Exception as e:
            return f"Error: {str(e)}"
