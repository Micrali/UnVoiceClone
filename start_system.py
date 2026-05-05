import os
import sys
import time
import socket
import threading
import subprocess
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(ROOT_DIR, "frontend", "web_static")
BACKEND_DIR = os.path.join(ROOT_DIR, "backend")


def is_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return sock.connect_ex(("127.0.0.1", port)) == 0


class StaticHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_DIR, **kwargs)


def run_static_server(port: int = 8080):
    server = ThreadingHTTPServer(("0.0.0.0", port), StaticHandler)
    print(f"[Static] serving at http://127.0.0.1:{port}")
    server.serve_forever()


def run_backend():
    env = os.environ.copy()
    env["PYTHONPATH"] = ROOT_DIR + os.pathsep + env.get("PYTHONPATH", "")
    return subprocess.Popen([sys.executable, "app.py"], cwd=BACKEND_DIR, env=env)


def main():
    backend_port = 5000
    static_port = 8080

    if is_port_in_use(static_port):
        print(f"[Warn] 静态站点端口 {static_port} 已被占用。")
    else:
        threading.Thread(target=run_static_server, args=(static_port,), daemon=True).start()

    if is_port_in_use(backend_port):
        print(f"[Warn] 后端端口 {backend_port} 已被占用。")
        backend_process = None
    else:
        backend_process = run_backend()
        print(f"[Backend] started with PID {backend_process.pid}")

    print("系统启动完成。")
    print(f"官网主页: http://127.0.0.1:{static_port}/index.html")
    print(f"后端健康检查: http://127.0.0.1:{backend_port}/api/health")

    try:
        while True:
            time.sleep(1)
            if backend_process and backend_process.poll() is not None:
                print("后端服务已退出。")
                break
    except KeyboardInterrupt:
        print("正在关闭系统...")
        if backend_process and backend_process.poll() is None:
            backend_process.terminate()


if __name__ == "__main__":
    main()
