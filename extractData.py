import re
import datetime

def extractData(input_string):
    current_date_time = datetime.datetime.now()
    formatted_date = current_date_time.strftime('%Y-%m-%d')
    formatted_time = current_date_time.strftime('%H:%M:%S')
    
    # Define a regular expression pattern to match the structure
    pattern1 = r'(\d*)([A-Za-z]+)(\d+)'
    pattern2 = r'(\d*)([A-Za-z]+) ?([A-Za-z]*)(\d+)'

    # Use re.match to find the pattern in the input string
    match1 = re.match(pattern1, input_string)
    match2 = re.match(pattern2, input_string)

    if match1:
        # Extract the groups from the match object
        id = match1.group(1)
        name = match1.group(2)
        phoneNo = match1.group(3)

        # print("ID:", id)
        # print("Name:", name)
        # print("Mobile No:", phoneNo)
        # # print(current_date_time)
        if id:
            l = [id, name, phoneNo, formatted_date, formatted_time]
        else:
            l = [name, phoneNo, formatted_date, formatted_time]
        return l
    elif match2:
        # Extract the groups from the match object
        id = match2.group(1)
        first_name = match2.group(2)
        last_name = match2.group(3)
        if last_name == '':
            name = first_name
        else:
            name = first_name + ' ' + last_name
        phoneNo = match2.group(4)
        # print("ID:", id)
        # print("Name:", name)
        # print("Mobile No:", phoneNo)
        # # print(current_date_time)
        if id:
            l = [id, name, phoneNo, formatted_date, formatted_time]
        else:
            l = [name, phoneNo, formatted_date, formatted_time]
        return l
    else:
        print("Pattern not found in the input string")

# print(extractData("Jeetha lal 855551654646"))
