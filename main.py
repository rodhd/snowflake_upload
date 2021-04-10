# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from utils.data_read import read_data


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_path = "/Users/user/Projects/personal/snowflake_upload/data/test.xlsx"
    schema_path = "/Users/user/Projects/personal/snowflake_upload/schemas/schema.csv"
    data_output = "/Users/user/Projects/personal/snowflake_upload/output/result.csv"
    log_output = "/Users/user/Projects/personal/snowflake_upload/output/log.csv"

    read_data(data_path,schema_path,data_output,log_output)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
