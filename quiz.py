from InquirerPy import inquirer
clubs = inquirer.select(
    message='Qual o seu time do coração?',
    choices=['Internacional','Grêmio','Flamengo','Palmeiras','Cruzeiro','Atlético Mineiro']
).execute()
print(f'Você é torcedor do {clubs}')