"""Field management tools for DocTypes."""
from mcp.server.fastmcp import FastMCP
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.executors.frappe_api import FrappeAPIClient

def register(mcp: FastMCP, frappe: "FrappeAPIClient"):

    @mcp.tool()
    async def erpnext_field_list(doctype: str) -> str:
        """List all fields for a DocType.

        Args:
            doctype: DocType name
        """
        try:
            doc = await frappe.get_doc("DocType", doctype)
            fields = doc.get("fields", [])
            result = [f"Fields in {doctype}:"]
            for f in fields:
                reqd = " (required)" if f.get("reqd") else ""
                result.append(f"- {f.get('fieldname')}: {f.get('fieldtype')}{reqd}")
            return "\n".join(result)
        except Exception as e:
            return f"Error: {str(e)}"

    @mcp.tool()
    async def erpnext_field_add(
        doctype: str,
        fieldname: str,
        label: str,
        fieldtype: str = "Data",
        options: str = "",
        required: bool = False
    ) -> str:
        """Add a custom field to an existing DocType.

        Args:
            doctype: Target DocType name
            fieldname: Field technical name (snake_case)
            label: Display label
            fieldtype: Field type (Data, Select, Link, Int, etc.)
            options: Options for Select/Link fields
            required: Whether field is required
        """
        try:
            # Check if field already exists
            doc = await frappe.get_doc("DocType", doctype)
            existing = [f for f in doc.get("fields", []) if f.get("fieldname") == fieldname]
            if existing:
                return f"Error: Field '{fieldname}' already exists in {doctype}"

            # Create custom field via API
            field_data = {
                "doctype": "Custom Field",
                "dt": doctype,
                "fieldname": fieldname,
                "label": label,
                "fieldtype": fieldtype,
                "options": options,
                "reqd": 1 if required else 0,
            }
            result = await frappe.create_doc("Custom Field", field_data)
            return f"Field '{fieldname}' added to {doctype}\nCustom Field: {result.get('name')}"
        except Exception as e:
            return f"Error: {str(e)}"

    @mcp.tool()
    async def erpnext_field_delete(doctype: str, fieldname: str) -> str:
        """Delete a custom field from a DocType.

        Args:
            doctype: DocType name
            fieldname: Field to delete
        """
        try:
            # Find custom field
            custom_fields = await frappe.list_docs("Custom Field", {"dt": doctype, "fieldname": fieldname})
            if not custom_fields:
                return f"No custom field '{fieldname}' found in {doctype}"

            cf_name = custom_fields[0]["name"]
            await frappe.delete_doc("Custom Field", cf_name)
            return f"Custom field '{fieldname}' deleted from {doctype}"
        except Exception as e:
            return f"Error: {str(e)}"

    @mcp.tool()
    async def erpnext_field_translate(
        doctype: str,
        fieldname: str,
        language: str,
        translation: str
    ) -> str:
        """Set translation for a field label.

        Args:
            doctype: DocType name
            fieldname: Field name
            language: Language code (e.g., 'zh-CN')
            translation: Translated label
        """
        try:
            # Get field label
            doc = await frappe.get_doc("DocType", doctype)
            fields = doc.get("fields", [])
            field = next((f for f in fields if f.get("fieldname") == fieldname), None)
            if not field:
                return f"Field '{fieldname}' not found in {doctype}"

            source_text = field.get("label", fieldname)

            # Check for existing translation
            existing = await frappe.list_docs("Translation", {
                "language": language,
                "source_text": source_text
            })

            if existing:
                await frappe.update_doc("Translation", existing[0]["name"], {
                    "translated_text": translation
                })
                return f"Updated translation for '{source_text}' in {language}"
            else:
                await frappe.create_doc("Translation", {
                    "language": language,
                    "source_text": source_text,
                    "translated_text": translation
                })
                return f"Created translation for '{source_text}' in {language}"
        except Exception as e:
            return f"Error: {str(e)}"