# generate_sas_url.py
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta
import os
import re
def generate_sas_url(connection_string, container_name, blob_name, expiry_hours=1):
    """
    SAS URLを生成します。

    Args:
        connection_string (str): Azure Blob Storageの接続文字列。
        container_name (str): コンテナ名。
        blob_name (str): Blob名。
        expiry_hours (int): SASトークンの有効期限（時間単位）。

    Returns:
        str: 生成されたSAS URL。
    """
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    # アカウント名とアカウントキーを取得
    account_name = blob_service_client.account_name
    # 接続文字列からアカウントキーを抽出
    match = re.search(r"AccountKey=([^;]+)", connection_string)
    if not match:
        raise ValueError("接続文字列からAccountKeyを取得できませんでした。")
    account_key = match.group(1)
    
    # SASトークンを生成
    sas_token = generate_blob_sas(
        account_name=account_name,
        container_name=container_name,
        blob_name=blob_name,
        account_key=account_key,
        permission=BlobSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(hours=expiry_hours)
    )
    
    # BlobのURLを取得
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_url = blob_client.url
    
    # SASトークンを付与したURLを作成
    sas_url = f"{blob_url}?{sas_token}"
    return sas_url

