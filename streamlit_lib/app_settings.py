
class AppSettings:
    tracking_file_name: str = None
    parsed_string_file_name: str = None

    def __init__(self, tracking_file_name, parsed_string_file_name):
        self.tracking_file_name = tracking_file_name
        self.parsed_string_file_name = parsed_string_file_name