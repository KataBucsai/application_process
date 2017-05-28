import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))

handle_db_queries = SourceFileLoader("query_handler", current_file_path + "query_handler.py").load_module()