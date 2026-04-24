"""SSH Executor for running commands in frappe container."""
import subprocess
import shlex
from dataclasses import dataclass

@dataclass
class SSHExecutor:
    host: str
    user: str
    container: str
    bench_dir: str
    bench_python: str

    def __init__(self, config):
        self.host = config.remote_host
        self.user = config.remote_user
        self.container = config.remote_container
        self.bench_dir = config.bench_dir
        self.bench_python = config.bench_python

    def exec_bench(self, command: str) -> tuple[str, str, int]:
        """Execute bench command in frappe container.

        Returns: (stdout, stderr, returncode)
        """
        cmd = f'docker exec {self.container} bash -c \'runuser -u frappe -- bash -c "cd {self.bench_dir} && source env/bin/activate && {command}"\''
        result = subprocess.run(
            ["ssh", f"{self.user}@{self.host}", cmd],
            capture_output=True,
            text=True
        )
        return result.stdout, result.stderr, result.returncode

    def write_file(self, path: str, content: str) -> bool:
        """Write file to bench volume via docker exec."""
        escaped_content = content.replace("'", "'\"'\"'")
        cmd = f"echo '{escaped_content}' > {path}"
        full_cmd = f'docker exec {self.container} bash -c {shlex.quote(cmd)}'
        result = subprocess.run(
            ["ssh", f"{self.user}@{self.host}", full_cmd],
            capture_output=True,
            text=True
        )
        return result.returncode == 0

    def read_file(self, path: str) -> str:
        """Read file from bench volume via docker exec."""
        cmd = f"cat {path}"
        full_cmd = f'docker exec {self.container} bash -c {shlex.quote(cmd)}'
        result = subprocess.run(
            ["ssh", f"{self.user}@{self.host}", full_cmd],
            capture_output=True,
            text=True
        )
        return result.stdout
