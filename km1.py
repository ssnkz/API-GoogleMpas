import googlemaps

def calcular_km_real(api_key, pontos):
    gmaps = googlemaps.Client(key=api_key)
    distancias = []
    total_km = 0.0
    total_tempo_segundos = 0 
    for i in range(len(pontos) - 1):
        origem = pontos[i]
        destino = pontos[i + 1]
        resultado = gmaps.distance_matrix(origins=origem, destinations=destino, mode="driving")
        distancia_metros = resultado['rows'][0]['elements'][0]['distance']['value']
        duracao_segundos = resultado['rows'][0]['elements'][0]['duration']['value']
        distancia_km = distancia_metros / 1000
        duracao_minutos = duracao_segundos / 60
        distancias.append((origem, destino, distancia_km, duracao_minutos))
        total_km += distancia_km
        total_tempo_segundos += duracao_segundos

    
    total_tempo_horas = total_tempo_segundos // 3600
    total_tempo_minutos = (total_tempo_segundos % 3600) // 60
    
    return distancias, total_km, total_tempo_horas, total_tempo_minutos

if __name__ == "__main__":
    API_KEY = "Sua_API"
    pontos = [
        "Exemplo: Nossa Casa (Rua Felipe...)",
        "Exemplo: Seu Trabalho (Total IP, Consolaç...)",
        "Adicione Quantos quiserem"

    ]
    
    distancias, total_km, total_horas, total_minutos = calcular_km_real(API_KEY, pontos)
    
    print("Distâncias e tempos entre os pontos:")
    for origem, destino, distancia, duracao in distancias:
        print(f"{origem} -> {destino}: {distancia:.2f} km, Tempo estimado: {duracao:.2f} minutos")
    
    print(f"\nDistância total percorrida: {total_km:.2f} km")
    print(f"Tempo total estimado: {total_horas} horas e {total_minutos} minutos")
