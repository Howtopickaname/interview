from interview import weather
import io


def test_replace_me():
    reader = io.StringIO("Station Name,Measurement Timestamp,Air Temperature,Wet Bulb Temperature,Humidity,Rain Intensity,Interval Rain,Total Rain,Precipitation Type,Wind Direction,Wind Speed,Maximum Wind Speed,Barometric Pressure,Solar Radiation,Heading,Battery Life,Measurement Timestamp Label,Measurement ID\n 63rd Street Weather Station,12/31/2016 11:00:00 PM,-1.3,-2.8,73,0.0,0.0,39.3,0.0,264,2.2,3.2,992.3,5,354.0,11.8,12/31/2016 11:00 PM,63rdStreetWeatherStation201612312300\n Foster Weather Station,12/31/2016 11:00:00 PM,-1.56,,63,,0.0,,,264,1.6,1.8,991.5,0,,14.8,12/31/2016 11:00 PM,FosterWeatherStation201612312300\n Oak Street Weather Station,12/31/2016 11:00:00 PM,-0.3,-2.2,67,0.0,0.0,135.1,0.0,334,0.9,1.7,992.6,2,0.0,12.0,12/31/2016 11:00 PM,OakStreetWeatherStation201612312300")
    writer = io.StringIO()
    weather.process_csv(reader, writer)
    assert writer.getvalue() == "Station Name,Date,Min Temp,Max Temp,First Temp,Last Temp\n 63rd Street Weather Station,12/31/2016,-1.3,-1.3,-1.3,-1.3\n Foster Weather Station,12/31/2016,-1.56,-1.56,-1.56,-1.56\n Oak Street Weather Station,12/31/2016,-0.3,-0.3,-0.3,-0.3\n"
