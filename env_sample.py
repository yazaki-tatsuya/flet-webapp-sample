def get_env_variable(key):

    env_variable_dict = {

        "DATABASE_CONN_STRING" : "データベース接続文字列",
    }
    ret_val = env_variable_dict.get(key, None)
    return ret_val