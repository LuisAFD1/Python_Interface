import Adafruit_DHT
import time
import matplotlib.pyplot as plt

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

def read_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return temperature, humidity
    else:
        return None

# Definimos los valores iniciales de la gráfica
x_data, temp_data, hum_data = [], [], []
fig, ax = plt.subplots(1, 1)
temp_line, = ax.plot(x_data, temp_data, 'b-', label='Temperature')
hum_line, = ax.plot(x_data, hum_data, 'g-', label='Humidity')
ax.legend(loc='upper left')
ax.set_ylim([0, 100])

# Iniciamos la gráfica
plt.ion()
plt.show()

# Comenzamos a leer y graficar los datos cada segundo
while True:
    try:
        sensor_data = read_sensor()
        if sensor_data is not None:
            temp, hum = sensor_data
            print(f'Temperature: {temp:.1f}°C, Humidity: {hum:.1f}%')

            # Agregamos los datos a los arrays y actualizamos la gráfica
            x_data.append(time.time())
            temp_data.append(temp)
            hum_data.append(hum)
            ax.relim()
            ax.autoscale_view()

            temp_line.set_xdata(x_data)
            temp_line.set_ydata(temp_data)
            hum_line.set_xdata(x_data)
            hum_line.set_ydata(hum_data)

            fig.canvas.draw()
            fig.canvas.flush_events()

        time.sleep(1)

    except KeyboardInterrupt:
        break

# Detenemos la gráfica
plt.ioff()
plt.show()
