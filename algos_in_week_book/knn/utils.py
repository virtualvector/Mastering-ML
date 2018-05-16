def load_data(file_name):
    ll= list()
    with open(file_name,"r") as fl:
        for line in fl:
            ll.append([i for i in line.split()])

    return ll
