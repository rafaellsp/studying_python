import pyautogui
import random
import time

pyautogui.PAUSE = 0.8

# clicar no campo turno
pyautogui.click(x=-1347, y=478)
# clicar no turno 2 
pyautogui.click(x=-1347, y=478)
# clicar no campo cns do prof
pyautogui.click(x=-732, y=510)
# #escrever no campo cns
pyautogui.write("francismar")
#selecionar o nome no cns
pyautogui.click(x=-750, y=533)
# clicar no campo cbo
pyautogui.click(x=-582, y=507)
#selecionar no campo cbo
pyautogui.click(x=-609, y=550)
# clicar no campo atividade
pyautogui.click(x=-1360, y=871)
# scroll
pyautogui.scroll(-900)

# clicar no campo publico alvo
pyautogui.click(x=-1358, y=299)
pyautogui.click(x=-1355, y=390)
pyautogui.click(x=-1360, y=458)
# clicar no campo temas para saúde
pyautogui.click(x=-1038, y=570)
# clicar em praticas
pyautogui.click(x=-695, y=370)


# Lista de participantes com CPF e data de nascimento
"""participantes = [
    {"cpf": "703603078354435", "data_nasc": "12/01/1946"},
    {"cpf": "898050044616688", "data_nasc": "24/12/1951"},
    {"cpf": "704101656779850", "data_nasc": "18/08/1940"},
    {"cpf": "898001259015450", "data_nasc": "22/01/1969"},
    {"cpf": "898050046757246", "data_nasc": "10/02/1952"},
    {"cpf": "702809103835360", "data_nasc": "21/03/1985"},
    {"cpf": "700508519401856", "data_nasc": "17/12/1936"},
    {"cpf": "708407295166064", "data_nasc": "04/06/1955"},
    {"cpf": "708709157773495", "data_nasc": "05/07/1956"},
    {"cpf": "709202214116733", "data_nasc": "18/02/1960"},
    {"cpf": "705804471114539", "data_nasc": "24/12/1974"},
    {"cpf": "700904947194592", "data_nasc": "07/11/1956"},
    {"cpf": "700005517834706", "data_nasc": "01/09/1958"},
    {"cpf": "706600500811510", "data_nasc": "17/09/1979"},
    {"cpf": "702809103835360", "data_nasc": "21/03/1985"},
    {"cpf": "700503989386557", "data_nasc": "17/03/1988"},
    {"cpf": "700603406274160", "data_nasc": "26/07/1954"},
    {"cpf": "700404970736643", "data_nasc": "22/04/1956"},
    {"cpf": "702701162078760", "data_nasc": "05/06/1950"},
    {"cpf": "700006664236804", "data_nasc": "17/05/1976"},
    {"cpf": "704205237448688", "data_nasc": "05/11/1964"},
    {"cpf": "708103586816730", "data_nasc": "11/01/1960"},
    {"cpf": "700008472439806", "data_nasc": "14/05/1957"},
    {"cpf": "700404937849450", "data_nasc": "18/02/1970"},
    {"cpf": "706808227982723", "data_nasc": "31/08/1955"}
    
]"""


participantes = [
    {"cpf": "703267643646292", "data_nasc": "20/02/1957"},
    {"cpf": "708409221610760", "data_nasc": "29/12/1948"},
    {"cpf": "700506776237255", "data_nasc": "02/10/1953"},
    {"cpf": "700500163757259", "data_nasc": "04/10/1947"},
    
    {"cpf": "702401033910020", "data_nasc": "25/10/1951"},
    {"cpf": "708702117163193", "data_nasc": "21/11/1948"},
    {"cpf": "704605130242523", "data_nasc": "14/05/1951"},
    {"cpf": "704008811151268", "data_nasc": "02/06/1959"},
    {"cpf": "705001618640351", "data_nasc": "22/04/1958"},
    {"cpf": "708003339328927", "data_nasc": "29/07/1955"},
    {"cpf": "704605162393527", "data_nasc": "09/05/1965"},
    {"cpf": "704809026194846", "data_nasc": "25/12/1964"},
    {"cpf": "700804467599786", "data_nasc": "13/08/1947"},
   
   
    {"cpf": "700804467589780", "data_nasc": "22/03/1953"},
    {"cpf": "700500155296957", "data_nasc": "04/09/1963"},
    {"cpf": "704105454753250", "data_nasc": "02/01/1942"},
    
  
    {"cpf": "704503399000017", "data_nasc": "17/01/1967"},
    
]

# Embaralhar e selecionar aleatoriamente os participantes sem duplicatas
random.shuffle(participantes)

# Quantidade de participantes que deseja processar
num_participantes = 8  # Altere para o número desejado
selecionados = participantes[:num_participantes]

# Processo automatizado para cada participante selecionado
for participante in selecionados:
    # Clicar no campo CPF
    pyautogui.click(x=-1301, y=686)
    pyautogui.write(participante["cpf"])

    # Clicar no campo data de nascimento
    pyautogui.click(x=-1176, y=690)
    pyautogui.write(participante["data_nasc"])

    # Clicar no campo sexo
    pyautogui.click(x=-964, y=689)

    # Selecionar feminino (ajuste conforme necessário)
    pyautogui.click(x=-1042, y=734)

    # Clicar no botão confirmar
    pyautogui.click(x=-473, y=725)
    
    
    # scrol para cima
pyautogui.scroll(500)
    

# Clicar no botão de número de participantes
pyautogui.click(x=-1273, y=493)

# Clicar no botão de numero de participantes
pyautogui.write("")


"""# Esperar para simular ações mais humanas (opcional)
    time.sleep(1)"""