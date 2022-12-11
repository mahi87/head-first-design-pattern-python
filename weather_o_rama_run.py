from weather_o_rama.publisher import WeatherData as WeatherDataPublisher
from weather_o_rama.subscriber import CurrentConditionDisplay

weather_data_publisher = WeatherDataPublisher(10, 10, 100)
display = CurrentConditionDisplay()
print(display)

display.subscribe(weather_data_publisher)

weather_data_publisher.temperature = 20
weather_data_publisher.humidity = 20
weather_data_publisher.measurement_changed()

weather_data_publisher.temperature = 30
weather_data_publisher.humidity = 50
weather_data_publisher.measurement_changed()

display.unsubscribe()

weather_data_publisher.temperature = 30
weather_data_publisher.humidity = 50
weather_data_publisher.measurement_changed()