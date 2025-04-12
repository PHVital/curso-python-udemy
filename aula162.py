from datetime import datetime

data = datetime.now()
print(data.timestamp())
print(datetime.fromtimestamp(1670849077))

# data_str_data = '2024/04/20 07:49:23'
data_str_data = '2024/04/20'
data_str_fmt = '%d/%m/%Y'

# data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
# data = datetime.strptime(data_str_data, data_str_fmt)