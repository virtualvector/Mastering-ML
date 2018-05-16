import knn
import sys
import utils

def main():
    k = int(raw_input("ENTER THE K VALUE\n"))
    test_data = [int(i) for i in raw_input().strip().split()]
    training_data = utils.load_data("input_file.txt")
    #print training_data
    knn.knn(training_data,k,test_data)
    



if __name__=='__main__':
    main()
