from starlette.config import Config
from starlette.datastructures import Secret

all_secret_variables = Config(".env")

try:
    conn_str = all_secret_variables("conn_str")

    conn_str_test = all_secret_variables("conn_str_test")
except Exception as e:
    print(e)
    raise e
    

# print(conn_str)
# print(conn_str_test)
