import os
import pandas as pd
import numpy as np
from functions import *

def app_pedidos_fresco(lunes,path):

  #local path
  path_formats = path + "/../Formats/formats.csv"
  # upload File paths
  path_products = path + "/Datos_para_balanza.csv"
  vpath_physical = path + "/Productos_por_proveedor_tienda.csv"
  vpath_online = path + "/Productos_por_proveedor_online.csv"

  # lpath_physical = path + "/Productos_por_proveedor_tienda.csv"
  lpath_online = path + "/Productos_por_proveedor_online.csv"

  path_fresco1 = path + "/FRESCO_1.xlsx"
  path_fresco2 = path + "/FRESCO_2.xlsx"

  # Provider paths
  provider_list_FRESCO_1 = ['Bio Trailla -Finca la Noria', 'Biomilanes S.L.','Ecoeduco','La Vall de la Casella','Pidebio','FruitalpuntBio','PAMIES VITAE (Pamies Horticoles SL)','Finca Dos Castanos']
  provider_list_FRESCO_2 = ['Biobardales -Comercial Beldrea', 'Pollos Sanchonar','Suerte Ampanera C.B.','COOPERATIVA CRICA','El Cantero de Letur','Carnes Braman','Pedaque']
  provider_dict = {
    'Bio Trailla -Finca la Noria'         : 'trailla',
    'Biomilanes S.L.'                     : 'biomilanes',
    'Ecoeduco'                            : 'ecoeduco',
    'La Vall de la Casella'               : 'casella',
    'Pidebio'                             : 'pidebio',
    'FruitalpuntBio'                      : 'fruitalpuntbio',
    'PAMIES VITAE (Pamies Horticoles SL)' : 'pamies',
    'Finca Dos Castanos'                  : 'castanos',
    'Biobardales -Comercial Beldrea'      : 'biobardales',
    'Pollos Sanchonar'                    : 'sanchonar',
    'Suerte Ampanera C.B.'                : 'ampanera',
    'COOPERATIVA CRICA'                   : 'CRICA',
    'El Cantero de Letur'                 : 'letur',
    'Carnes Braman'                       : 'braman',
    'Pedaque'                             : 'pedaque'
  }

  products = read_productos(path_products)
  products = add_provider_from_dict(products, provider_dict)
  products = add_formats(path_formats, products)

  if not lunes:
    vdata_physical = read_productos_por_proveedor(vpath_physical)
    vdata_online = read_productos_por_proveedor(vpath_online)

    # provider_list = get_provider_list(vdata_physical,vdata_online)
    fresco_1 = merge_provider_data (products, vdata_physical, vdata_online, provider_list_FRESCO_1, path_fresco1)
    fresco_2 = merge_provider_data (products, vdata_physical, vdata_online, provider_list_FRESCO_2, path_fresco2)


    for provider in sorted(fresco_1.iterkeys()):
      save_excel(path_fresco1, fresco_1[provider], provider)
    delete_blank_sheet(path_fresco1)

    for provider in sorted(fresco_2.iterkeys()):
      save_excel(path_fresco2, fresco_2[provider], provider)
    delete_blank_sheet(path_fresco2)

  # Lunes
  if lunes:

    # if os.path.exists(lpath_physical):
    #   ldata_physical = read_productos_por_proveedor(lpath_physical)
    # else:
    ldata_physical = pd.DataFrame(columns=['Proveedor','descripcion','cantidad'])
    #   print 'INFO: No hay datos de venta en tienda para el lunes. Se mostraran vacios en el fichero de salida.'

    if os.path.exists(lpath_online):
      ldata_online = read_productos_por_proveedor(lpath_online)
    else:
      ldata_online = pd.DataFrame(columns=['Proveedor','descripcion','cantidad'])
      print 'INFO: No hay datos de venta online para el lunes. Se mostraran vacios en el fichero de salida.'

    lfresco_1 = merge_provider_data (products, ldata_physical, ldata_online, provider_list_FRESCO_1, path_fresco1)
    lfresco_2 = merge_provider_data (products, ldata_physical, ldata_online, provider_list_FRESCO_2, path_fresco2)

    # add Lunes data to excel
    for provider in sorted(lfresco_1.iterkeys()): #was  fresco_1 ...
      edit_excel(path_fresco1, lfresco_1[provider], provider)

    for provider in sorted(lfresco_2.iterkeys()): #was  fresco_1 ...
      edit_excel(path_fresco2, lfresco_2[provider], provider)

    # get rows which are not in friday's dataframe (new products)
    # for provider in lfresco_1:
    #   df1 = fresco_1[provider]
    #   df2 = lfresco_1[provider]
    #   df_all = df1.merge(df2.drop_duplicates(), on=['Nombre_producto'], how='right', suffixes=('_viernes', '_lunes'), indicator=True)
    #   df_new = df_all[df_all['_merge'] == 'right_only']
    #   df_both = df_all[df_all['_merge'] == 'both']
    #   if not df_new.empty:
    #     add_new_products_excel(path_fresco1, df_new, provider)

    # for provider in lfresco_2:
    #   df1 = fresco_2[provider]
    #   df2 = lfresco_2[provider]
    #   df_all = df1.merge(df2.drop_duplicates(), on=['Nombre_producto'], how='right', suffixes=('_viernes', '_lunes'), indicator=True)
    #   df_new = df_all[df_all['_merge'] == 'right_only']
    #   if not df_new.empty:
    #     add_new_products_excel(path_fresco2, df_new, provider)
