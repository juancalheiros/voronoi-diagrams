import os

hosp_acari=[66.9610, 747.4966]
hosp_fundao=[68.0904, 747.2955]
hosp_bonsucesso=[67.9730, 747.0264]
hosp_salgado_filho=[67.6645, 746.6516]
hosp_jesus=[68.0143, 746.5210]
hosp_pedro_ernesto=[68.0806, 746.4871]
hosp_souza_aguiar=[68.5663, 746.5527]
hosp_miguel_couto=[68.2025, 745.7857]
hospital_servidores_estado = [68.591385, 746.681259]
hospital_andarai = [67.926446, 746.345886]
hospital_ipanema = [68.496222, 745.711813]
hospital_lagoa = [68.300140, 745.940202]
hospital_cardoso_fontes = [67.278260, 746.371334]
hospital_getulio_vargas = [67.599062, 747.327643]
hospital_carlos_chagas = [66.679933, 747.049433]
hospital_anchieta = [68.274729, 746.923131]
hospital_albert_schweitzer = [65.991324, 747.039942]
hospital_pedro_ii = [63.459189, 746.554422]
hospital_lourenco_jorge = [66.781022, 745.610268]
hospital_rocha_faria = [64.754113, 746.594146]
hospital_piedade = [67.347030, 746.749239]
hospital_evandro_freire = [68.390212, 747.709636]


FULL_HOSPITAL = os.environ.get('FULL_HOSPITAL', [
    hosp_acari, hosp_fundao, hosp_bonsucesso, hosp_salgado_filho, hosp_jesus, hosp_pedro_ernesto, hosp_souza_aguiar, hosp_miguel_couto,
    hospital_servidores_estado, hospital_andarai, hospital_ipanema, hospital_lagoa, hospital_cardoso_fontes,hospital_getulio_vargas,
    hospital_carlos_chagas, hospital_anchieta, hospital_albert_schweitzer, hospital_pedro_ii, hospital_lourenco_jorge, hospital_rocha_faria,
    hospital_piedade, hospital_evandro_freire
])

HOSPITAL = os.environ.get('HOSPITAL', [ hosp_acari, hosp_salgado_filho, hosp_fundao, hosp_bonsucesso, hosp_jesus, hosp_pedro_ernesto, hosp_souza_aguiar, hosp_miguel_couto])

QNTD_POINTS = os.environ.get('QNTD_POINTS', 20)

SCALA = os.environ.get('SCALA', 100000)


