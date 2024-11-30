# app03_services/speech_service.py
# 音声データのダウンロードと文字起こしという、データ取得および処理のロジックを担当します。
import os
import tempfile
from app03_services.file_access import download_blob_from_azure
from app03_services.file_access import download_file_from_azure
from app03_services.speech_recognition import speech_to_text

def process_speech_recognition_blob(connection_string, container_name, blob_name, subscription_key, region):
    """
    Azure Blob Storageから音声ファイルをダウンロードし、テキストに変換します。

    :param connection_string: Blob Storageの接続文字列
    :param container_name: コンテナ名
    :param blob_name: ブロブ名
    :param subscription_key: Azure Speechサービスのサブスクリプションキー
    :param region: Azure Speechサービスのリージョン
    :return: 認識されたテキスト
    """
    # 一時ファイルのパスを作成
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        temp_file_path = temp_file.name

    try:
        # 音声ファイルをダウンロード
        downloaded_file = download_blob_from_azure(container_name, blob_name, connection_string, temp_file_path)
        print(f"Image data length: {len(downloaded_file)}")  # デバッグ用
        print(f"Image data preview: {downloaded_file[:100]}...")  # 画像データの一部を表示

        # 音声認識を実行
        text = speech_to_text(temp_file_path, subscription_key, region)
        return text
    finally:
        # 一時ファイルを削除
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

def process_speech_recognition_file_share(connection_string, share_name, directory_name, file_name, subscription_key, region):
    """
    Azure File Storageから音声ファイルをダウンロードし、テキストに変換します。

    :param connection_string: File Storageの接続文字列
    :param share_name: ファイル共有名
    :param directory_name: ディレクトリ名
    :param file_name: ファイル名
    :param subscription_key: Azure Speechサービスのサブスクリプションキー
    :param region: Azure Speechサービスのリージョン
    :return: 認識されたテキスト
    """
    # 一時ファイルのパスを作成
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        temp_file_path = temp_file.name

    try:
        # 音声ファイルをダウンロード
        download_file_from_azure(share_name, directory_name, file_name, connection_string, temp_file_path)

        # 音声認識を実行
        text = speech_to_text(temp_file_path, subscription_key, region)
        return text
    finally:
        # 一時ファイルを削除
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
