import pandas as pd
import numpy as np
import sqlalchemy
import xlrd
from sqlalchemy import create_engine
import sys
import mysql.connector
import pymysql
from functionsss import *

# REMOTE
# mysql -u root -p6g3dMge9TCder4ks -h panel.lagarbancitaecologica.org lagarbancitaecologica_org_dolibarr 

# LOCAL
# engine = create_engine('mysql+pymysql://root:PASSWORD@localhost/dolibarr')

def report_generation(input_path, output_path):
	# SERVER Garbancita
	engine = create_engine('mysql://lagarbancitaecol:3eshMD934=6r@panel.lagarbancitaecologica.org/lagarbancitaecologica_org_dolibarr?charset=utf8mb4')
	conn = engine.connect()
	#conn = pymysql.connect(host='panel.lagarbancitaecologica.org',user='lagarbancitaecol',passwd='3eshMD934=6r',db='lagarbancitaecologica_org_dolibarr')


	# Read products table
	db_products = pd.read_sql('SELECT * FROM llx_product', conn)

	# Read provider products and buy prices table
	db_products_provider = pd.read_sql('SELECT * FROM llx_product_fournisseur_price', conn)
	db_products_provider['precio_compra_con_iva'] = db_products_provider['price'] * (1+(db_products_provider['tva_tx'].div(100)))
	db_products_provider = db_products_provider[['fk_product','precio_compra_con_iva']]
	db_products_provider = db_products_provider.rename(columns={'fk_product': 'rowid'})

	# Add precio_compra_con_iva to db_products dataframe
	db_products = db_products.merge(db_products_provider, on='rowid', how='left')


	# Read updated stocks
	product_stocks = pd.read_excel(input_path + '/product_list.xlsx')
	product_stocks = product_stocks.rename(columns={'ID': 'rowid'})
	product_stocks = product_stocks[['rowid','stock']]

	# Modify table stocks based on id
	report = pd.DataFrame()
	df_merged = db_products.merge(product_stocks, on='rowid', how='left')
	df_merged['stock'] = df_merged['stock_y'].combine_first(df_merged['stock_x'])
	report[['ID','ref','label','precio_compra_con_iva','pre-inventario','post_inventario']] = df_merged[['rowid','ref','label','precio_compra_con_iva','stock_x','stock']]
	report['diferencia'] = report['pre-inventario'] - report['post_inventario']
	df_merged = df_merged.drop(columns=['stock_x', 'stock_y'])
	db_products = df_merged

	# save report in excel
	report.to_excel(output_path + '/stock_reporte.xlsx')

	# disconnect from server
	conn.close()

	# d = {'col1': [1, 2], 'col2': [3, 4]}
	# report = pd.DataFrame(data=d)
	# report.to_excel(output_path + '/stock_reporte.xlsx')

