from filemodule import *
import logging

logging.basicConfig(filename=r"D:\SANTHOSH\Batches\Batch165-10am-Weekend-Python\progs\progsimple\log\run.log",format='%(asctime)s %(message)s',filemode='a')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

logger.info("Process started")

# extracts all the data from the input file in list format
filedata = extractInputData(r'D:\SANTHOSH\Batches\Batch165-10am-Weekend-Python\progs\progsimple\input\data.txt')
print(filedata)
logger.info("Extracted the data successfully")

# gets the output in dictionary format with country as key and its ips as values
allcountries = processFiledata(filedata)
print(allcountries)
logger.info(allcountries)
logger.info("Finally data bifurcation is success")

# finally write the output data in to json file
op = createOutputFile(allcountries)
print(op)
logger.info("Complete the process and created the file")

logger.info("Process Completed")