from cowin_api import CoWinAPI
from datetime import datetime as DateTime, timedelta as TimeDelta
import beepy as beep


def checkAvailability( available_centers ):
   
   centerarray = available_centers["centers"]
   for center in centerarray:
      center_name = center["name"]
      district_name = center["district_name"]
      sessions_array = center["sessions"]
      for session in sessions_array:
         dose1Avail = session["available_capacity_dose1"]
         if(dose1Avail > 0):
            #print('\a')
            print(dose1Avail+" 1st dose(s) available"+" at "+center_name +", district: "+district_name+" "+DateTime.today().strftime("%d-%m-%Y %H:%M:%S"))
            beep.beep(1)
            beep.beep(1)
   return


def getDateArray( numDaysToCheck ):
   dates = []
   date_1 = DateTime.today()
   for day in range(numDaysToCheck):
   	end_date = date_1 + TimeDelta(days=day)
   	date=end_date.strftime("%d-%m-%Y")
   	dates.append(date)
   return dates


# b urban - 265
# bbmp - 294
districts = ['265','294']
min_age_limit = 18  
numDaysToCheck = 7 

dates = getDateArray(numDaysToCheck)
print(".")
 

cowin = CoWinAPI()
for date in dates:
	for district in districts:
		available_centers = cowin.get_availability_by_district(district, date, min_age_limit)
		checkAvailability(available_centers)
