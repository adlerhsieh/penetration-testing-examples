import os

import subprocess

class Terminal:
    def __init__(self, commands_dict):
        self.commands = commands_dict

    def _open_terminal(self, cmd):
        output = "[+] Executed: {0} \r\n".format(cmd[1])
        print("- Analyzing: {0}".format(cmd[0]))
        if "#" in cmd[0]:
            print("Skipped.")
            print("")
            return ""
        print("- Running: {0}".format(cmd[1]))
        # try:
        process_stdout = subprocess.check_output(cmd[1], shell=True, stderr=subprocess.STDOUT)
        output += str(process_stdout)
        output += '\r\n'
        # except Exception as e:
        #     output += str(e)
        output += "----------------\r\n"
        return output

    def execute(self, commands):
        result = ''
        for index, command in self.commands.items():
            output = self._open_terminal(command)
            result += output
        return result

    def save_results(self, results, folder_name, file_name):
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        file_name = "{0}/{1}".format(folder_name, file_name)
        file_to_save = open(file_name, 'w')
        file_to_save.write(results)
        file_to_save.close()

