import requests

# Send a GET request to the website
url = "https://raw.githubusercontent.com/rackerlabs/rs-flex-uptime/refs/heads/master/README.md"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    uptxt = 'All systems operational'
    degradedtxt = 'Degraded performance'
    fullouttxt = 'Complete outage'
    partialouttxt = 'Partial outage'
    outdict = {"schemaVersion": 1,
              "label": "status",
              "message": "operational",
              "color": "brightgreen"
              }
    if degradedtxt in response.content:
        outdict['message'] = 'degraded'
        outdict['color'] = 'yellow'
    elif fullouttxt in response.content:
        outdict['message'] = 'outage'
        outdict['color'] = 'red'
    elif partialouttxt in response.content:
        outdict['message'] = 'partial outage'
        outdict['color'] = 'orange'
else:
    print("Failed to retrieve the website")

f = open("status.txt", "w")
f.write(str(outdict))
f.close()
