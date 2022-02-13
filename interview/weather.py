import pandas as pd
def process_csv(reader, writer):
    df = pd.read_csv(reader, dtype={'Air Temperature': float})
    df['Datetime'] = pd.to_datetime(df['Measurement Timestamp'], format='%m/%d/%Y %I:%M:%S %p')
    df['Date'] = df['Datetime'].dt.strftime('%m/%d/%Y')
    df.sort_values(['Station Name', 'Datetime'])
    res = df.groupby(['Station Name', 'Date'])['Air Temperature'].agg(['min', 'max', 'first', 'last'])
    res = res.rename(columns={'min': 'Min Temp', 'max': 'Max Temp', 'first': 'First Temp', 'last': 'Last Temp'})
    csv = res.to_csv(date_format='%m/%d/%Y')
    writer.write(csv)
