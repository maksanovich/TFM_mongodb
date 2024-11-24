import sys

sys.path.append('../plg_UBUNTU/')
from a00_items import *


def LIST_read_csv_server(file_paths: List[str]):
    try:
        df = pd.concat(map(pd.read_csv, file_paths), ignore_index=True)

        # Remove duplicates
        df.drop_duplicates(inplace=True)

        # Convert the merged DataFrame to a list of dictionaries
        LIST_data = df.to_dict(orient='records')

        return LIST_data

    except Exception as e:
        print(f"An error occurred: {e}")

        return None


def read_csv(file_paths):
    try:
        LIST_data = pd.read_csv(file_paths)

        return LIST_data

    except Exception as e:
        print(f"An error occurred: {e}")

        return None
