import time as timeLib

def timedRun(fn, args):
    startTime = timeLib.time()
    output = fn(*args)
    endTime = timeLib.time()
    executionTime = endTime - startTime
    functionName = fn.__name__

    print(f'''Time (seconds) taken in process {fn.__name__}:   {endTime - startTime}.''')
    return {
        "output": output,
        "functionName": functionName,
        "executionTime": executionTime
    }

def saveTimeStatInCSV(csvFilePath, function_name, options, timeseries_shape, execution_time):
    file = open(csvFilePath, 'a')
    # file.write("function_name, options, timeseries_shape, execution_time")
    # file.write("\n")
        
    file.write(function_name)
    file.write(", ")
    file.write(str(options).replace(",", ";"))
    file.write(", ")
    file.write(str(str(timeseries_shape)).replace(",", ";"))
    file.write(", ")
    file.write(str(execution_time))
    file.write("\n")
    # file.close()
    
