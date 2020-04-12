import json
import os


class Speech:
    def __init__(self, user)


class TreeSystem:
    def __init__(self, config, json_dir):
        self.json_dir = json_dir
        os.system("rm {}".format(os.path.join(json_dir, "/*.json")))

        self.disagree_branches = config['disagree_branches']
        self.disgust_branches = config['disgust_branches']


    def map_users(user_profiles):
        self.user_profiles = user_profiles

        num_users = len(user_profiles)
        prefix_len = len(self.disagree_branches)+len(self.disgust_branches)
        self.map_array = np.zeros((prefix_len, num_users), dtype=int)

        # random mapping policy
        digit_count = 0
        for branches in [self.disagree_branches, self.disgust_branches]:
            for i in range(len(branches)):
                temp1 = num_users // branches[i]
                temp2 = num_users % branches[i]
                ones = np.ones(temp1)
                rand = [np.random.choice(branches[i]) \
                        for _ in range(temp2)]
                ways = np.concatenate([ones*j\
                        for j in range(branches[i])])
                ways = np.concatenate([ways, rand])
                np.random.shuffle(ways)

                for iuser in range(num_users):
                    self.map_array[iuser][digit_count] = ways[iuser]

                digit_count += 1

        self.reverse_map = dict()
        for iuser in range(num_users):
            digits = ''.join( [ str(x) for x in self.map_array[iuser] ] )
            if digits in reverse_map:
                self.reverse_map[digits].append(iuser)
            else:
                self.reverse_map[digits] = iuser

        self.thres_table = dict()

    @staticmethod
    def speak(user):
        pass

    @staticmethod
    def letpass(users, speech, thres):
        pass

    @staticmethod
    def collect(node, thres_table): # node.* : children, speeches, prefix, thres
        for child in node.children:
            if child == None: continue
            collect(child)

            i = 0
            while i < len(child.speeches):
                users = []
                for prefix_key in self.reverse_map:
                    if child.prefix in prefix_key:
                        users.extend( self.reverse_map[prefix_key] )

                if TreeSystem.letpass(users, child.speeches[i], \
                                      thres=thres_table[node.prefix]):
                    node.speeches.append( child.speeches[i] )
                    del child.speeches[i]
                else:
                    i += 1


    def let_speak(self):
        branches = self.disagree_branches
        branches.extend(self.disgust_branches)

        self.speech_tree = TreeContainer(branches)

        num_users = len(self.user_profiles)
        for iuser in range(num_users):
            prefix = self.map_array[iuser]
            user = self.user_profiles[iuser]
            # user['accept']
            # user['produc']
            # user['']
            speech = TreeSystem.speak(user)
            self.speech_tree.addto(prefix, speech)

        TreeSystem.collect(self.speech_tree.root, thres_table=thres_table)


    def dump_record(self, epoch):
        # everone's recover, pollution, population's politeness
        dic = dict()
        dic['recover'] = 
        dic['pollution'] = 
        dic['politeness'] = 
        json.dump( dic, open(os.path.join(self.json_dir, "record_epoch={}.json".format(epoch)), "w") )
