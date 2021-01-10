import matplotlib.pyplot as plt
import numpy as np


def print_graph(java_result: list, phyton_result: list, nx_result: list, function: str):
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    plt.title(function)
    plt.xlabel('Graphs')
    plt.ylabel('Average times in seconds')
    x = ["Graph 1", "Graph 2", "Graph 3", "Graph 4", "Graph 5", "Graph 6"]

    plt.plot(x, java_result, label="java")
    plt.plot(x, phyton_result, label="phyton",linestyle='dotted')
    plt.plot(x, nx_result, label="network x", linestyle='dashed')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    print_graph([0.0, 6.666666666666667e-05, 0.001, 0.016266666666666665, 0.04753333333333333, 0.06423333333333334], [0.00016456, 0.0011549020, 0.01512, 0.1970, 0.4499, 0.708], [1.1972000000006756e-05, 2.564600000000139e-05, 6.494399999997125e-05, 0.00011, 0.000171, 0.000254], "shortest path")
    # print_graph([ 0.0, 1.0e-04, 0.0025, 0.40570000000000006, 1.2527, 3.6420000000000003], [7.75782000000036e-05 , 0.0006250449999999941, 0.007937774999999985, 0.5993829300000002, 1.839445985999999, 5.387590610000002], [9.007200000001881e-06 , 1.657400000000142e-05, 1.850000000002683e-05, 1.8359999999706388e-05, 2.5771999999903984e-05, 2.157000000151399e-05], "graph connected components")
    # print_graph([ 0.0, 1.5000000000000001E-4, 0.0025499999999999997, 0.045, 0.10515000000000001, 0.17204999999999998], [5.589019999999922e-05, 0.00046139219999999435, 0.005715402999999954, 0.07630921599999992, 0.19767955600000023 , 0.31341086799999984], [9.007200000001881e-06 , 1.657400000000142e-05, 1.850000000002683e-05, 1.8359999999706388e-05, 2.5771999999903984e-05, 2.157000000151399e-05], "Node connected components")

