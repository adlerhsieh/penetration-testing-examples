import webbrowser
import time
import os

from lib.terminal  import Terminal

class Core:
    def __init__(self, company_domain_name, utilities):
        self.company_domain_name = company_domain_name
        self.utilities = utilities

    def _create_client_domain_folder(self):
        root_folder_path = self.utilities.reports_folder_name + "/" + self.company_domain_name
        if not os.path.isdir(root_folder_path):
            os.makedirs(root_folder_path)

    def _inject_parameter_in_file(self, line):
        line = line.replace('[domain]', self.company_domain_name)
        line = line.replace('[name]', self.utilities.extract_company_name(self.company_domain_name))
        return line

    def _get_commands_from_file(self, action_name):
        commands = {}
        commands_file_path = self.utilities.reconnaissance_category + "/" + action_name + "_commands.txt"
        if os.path.isfile(commands_file_path):
            commands_file = open(commands_file_path, 'r')
            counter = 0
            for command_line in commands_file.readlines():
                try:
                    command_line_splitted = command_line.split(":")
                    commands[counter] = [command_line_splitted[0], self._inject_parameter_in_file(command_line_splitted[1])]
                    # commands[command_line_splitted[0]] = command_line_splitted[1]
                    counter += 1
                except Exception as e:
                    print(self.utilities.red_color + "Error")
        return commands

    def _get_websites_from_file(self, action_name):
        websites = {}
        file_path = self.utilities.reconnaissance_category + "/" + action_name + "_websites.txt"
        if os.path.isfile(file_path):
            websites_file = open(file_path, 'r')
            counter = 0
            for website_line in websites_file.readlines():
                # try:
                websites[counter] = self._inject_parameter_in_file(website_line)
                counter += 1
                # except Exception as e:
                #     print(self.utilities.red_color + "Error")
        return websites

    def _open_websites(self, websites):
        for index, website in websites.items():
            webbrowser.open_new_tab(website)
            time.sleep(4)

    def _start(self, commands, websites, folder_name, file_name):
        if websites != []:
            self._open_websites(websites)
        if commands != {}:
            terminal = Terminal(commands)
            results = terminal.execute(commands)
            print("Result: {0}".format(results))
            terminal.save_results(results, folder_name, file_name)

    def pen_test(self, action_name, category_name):
        self._create_client_domain_folder()
        commands = self._get_commands_from_file(action_name)
        websites = self._get_websites_from_file(action_name)
        folder_name = self.utilities.reports_folder_name + "/" + self.company_domain_name + "/" + category_name
        file_name = action_name + "_report.txt"
        self._start(commands, websites, folder_name, file_name)
