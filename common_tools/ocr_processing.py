# ocr_processing.py
from PIL import Image
import pytesseract

def perform_ocr(image_path):
    """
    画像からOCRを実行してテキストを抽出します。
    """
    image = Image.open(image_path)
    ocr_result = pytesseract.image_to_string(image, lang='jpn')  # 日本語の場合
    return ocr_result
