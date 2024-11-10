# # ocr_processing.py
# from PIL import Image
# import pytesseract

# def perform_ocr(image_path):
#     """
#     画像からOCRを実行してテキストを抽出します。
#     """
#     image = Image.open(image_path)
#     ocr_result = pytesseract.image_to_string(image, lang='jpn')  # 日本語の場合
#     return ocr_result

# ocr_processing.py
import os
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
import time
import env_production

def perform_ocr(image_path):
    """
    画像からAzure Computer Visionを使用してOCRを実行し、テキストを抽出します。
    """
    # 環境変数からAzure Computer Visionのエンドポイントとキーを取得
    endpoint = env_production.get_env_variable("AZURE_COMPUTER_VISION_ENDPOINT")
    key = env_production.get_env_variable("AZURE_COMPUTER_VISION_KEY")

    # エンドポイントとキーが設定されていない場合はエラー
    if not endpoint or not key:
        raise ValueError("Azure Computer Visionのエンドポイントまたはキーが設定されていません。")

    # Computer Visionクライアントの作成
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))

    # 画像ファイルをバイナリモードで開く
    with open(image_path, "rb") as image_stream:
        # OCRのリクエストを送信
        ocr_result = computervision_client.read_in_stream(image_stream, language="ja", raw=True)

    # Operation-LocationヘッダーからOperation IDを取得
    operation_location = ocr_result.headers["Operation-Location"]
    operation_id = operation_location.split("/")[-1]

    # OCRの処理が完了するまで待機
    while True:
        result = computervision_client.get_read_result(operation_id)
        if result.status not in [OperationStatusCodes.running, OperationStatusCodes.not_started]:
            break
        print("OCR処理中...")
        time.sleep(1)

    # OCRの結果を取得
    if result.status == OperationStatusCodes.succeeded:
        print("OCR処理が完了しました。")
        extracted_text = ""
        # ページごとにテキストを抽出
        for page in result.analyze_result.read_results:
            # 行ごとにテキストを抽出
            for line in page.lines:
                extracted_text += line.text + "\n"
        return extracted_text
    else:
        raise RuntimeError("OCR処理が失敗しました。ステータス: {}".format(result.status))
