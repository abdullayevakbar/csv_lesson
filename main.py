
def get_column(data):
    column_name = []
    for i in data:
        y = i.split(',')
        # print(y[1])
        column_name.append(y[1])
    return column_name


data = open('data.csv').read()
data = data.split('\n')
get_column(data)
# print(data)
