import pandas as pd
def parse_chartdata(data):
    total = 0
    for e in data:
        total += int(e['value']) if e['value'] != '' else 0
    return f'{total/len(data):.2f}'

df = pd.read_json('./data_2021.json')
df['data'] = df['chartdata'].map(parse_chartdata)
df.drop(columns=['chartdata'], axis=1, inplace=True)
print(df.head())
df.to_csv('index_2021.csv', index=False)