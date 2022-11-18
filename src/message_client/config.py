debug = True
cseBaseName = "acme-onem2m-cse-ix62mzt6pa-uc.a.run.app"    # <== Put your own ACME CSE server here
use_https = True
encoding = "ISO-8859-1"
requestIdentifier = "RoboCarClient"
controllerContainer = "control"
heartbeatContainer = "RoboCarClientHeartBeat"
trafficLightContainer = "trafficLight"
stopSignContainer = "stopSign"
originator = "CAdmin" # "RoboCar" # "CAdmin" #
releaseVersionIndicator = "3"
aeBaseName = "/cse-in/CAdmin"
logFile = "RoboCar.log" # "/home/pi/RoboCar.log"
if debug:
    retrieveDelay = 1
else:
    retrieveDelay = 0.1