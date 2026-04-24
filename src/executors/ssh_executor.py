"""Docker Executor for running commands in frappe container."""
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
        # Build the command to run inside the container
        inner_cmd = f'runuser -u frappe -- bash -c "cd {self.bench_dir} && source env/bin/activate && {command}"'
        cmd = ["docker", "exec", self.container, "bash", "-c", inner_cmd]
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )
        return result.stdout, result.stderr, result.returncode

    def write_file(self, path: str, content: str) -> bool:
        """Write file to bench volume via docker exec."""
        escaped_content = content.replace("'", "'\"'\"'")
        cmd = ["docker", "exec", self.container, "bash", "-c", f"echo '{escaped_content}' > {path}"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0

    def read_file(self, path: str) -> str:
        """Read file from bench volume via docker exec."""
        cmd = ["docker", "exec", self.container, "bash", "-c", f"cat {path}"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
