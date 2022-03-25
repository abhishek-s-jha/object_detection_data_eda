import os
from datetime import datetime
from additional_info import logs, timestamp_format, sub_dir
from dir_structure_generator import dir_structure_generator
from dataset_downloader import dataset_downloader
from dataset_extractor import Data_Extractor

def main():
    """
    This is the base function whill will call all other modules.
    These modules are called:
    1. data structure generator : to ensure that directory structure is correct.
    2. dataset downloader : this will download the dataset mentioned in the additional_info file.
    3. data extractor : this will extract the dataset downloaded to their respective folder as defined in additional_info file.
    :return: None
    """
    function_name = main.__name__
    logs(datetime.now().strftime(timestamp_format), function_name, "start")

    logs(datetime.now().strftime(timestamp_format), function_name, "directory structure check start")
    dir_structure_generator()
    logs(datetime.now().strftime(timestamp_format), function_name, "directory structure check stop")

    logs(datetime.now().strftime(timestamp_format), function_name, "dataset downloader start")
    dataset_downloader()
    logs(datetime.now().strftime(timestamp_format), function_name, "dataset downloader stop")

    logs(datetime.now().strftime(timestamp_format), function_name, "dataset extractor start")
    selected_dataset_loc = os.path.join(sub_dir['dir_data'], "coco")
    logs(datetime.now().strftime(timestamp_format), function_name, "selected dataset location : {}".format(selected_dataset_loc))

    # reading dataset file which we need to extract one by one
    for file in os.listdir(selected_dataset_loc):
        logs(datetime.now().strftime(timestamp_format), function_name, "current file : {}".format(file))
        data_extractor = Data_Extractor(file_name=file,
                                        file_type=file.split(".")[-1],
                                        dest_dir=selected_dataset_loc)
        logs(datetime.now().strftime(timestamp_format), function_name, "checking file type")

        # selecting files in zip format for extraction
        if data_extractor.file_type == 'zip':
            logs(datetime.now().strftime(timestamp_format), function_name, "file type : zip")
            data_extractor.zip_file()
    logs(datetime.now().strftime(timestamp_format), function_name, "dataset extractor stop")


if __name__ == '__main__':
    main()
