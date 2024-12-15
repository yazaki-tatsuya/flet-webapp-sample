# app03_services/speech_recognition.py
# 音声ファイルをテキストに変換します。
import azure.cognitiveservices.speech as speechsdk
import env_production

############################################
# パターン1: 音声ファイルをテキストに変換する
############################################
def speech_to_text(audio_file_path: str, speech_key, service_region) -> str:
    """
    音声データをテキストに変換します。

    :param audio_config: AudioConfigオブジェクト（音声データの設定）
    :param subscription_key: Azure Speechサービスのサブスクリプションキー
    :param region: Azure Speechサービスのリージョン
    :return: 認識されたテキスト
    """

    if not speech_key or not service_region:
        raise Exception("Azure Speechサービスのキーとリージョンが設定されていません。")

    # Speech SDKの構成
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    # 日本語を指定
    speech_config.speech_recognition_language = "ja-JP"
    audio_config = speechsdk.audio.AudioConfig(filename=audio_file_path)

    # 音声認識オブジェクトの作成
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    # 音声認識の実行
    result = speech_recognizer.recognize_once_async().get()

    # 結果の処理
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        raise Exception(f"音声を認識できませんでした: {result.no_match_details}")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        error_msg = f"音声認識がキャンセルされました: {cancellation_details.reason}"
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            error_msg += f"\nエラー詳細: {cancellation_details.error_details}"
        raise Exception(error_msg)

############################################
# パターン2: マイクから音声をテキストに変換する
############################################
def speech_to_text_microphone(subscription_key, region, language="ja-JP"):
    """
    マイクから音声を認識し、テキストを返します。
    """
    try:
        # Speech Config を作成
        speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
        speech_config.speech_recognition_language = language
        audio_config = speechsdk.AudioConfig(use_default_microphone=True)

        # Speech Recognizer を作成
        recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        print("マイク入力を開始します。話してください...")

        # 音声認識を実行
        result = recognizer.recognize_once_async().get()

        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return result.text
        elif result.reason == speechsdk.ResultReason.NoMatch:
            return "音声を認識できませんでした。"
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            return f"認識がキャンセルされました: {cancellation_details.error_details}"

        # 不要？？
        # # イベントリスナーを登録
        # speech_recognizer.recognized.connect(recognized_cb)

        # # 継続的に音声を認識
        # speech_recognizer.start_continuous_recognition()

        # try:
        #     while True:
        #         pass  # 無限ループで待機（Ctrl+Cで停止）
        # except KeyboardInterrupt:
        #     print("終了します...")
        #     speech_recognizer.stop_continuous_recognition()

    except Exception as e:
        return f"エラーが発生しました: {e}"
