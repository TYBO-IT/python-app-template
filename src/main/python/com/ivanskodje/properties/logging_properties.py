    
class LoggingProperties:
    logging_properties: dict

    def __init__(self, logging_properties) -> None:
        self.logging_properties = logging_properties

    
    def get_console_level(self):
        return self.logging_properties["console"]["level"]

    def get_file_level(self):
        return self.logging_properties["file"]["level"]
    
    def get_file_name(self):
        return self.logging_properties["file"]["name"]
    
    def get_file_path(self):
        return self.logging_properties["file"]["path"]