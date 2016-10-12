import webbrowser
import time
import os
import subprocess
import argparse

class Utilities:
    seperator_single_line = '-----------------------'
    seperator_double_line = '======================='

    reports_folder_name = "Reports"
    reconnaissance_category = "Reconnaissance"
    red_color = '\033[31m'
    blue_color = '\033[34m'
    purple_color = '\033[35m'
    def __init__(self):
        self.name = 'static class'

class Core:
    def _create_client_domain_folder(self):
        root_folder_path = self.utilities.reports_folder_name + "/" + self.company_domain_name
        if not os.path.isdir(root_folder_path):
            os.mkdir(root_folder_path)

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
                try:
                    websites[counter] = self._inject_parameter_in_file(website_line)
                    counter += 1
                except Exception as e:
                    print(self.utilities.red_color + "Error")
        return websites
        
    def _open_websites(self, websites):
        for website in websites:
            webbrowser.open_new_tab(website)

    def _start(self, commands, websites, folder_name, file_name):
        if commands == {} and websites == []:
            results = self.execute_commands(commands)
            print(results)
            self._save_results(results, folder_name, file_name)
        if websites != []:
            self._open_websites(websites)
        
    def pen_test(self, action_name, category_name):
        self._create_client_domain_folder()
        commands = self._get_commands_from_file(action_name)
        websites = self._get_websites_from_file(action_name)
        folder_name = self.utilities.reports_folder_name + "/" + self.company_domain_name + "/" + category_name
        file_name = action_name + "_report.txt"
        self._start(commands, websites, folder_name, file_name)

class Main:
    def _usage(self):
        print("Penetest Automation Tool")
        print(self.utilities.seperator_single_line)
        exit(0)

    def _print_banner(self, company_domain_name):
        print("Penetesting Client Domain Name " + company_domain_name)
        print(self.utilities.seperator_single_line)
        print()

    def _process_argument(self, args, core):
        if args.dns_test:
            core.pen_test('dns', self.utilities.reconnaissance_category)
        if args.whois_test:
            core.pen_test('whois', self.utilities.reconnaissance_category)
        if args.emails_test:
            core.pen_test('emails', self.utilities.reconnaissance_category)
        if args.socialmedia_test:
            core.pen_test('socialmedia', self.utilities.reconnaissance_category)
        if args.files_test:
            core.pen_test('files', self.utilities.reconnaissance_category)
        if args.websearch_test:
            core.pen_test('websearch', self.utilities.reconnaissance_category)

    def _initialize_arguments(self):
        parser = argparse.ArgumentParser('A Tool')
        parser.add_argument("-c", "--company", type=str, help="Client Company Domain Name")
        parser.add_argument("-dns", "--dns_test", help="Check/Test DNS security", action="store_true")
        parser.add_argument("-whois", "--whois_test", help="Check/Test WHOIS data", action="store_true")
        parser.add_argument("-emails", "--emails_test", help="Look for email addresses", action="store_true")
        parser.add_argument("-socialmedia", "--socialmedia_test", help="Social Media Search", action="store_true")
        parser.add_argument("-files", "--files_test", help="Look for juicy files", action="store_true")
        parser.add_argument("-websearch", "--websearch_test", help="Search engine search", action="store_true")

        args = parser.parse_args()

        if args.company == None:
            self._usage()

        return args
        
    def start(self):
        args = self._initialze_arguments()
        core = Core(args.company, self.utilities)
        self._print_banner(args.company)
        self._process_arguments(args, core)

if __name__ == '__main__':
    utilities = Utilities()
    main = Main(utilties)
    main.start()
