import argparse
import os
import json

def main(params):
    generator = Generator(params['population'])
    user_profiles = generator.generate()
    tree_system = TreeSystem(params['tree_system'], json_dir="./results/")
    for trials in range(Meta.TRIALS):
        tree_system.map_users(user_profiles)
        for epoch in range(Meta.EPOCHS):
            tree_system.let_speak()
            tree_system.dump_record(epoch) # everone's recover, pollution, population's politeness


if __name__ == '__main__':
    argparse.ArgumentParser()

    parser = argparse.ArgumentParser(description='input parameters')
    parser.add_argument('file', type=str, help='select input file')

    jsonname = parser.parse_args(['file'])
    params = json.load(jsonname)
    main(params)
