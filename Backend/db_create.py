#!/usr/local/bin/python
# coding: utf-8

from application import db
from application.models import Provider, User


db.create_all()

admin = User(username='Admin', email='admin@admin.com', password='sha256$RiJPq3hT$74f39e5334d7650bfb30e8294aac9b4275d304507e0e140abc2bec7c6ecebf50', user_role="ADMIN", is_active = True)
db.session.add(admin)
db.session.flush()

no_admin = User(username='no_admin', email='noadmin@admin.com', password='sha256$RiJPq3hT$74f39e5334d7650bfb30e8294aac9b4275d304507e0e140abc2bec7c6ecebf50', user_role="CUSTOMER", is_active = True)
db.session.add(no_admin)
db.session.flush()

# Add Providers
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

for item in provider_dict:
	print(provider_dict[item])

for provider in provider_list_FRESCO_1:
	provider = Provider(name = provider, keyword = provider_dict[provider], group = 1)
	db.session.add(provider)
db.session.flush()

for provider in provider_list_FRESCO_2:
	provider = Provider(name = provider, keyword = provider_dict[provider], group = 2)
	db.session.add(provider)
db.session.flush()


providersNP = [
        {
          'value': 'segura',
          'label': 'El rincón del segura'
        },
        {
          'value': 'gumendi',
          'label': 'Gumendi'
        },
        {
          'value': 'biogra',
          'label': 'Biográ'
        },
        {
          'value': 'bioprasad',
          'label': 'Bioprasad'
        },
        {
          'value': 'bailandera',
          'label': 'La Bailandera'
        },
        {
          'value': 'taibilla',
          'label': 'Valle del Taibilla'
        },
        {
          'value': 'buen',
          'label': 'El Buen Pastor'
        },
        {
          'value': 'olivateria',
          'label': 'L\'olivateria'
        },
        {
          'value': 'catxol',
          'label': 'Mas de Catxol'
        },
        {
          'value': 'agreco',
          'label': 'Agrecoastur'
        },
        {
          'value': 'biocosmetics',
          'label': 'Amapola Biocosmetics'
        },
        {
          'value': 'saper',
          'label': 'Saper'
        },
        {
          'value': 'lilliput',
          'label': 'Lilliput'
        },
        {
          'value': 'labranza',
          'label': 'Labranza Toledana'
        },
        {
          'value': 'biogredos',
          'label': 'Biogredos'
        },
        {
          'value': 'sojade',
          'label': 'Sojade'
        },
        {
          'value': 'antonio simon',
          'label': 'Antonio Simón'
        },
        {
          'value': 'meli',
          'label': 'La Abeja Meli'
        },
        {
          'value': 'asturcilla',
          'label': 'Asturcilla'
        },
        {
          'value': 'sole',
          'label': 'Chocolates Solé'
        },
        {
          'value': 'leña',
          'label': 'El horno de leña'
        },
        {
          'value': 'espanica',
          'label': 'Espanica'
        },
        {
          'value': 'pamies',
          'label': 'Pamies Vitae'
        },
        {
          'value': 'granero',
          'label': 'El granero'
        },
        {
          'value': 'herbes',
          'label': 'Herbes del Molí'
        },
        {
          'value': 'fruitalpuntbio',
          'label': 'Fruitalpuntbio'
        },
        {
          'value': 'esencia',
          'label': 'Esencia Rural'
        },
        {
          'value': 'lluna',
          'label': 'Cervezas Lluna'
        },
        {
          'value': 'pistachos',
          'label': 'Maná Pistachos'
        },
        {
          'value': 'algamar',
          'label': 'Algamar'
        },
        {
          'value': 'riet',
          'label': 'Riet Vell'
        },
        {
          'value': 'ecolecera',
          'label': 'Ecolécera'
        },
        {
          'value': 'coato',
          'label': 'Ecoato'
        },
        {
          'value': 'pandomar',
          'label': 'PanDoMar'
        },
        {
          'value': 'ecoandes',
          'label': 'Ecoandes'
        },
        {
          'value': 'verdera',
          'label': 'La verdera'
        },
        {
          'value': 'cachopo',
          'label': 'Cachopo'
        },
        {
          'value': 'biobel',
          'label': 'Biobel'
        },
        {
          'value': 'granovita',
          'label': 'Granovita'
        },
        {
          'value': 'ahimsa',
          'label': 'Ahimsa'
        },
        {
          'value': 'josenea',
          'label': 'Irati - Josenea'
        },
        {
          'value': 'copa',
          'label': 'Red Copa de Luna'
        },
        {
          'value': 'riojavina',
          'label': 'Riojavina'
        },
        {
          'value': 'colmena',
          'label': 'La Colmena'
        },
        {
          'value': 'ecorazon',
          'label': 'Ecorazón de la Mancha'
        },
        {
          'value': 'ochoa',
          'label': 'Jesús Ochoa'
        }
]

for provider in providersNP:
	provider = Provider(name = provider['label'].decode('utf-8'), keyword = provider['value'].decode('utf-8'), group = 0)
	db.session.add(provider)
db.session.flush()

try: 
	db.session.commit()
except: 
	db.session.rollback()

print("DB created.")
