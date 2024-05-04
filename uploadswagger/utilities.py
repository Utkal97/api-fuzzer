import re
def filterAndGroupLines(lines):
    groupedLines = []

    currentLine = {}

    for line in lines:
        if ("->" in line):
            currentLine["endPoint"] = line
        elif ("PREVIOUS RESPONSE" in line):
            currentLine["response"] = line
        elif ("producer_timing_delay" in line) or ("max_async_wait_time" in line):
            pass
        else:
            if "endPoint" in currentLine and "response" in currentLine:
                groupedLines.append(currentLine)
            currentLine = {}

    return groupedLines


def parseChecker(filename=""):

    # Remove this filepath and call the function with required filepath
    # filename = "../media/example_files/DataDrivenChecker_20x_1.txt"
    f = open(filename, "r")
    match = re.match(r'^[^_]*', filename)
    if match:
        checkerName = match.group(0)
    f = open(filename, "r")

    try:
        if f.readable()==False:
            raise Exception("File is not readable")
        
        reportLines = f.readlines()
        
        reportedError = filterAndGroupLines(reportLines)
        errors = []

        for group in reportedError:
            
            endPointItems = group['endPoint'].split(" ")
            endPointHttpMethod = endPointItems[1]
            endPoint = endPointItems[2]

            responseItems = group['response'].split(" ")
            responseCode = responseItems[3]
            responseValue = responseItems[5]
            
            error = {
                'httpMethod': endPointHttpMethod,
                'endPoint': endPoint, 
                'statusCode': responseCode, 
                'response': responseValue,
                'checker': checkerName
                }

            errors.append(error)
            
        return errors
        
    except Exception as error:
        print(error)
    finally:
        f.close()

#parseChecker()