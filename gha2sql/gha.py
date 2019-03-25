import os
import requests
import gzip
import json
from core import *
import pandas as pd
from functools import reduce


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


if __name__ == '__main__':
    create_dir('./tmp')
    # load the list of java_projects
    java_projects_df = pd.read_csv('../graph_data/projects.csv')
    java_projects = tuple(java_projects_df['full_name'])
    # create the queue for 1 day
    day_of_the_mounth = ( (2016, 1, day) for day in range(1,32) )
    for day in tqdm(day_of_the_mounth):
        queue = [ (*day, hour) for hour in range(24) ]
        # define the task for the threads
        event_black_list = ('WatchEvent')
        def task(year, mounth, day, hour):
            events = list()
            with GHA(year, mounth, day, hour, clean=False) as gha:
                for event in gha:
                    if event['repo']['name'] in java_projects:
                        events.append(event)
            return events
        res = multi_threading(queue, 4, task)
        create_dir('./raw')
        data_of_the_day = list(reduce(list.__add__, res.values()))
        print(len(data_of_the))
        with open('./raw/%d-%d-%d.json' % day, mode='w') as outfile:
            json.dump( data_of_the_day, outfile)
