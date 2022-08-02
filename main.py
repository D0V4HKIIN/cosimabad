import requests
import time


# field names
fields = ['']

# name of csv file
filename = "cosimabad.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    csvfile.write("time,personCount,maxPersonCount\n")

    while True:
        print("sending request")
        response = requests.get(
            "https://functions.api.ticos-systems.cloud/api/gates/counter?organizationUnitIds=30190", headers={"Abp.TenantId": "69", "Host": "functions.api.ticos-systems.cloud"}).json()[0]

        data = [str(time.time()), str(response["personCount"]),
                str(response["maxPersonCount"])]
        print(",".join(data) + "\n")

        csvfile.write(",".join(data) + "\n")
        csvfile.flush()
        time.sleep(60)
