# # Shop order prediction for all products that has stock (not all products!)
import os
import csv, re, os
import pandas as pd
from functionss import *

def app_pedidosNP(provider, path):
	# select provider
	# provider = 'segura'

	# get stock
	# stock_path = os.path.join(application.root_path, '../Documents/Datos_para_balanza')
	stock_path = path + "/Products_Stocks.csv"
	data_stock = get_stock(stock_path)

	# 12 meses
	online_path = path + "/sales_online_12months.csv"
	physical_path = path + "/sales_physical_12months.csv"
	months = 12

	data_online = clean_data(online_path,provider,'online')
	data_physical = clean_data(physical_path,provider,'physical')
	data_sales = get_sales(data_online,data_physical, months)
	output_12months = merge_sales_stock(data_sales,data_stock)

	# 3 meses antes
	online_path = path + "/sales_online_3months_prior.csv"
	physical_path = path + "/sales_physical_3months_prior.csv"
	months = 3

	data_online = clean_data(online_path,provider,'online')
	data_physical = clean_data(physical_path,provider,'physical')
	data_sales = get_sales(data_online,data_physical, months)
	output_3months_prior = merge_sales_stock(data_sales,data_stock)

	# 3 meses despues
	online_path = path + "/sales_online_3months_after.csv"
	physical_path = path + "/sales_physical_3months_after.csv"
	months = 3

	data_online = clean_data(online_path,provider,'online')
	data_physical = clean_data(physical_path,provider,'physical')
	data_sales = get_sales(data_online,data_physical, months)
	output_3months_after = merge_sales_stock(data_sales,data_stock)

	# Comparison
	data_compare = comparison(data_stock, output_12months, output_3months_prior, output_3months_after)


	# if output file exist, remove it.
	if os.path.exists(path + '/../Salida/output.xlsx'):
		os.remove(path + '/../Salida/output.xlsx')

	writer = pd.ExcelWriter(path + '/../Salida/output.xlsx')
	print provider

	# RENAME COLUMNS
	output_12months = output_12months.rename(columns={'descripcion': 'Nombre_producto', 'sales_total': 'ventas_periodo', 'sales_total_mes': 'ventas_mensuales','to_buy_total': 'pedido_periodo'})
	output_3months_prior = output_3months_prior.rename(columns={'descripcion': 'Nombre_producto', 'sales_total': 'ventas_periodo', 'sales_total_mes': 'ventas_mensuales','to_buy_total': 'pedido_periodo'})
	output_3months_after = output_3months_after.rename(columns={'descripcion': 'Nombre_producto', 'sales_total': 'ventas_periodo', 'sales_total_mes': 'ventas_mensuales','to_buy_total': 'pedido_periodo'})

	# print certain columns only
	output_12months[['Nombre_producto','ventas_periodo','ventas_mensuales','stock']].to_excel(writer,'12 meses')
	output_3months_prior[['Nombre_producto','ventas_periodo','ventas_mensuales','stock']].to_excel(writer,'3 meses antes')
	output_3months_after[['Nombre_producto','ventas_periodo','ventas_mensuales','stock']].to_excel(writer,'3 meses despues')
	data_compare.to_excel(writer,'Comparativa')

	writer.save()
