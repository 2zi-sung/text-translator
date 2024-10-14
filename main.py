import os
import time
from codes.wrapper.wrapperTranslator import WrapperTranslator

def main():
    cur_path = os.getcwd()
    code_path = os.path.join(cur_path, 'codes')
    data_path = os.path.join(cur_path, 'data')
    raw_data_folder_path = os.path.join(data_path, 'rawData')

    translator = WrapperTranslator(raw_data_folder_path, "google")
    translator.run('test_data.xlsx', data_path)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(end_time - start_time)