import os
import json
from time import sleep


config = json.loads(open('config.json', 'r').read())
path = config['path']

'''
####################
Created: Ducky.py
Data: 09/02/22
####################
'''

#list_ls = os.listdir(path)

def main():
    name_project = input('Nome do projeto: ')
    try:
        os.mkdir(f'{path}/{name_project}')
        sleep(1)
        print(f'[ LOG ] {name_project} Criado com sucesso')
        os.mkdir(f'{path}/{name_project}/modules')
        sleep(1)
        print(f'[ LOG ] {name_project}/modules Criado com sucesso')
        os.system(f'echo "" > {path}/{name_project}/main.py')
        sleep(1)
        print(f'[ LOG ] {name_project}/main.py Criado com sucesso')
        os.system(f'echo "" > {path}/{name_project}/modules/__init__.py')
        sleep(1)
        print(f'[ LOG ] {name_project}/modules/__init__.py Criado com sucesdo')
        print(f'[{name_project}] Projeto criado com sucesso :)')
    except:
        print('[ ERROR ] Este projeto ja existe ou o nome é invalido')
        main()

main()