
import json
import os


if __name__ == '__main__':
    jsonname = input("jsonname: ")
    dic = {\
        'tree_system':{
            'disgust_branches': [3],
            'disagree_branches': [3],
        },
        'population':{
            'num_users': 100,
            'num_opinions': 100,
            'mean_acceptable': 1,
            'dev_acceptable': 2,
            'mean_speech_per_epoch': 10,
            'dev_speech_per_epoch': 5,
        },
    }
    json.dump(dic, open("{}.json".format(jsonname), "w"))
