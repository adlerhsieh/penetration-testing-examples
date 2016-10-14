class Utilities:
    seperator_single_line = '-----------------------'
    seperator_double_line = '======================='

    reports_folder_name = "Reports"
    reconnaissance_category = "Reconnaissance"
    red_color = '\033[31m'
    blue_color = '\033[34m'
    purple_color = '\033[35m'

    def extract_company_name(self, domain_name):
        return domain_name.replace("http://", "").replace("https://", "")

    def __init__(self):
        self.name = 'static class'
