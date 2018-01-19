import pandas as pd

log_data = pd.read_csv('../data/mp/SELECT___from_vendas_log.csv')

print(log_data.groupby(log_data.columns[2]).count())