import pyodbc
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import env_production

def parse_connection_string(raw_connection_string):
    # "Server=tcp:..." のような形式の接続文字列を解析してPython用の接続文字列に変換
    params = dict(item.split('=', 1) for item in raw_connection_string.split(';') if item)
    
    # 必要なパラメータを取得、欠けている場合は例外を出す
    server = params.get("Server", "").replace("tcp:", "").replace(",1433", "")
    database = params.get("Initial Catalog", "")
    user_id = params.get("User ID", "")
    password = params.get("Password", "")

    if not server or not database or not user_id or not password:
        raise ValueError("接続文字列に必要なパラメータが不足しています。")

    # Python用の接続文字列を構築
    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={user_id};"
        f"PWD={password};"
    )
    return connection_string


def get_data_from_db():
    # 環境変数の設定を読み込み
    raw_conn_string = env_production.get_env_variable('DATABASE_CONN_STRING')
    database_conn_string = parse_connection_string(raw_conn_string)
    print(database_conn_string)
    try:
        # Azure SQL Serverに接続する
        connection = pyodbc.connect(database_conn_string)
        cursor = connection.cursor()

        # SQLクエリを実行してデータを取得
        cursor.execute("SELECT TOP 10 * FROM EmployeeInfo")
        rows = cursor.fetchall()

        # 結果を整形
        data = []
        for row in rows:
            data.append(str(row))

        # クエリ終了後、接続を閉じる
        cursor.close()
        connection.close()

        return data

    except pyodbc.Error as e:
        raise Exception(f"Database error: {str(e)}")
