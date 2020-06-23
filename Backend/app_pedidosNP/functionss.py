import csv, re, os
import pandas as pd

def get_stock(filepath):
	stock = pd.read_csv(filepath, skiprows=1)
	stock.drop(['Unnamed: 4'], axis = 1, inplace = True)
	stock = stock.rename(columns={ stock.columns[1]: "descripcion" })
	stock_almacen = stock.loc[stock['Almacen'] == 'Almacen central']
	stock_sector3 = stock.loc[stock['Almacen'] == 'GAK Sector 3']

	data_stock = pd.merge(stock_sector3[['descripcion','stock']], stock_almacen[['descripcion','stock']], on='descripcion', how='outer', sort='True')
	data_stock = data_stock.rename(columns={'stock_x': 'stock_sector3', 'stock_y': 'stock_almacen'})
	data_stock = data_stock.fillna(0)

	#avoid stock = 100 or near.
	#data_stock['stock_online'].loc[data_stock['stock_online'] > 90] = data_stock['stock_online'].loc[data_stock['stock_online'] > 90] - 100

	data_stock['stock'] = data_stock['stock_sector3'] + data_stock['stock_almacen']
	data_stock = data_stock [['descripcion','stock']] #save only stock total
	return data_stock


def clean_data(filepath,provider,type_csv):
	data = pd.read_csv(filepath, skiprows=1)
	data.drop(['Unnamed: 7'], axis = 1, inplace = True)
	if type_csv is 'online':
		data = data.rename(columns={ data.columns[1]: "descripcion", data.columns[2]: "cantidad" })
	data = data[['Proveedor','descripcion','cantidad']]

	#data_provider = data.loc[data['Proveedor'] == provider]
	data_provider = data[data['Proveedor'].str.contains(provider,case=False) ==True]
	return data_provider


def get_sales(data_provider_online,data_provider_physical,months):

	items_in_common = pd.merge(data_provider_physical[['descripcion','cantidad']], data_provider_online[['descripcion','cantidad']], on=['descripcion'], how = 'outer')
	items_in_common = items_in_common.rename(columns={'cantidad_x': 'sales_physical_total', 'cantidad_y': 'sales_online_total'})
	items_in_common = items_in_common.fillna('0')
	items_in_common['sales_physical_total'] = items_in_common['sales_physical_total'].str.replace(',','.')
	items_in_common['sales_physical_total'] = items_in_common['sales_physical_total'].str.replace(' ','')
	items_in_common['sales_physical_total'] = items_in_common['sales_physical_total'].astype('float64')
	items_in_common['sales_online_total'] = items_in_common['sales_online_total'].str.replace(',','.')
	items_in_common['sales_online_total'] = items_in_common['sales_online_total'].str.replace(' ','')
	items_in_common['sales_online_total'] = items_in_common['sales_online_total'].astype('float64')

	items_in_common = items_in_common.fillna(0)

	items_in_common['sales_total'] = items_in_common['sales_physical_total'] + items_in_common['sales_online_total']

	items_in_common['sales_physical_mes'] = items_in_common['sales_physical_total'].astype('float64') / months
	items_in_common['sales_physical_mes'] = items_in_common['sales_physical_mes'].round(2)
	items_in_common['sales_online_mes'] = items_in_common['sales_online_total'].astype('float64') / months
	items_in_common['sales_online_mes'] = items_in_common['sales_online_mes'].round(2)

	items_in_common = items_in_common.fillna(0)

	items_in_common['sales_total_mes'] = items_in_common['sales_physical_mes'] + items_in_common['sales_online_mes']
	
	return items_in_common

# merge sales and stock to get buying results.
def merge_sales_stock (data_sales, data_stock):
	output = pd.merge(data_sales, data_stock, on=['descripcion'], how = 'inner') #non existent products had 0 sales 
	output['to_buy_total'] = output['sales_total'] - output['stock']
	output['to_buy_total'].loc[output['to_buy_total'] < 0] = 'No comprar'
	return output

def comparison(data_stock,df1,df2,df3):
	df1 = df1[['descripcion','sales_total_mes']]
	df1 = df1.rename(columns={'sales_total_mes': '12mo_mensual'})
	df2	= df2[['descripcion','sales_total_mes']]
	df2 = df2.rename(columns={'sales_total_mes': '3mo_pre_mensual'})
	df3	= df3[['descripcion','sales_total_mes']]
	df3 = df3.rename(columns={'sales_total_mes': '3mo_post_mensual'})

	output = pd.merge(df1, df2, on=['descripcion'], how = 'outer')
	output = pd.merge(output, df3, on=['descripcion'], how = 'outer')
	output = pd.merge(output,data_stock, on=['descripcion'], how = 'inner')
	output = output.fillna(0)
	return output