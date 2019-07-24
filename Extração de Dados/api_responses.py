import json
import requests

for i in range(1000):
    aux = input()
    response = requests.get('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=4C600DB6CDDD9A219350C6FAECBA5575&steamid='+ aux +'&format=json') #resposta da API para determinado user 
    if len(response.text) <= 15: #teste para verificar se a resposta é vazia. Se for, não é criado um arquivo
        continue
    else:
        resp = json.loads(response.text)
        games_count = resp["response"]["game_count"] #quantidade de jogos no JSON
        arq = open("/home/tunin/api_responses/" + aux + ".txt", "w+")
        for x in range(games_count):
            game = resp["response"]["games"][x]  
            if game["playtime_forever"] == 0: #se o usuário não tiver jogado determinado jogo, esse ID não será considerado
                continue
            else:    
                arq.write(str(game["appid"]))
                arq.write('\n')
        arq.close()
