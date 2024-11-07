from azure.storage.fileshare import ShareFileClient
from azure.storage.blob import BlobServiceClient

# Azure Blob Storageからファイルをダウンロード
def download_blob_from_azure(container_name, blob_name, connection_string, download_path):
    """
    Azure Blob Storageからファイルをダウンロードします。
    """
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    
    with open(download_path, "wb") as download_file:
        download_stream = blob_client.download_blob()
        download_file.write(download_stream.readall())
    
    return download_path

# Azure File Storageからファイルをダウンロード
def download_file_from_azure(share_name, directory_name, file_name, connection_string, download_path):
    """
    Azure File Storageからファイルをダウンロードします。
    """
    file_client = ShareFileClient.from_connection_string(
        conn_str=connection_string,
        share_name=share_name,
        file_path=f"{directory_name}/{file_name}"
    )
    
    with open(download_path, "wb") as download_file:
        download_stream = file_client.download_file()
        download_file.write(download_stream.readall())
    
    return download_path
