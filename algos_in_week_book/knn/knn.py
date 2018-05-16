import math


def comparator(a,b):
    if(int(a[1])<int(b[1])): return -1
    else : return 1


def knn(training_data,k,test_data):
    #print training_data,k,test_data
    distances = find_distances(training_data,test_data)
    #print distances
    
    distances_list = [(key,val) for key,val in distances.items()]
    distances_list.sort(comparator)
    k_nearest_neighbours= distances_list[:k]
    print k_nearest_neighbours

    class_assigned = assign_class(k_nearest_neighbours);
    print class_assigned
    return class_assigned


def assign_class(k_nearest_neighbours):
    plus_class=0
    minus_class=0
    for i in k_nearest_neighbours:
        if(i[0][2]=="+"): plus_class+=1
        else: minus_class+=1

    print("plus_count is ",plus_class)
    print("minus_count is",minus_class)

    if(plus_class>minus_class): return "+"
    else: return "-"

    




def find_distances(training_data,test_data):
    dist_dict = dict()
    print "distances"
    for x,y,class_label in training_data:
        x = int(x)
        y = int(y)
        x1 = test_data[0]
        y1 = test_data[1]
        dist = math.sqrt(abs((x1-x)**2 + (y1-y)**2))

        print "(",x,y,x1,y1,")","->",dist

        dist_dict[(x,y,class_label)]=dist

    print " "
    return dist_dict
