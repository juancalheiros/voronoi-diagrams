"""
Create Index

Usage:
    app.py [options]

Options:
    -d --data= <array of coordinates>
    --hosp=<string>

"""

from docopt import docopt

from voronoi.settings import FULL_HOSPITAL, HOSPITAL
from voronoi.diagrams_voronoi import diagrams_of_voronoi



def main(arguments): 
    hosp = arguments['--hosp']
    data = arguments['--data']

    if data != None:
        COORDINATES = data
    else:
        COORDINATES = HOSPITAL if hosp == "hospital" else FULL_HOSPITAL
        
    
    diagrams_of_voronoi(COORDINATES)
    

if __name__ == "__main__":
    arguments = docopt(__doc__)
    main(arguments)