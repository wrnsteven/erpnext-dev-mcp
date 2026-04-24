"""Frappe API client for document operations."""
import httpx
import base64
from typing import Optional

class FrappeAPIClient:
    def __init__(self, config):
        self.url = config.erpnext_url
        self.api_key = config.erpnext_api_key
        self.api_secret = config.erpnext_api_secret
        self.client = httpx.AsyncClient(timeout=30.0)

    def _auth_headers(self) -> dict:
        token = base64.b64encode(f"{self.api_key}:{self.api_secret}".encode()).decode()
        return {"Authorization": f"Basic {token}"}

    async def get_doc(self, doctype: str, name: str) -> dict:
        """Get document by doctype and name."""
        response = await self.client.get(
            f"{self.url}/api/resource/{doctype}/{name}",
            headers=self._auth_headers()
        )
        response.raise_for_status()
        return response.json()["data"]

    async def create_doc(self, doctype: str, data: dict) -> dict:
        """Create document."""
        response = await self.client.post(
            f"{self.url}/api/resource/{doctype}",
            json=data,
            headers=self._auth_headers()
        )
        response.raise_for_status()
        return response.json()["data"]

    async def update_doc(self, doctype: str, name: str, data: dict) -> dict:
        """Update document."""
        response = await self.client.put(
            f"{self.url}/api/resource/{doctype}/{name}",
            json=data,
            headers=self._auth_headers()
        )
        response.raise_for_status()
        return response.json()["data"]

    async def delete_doc(self, doctype: str, name: str) -> bool:
        """Delete document."""
        response = await self.client.delete(
            f"{self.url}/api/resource/{doctype}/{name}",
            headers=self._auth_headers()
        )
        return response.status_code == 202

    async def list_docs(self, doctype: str, filters: Optional[dict] = None) -> list:
        """List documents with optional filters."""
        params = {"fields": '["name"]'}
        if filters:
            params["filters"] = str(filters)
        response = await self.client.get(
            f"{self.url}/api/resource/{doctype}",
            params=params,
            headers=self._auth_headers()
        )
        response.raise_for_status()
        return response.json()["data"]