# This versions imports records to the Cloud SQL Server 
# Running on a Free Trial Subscription on Microsoft Azure
import xml.dom.minidom
import pyodbc
import time

t0 = time.time()

server = 'tcp:wfrm.database.windows.net' 
database = 'data' 
username = 'user1' 
password = 'Vick3217' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


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

def ret_2019(vi):
    doc2 = xml.dom.minidom.parse("20100021_2.xml")
    veic2019 = doc2.getElementsByTagName("Series")
    for v2 in veic2019:
        VId2 = v2.getAttribute("VECTOR_ID")
        if VId2 == vi:
            list_obs2019 = v2.getElementsByTagName("Obs")
            dt = list_obs2019[0].getAttribute("TIME_PERIOD")
            vl = list_obs2019[0].getAttribute("OBS_VALUE")
            break
    return(dt,vl)

def load():
    doc1 = xml.dom.minidom.parse("20100021_1.xml")
    veic1 = doc1.getElementsByTagName("Series")

    count = 0 

    for v1 in veic1:
        VId = v1.getAttribute("VECTOR_ID")
        Geo = ret_geo(v1.getAttribute("Geography"))
        Fuel = ret_fuel(v1.getAttribute("Fuel_Type"))
        VecType = ret_vectp(v1.getAttribute("Vehicle_type"))
        List_obs = v1.getElementsByTagName("Obs")
      
        for l1 in List_obs:
            count += 1
            date = l1.getAttribute("TIME_PERIOD")
            value = l1.getAttribute("OBS_VALUE")
            cursor.execute("""
            INSERT INTO Vehicles VALUES (?,?,?,?,?,?)""",
            VId, Geo, Fuel, VecType, date, value)
            cnxn.commit()

        
        ReturnedTime, ReturnedValue = ret_2019(VId)
        cursor.execute("""
        INSERT INTO Vehicles VALUES (?,?,?,?,?,?)""",
        VId, Geo, Fuel, VecType, ReturnedTime, ReturnedValue)
        cnxn.commit()

    t1 = time.time()
    et = t1 - t0
    print("Elapsed Time: ", et)
    print("Total records: " + str(count))
    
              
if __name__ == "__main__":
    load()