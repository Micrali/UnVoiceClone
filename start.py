import os
import sys
import subprocess


def run_python(script_name: str):
    return subprocess.Popen([sys.executable, script_name], cwd=os.path.dirname(__file__))


def main():
    print("=" * 60)
    print("UnVoiceClone System 启动器")
    print("1. 传统静态页面模式（推荐）")
    print("2. 直接启动完整系统服务")
    print("=" * 60)
    choice = input("请选择启动模式（1/2，默认1）: ").strip() or "1"

    if choice == "1":
        process = run_python("start_system.py")
        print(f"系统已启动，进程 ID: {process.pid}")
    elif choice == "2":
        process = run_python("start_system.py")
        print(f"完整系统服务已启动，进程 ID: {process.pid}")
    else:
        print("无效选项，默认启动静态页面模式。")
        process = run_python("start_system.py")
        print(f"系统已启动，进程 ID: {process.pid}")

    print("请访问 http://127.0.0.1:8080/index.html")


if __name__ == "__main__":
    main()
