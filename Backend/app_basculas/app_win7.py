import csv
import pickle

#Open department dictionary
with open('tmp/dicc_dpt.pickle', 'rb') as handle:
	dicc_dpt = pickle.load(handle)

#Open fam dictionary
with open('tmp/dicc_fam.pickle', 'rb') as handle:
    dicc_fam = pickle.load(handle)

# Read .csv file
fileName = 'Entrada/Datos_para_balanza.csv'
with open(fileName , "rb") as f:
	data = csv.reader(f)
	rows = list(data)

rows = rows[2:] # delete header
rows = 	rows[:-1] # delete last line (blank)

output_data = []
codigos_barras = []
count_dpt = len(dicc_dpt)+1
count_fam = len(dicc_fam)+1
#create dictionary
dicc_dpt = {}
dicc_fam = {}
count_dpt = 1 #change when loading dicc
count_fam = 1 #change when loading dicc
for row in rows:
	department = row[15]
	if department in dicc_dpt:
		continue
	else:
		dicc_dpt[department] = count_dpt
		count_dpt = count_dpt + 1

for row in rows:
	family = row[16]
	if family in dicc_fam: 
		continue
	else:
		dicc_fam[family] = count_fam
		count_fam = count_fam + 1

# replace columns
	

# generate output_data
for row in rows:
	num_dpt = dicc_dpt[row[15]]
	num_fam = dicc_fam[row[16]];
	if row[12] == '':
		row[12] == 0
	else:
		row[12] = float(row[12])*100;
	row[12] = str(row[12])

	if row[3] == '0' or row[3] == '':
		row[3] = 1

	price = float(row[2]) / float(row[3]) 
	price = float('%.2f'%(price))

	if row[18] == "S" and row[19] == "S":
		a_bascula = 'S'
		if row[15] == 'Lacteos y huevos' or row[15] == 'Pescados y carne':
			Vendible = 'N'
		else:
			Vendible = 'S'
	else:
		a_bascula = 'N'
		Vendible = 'N'

	if row[19] == "S":
		row[19] = 2
	else:
		row[19] = ''

	descrip = row[13]
	descrip_abreviada = descrip[0:9]

	if len(descrip) < 6:
		graf1 = descrip
		graf2 = ''
		graf3 = ''
	elif len(descrip) < 12:
		graf1 = descrip[0:6] 
		graf2 = descrip[7:len(descrip)]
		graf3 = ''
	elif len(descrip) < 18:
		graf1 = descrip[0:6]
		graf2 = descrip[6:12]
		graf3 = descrip[13:len(descrip)]
	else:
		graf1 = descrip[0:6]
		graf2 = descrip[6:12]
		graf3 = descrip[12:18]
	if a_bascula == 'S':
		output_data.append([row[17],row[13],num_fam,1,0,0,'S',row[19],num_dpt,price,0,0,0,0,row[12],row[18],Vendible,'N',descrip_abreviada,'','',graf1,graf2,graf3,row[3],'',0,'S','S','N','N','N','N',row[13],'','','S']);
		codigos_barras.append([row[17],str(int((str(99) + str(row[17]).zfill(5) + '000000'))),0,0,2])


# write csv outputs
csvfile = "Salida/output.csv"
codfile = "Salida/cod_barras.csv"
dictionary_department = "Salida/dictionary_department.csv"	#csv fams are dptments
dictionary_fam = "Salida/dictionary_fam.csv" 		#csv subfams are fams
dictionary_subfam = "Salida/dictionary_subfam.csv"

#Assuming csvfile is a list of lists
#with open(codfile, "w") as output:
	#for entries in codigos_barras:
		#output.write(entries)
		#output.write("\r\n")
    #writer = csv.writer(output, lineterminator='\r\n')
    #writer.writerows(output_data)

with open(codfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(codigos_barras)

with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(output_data)

dicc_dpt_list = []
for key,value in dicc_dpt.iteritems():
    dicc_dpt_list.append([value,key,key[0:9]])

with open(dictionary_department, "w") as output:
	writer = csv.writer(output, lineterminator = '\n')
	writer.writerows(dicc_dpt_list)

dicc_fam_list = []
for key,value in dicc_fam.iteritems():
    dicc_fam_list.append([value,key])

with open(dictionary_fam, "w") as output:
	writer = csv.writer(output, lineterminator = '\n')
	writer.writerows(dicc_fam_list)

with open(dictionary_subfam, "w") as output:
	writer = csv.writer(output, lineterminator = '\n')
	subfam_default=[]
	subfam_default.append([1,'SUBFAMILIA 1'])
	writer.writerows(subfam_default)

with open('tmp/dicc_dpt.pickle', 'wb') as handle:
	pickle.dump(dicc_dpt, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('tmp/dicc_fam.pickle', 'wb') as handle:
	pickle.dump(dicc_fam, handle, protocol=pickle.HIGHEST_PROTOCOL)
