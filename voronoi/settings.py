import os

hosp_acari=[66.9610, 747.4966]
hosp_fundao=[68.0904, 747.2955]
hosp_bonsucesso=[67.9730, 747.0264]
fiocrus=[68.0452, 746.8814]
hosp_salgado_filho=[67.6645, 746.6516]
hosp_jesus=[68.0143, 746.5210]
hosp_pedro_ernesto=[68.0806, 746.4871]
hosp_souza_aguiar=[68.5663, 746.5527]
hosp_miguel_couto=[68.2025, 745.7857]
hosp_camp_maracana=[68.1224, 746.5115]
hosp_camp_leblon=[68.1952, 745.7586]
hosp_camp_riocentro=[66.2843, 745.7806]
hosp_camp_parque_atletas=[66.3299, 745.7940]

#full
COORDINATES = os.environ.get('COORDINATES', [ hosp_acari, hosp_salgado_filho, hosp_fundao, hosp_bonsucesso, hosp_jesus, hosp_pedro_ernesto, hosp_camp_maracana, hosp_souza_aguiar, hosp_miguel_couto, hosp_camp_leblon, hosp_camp_riocentro, hosp_camp_parque_atletas])

#hosp
#COORDINATES = os.environ.get('COORDINATES', [ hosp_acari, hosp_salgado_filho, hosp_fundao, hosp_bonsucesso, hosp_jesus, hosp_pedro_ernesto, hosp_souza_aguiar, hosp_miguel_couto])


QNTD_POINTS = os.environ.get('QNTD_POINTS', 20)

SCALA = os.environ.get('SCALA', 100000)

PATH_SAVE = OPACITY = os.environ.get('PATH_SAVE','./voronoi/images/diagram_of_voronoi.png')

