import collections
def main():
    get_list()



def get_list():
    list = collections.defaultdict(int)
    while True:
        try:
            item = input()
            list[item.upper()] += 1
        except EOFError:
            print()
            # sorted_dict = collections.OrderedDict(sorted(list.items()))
            # for k, v in sorted_dict.items():
            #     print(v, k)

            sorted_key = sorted(list.keys())
            sorted_dict = {k: list[k] for k in sorted_key}
            for k, v in sorted_dict.items():
                print(v, k)

            
            break

main()


"""

OrderedDict remains the order in which the keys were inserted

while deleting and re-inserting the same key will push the key to the last 
to remain the order of the insertion of the key

"""