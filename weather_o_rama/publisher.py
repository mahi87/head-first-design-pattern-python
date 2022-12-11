class WeatherData():
    def __init__(self,temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.subscribers = []
        
    def register_subscriber(self, obj):
        self.subscribers.append(obj)
        
    def unregister_subscriber(self, obj):
        self.subscribers.remove(obj)
        
    def notify(self):
        for subscriber in self.subscribers:
            subscriber.on_update(self.temperature, self.humidity, self.pressure)
            
    def measurement_changed(self):
        self.notify()