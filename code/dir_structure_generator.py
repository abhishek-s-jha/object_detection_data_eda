import os
from datetime import datetime
from additional_info import logs, sub_dir, timestamp_format, main_dir


def dir_structure_generator():
    """
    This function check the structure of the directory as defined in additional_info file.
    If there is any mismatch, it will fix it and then continue with the process.
    :return: None
    """

    function_name = dir_structure_generator.__name__
    logs(datetime.now().strftime(timestamp_format), function_name, "start")

    if not os.path.exists(main_dir):
        os.mkdir(main_dir)
        logs(datetime.now().strftime(timestamp_format), function_name, "main directory created")

        for key in sub_dir:
            os.mkdir(sub_dir[key])
            logs(datetime.now().strftime(timestamp_format), function_name, "sub directory {} created".format(key))

    else:
        logs(datetime.now().strftime(timestamp_format), function_name, "main directory present")
        for key in sub_dir:
            if not os.path.exists(sub_dir[key]):
                os.mkdir(sub_dir[key])
                logs(datetime.now().strftime(timestamp_format), function_name, "sub directory {} created".format(key))
            else:
                logs(datetime.now().strftime(timestamp_format), function_name, "sub directory {} present".format(key))

    logs(datetime.now().strftime(timestamp_format), function_name, "stop")


