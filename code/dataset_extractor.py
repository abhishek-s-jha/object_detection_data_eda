import os
from tqdm import tqdm
from zipfile import ZipFile
from datetime import datetime

from additional_info import logs, timestamp_format

class Data_Extractor:
    def __init__(self, file_name, file_type, dest_dir):
        self.file_name = file_name
        self.file_type = file_type
        self.dest_dir = dest_dir
        self.file_loc = os.path.join(dest_dir, file_name)

    def zip_file(self):
        function_name = Data_Extractor.zip_file.__name__
        logs(datetime.now().strftime(timestamp_format), function_name, "start")

        # opening the zip file in READ mode
        with ZipFile(self.file_loc, 'r') as fp:
            # printing all the contents of the zip file
            logs(datetime.now().strftime(timestamp_format), function_name, "number of files inside = {}".format(len(fp.filelist)))
            logs(datetime.now().strftime(timestamp_format), function_name, "files info : ")
            display_line_count = 0
            for index, file in enumerate(fp.filelist):
                if display_line_count < 50:
                    logs(datetime.now().strftime(timestamp_format), function_name, "s.no. {} :: file name = {} :: size = {} kb".format(index + 1,
                                                                                                                                       file.filename,
                                                                                                                                       round((file.file_size / 1024), ndigits=2)))
                    display_line_count += 1
                else:
                    logs(datetime.now().strftime(timestamp_format), function_name, "..........")
                    logs(datetime.now().strftime(timestamp_format), function_name, "..........")
                    logs(datetime.now().strftime(timestamp_format), function_name, "..........")
                    logs(datetime.now().strftime(timestamp_format), function_name,
                         "s.no. {} :: file name = {} :: size = {} kb".format(len(fp.filelist), fp.filelist[-1].filename,
                                                round((fp.filelist[-1].file_size / 1024), ndigits=2)))

                    break
            logs(datetime.now().strftime(timestamp_format), function_name, "extracting files at {}".format(self.dest_dir))
            logs(datetime.now().strftime(timestamp_format), function_name, "extraction start")
            # extracting file to defined location
            for file in tqdm(fp.filelist, desc=self.file_name):
                fp.extract(file, path=self.dest_dir)
            logs(datetime.now().strftime(timestamp_format), function_name, "extraction stop")
        logs(datetime.now().strftime(timestamp_format), function_name, "stop")
