import subprocess
import os

def open_terminal(app_name, cmd):
    output = "[+] Executing: {0} \r\n".format(app_name)
    try:
        process_stdout = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        output += str(process_stdout)
        output += '\r\n'
    except Exception as e:
        output += str(e)
    output += "----------------\r\n"
    return output

def execute_commands():
    commands = {"list files":"ls","current_directory":"pwd"}
    result = ''
    for key, val in commands.items():
        output = open_terminal(key, val)
        result += output
    return result

def save_results(results, folder_name, file_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    file_name = "{0}/{1}".format(folder_name, file_name)
    file_to_save = open(file_name, 'w')
    file_to_save.write(results)
    file_to_save.close()

def main():
    results = execute_commands()
    print(results)

    save_results(results, 'results', 'reports.txt')

if __name__ == '__main__':
    main()
