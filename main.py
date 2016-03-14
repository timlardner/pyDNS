import os
import subprocess

def build_string(records):
    output = ""
    for line in records:
        output = output + line + "\r\n"
    return output

def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

def get_records():
    command = 'C:\\Users\\timla\\Downloads\\unbound-1.5.8\\unbound-host -v -D -t TXT keys.lardnerdesign.com'
    result = run_command(command)
    records = []
    for line in result:
        if 'secure' in line:
            keys = line.split('"')
            records.append(keys[1])
    final_string = build_string(records)
    return final_string

if __name__ == '__main__':
    print get_records()


