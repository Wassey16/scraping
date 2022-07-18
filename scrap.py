import extract
import time

starttime = time.time()
#running scrapper from extract.py every second to extract data every second
while True:
    extract.scrapper_json()
    time.sleep(1)





