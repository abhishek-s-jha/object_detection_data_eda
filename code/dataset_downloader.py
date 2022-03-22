import os
import requests
from tqdm import tqdm
from datetime import datetime
from additional_info import logs, timestamp_format, dataset_url, sub_dir

def dataset_downloader():
    """
    This function will download datasets mentioned in the additional_info file.
    It also creates additional directory according to the dataset if not present and download the data there.
    :return: None
    """
    function_name = dataset_downloader.__name__
    logs(datetime.now().strftime(timestamp_format), function_name, "start")
    logs(datetime.now().strftime(timestamp_format), function_name,
         "number datasets to be downloaded : {}".format(len(dataset_url)))
    logs(datetime.now().strftime(timestamp_format), function_name,
         "name of datasets to be downloaded : {}".format(list(dataset_url.keys())))

    for dataset in dataset_url:
        logs(datetime.now().strftime(timestamp_format), function_name, "download {} dataset".format(dataset))
        for url in dataset_url[dataset]:
            data_url = url
            dataset_name = dataset

            save_loc = os.path.join(sub_dir['dir_data'], dataset)
            file_name = url.split("/")[-1]
            if len(file_name) > 30:
                file_name = file_name[0:file_name.find(".zip") + 4]

            if not os.path.exists(save_loc):
                os.mkdir(save_loc)
                logs(datetime.now().strftime(timestamp_format), function_name, "{} directory created".format(dataset))
            else:
                logs(datetime.now().strftime(timestamp_format), function_name,
                     "{} directory already present".format(dataset))

            save_loc = os.path.join(save_loc, file_name)

            if not os.path.exists(save_loc):
                logs(datetime.now().strftime(timestamp_format), function_name, "requesting data")
                data = requests.get(data_url, stream=True)

                # check status code, if 200 then OK
                if data.status_code == 200:
                    logs(datetime.now().strftime(timestamp_format), function_name, "data info received")
                    # reading total size of data
                    total_length = int(data.headers.get('content-length'))
                    logs(datetime.now().strftime(timestamp_format), function_name, "name = {}".format(dataset_name))
                    logs(datetime.now().strftime(timestamp_format), function_name,
                         "save location = {}".format(save_loc))
                    logs(datetime.now().strftime(timestamp_format), function_name,
                         "dataset size = {} GB".format(round((total_length / 1024) / 1024) / 1024, ndigits=2))
                    logs(datetime.now().strftime(timestamp_format), function_name, "download start")

                    # downloading starts from here
                    progress_bar = tqdm(desc=file_name, total=total_length,unit_divisor=1024)
                    with open(save_loc, 'wb') as fp:
                        for chunk in (data.iter_content(chunk_size=1024)):
                            progress_bar.update(fp.write(chunk))
                            fp.flush()
                        del progress_bar
                        logs(datetime.now().strftime(timestamp_format), function_name, "download complete")

                else:
                    logs(datetime.now().strftime(timestamp_format), function_name, "data request failed")

            else:
                logs(datetime.now().strftime(timestamp_format), function_name,
                     "{} dataset {} file already present".format(dataset, file_name))

        logs(datetime.now().strftime(timestamp_format), function_name, "download {} dataset complete".format(dataset))

    logs(datetime.now().strftime(timestamp_format), function_name, "stop")
