# covid-vaccine-slots-finder
Customizable Code to check the slots for vaccine for next few days in India.

Configurations:
1. Choose dose 1 or dose 2
2. Choose a district or set of districts to check
3. Choose the number of days to check for availability
4. Choose how frequently to check for slots, per minute or 5 mins

Please make sure the python package is installed:
https://pypi.org/project/CoWIN-API-by-Kunal-Kumar-Sahoo/


Its basic currently, will be adding more functionality going forward.
Contributions are welcome!


**Instructions to run:**

1. git clone https://github.com/raviorteja/covid-vaccine-slots-finder.git
2. cd covid-vaccine-slots-finder
3. chmod +x runScript.sh 
4. nohup ./runScript.sh &
5. tail -f nohup.out for checking the output.

The script runs every 1 min and beeps when there is an availability.
Please edit the file when you want to run it for different districts, or age groups.

