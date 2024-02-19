import re

class FileNameExtractor:
    @staticmethod
    def extract_file_name(dirty_file_name):
        match = re.search(r'[\d+]_{match}.OTHEREXTENSION', dirty_file_name))
        return match