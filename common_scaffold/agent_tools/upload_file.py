import io

def upload_to_client(client, json_str, filename):

    json_bytes = json_str.encode('utf-8')
    json_file = io.BytesIO(json_bytes)
    json_file.name = filename

    response = client.files.create(
        file=json_file,
        purpose="assistants"
    )

    file_id = response.id
    return file_id