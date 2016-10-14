import argparse

from lib.utilities import Utilities
from lib.core      import Core

class Main:
    def __init__(self, utilities):
        self.utilities = utilities

    def _usage(self):
        print("Penetest Automation Tool")
        print(self.utilities.seperator_single_line)
        exit(0)

    def _print_banner(self, company_domain_name):
        print("Penetesting Client Domain Name " + company_domain_name)
        print(self.utilities.seperator_single_line)
        print("")

    def _process_arguments(self, args, core):
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
        if args.test_test:
            core.pen_test('test', self.utilities.reconnaissance_category)

    def _initialize_arguments(self):
        parser = argparse.ArgumentParser('A Tool')
        parser.add_argument("-c", "--company", type=str, help="Client Company Domain Name")
        parser.add_argument("-dns", "--dns_test", help="Check/Test DNS security", action="store_true")
        parser.add_argument("-whois", "--whois_test", help="Check/Test WHOIS data", action="store_true")
        parser.add_argument("-emails", "--emails_test", help="Look for email addresses", action="store_true")
        parser.add_argument("-socialmedia", "--socialmedia_test", help="Social Media Search", action="store_true")
        parser.add_argument("-files", "--files_test", help="Look for juicy files", action="store_true")
        parser.add_argument("-websearch", "--websearch_test", help="Search engine search", action="store_true")
        parser.add_argument("-test", "--test_test", help="Testing this tool is functioning", action="store_true")

        args = parser.parse_args()

        if args.company == None:
            self._usage()

        return args

    def start(self):
        args = self._initialize_arguments()
        core = Core(args.company, self.utilities)
        self._print_banner(args.company)
        self._process_arguments(args, core)

if __name__ == '__main__':
    utilities = Utilities()
    main = Main(utilities)
    main.start()
