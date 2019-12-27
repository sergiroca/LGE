import pandas as pd
import numpy as np
import sqlalchemy
import mysql.connector
import pymysql
from functionsss import *

def generar_excels(output_path):

    # db = pymysql.connect(host='localhost',user='root',passwd='PASSWORD',db='dolibarr')
    db = pymysql.connect(host='panel.lagarbancitaecologica.org',user='lagarbancitaecol',passwd='3eshMD934=6r',db='lagarbancitaecologica_org_dolibarr')

    # cursor = db.cursor()
    # query = ("SELECT * FROM llx_categorie")
    # cursor.execute(query)
    # for r in cursor:
    #     print (r)

    # Read sql
    db_category = pd.read_sql('SELECT * FROM llx_categorie', db)
    db_category['label'] = db_category['label']

    # Get category
    category = db_category[db_category['fk_parent'] == 0]
    category = category[category['type'] == 0]

    # Get subcategory
    subcategory = db_category[db_category['fk_parent'] != 0]

    subsubcategory = []
    for index, subcategory_row in subcategory.iterrows():
        fk_parent = subcategory_row['fk_parent']
        category_row = category[category['rowid'] == fk_parent]
        category_name = category_row['label']
        category_name = category_name.values
        subcategory_name = subcategory_row['label']

        parent_subcat = subcategory.loc[subcategory['rowid'] == fk_parent]
        if parent_subcat.empty:
            subsubcategory_name = 'NaN'
        else:
            subsubcategory_name = subcategory_row['label']
            subsubcategory.append(subcategory_row)

    subsubcategory = pd.DataFrame(subsubcategory)

    category = category[['rowid', 'label']]
    subcategory = subcategory[['rowid', 'fk_parent', 'label']]
    subsubcategory = subsubcategory[['rowid','fk_parent', 'label']]

    df1 = pd.DataFrame(columns={'rowid','cat', 'subcat', 'subsubcat'})
    for index, ss_row in subsubcategory.iterrows():
        fk_parent = ss_row['fk_parent']
        s_row = subcategory.loc[subcategory['rowid'] == fk_parent]
        scat= s_row['label'].values
        fk_cat = s_row.iloc[0]['fk_parent']

        c_row = category.loc[category['rowid'] == fk_cat]
        cat = c_row['label'].values
        sscat = ss_row['label']
        df2 = pd.DataFrame(data={'rowid':ss_row['rowid'],'cat': cat, 'subcat': scat, 'subsubcat': sscat})
        df1 = df1.append(df2)

    for index, s_row in subcategory.iterrows():
        fk_parent = s_row['fk_parent']
        c_row = category.loc[category['rowid'] == fk_parent]
        cat = c_row['label'].values
        scat = s_row['label']
        df2 = pd.DataFrame(data={'rowid':s_row['rowid'],'cat': cat, 'subcat': scat, 'subsubcat': ''})
        df1 = df1.append(df2)

    for index, row in category.iterrows():
        df2 = pd.DataFrame(data={'rowid': [row['rowid']], 'cat': [row['label']], 'subcat': '', 'subsubcat': ''})
        df1 = df1.append(df2)


    df1 = df1.sort_values('rowid')
    categories = df1



    # Read sql
    db_products = pd.read_sql('SELECT * FROM llx_product', db)
    db_products = db_products[(db_products['tobuy'] == 1) | (db_products['tosell'] == 1)]
    products = db_products[['rowid','label','stock','tobuy','tosell','price_ttc','ref','barcode']]
    db_category_products = pd.read_sql('SELECT * FROM llx_categorie_product', db)
    mixtable = db_category_products[['fk_categorie','fk_product']]

    for i,row in products.iterrows():
        fk_product = row['rowid']
        match = mixtable.loc[mixtable['fk_product'] == fk_product]
        fk_categorie = match['fk_categorie']
        c_row = categories.loc[categories['rowid'].values == fk_categorie.values]
        products.at[i,'category'] = c_row.iloc[0]['cat']
        products.at[i,'subcategory'] = c_row.iloc[0]['subcat']
        products.at[i,'subsubcategory'] = c_row.iloc[0]['subsubcat']


    # reorder columns and add new (blank) columns
    products = products[['rowid','ref','label','barcode','price_ttc','stock','category','subcategory','subsubcategory']]

    # save data in inventory excels
    list_cat = products['category'].unique()
    for category in list_cat:
        product_cat = products[products['category'] == category]
        pathdir = output_path + '/inv_' + strip_accents(category) + '.xlsx'
        if os.path.exists(pathdir):
            os.remove(pathdir)

        wb = Workbook()
        wb.save(filename=pathdir)

        # load workbook
        wb = load_workbook(filename=pathdir)

        list_subcat = product_cat['subcategory'].unique()
        print list_subcat
        for subcat in list_subcat:
            product_subcat = product_cat[product_cat['subcategory'] == subcat]
            product_subcat = product_subcat.drop(columns=['category', 'subcategory', 'subsubcategory'])
            if len(subcat) > 20:
                subcat = subcat[:20]

            if subcat == '':
                subcat = 'Sin subcategoria'

            print(subcat)
            subcat = strip_accents(subcat)
            ws = wb.create_sheet(title=subcat)

            # add header
            ws.cell(row=1, column=2, value='Fecha')
            ws.cell(row=2, column=2, value='Nombre')
            ws.cell(row=3, column=2, value='Firma')
            ws.cell(row=4, column=2, value='Categoria')
            ws.cell(row=4, column=3, value=category)
            ws.cell(row=5, column=2, value='Subcategoria')
            ws.cell(row=5, column=3, value=subcat)
            ws.cell(row=6, column=1, value='ID')
            ws.cell(row=6, column=2, value='Ref')
            ws.cell(row=6, column=3, value='Descripcion')
            ws.cell(row=6, column=4, value='C. Barras')
            ws.cell(row=6, column=5, value='PVP (IVA incl.)')
            ws.cell(row=6, column=6, value='Stock Dolibarr')
            ws.cell(row=6, column=7, value='Pte Recibir')
            ws.cell(row=6, column=8, value='Tienda')
            ws.cell(row=6, column=9, value='Almacenes')
            ws.cell(row=6, column=10, value='Stock Real')
            ws['B1'].font = Font(bold=True, size=11)
            ws['B2'].font = Font(bold=True, size=11)
            ws['B3'].font = Font(bold=True, size=11)
            ws['B4'].font = Font(bold=True, size=11)
            ws['B5'].font = Font(bold=True, size=11)
            hdr_row = ws[6]
            for column in hdr_row:
                column.font = Font(bold=True, size=11)

            # add dataframe data
            rows = dataframe_to_rows(product_subcat, index=False, header=False)
            for r_idx, row in enumerate(rows, 7):
                for c_idx, value in enumerate(row, 1):
                    ws.cell(row=r_idx, column=c_idx, value=value)

            # # adjust column size
            # for col in ws.columns:
            #     max_length = 0
            #     column = col[0].column  # Get the column name
            #     for cell in col:
            #         try:  # Necessary to avoid error on empty cells
            #             if len(str(cell.value)) > max_length:
            #                 max_length = len(cell.value)
            #         except:
            #             pass
            #     adjusted_width = (max_length + 2) * 1.2
            #     ws.column_dimensions[column].width = adjusted_width

            wb.save(pathdir)
            wb.close()

        delete_blank_sheet(pathdir)

    # create product list + stock
    pathdir = output_path + '/product_list.xlsx'
    if os.path.exists(pathdir):
        os.remove(pathdir)

    wb = Workbook()
    wb.save(filename=pathdir)

    # load workbook
    wb = load_workbook(filename=pathdir)
    prod_list = products[['rowid','label','stock']]

    ws = wb.active

    # add header
    ws.cell(row=1, column=1, value='ID')
    ws.cell(row=1, column=2, value='descripcion')
    ws.cell(row=1, column=3, value='stock')
    ws['A1'].font = Font(bold=True, size=11)
    ws['B1'].font = Font(bold=True, size=11)
    ws['C1'].font = Font(bold=True, size=11)

    # add dataframe data
    rows = dataframe_to_rows(prod_list, index=False, header=False)
    for r_idx, row in enumerate(rows, 2):
        for c_idx, value in enumerate(row, 1):
            ws.cell(row=r_idx, column=c_idx, value=value)

    wb.save(pathdir)
    wb.close()


    # disconnect from server
    db.close()
