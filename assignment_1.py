from numpy import * 

def run():
    #Step 1 collecting data

    points = genfromtxt('ex1data1.txt', delimiter=',')
    
    print points
    #Step2 definning hyperparameters
    learning_rate = 0.01
    initial_b = 0
    initial_m = 0


if __name__ == '__main__':
    run()
