import os
import json
import pandas as pd

def read_json(file_path):
    with open(file_path) as f:
        data = json.loads(f.read())
        j_obj = json.dumps(data['results'], indent=4)
    return j_obj


def json_helper(JSON_ROOT):
    df_list = []
    for file in os.listdir(JSON_ROOT):
        if '.json' in str(file):
            new_file_path = os.path.join(JSON_ROOT,file)
            new_json_contents = read_json(new_file_path)
            new_df = pd.read_json(new_json_contents)
            new_df['source'] = file
            df_list.append(new_df)
            print(str(new_file_path))
    cat_df = pd.concat(df_list)
    cat_df = cat_df.reset_index(drop=True)
    return cat_df