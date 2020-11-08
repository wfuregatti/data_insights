import xml.dom.minidom

def ret_geo(geo):
    sw_geo = {
          '1': "Canada",
          '2': "Newfoundland and Labrador",
          '3': "Prince Edward Island",
          '4': "Nova Scotia",
          '5': "New Brunswick",
          '6': "Quebec",
          '7': "Ontario",
          '8': "Manitoba",
          '9': "Saskatchewan",
          '10': "Alberta",
          '11': "British Columbia and the Territories"
    }
    return sw_geo.get(geo,"Geography Error")
    
def ret_fuel(fuel):
    sw_fuel ={
        '1': "All fuel types",
        '2': "Gasoline",
        '3': "Diesel",
        '4': "Battery electric",
        '5': "Hybrid electric",
        '6': "Plug-in hybrid electrics",
        '7': "Other fuel types"
    }
    return sw_fuel.get(fuel, "Fuel error")

def ret_vectp(vehic):
    sw_vehic = {
        '1': "Total, vehicle type",
        '2': "Passenger cars",
        '3': "Pick up trucks",
        '4': "Multi-purpose vehicles",
        '5': "Vans"
    }
    return sw_vehic.get(vehic,"Vehicle Type error")

def load():
    doc1 = xml.dom.minidom.parse("20100021_1.xml")
    veic1 = doc1.getElementsByTagName("Series")

    count = 0 
    
    for v1 in veic1:
        Geo = ret_geo(v1.getAttribute("Geography"))
        Fuel = ret_fuel(v1.getAttribute("Fuel_Type"))
        VecType = ret_vectp(v1.getAttribute("Vehicle_type"))
        List_obs = v1.getElementsByTagName("Obs")
      
        for l1 in List_obs:
            count += 1
            date = l1.getAttribute("TIME_PERIOD")
            value = l1.getAttribute("OBS_VALUE")

            print("Geography: ", Geo)
            print("Fuel_Type: ", Fuel)
            print("Vehicle_type: ", VecType)
            print("TIME_PERIOD: ", date)
            print("OBS_VALUE: ", value)
            print("--------")

    
    print("Total records: " + str(count))
          
if __name__ == "__main__":
    load()