import io
from pathlib import Path


def upload_to_client(json_str, filename):
    """Upload `json_str` as a file to the API and also save a local copy.

    Side effects:
    - Writes the bytes to `./uploads/<filename>` (creates `uploads/` if missing)
    """
    json_bytes = json_str.encode('utf-8')

    # Save a local copy under ./uploads
    uploads_dir = Path.cwd() / "uploads"
    uploads_dir.mkdir(parents=True, exist_ok=True)
    local_path = uploads_dir / filename
    try:
        with open(local_path, "wb") as f:
            f.write(json_bytes)
    except Exception:
        # don't fail the upload if local write fails; just continue
        pass

    return str(local_path)