"""
Create Index

Usage:
    app.py [options]

Options:
    -d --data= <array of coordinates>
    --hosp=<bool>
    --randon=<bool>
    --qnt_point=<int>

"""

from docopt import docopt
import numpy as np
from voronoi.settings import FULL_HOSPITAL, HOSPITAL
from voronoi.diagrams_voronoi import diagrams_of_voronoi



def main(hosp, randon, qnt_point): 
    SCALA = 100
    if randon:
        COORDINATES = np.random.rand(int(qnt_point), 2)*SCALA
    else:
        COORDINATES = HOSPITAL if hosp else FULL_HOSPITAL
        
    
    diagrams_of_voronoi(COORDINATES)
    

if __name__ == "__main__":
    arguments = docopt(__doc__)
    
    hosp = arguments['--hosp']
    randon = arguments['--randon']
    qnt_point = arguments['--qnt_point'] if arguments['--qnt_point'] else 10
    
    main(hosp, randon, qnt_point)