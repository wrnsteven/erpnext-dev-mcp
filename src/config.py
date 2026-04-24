"""Configuration management."""
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    # ERPNext connection
    erpnext_url: str
    erpnext_api_key: str
    erpnext_api_secret: str

    # Remote server
    remote_host: str
    remote_user: str
    remote_container: str

    # Bench paths
    bench_dir: str
    bench_python: str

    @classmethod
    def from_env(cls) -> "Config":
        return cls(
            erpnext_url=os.getenv("ERPNEXT_URL", "http://localhost:8088"),
            erpnext_api_key=os.getenv("ERPNEXT_API_KEY", ""),
            erpnext_api_secret=os.getenv("ERPNEXT_API_SECRET", ""),
            remote_host=os.getenv("REMOTE_HOST", "192.168.18.60"),
            remote_user=os.getenv("REMOTE_USER", "erpnext"),
            remote_container=os.getenv("REMOTE_CONTAINER", "erpnext-dev-frappe-1"),
            bench_dir=os.getenv("BENCH_DIR", "/home/frappe/frappe-bench"),
            bench_python=os.getenv("BENCH_PYTHON", "/home/frappe/frappe-bench/env/bin/python"),
        )