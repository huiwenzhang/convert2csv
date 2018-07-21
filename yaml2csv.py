#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Parse the yaml file, extract useful data and store in csv format
"""

import argparse
import os
import yaml
import pandas as pd

def parse_yaml(directoryName, out):
    if not os.path.isdir(directoryName):
        print "Directory is not exist"
        exit(0)
    filesName = [f for f in os.listdir(directoryName) if os.path.isfile(os.path.join(directoryName, f))
                 and f.startswith('demo')]
    for f in filesName:
        with open(os.path.join(directoryName, f)) as ss:
            yaml_dict = yaml.load(ss)
            joint_data = yaml_dict['play_motion']['motions']['LBD_1X']['points']
            joint_name = yaml_dict['play_motion']['motions']['LBD_1X']['joints']
            joint_mat = [[pos_dict['time_from_start']] + pos_dict['positions'] for pos_dict in joint_data]
            my_df = pd.DataFrame(joint_mat)
            out_name = f.split('.')[0] + '.csv'

            if out is None:
                path = os.path.join(directoryName, out_name)
            else:
                path = os.path.join(out, out_name)
            my_df.to_csv(path, index=False, header=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, type=str, help="Please input the folder name where yaml files are sotored")
    parser.add_argument('--out', default=None, type=str, help="Folder name used for store parsed csv files")
    args = parser.parse_args()

    input = args.input
    out = args.out
    parse_yaml(input, out)