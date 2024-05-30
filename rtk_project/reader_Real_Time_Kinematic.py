import serial
import pynmea2
import folium

def read_rtk_data(port, baudrate):
    points = []
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        print(f"Conectado ao dispositivo RTK na porta {port} com baudrate {baudrate}")

        while True:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line.startswith('$'):
                try:
                    msg = pynmea2.parse(line)
                    if isinstance(msg, pynmea2.types.talker.GGA):
                        point = {
                            'latitude': msg.latitude,
                            'longitude': msg.longitude,
                            'altitude': msg.altitude,
                        }
                        points.append(point)
                        print(f"Dados captados: {point}")

                        # Para evitar um loop infinito no exemplo, vamos parar após 10 pontos
                        if len(points) >= 10:
                            break
                except pynmea2.ParseError as e:
                    print(f"Erro ao parsear a linha NMEA: {e}")

    except serial.SerialException as e:
        print(f"Erro ao acessar a porta serial: {e}")
    except KeyboardInterrupt:
        print("Leitura interrompida pelo usuário.")
    finally:
        ser.close()
        print("Conexão serial fechada.")
    return points

def create_map(points, output_file='map.html'):
    if not points:
        print("Nenhum ponto captado para mapear.")
        return

    # Usa o primeiro ponto como centro do mapa
    center_lat = points[0]['latitude']
    center_lon = points[0]['longitude']

    m = folium.Map(location=[center_lat, center_lon], zoom_start=15)

    for point in points:
        folium.Marker(
            location=[point['latitude'], point['longitude']],
            popup=f"Altitude: {point['altitude']}m"
        ).add_to(m)

    m.save(output_file)
    print(f"Mapa salvo como {output_file}")

if __name__ == "__main__":
    # Substitua 'COM3' pela porta serial correta e 9600 pelo baudrate correto do seu dispositivo RTK
    points = read_rtk_data(port='COM3', baudrate=9600)
    create_map(points)
