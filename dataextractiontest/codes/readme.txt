
dependencies:

Following are the python libraries required to be installed to run the code:
pandas
googleapiclient for python (command: pip install --upgrade google-api-python-client)
bitly.py (open source bitly python api client. Attached in the zip file. It needs to be present in the directory of codes.
I have made some modifications to the code to suit the current requirement)
urllib
urllib2
json
urlparse
time

Instructions to run the code:
assign <dataloc> in mainFlow.py - path to the directory of inputfile (json input)
assign <resultsloc> in mainFlow.py - path to the directory of outputfile
assign <inpFileName> in mainFlow.py - name of the input json file containing the streaming twitter output
assign <outFileName> in mainFlow.py - name of the outputfile (csv containing the youtube links in twitter along with statistics like shares, likes, etc.)

run the code as- <python mainFlow.py>
This command needs to be executed from the code directory
