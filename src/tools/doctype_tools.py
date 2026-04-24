"""DocType creation and management tools."""
from mcp.server.fastmcp import FastMCP
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from src.executors.ssh_executor import SSHExecutor
    from src.executors.frappe_api import FrappeAPIClient

def register(mcp: FastMCP, ssh: "SSHExecutor", frappe: "FrappeAPIClient"):

    @mcp.tool()
    async def erpnext_doctype_list(module_name: Optional[str] = None) -> str:
        """List DocTypes, optionally filtered by module.

        Args:
            module_name: Optional module name to filter by
        """
        try:
            filters = {"module": module_name} if module_name else None
            doctypes = await frappe.list_docs("DocType", filters)
            names = [d["name"] for d in doctypes]
            return f"Found {len(names)} DocTypes:\n" + "\n".join(names[:50])
        except Exception as e:
            return f"Error: {str(e)}"

    @mcp.tool()
    async def erpnext_doctype_get(doctype_name: str) -> str:
        """Get DocType details including fields.

        Args:
            doctype_name: Name of the DocType
        """
        try:
            doc = await frappe.get_doc("DocType", doctype_name)
            fields = doc.get("fields", [])
            field_info = []
            for f in fields:
                field_info.append(f"- {f.get('fieldname')}: {f.get('fieldtype')} ({f.get('label', '')})")
            return f"DocType: {doctype_name}\nModule: {doc.get('module')}\nFields:\n" + "\n".join(field_info)
        except Exception as e:
            return f"Error: {str(e)}"

    @mcp.tool()
    async def erpnext_doctype_create(
        doctype_name: str,
        module_name: str,
        fields: list[dict],
        is_submittable: bool = False,
        custom: bool = False
    ) -> str:
        """Create a new DocType with specified fields.

        Args:
            doctype_name: Name of the DocType (Title Case, e.g., 'Article')
            module_name: Module to place the DocType in
            fields: List of field definitions [{"fieldname": "article_name", "fieldtype": "Data", "label": "Article Name"}]
            is_submittable: Whether the DocType is submittable
            custom: Whether to create as custom DocType (no file generation)
        """
        # Create via Frappe API
        doc_data = {
            "doctype": "DocType",
            "name": doctype_name,
            "module": module_name,
            "custom": custom,
            "is_submittable": is_submittable,
            "fields": [
                {
                    "doctype": "DocField",
                    "fieldname": f["fieldname"],
                    "fieldtype": f.get("fieldtype", "Data"),
                    "label": f.get("label", f["fieldname"].replace("_", " ").title()),
                    "reqd": f.get("required", 0),
                    "options": f.get("options", ""),
                }
                for f in fields
            ],
        }

        try:
            result = await frappe.create_doc("DocType", doc_data)
            return f"DocType '{doctype_name}' created successfully!\nName: {result.get('name')}"
        except Exception as e:
            return f"Error creating DocType: {str(e)}"