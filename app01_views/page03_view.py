# views/page2_view.py
import flet as ft
from app02_ui_components.navbar import navbar
from app03_services.speech_service import process_speech_recognition_blob, process_speech_recognition_michrophone
import env_production
import threading

def page03_view(page: ft.Page):
    """
    音声認識結果を表示するページを定義します。
    """
    page.title = "レシート読み取りアプリ - 音声認識ページ"

    # UIコンポーネントの定義
    result_text = ft.Text(value="音声認識結果がここに表示されます。", size=14, selectable=True)
    status_text = ft.Text(value="音声認識を開始するにはボタンをクリックしてください。", size=14)

    ############################################
    # パターン1: 音声認識をAzure Blob Storageから実行する
    ############################################
    # 音声認識を開始するボタンのクリックイベントハンドラ
    def on_recognize_click(e):
        # ボタンを無効化して複数クリックを防止
        recognize_button.disabled = True
        status_text.value = "音声認識を実行中..."
        page.update()

        try:
            # 環境変数から設定情報を取得
            connection_string = env_production.get_env_variable("AZURE_STORAGE_CONNECTION_STRING")
            container_name = env_production.get_env_variable("AZURE_STORAGE_CONTAINER_NAME")
            blob_name = env_production.get_env_variable("AZURE_STORAGE_BLOB_NAME")
            subscription_key = env_production.get_env_variable("AZURE_SPEECH_KEY")
            region = env_production.get_env_variable("AZURE_SPEECH_REGION")

            # 音声認識を実行
            audio_text = process_speech_recognition_blob(
                connection_string, container_name, blob_name, subscription_key, region
            )

            # UIを更新
            result_text.value = audio_text
            status_text.value = "音声認識が完了しました。"
        except Exception as ex:
            # エラーメッセージを表示
            result_text.value = f"エラーが発生しました: {ex}"
            status_text.value = "音声認識中にエラーが発生しました。"
        finally:
            recognize_button.disabled = False
            page.update()

    recognize_button = ft.ElevatedButton(text="音声認識を開始", on_click=on_recognize_click)

    ############################################
    # パターン2: 音声認識をマイクから実行する
    ############################################
    # 音声認識ボタンのハンドラ
    def on_recognize_click(e):
        status_text.value = "音声認識中..."
        page.update()

        try:
            # 環境変数から設定情報を取得
            subscription_key = env_production.get_env_variable("AZURE_SPEECH_KEY")
            region = env_production.get_env_variable("AZURE_SPEECH_REGION")

            # 音声認識の実行
            recognized_text = process_speech_recognition_michrophone(subscription_key, region)

            # 結果を画面に反映
            result_text.value = recognized_text
            status_text.value = "音声認識が完了しました。"
        except Exception as ex:
            # エラーメッセージを表示
            result_text.value = f"エラーが発生しました: {ex}"
            status_text.value = "音声認識中にエラーが発生しました。"
        finally:
            page.update()

    recognize_button_microphone = ft.ElevatedButton(text="マイクから音声認識を開始", on_click=on_recognize_click)


    # UIレイアウトの構築
    content = ft.Column(
        controls=[
            ft.Text("音声認識結果", size=20, weight="bold"),
            result_text,
            ft.Container(height=20),
            status_text,
            ft.Container(height=20),
            recognize_button,
            recognize_button_microphone,
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
    )

    # ナビゲーションバーとコンテンツを含むビューの作成
    view = ft.View(
        "/page03",
        controls=[
            navbar(page),
            ft.Container(content=content, padding=20),
        ]
    )

    return view