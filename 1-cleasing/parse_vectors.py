
'''
This script parses the feature vectors to a more suitable format

mari wahl @ 2014
'''

import math
import os
from collections import defaultdict

#FOLDERS_OUT = ['m_s5000', 'm_s500', 's_n4', 'm_s1000']
#FOLDERS_IN  = ['m_s5000/', 'm_s500/', 's_n4/', 'm_s1000/']

FOLDERS_OUT = ['n2000',   'n1500', 'n500']
FOLDERS_IN  = ['n2000/',  'n1500/', 'n500/']

SUBFOLDERS = ['atlas', 'auto', 'carbon', 'cellular', 'citation','collaboration','communication', 'ground','location','meme','metabolic','products','road','signed','social','webgraphs','wiki','yeast']
FEATURES   = ['Size', 'Order', 'Assortativity', 'Transitivity', 'Degree', 'Coreness', 'Number_Triangles', 'Number_Cliques', 'Clique_Number', 'Clustering', 'Edge_connectivity', 'Eccentricity', 'Diameter', 'Closeness', 'Betweeness', 'Density', 'Radius', 'Square_clust', 'Communicability', 'Ave_Node_conn', 'Pagerank']


def parse_feature_vector(fraw):
    '''
        Create dictionary of features
    '''
    d = defaultdict(dict)
    for line in open(fraw,'r'):
        line = line.strip('\n')
        linea = line.split(': ')
        if linea[0] != ''  and len(linea)>1 and  linea[1][0] != '[' and not math.isnan(float(linea[1])):
            #if linea[0] == 'Num_Triangles': linea[0] = 'Number_Triangles'
            #if linea[0] == 'Num_Cliques': linea[0] = 'Number_Cliques'
            d[linea[0]] = linea[1]

    return d


def save_vectors(d, output):
    '''
        Salve output vector
    '''
    with open(output, "a") as f:
        if d:
            for feat in FEATURES:
                value = d[feat]
                if value:
                    f.write( value)
                else:
                    f.write( '-')
                    #f.write( '0')
                if feat != FEATURES[-1]:
                    f.write( ',')
        f.write('\n')



if __name__ == '__main__':

    # Loop into all the data folders
    for i in range(len(FOLDERS_IN)):

        # Loop into all the network folders
        for folder in SUBFOLDERS:

            # Create the vector file and save some label info
            OUTPUT_PATH =  'vectors_neat/' + folder + '_' + FOLDERS_OUT[i] + '.data'
            with open(OUTPUT_PATH, "w") as f:
                    f.write('#')
                    for feat in FEATURES:
                        f.write(feat + ' ')
                    f.write('\n')

        # Loop again, now saving the values for each file
        for folder in SUBFOLDERS:
            
            INPUT_PATH = 'data_neat/' + FOLDERS_IN[i] + folder + '/'
            OUTPUT_PATH =  'vectors_neat/' + folder + '_' + FOLDERS_OUT[i] + '.data'

            print 'Processing ' + INPUT_PATH 
            for fraw in os.listdir(INPUT_PATH):
                    # get dictionary of values
                    d = parse_feature_vector(INPUT_PATH + fraw)

                    # save the dictionary in files
                    save_vectors(d, OUTPUT_PATH)
          


    print '\nDone!!!'