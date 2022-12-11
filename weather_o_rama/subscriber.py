class CurrentConditionDisplay():
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.publisher = None
    
    def __eq__(self, other):
        return self.temperature == other.temperature and \
            self.humidity==other.humidity and self.publisher==other.publisher
        
    def __str__(self) -> str:
        return f"<CurrentCondition: temp: {self.temperature}, humidity: {self.humidity}>"
        
    def on_update(self, temperature,humidity,pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()
    
    def subscribe(self, publisher):
        self.publisher = publisher
        self.publisher.register_subscriber(self)
    
    def unsubscribe(self):
        self.publisher.unregister_subscriber(self)
        
    def display(self):
        print('Current Temp: {}, Humidity: {}'.format(self.temperature,self.humidity))