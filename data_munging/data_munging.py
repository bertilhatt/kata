import os
import pandas as pd

folder = ''


class Source:
    def __init__(self):
        self.data_frame = pd.DataFrame()

    def open_file_fwf(self, file_name, col_spec):
        with open(os.path.join(folder, file_name), 'r') as file:
            self.data_frame = pd.read_fwf(file, colspecs=col_spec)

    def replace_col_int(self, source, target):
        data_clean = self.data_frame[source].str.replace('\D+', '')
        empty = (data_clean == '')
        self.data_frame.drop(self.data_frame[empty].index, inplace=True)
        data_clean.drop(data_clean[empty].index, inplace=True)
        self.data_frame[target] = data_clean.astype(int)

    def find_least_diff(self, a, b, c):
        self.replace_col_int(a, 'a')
        self.replace_col_int(b, 'b')
        self.data_frame['diff'] = self.data_frame['a'] - self.data_frame['b']
        arg_min = (self.data_frame['diff'] == min(abs(self.data_frame['diff'])))
        return self.data_frame[arg_min][c].values[0]


if __name__ == '__main__':
    weather_col_spec = [
        (0, 3), (4, 9), (10, 15), (16, 21), (22, 28),
        (29, 33), (34, 38), (39, 44), (45, 51), (52, 56),
        (57, 61), (62, 65), (66, 69), (70, 74), (75, 78),
        (79, 82), (83, 88),
    ]
    weather = Source()
    weather.open_file_fwf('weather.dat', weather_col_spec)
    print(weather.find_least_diff(a='MxT', b='MnT', c='D'))

    football_col_spec = [
        (0, 7), (7, 23), (23, 29), (29, 33), (33, 39),
        (39, 45), (49, 56), (56, 62),
    ]
    football = Source()
    football.open_file_fwf('football.dat', football_col_spec)
    print(football.find_least_diff(a='A', b='F', c='Team'))
