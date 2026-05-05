import os
import shutil
import uuid
from werkzeug.datastructures import FileStorage

UPLOAD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "uploads"))
OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "outputs"))

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_upload(file: FileStorage) -> str:
    ext = os.path.splitext(file.filename or "upload.bin")[1]
    filename = f"{uuid.uuid4().hex}{ext}"
    path = os.path.join(UPLOAD_DIR, filename)
    file.save(path)
    return path


def copy_as_output(input_path: str, suffix: str = "defended") -> str:
    base, ext = os.path.splitext(os.path.basename(input_path))
    output_path = os.path.join(OUTPUT_DIR, f"{base}_{suffix}{ext or '.bin'}")
    shutil.copyfile(input_path, output_path)
    return output_path
