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


def update_stock(input_path):
	# SERVER Garbancita
	engine = create_engine('mysql://lagarbancitaecol:3eshMD934=6r@panel.lagarbancitaecologica.org/lagarbancitaecologica_org_dolibarr')
	conn = engine.connect()
	#conn = pymysql.connect(host='panel.lagarbancitaecologica.org',user='lagarbancitaecol',passwd='3eshMD934=6r',db='lagarbancitaecologica_org_dolibarr')



	# Read table
	db_products = pd.read_sql('SELECT * FROM llx_product', conn)

	# Read updated stocks
	#path = 'output/product_list.xlsx'
	product_stocks = pd.read_excel(input_path + '/product_list.xlsx')
	product_stocks = product_stocks.rename(columns={'ID': 'rowid'})
	product_stocks = product_stocks[['rowid','stock']]

	# Modify table stocks based on id
	report = pd.DataFrame()
	df_merged = db_products.merge(product_stocks, on='rowid', how='left')
	df_merged['stock'] = df_merged['stock_y'].combine_first(df_merged['stock_x'])
	report[['ID','ref','label','stock_anterior','stock_actualizado']] = df_merged[['rowid','ref','label','stock_x','stock']]
	report['diferencia'] = report['stock_anterior'] - report['stock_actualizado']
	df_merged = df_merged.drop(columns=['stock_x', 'stock_y'])
	db_products = df_merged


	# send table to sql (and replace existing table)
	###conn.execute('CREATE TABLE llx_product_temp LIKE llx_product')
	db_products.to_sql('llx_product_temp', conn, if_exists='replace', index=False)
	sql 	= " UPDATE llx_product AS f join llx_product_temp AS t  on f.rowid = t.rowid  SET f.stock = t.stock "
	sql2 	= " UPDATE llx_product_stock AS f join llx_product_temp AS t  on f.fk_product = t.rowid AND f.fk_entrepot=1 SET f.reel = t.stock "
	sql3 	= " UPDATE llx_product_stock AS f join llx_product_temp AS t  on f.fk_product = t.rowid AND f.fk_entrepot=2 SET f.reel = 0 "
	sql4 	= " UPDATE llx_ecom_product AS f join llx_product_temp AS t  on f.doli_product = t.rowid AND t.NoStock=1 SET f.site_stock = t.stock "
	print 'ok connection to sql!!'
	with engine.begin() as conn:
	   conn.execute(sql)
	   conn.execute(sql2)
	   conn.execute(sql3)
	   conn.execute(sql4)

	# disconnect from server
	conn.close()



# ############# Clone table and all table attributes/column types/formats, etc keeping ut8_general_ci

# ### ojo cuidao https://dev.mysql.com/doc/refman/8.0/en/create-table-like.html
# # (on mysql CMD shell docker)
# # CREATE TABLE new_table LIKE original_table;
# ####### INSERT new_table SELECT * FROM original_table;
