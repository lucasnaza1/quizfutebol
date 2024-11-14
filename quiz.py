from InquirerPy import inquirer
campeao_cdb = inquirer.select(
    message='Quem é o maior campeão da Copa do Brasil?',
    choices=['Grêmio','Flamengo','Palmeiras','Cruzeiro','Atlético Mineiro']
).execute()
if campeao_cdb == 'Cruzeiro': 
    print('Você acertou, o Cruzeiro é maior campeão da copa do Brasil com 6 titulos!')
else: print('Você errou, tente novamente!')

'''campeao_br = inquirer.select(
    message='Quem é o maior campeão do Campeonato Brasileiro?(Incluindo taça Brasil)'
    choices=['Santos','Vasco','Flamengo','Corinthians','Palmeiras']
)if campeao_br == 'Palmeiras':
    print('Você acertou, o Palmeiras é o maior campeão brasileiro com 13 títulos!')
else: print('Você errou, tente novamente')'''