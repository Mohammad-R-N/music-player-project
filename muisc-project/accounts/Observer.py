class TemperatureDisplay:
    def update(self, temperature, humidity):
        print(f"Temperature: Temperature={temperature}, Humidity={humidity}")


class HumidityDisplay:
    def update(self, temperature, humidity):
        print(f"Humidity: Temperature={temperature}, Humidity={humidity}")


class WeatherStation:
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity)

    def set_weather(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
        self.notify()

weather_station = WeatherStation()
temperature = TemperatureDisplay()
humidity = HumidityDisplay()

weather_station.register(temperature)
weather_station.register(humidity)
weather_station.set_weather(25, 60) 
weather_station.unregister(temperature)
weather_station.set_weather(30, 55)