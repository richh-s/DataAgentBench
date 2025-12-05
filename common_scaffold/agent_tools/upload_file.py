import io
import os
from datetime import datetime

def upload_to_client(client, json_str, filename, filedir):

    json_bytes = json_str.encode('utf-8')
    json_file = io.BytesIO(json_bytes)
    json_file.name = filename

    response = client.files.create(
        file=json_file,
        purpose="assistants"
    )

    filename_without_ext = os.path.splitext(filename)[0]
    filename_ext = os.path.splitext(filename)[1]
    cur_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(filedir, f"{filename_without_ext}_{cur_time}.{filename_ext}")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(json_str)

    

    file_id = response.id
    return file_id