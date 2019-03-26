import os
import requests
import gzip
import json
from core import *
import pandas as pd
from functools import reduce
from calendar import monthrange


class GHA:

    def __init__(self, year, mounth, day, hour, clean=True):
        self.year = year
        self.mounth = mounth
        self.day = day
        self.hour = hour
        self.data = None
        self.clean = clean


    def get_gz_path(self):
        return f'./tmp/{self.year}-{self.mounth:02}-{self.day:02}-{self.hour}.json.gz'


    def clean_files(self):
        os.remove(self.get_gz_path())


    def download(self):
        url = f'http://data.gharchive.org/{self.year}-{self.mounth:02}-{self.day:02}-{self.hour}.json.gz'
        r = requests.get(url)
        with open(self.get_gz_path(), 'wb') as f:
            f.write(r.content)


    def is_dowloaded(self):
        return os.path.exists(self.get_gz_path())


    def __read_gz(self):
        if not self.is_dowloaded():
            self.download()
        try:
            file_content = ''
            with gzip.open(self.get_gz_path(), 'rb') as f:
                file_content = f.read()
            return file_content.decode("utf-8")
        except OSError:
            return ''


    def read(self):
        self.raw_data = self.__read_gz()
        self.raw_lines = self.raw_data.split('\n')
        self.data = [ json.loads(line) for line in self.raw_lines if len(line) >= 2 ]
        self.df = pd.DataFrame.from_dict(self.data)
        return self.data


    def __len__(self):
        if self.data is None:
            self.read()
        return len(self.data)


    def __iter__(self):
        if self.data is None:
            self.read()
        return ( line for line in self.data )


    def __enter__(self):
        return self


    def __exit__(self, type, value, traceback):
        if self.clean:
            self.clean_files()

def get_schema():
    schema = open_json('./schema.json')
    return [ element['name'] for element in schema ]

def download_day(year, month, day, java_projects):
    queue = [ (year, month, day, hour) for hour in range(24) ]
    # define the task for the threads
    event_black_list = ('WatchEvent')
    def task(year, mounth, day, hour):
        events = list()
        with GHA(year, mounth, day, hour, clean=False) as gha:
            gha.read()
            events = gha.df[gha.df.repo.apply(lambda x: x['name'] in java_projects)]
        return events
    res = multi_threading(queue, 4, task)
    return reduce(lambda x,y: x.append(y, ignore_index=True), res.values())


def download_mounth(year, month, java_projects):
    number_of_days = monthrange(year, month)[1] # (weekday of the first day, number of days)
    day_of_the_mounth = [ (2016, 1, day) for day in range(1,number_of_days+1) ]
    create_dir('./raw/')
    for day in tqdm(day_of_the_mounth):
        data_of_the_day = download_day(*day, java_projects)
        data_of_the_day.to_csv('./raw/%d-%d-%d.csv' % day)
        # with open('./raw/%d-%d-%d.json' % day, mode='w') as outfile:
        #     json.dump( data_of_the_day, outfile)

        # fieldnames = tuple(data_of_the_day[0].keys())
        # print(fieldnames)
        # with open('./raw/%d-%d-%d.csv', mode='w') as csv_file:
        #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        #     writer.writeheader()
        #     for row in data_of_the_day:
        #         writer.writerow(row)
if __name__ == '__main__':
    create_dir('./tmp')
    # load the list of java_projects
    java_projects_df = pd.read_csv('../graph_data/projects.csv')
    java_projects = tuple(java_projects_df['full_name'])
    schema = get_schema()
    # with GHA(2016, 1, 1, 1, clean=False) as gha:
    #     gha.read()
    #     # print(gha.df[gha.df.repo.apply(lambda x: x['name'] in java_projects)])
    # create the queue for 1 day
    # download_day(2016, 1, 1, java_projects).to_csv('./raw/test.csv')
    # print(schema)
    download_mounth(2016,1, java_projects)
