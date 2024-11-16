def get_env_variable(key):

    env_variable_dict = {
        # Azure SQL Database
        "DATABASE_CONN_STRING" : "データベース接続文字列",
        # Azure Storage Account
        "AZURE_CONNECTION_STRING" : "Azure Storage Accountの接続文字列",
        "AZURE_SHARE_NAME" : "",
        "AZURE_DIRECTORY_NAME" : "",
        "AZURE_FILE_NAME" : "",
        # Azure Computer Vision
        "AZURE_COMPUTER_VISION_ENDPOINT" : "",
        "AZURE_COMPUTER_VISION_KEY" : "",
        # Azure Speech
        "AZURE_SPEECH_KEY" : "",
        "AZURE_SPEECH_REGION" : "", 
    }
    ret_val = env_variable_dict.get(key, None)
    return ret_val