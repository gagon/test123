import json
import os
import csv
import datetime
# required for saving json files
dirname=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')) # added after restructuring files/folders

def get_session_json():
    json_fullpath=os.path.join(dirname,r"temp\session.json")
    if os.path.isfile(json_fullpath):
        data = json.load(open(json_fullpath))
    else:
        data={}
    return data


def save_session_json(session):
    json_fullpath=os.path.join(dirname,r"temp\session.json")
    json.dump(session, open(json_fullpath, 'w'),indent=4, sort_keys=True)
    return "None"


def read_txt(file,type):
    res=[]
    with open(file, newline='') as csvfile:
        s = csv.reader(csvfile, delimiter='\n')
        for row in s:
            if type=="float":
                res.append(float(row[0]))
            elif type=="geothermal":
                r=str(row[0]).split("\t")
                res.append([float(r[0]),float(r[1])])
            else:
                res.append(row[0])
    return res


def read_pt(file):
    res=[]
    with open(file, newline='') as csvfile:
        s = csv.reader(csvfile, delimiter='\n')
        for row in s:
            r=str(row[0]).split("\t")
            t=datetime.datetime.strptime(r[0],"%m/%d/%Y %h:%M")
            t=t.strftime("%Y-%m-%d %H:%M:%S")
            res.append([t,float(r[1]),float(r[1])])

    return res

def convert_timestamps(timestamps,format1,format2):
    t_new=[]
    for t in timestamps:
        t=datetime.datetime.strptime(t,format1)
        t_new.append(t.strftime(format2))
    return t_new
