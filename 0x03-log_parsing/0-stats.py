#!/usr/bin/python3
"""
Develop a script that reads stdin line by line to compute metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (skip the line if the format does
not match this one)
After every 10 lines or a keyboard interruption (CTRL + C),
output these statistics from the start:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
(based on the format outlined above)
Count of lines by status code:
Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500
If a status code is missing or non-integer,
don’t display anything for that status code
format: <status code>: <count>
Status codes must be printed in ascending order

line list = [<IP Address>, -, [<date>], "GET /projects/260 HTTP/1.1",
<status code>, <file size>]
"""

import sys

# store the count of all status codes in a dictionary
status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

total_size = 0
count = 0  # keep count of the number lines counted

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            # check if the status code receive exists in the dictionary and
            # increment its count
            if status_code in status_codes_dict.keys():
                status_codes_dict[status_code] += 1

            # update total size
            total_size += file_size

            # update count of lines
            count += 1

        if count == 10:
            count = 0  # reset count
            print('File size: {}'.format(total_size))

            # print out status code counts
            for key, value in sorted(status_codes_dict.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
