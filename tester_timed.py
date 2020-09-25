import time as timeLib
import json

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

def saveTimeStatInCSV(csvFilePath, function_name, hurstCoeff, statOption, options, timeseries_shape, execution_time):
    file = open(csvFilePath, 'a')
    # file.write("function_name, options, timeseries_shape, execution_time")
    # file.write("\n")

    file.write(function_name)
    file.write(", ")
    file.write(str(hurstCoeff))
    file.write(", ")
    file.write(str(options).replace(",", ";"))
    file.write("; ")
    file.write(f'stat:{statOption}')
    file.write(", ")
    file.write(str(str(timeseries_shape)).replace(",", ";"))
    file.write(", ")
    file.write(str(execution_time))
    file.write("\n")
    file.close()

def saveOutput(function_name, hurstCoeff, statOption, options, timeseries, results):
    optionsString = str(options).replace('{', '__').replace('}', '__').replace(':', '_').replace("'","")
    timeseriesShapeString = f'size_{str(timeseries.shape[0])}'
    statOptionString = f'statOption_{statOption}'
    hurstCoeffString = f'H_{hurstCoeff}'
    outputContent = {
        "timeseries": timeseries.tolist(),
        "results": str(results)
    }

    output_json_path = f'./output/jsons/{function_name}__{hurstCoeffString}__{optionsString}__{timeseriesShapeString}__{statOptionString}.json'

    file = open(output_json_path, "w+")
    json.dump(outputContent, file)
