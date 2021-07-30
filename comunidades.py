import sys, os, django, json, time 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hamsterserv.settings")
django.setup()

from suir.models import Municipio, Comunidad

json_mun = '''[
    {
      "nombre" : "Bluefields",
      "nombre_corto" : "bef",
      "region" : "raccs",
      "area" : 47775,
      "poblacion" : 49909
    },
    {
      "nombre" : "Corn Island",
      "nombre_corto" : "cis",
      "region" : "raccs",
      "area" : 9,
      "poblacion" : 7600
    },
    {
      "nombre" : "Desembocadura de Rio Grande",
      "nombre_corto" : "drg",
      "region" : "raccs",
      "area" : 1738,
      "poblacion" : 3957
    },
    {
      "nombre" : "Kukra Hill",
      "nombre_corto" : "khl",
      "region" : "raccs",
      "area" : 1193,
      "poblacion" : 9783
    },
    {
      "nombre" : "La Cruz de Rio Grande",
      "nombre_corto" : "lcrg",
      "region" : "raccs",
      "area" : 3449,
      "poblacion" : 43082
    },
    {
      "nombre" : "Laguna de Perlas",
      "nombre_corto" : "lgp",
      "region" : "raccs",
      "area" : 1963,
      "poblacion" : 19406
    },
    {
      "nombre" : "Paiwas",
      "nombre_corto" : "pwas",
      "region" : "raccs",
      "area" : 2089,
      "poblacion" : 36256
    },
    {
      "nombre" : "El Rama",
      "nombre_corto" : "rma",
      "region" : "raccs",
      "area" : 3753,
      "poblacion" : 58607
    },
    {
      "nombre" : "El Tortuguero",
      "nombre_corto" : "trtg",
      "region" : "raccs",
      "area" : 3403,
      "poblacion" : 57880
    }
]'''

json_com = '''[
    {
      "lat" : 11.9958,
      "lng" : -83.68998,
      "municipio" : "bef",
      "nombre" : "El Bluff (Puerto El Bluff)"
    },
    {
      "lat" : 11.40753,
      "lng" : -84.28327,
      "municipio" : "bef",
      "nombre" : "Aguas Frías"
    },
    {
      "lat" : 11.37873,
      "lng" : -84.2923,
      "municipio" : "bef",
      "nombre" : "Aguas Gatas"
    },
    {
      "lat" : 11.86704,
      "lng" : -84.03728,
      "municipio" : "bef",
      "nombre" : "Asentamiento"
    },
    {
      "lat" : 11.984167,
      "lng" : -83.858317,
      "municipio" : "bef",
      "nombre" : "Asentamiento Augusto C. Sandino"
    },
    {
      "lat" : 11.57932,
      "lng" : -84.01302,
      "municipio" : "bef",
      "nombre" : "Atlanta"
    },
    {
      "lat" : 11.56707,
      "lng" : -83.72275,
      "municipio" : "bef",
      "nombre" : "Bangkukuk Taik (Punta de Águila)"
    },
    {
      "lat" : 11.78974,
      "lng" : -83.82673,
      "municipio" : "bef",
      "nombre" : "Big Creek"
    },
    {
      "lat" : 12.1007,
      "lng" : -83.997,
      "municipio" : "bef",
      "nombre" : "Boca de Mahaganny"
    },
    {
      "lat" : 11.58181,
      "lng" : -84.09748,
      "municipio" : "bef",
      "nombre" : "Boca Tapada"
    },
    {
      "lat" : 11.83733,
      "lng" : -84.12412,
      "municipio" : "bef",
      "nombre" : "Boquita de Silva 1"
    },
    {
      "lat" : 11.84975,
      "lng" : -84.10309,
      "municipio" : "bef",
      "nombre" : "Boquita de Silva 2"
    },
    {
      "lat" : 11.772783,
      "lng" : -83.97055,
      "municipio" : "bef",
      "nombre" : "Buenos Aires"
    },
    {
      "lat" : 11.52169,
      "lng" : -83.90505,
      "municipio" : "bef",
      "nombre" : "Camilo"
    },
    {
      "lat" : 11.77224,
      "lng" : -84.01823,
      "municipio" : "bef",
      "nombre" : "Caño Azul 1"
    },
    {
      "lat" : 11.78041,
      "lng" : -84.01593,
      "municipio" : "bef",
      "nombre" : "Caño Azul 2"
    },
    {
      "lat" : 11.997283,
      "lng" : -83.90945,
      "municipio" : "bef",
      "nombre" : "Caño Azul de Santa Elena"
    },
    {
      "lat" : 12.043778,
      "lng" : -83.83507,
      "municipio" : "bef",
      "nombre" : "Caño Blanco"
    },
    {
      "lat" : 11.8387,
      "lng" : -83.95057,
      "municipio" : "bef",
      "nombre" : "Caño Maíz"
    },
    {
      "lat" : 12.12004,
      "lng" : -83.80385,
      "municipio" : "bef",
      "nombre" : "Caño Negro"
    },
    {
      "lat" : 11.77617,
      "lng" : -84.03489,
      "municipio" : "bef",
      "nombre" : "Coco 1"
    },
    {
      "lat" : 11.79086,
      "lng" : -84.05452,
      "municipio" : "bef",
      "nombre" : "Coco 2"
    },
    {
      "lat" : 11.73753,
      "lng" : -83.94409,
      "municipio" : "bef",
      "nombre" : "Colorado"
    },
    {
      "lat" : 11.70981,
      "lng" : -84.08797,
      "municipio" : "bef",
      "nombre" : "Colorado de Masayita"
    },
    {
      "lat" : 12.09822,
      "lng" : -83.94537,
      "municipio" : "bef",
      "nombre" : "Crisimbila"
    },
    {
      "lat" : 11.56048,
      "lng" : -84.05544,
      "municipio" : "bef",
      "nombre" : "Daniel Guido"
    },
    {
      "lat" : 11.4404,
      "lng" : -83.93886,
      "municipio" : "bef",
      "nombre" : "Diriangén de Pijibay"
    },
    {
      "lat" : 11.80499,
      "lng" : -83.91713,
      "municipio" : "bef",
      "nombre" : "Dokuno"
    },
    {
      "lat" : 11.62033,
      "lng" : -84.08635,
      "municipio" : "bef",
      "nombre" : "Dos de Oro Dos"
    },
    {
      "lat" : 11.80747,
      "lng" : -84.00914,
      "municipio" : "bef",
      "nombre" : "El Cañal"
    },
    {
      "lat" : 11.51522,
      "lng" : -84.11894,
      "municipio" : "bef",
      "nombre" : "El Coco"
    },
    {
      "lat" : 11.87619,
      "lng" : -84.0845,
      "municipio" : "bef",
      "nombre" : "El Coloradito"
    },
    {
      "lat" : 11.56019,
      "lng" : -83.81504,
      "municipio" : "bef",
      "nombre" : "El Corozo"
    },
    {
      "lat" : 11.93901,
      "lng" : -83.82288,
      "municipio" : "bef",
      "nombre" : "El Danto"
    },
    {
      "lat" : 11.49817,
      "lng" : -84.09534,
      "municipio" : "bef",
      "nombre" : "El Diamante"
    },
    {
      "lat" : 11.91302,
      "lng" : -84.08329,
      "municipio" : "bef",
      "nombre" : "El Diamante de Kukra River"
    },
    {
      "lat" : 11.7065,
      "lng" : -83.88731,
      "municipio" : "bef",
      "nombre" : "El Gorrión"
    },
    {
      "lat" : 11.77086,
      "lng" : -83.90844,
      "municipio" : "bef",
      "nombre" : "El Guapote"
    },
    {
      "lat" : 11.54345,
      "lng" : -84.05128,
      "municipio" : "bef",
      "nombre" : "El Guineo 1"
    },
    {
      "lat" : 11.50858,
      "lng" : -84.0554,
      "municipio" : "bef",
      "nombre" : "El Guineo 2"
    },
    {
      "lat" : 11.5904,
      "lng" : -83.8137,
      "municipio" : "bef",
      "nombre" : "El Javillo"
    },
    {
      "lat" : 11.7956,
      "lng" : -84.15121,
      "municipio" : "bef",
      "nombre" : "El Limón"
    },
    {
      "lat" : 11.56408,
      "lng" : -83.9576,
      "municipio" : "bef",
      "nombre" : "El Masayón"
    },
    {
      "lat" : 11.82317,
      "lng" : -84.03282,
      "municipio" : "bef",
      "nombre" : "El Naranjal"
    },
    {
      "lat" : 11.51715,
      "lng" : -84.01287,
      "municipio" : "bef",
      "nombre" : "El Naranjo"
    },
    {
      "lat" : 11.35494,
      "lng" : -84.31197,
      "municipio" : "bef",
      "nombre" : "El Pajarito"
    },
    {
      "lat" : 11.34271,
      "lng" : -84.33852,
      "municipio" : "bef",
      "nombre" : "El Pájaro"
    },
    {
      "lat" : 11.6223,
      "lng" : -83.9273,
      "municipio" : "bef",
      "nombre" : "El Papayo"
    },
    {
      "lat" : 11.77958,
      "lng" : -84.06685,
      "municipio" : "bef",
      "nombre" : "El Paraíso de Kukra River"
    },
    {
      "lat" : 11.6267,
      "lng" : -83.9531,
      "municipio" : "bef",
      "nombre" : "El Pato"
    },
    {
      "lat" : 11.47395,
      "lng" : -83.87747,
      "municipio" : "bef",
      "nombre" : "El Pijibay"
    },
    {
      "lat" : 11.5353,
      "lng" : -83.8712,
      "municipio" : "bef",
      "nombre" : "El Porvenir"
    },
    {
      "lat" : 11.65758,
      "lng" : -83.92728,
      "municipio" : "bef",
      "nombre" : "El Progreso"
    },
    {
      "lat" : 11.8737,
      "lng" : -84.10686,
      "municipio" : "bef",
      "nombre" : "El Quebradón"
    },
    {
      "lat" : 11.59193,
      "lng" : -84.06582,
      "municipio" : "bef",
      "nombre" : "El Quemado"
    },
    {
      "lat" : 11.90854,
      "lng" : -84.14486,
      "municipio" : "bef",
      "nombre" : "El Virgen"
    },
    {
      "lat" : 11.53302,
      "lng" : -83.93403,
      "municipio" : "bef",
      "nombre" : "Eloysa"
    },
    {
      "lat" : 11.99844,
      "lng" : -84.10606,
      "municipio" : "bef",
      "nombre" : "Guana Creek"
    },
    {
      "lat" : 11.31581,
      "lng" : -84.30588,
      "municipio" : "bef",
      "nombre" : "Jasmín del Guineo"
    },
    {
      "lat" : 11.30132,
      "lng" : -84.33234,
      "municipio" : "bef",
      "nombre" : "Jasmín del Guineo 2"
    },
    {
      "lat" : 11.85135,
      "lng" : -84.04189,
      "municipio" : "bef",
      "nombre" : "La Aurora"
    },
    {
      "lat" : 11.56393,
      "lng" : -83.9455,
      "municipio" : "bef",
      "nombre" : "La Bocana Masayón"
    },
    {
      "lat" : 11.30272,
      "lng" : -84.21894,
      "municipio" : "bef",
      "nombre" : "La Concepción de Piedra Fina"
    },
    {
      "lat" : 11.58364,
      "lng" : -83.85189,
      "municipio" : "bef",
      "nombre" : "La Coquera Monte Cristo"
    },
    {
      "lat" : 11.77104,
      "lng" : -83.8166,
      "municipio" : "bef",
      "nombre" : "La Cuna"
    },
    {
      "lat" : 11.4986,
      "lng" : -84.1539,
      "municipio" : "bef",
      "nombre" : "La Gloria"
    },
    {
      "lat" : 11.39011,
      "lng" : -84.33554,
      "municipio" : "bef",
      "nombre" : "La Guitarra"
    },
    {
      "lat" : 11.93189,
      "lng" : -84.03293,
      "municipio" : "bef",
      "nombre" : "Las Breñas 1"
    },
    {
      "lat" : 11.9301,
      "lng" : -84.0149,
      "municipio" : "bef",
      "nombre" : "Las Breñas 2"
    },
    {
      "lat" : 11.92626,
      "lng" : -83.93176,
      "municipio" : "bef",
      "nombre" : "Las Cuevas"
    },
    {
      "lat" : 11.6268,
      "lng" : -83.95235,
      "municipio" : "bef",
      "nombre" : "Las Delicias"
    },
    {
      "lat" : 11.4624,
      "lng" : -84.02398,
      "municipio" : "bef",
      "nombre" : "Las Flores"
    },
    {
      "lat" : 11.6919,
      "lng" : -83.7303,
      "municipio" : "bef",
      "nombre" : "Las Nubes"
    },
    {
      "lat" : 11.6129,
      "lng" : -83.7536,
      "municipio" : "bef",
      "nombre" : "Las Pavas"
    },
    {
      "lat" : 11.70569,
      "lng" : -84.01929,
      "municipio" : "bef",
      "nombre" : "Los Ángeles de Masayon"
    },
    {
      "lat" : 11.83163,
      "lng" : -84.16652,
      "municipio" : "bef",
      "nombre" : "Los Peñones"
    },
    {
      "lat" : 11.58902,
      "lng" : -83.88978,
      "municipio" : "bef",
      "nombre" : "Masayita"
    },
    {
      "lat" : 11.54457,
      "lng" : -84.00952,
      "municipio" : "bef",
      "nombre" : "Molinares"
    },
    {
      "lat" : 11.5959,
      "lng" : -83.65817,
      "municipio" : "bef",
      "nombre" : "Monkey Point"
    },
    {
      "lat" : 11.6296,
      "lng" : -83.87556,
      "municipio" : "bef",
      "nombre" : "Monte Cristo"
    },
    {
      "lat" : 11.39196,
      "lng" : -84.1608,
      "municipio" : "bef",
      "nombre" : "Monte Verde"
    },
    {
      "lat" : 11.94598,
      "lng" : -83.80852,
      "municipio" : "bef",
      "nombre" : "Musilaina"
    },
    {
      "lat" : 11.59824,
      "lng" : -83.80273,
      "municipio" : "bef",
      "nombre" : "Nueva Esperanza"
    },
    {
      "lat" : 11.42363,
      "lng" : -84.31906,
      "municipio" : "bef",
      "nombre" : "Nuevo Delirio"
    },
    {
      "lat" : 11.47993,
      "lng" : -84.35619,
      "municipio" : "bef",
      "nombre" : "Nuevo San Antonio"
    },
    {
      "lat" : 11.52917,
      "lng" : -83.92187,
      "municipio" : "bef",
      "nombre" : "Palo Bonito"
    },
    {
      "lat" : 11.43937,
      "lng" : -84.23344,
      "municipio" : "bef",
      "nombre" : "Paraíso de Aguas Zarcas"
    },
    {
      "lat" : 11.37988,
      "lng" : -84.21774,
      "municipio" : "bef",
      "nombre" : "Piedra Fina"
    },
    {
      "lat" : 11.73507,
      "lng" : -83.98042,
      "municipio" : "bef",
      "nombre" : "Poza Azul"
    },
    {
      "lat" : 11.7177,
      "lng" : -83.9803,
      "municipio" : "bef",
      "nombre" : "Poza Azul de Kukra River"
    },
    {
      "lat" : 11.60707,
      "lng" : -84.08647,
      "municipio" : "bef",
      "nombre" : "Pueblo Nuevo"
    },
    {
      "lat" : 11.88227,
      "lng" : -83.80937,
      "municipio" : "bef",
      "nombre" : "Rama Cay"
    },
    {
      "lat" : 11.29191,
      "lng" : -83.8754,
      "municipio" : "bef",
      "nombre" : "Río Maíz"
    },
    {
      "lat" : 11.76438,
      "lng" : -84.12022,
      "municipio" : "bef",
      "nombre" : "Rubén Darío"
    },
    {
      "lat" : 11.50233,
      "lng" : -84.18549,
      "municipio" : "bef",
      "nombre" : "Salto de León"
    },
    {
      "lat" : 12.06309,
      "lng" : -83.81287,
      "municipio" : "bef",
      "nombre" : "San Antonio (Playa Seca)"
    },
    {
      "lat" : 11.28511,
      "lng" : -84.22472,
      "municipio" : "bef",
      "nombre" : "San Diego"
    },
    {
      "lat" : 11.41563,
      "lng" : -84.2506,
      "municipio" : "bef",
      "nombre" : "San Francisco de Agua Frías"
    },
    {
      "lat" : 11.74706,
      "lng" : -84.11324,
      "municipio" : "bef",
      "nombre" : "San Isidro"
    },
    {
      "lat" : 11.89238,
      "lng" : -84.01556,
      "municipio" : "bef",
      "nombre" : "San José"
    },
    {
      "lat" : 11.296194,
      "lng" : -84.173222,
      "municipio" : "bef",
      "nombre" : "San José de las Brisas"
    },
    {
      "lat" : 11.38826,
      "lng" : -84.35466,
      "municipio" : "bef",
      "nombre" : "San Luis de Aguas Gatas"
    },
    {
      "lat" : 12.09247,
      "lng" : -83.79631,
      "municipio" : "bef",
      "nombre" : "San Mariano"
    },
    {
      "lat" : 11.60723,
      "lng" : -83.85622,
      "municipio" : "bef",
      "nombre" : "San Miguel"
    },
    {
      "lat" : 12.10022,
      "lng" : -83.79968,
      "municipio" : "bef",
      "nombre" : "San Nicolás"
    },
    {
      "lat" : 11.4656,
      "lng" : -84.22239,
      "municipio" : "bef",
      "nombre" : "San Pablo"
    },
    {
      "lat" : 11.39193,
      "lng" : -84.19623,
      "municipio" : "bef",
      "nombre" : "San Pedro"
    },
    {
      "lat" : 11.69259,
      "lng" : -83.83772,
      "municipio" : "bef",
      "nombre" : "San Rafael"
    },
    {
      "lat" : 11.31276,
      "lng" : -84.21377,
      "municipio" : "bef",
      "nombre" : "San Rafael del Zahino"
    },
    {
      "lat" : 11.97603,
      "lng" : -83.96525,
      "municipio" : "bef",
      "nombre" : "San Sebastian"
    },
    {
      "lat" : 11.47545,
      "lng" : -84.20694,
      "municipio" : "bef",
      "nombre" : "San Sebastian de Aguas Zarcas"
    },
    {
      "lat" : 11.37594,
      "lng" : -84.10844,
      "municipio" : "bef",
      "nombre" : "Santa Elena"
    },
    {
      "lat" : 11.87166,
      "lng" : -83.95303,
      "municipio" : "bef",
      "nombre" : "Santa Elisa"
    },
    {
      "lat" : 11.80407,
      "lng" : -84.11934,
      "municipio" : "bef",
      "nombre" : "Santa Fé"
    },
    {
      "lat" : 11.31374,
      "lng" : -84.26465,
      "municipio" : "bef",
      "nombre" : "Santa Fé del Caracol"
    },
    {
      "lat" : 11.6559,
      "lng" : -84.0332,
      "municipio" : "bef",
      "nombre" : "Santa Isabel"
    },
    {
      "lat" : 11.47561,
      "lng" : -84.05727,
      "municipio" : "bef",
      "nombre" : "Santa Rosa del Guineo"
    },
    {
      "lat" : 11.528533,
      "lng" : -83.880233,
      "municipio" : "bef",
      "nombre" : "Santa Rosa del Porvenir"
    },
    {
      "lat" : 11.68877,
      "lng" : -83.96998,
      "municipio" : "bef",
      "nombre" : "Santo Tomás Masayón"
    },
    {
      "lat" : 12.02223,
      "lng" : -83.81683,
      "municipio" : "bef",
      "nombre" : "Scofram"
    },
    {
      "lat" : 12.117,
      "lng" : -83.7411,
      "municipio" : "bef",
      "nombre" : "Smokey Lane"
    },
    {
      "lat" : 11.95992,
      "lng" : -83.98203,
      "municipio" : "bef",
      "nombre" : "Taleno"
    },
    {
      "lat" : 11.89594,
      "lng" : -83.93416,
      "municipio" : "bef",
      "nombre" : "Ticktick- Caanu (Zompopera)"
    },
    {
      "lat" : 11.81295,
      "lng" : -84.05183,
      "municipio" : "bef",
      "nombre" : "Toboba"
    },
    {
      "lat" : 11.7731,
      "lng" : -83.8941,
      "municipio" : "bef",
      "nombre" : "Torsuanny"
    },
    {
      "lat" : 11.81753,
      "lng" : -84.07974,
      "municipio" : "bef",
      "nombre" : "Villa Nueva"
    },
    {
      "lat" : 11.73907,
      "lng" : -83.76717,
      "municipio" : "bef",
      "nombre" : "Willin Cay 1"
    },
    {
      "lat" : 11.70666,
      "lng" : -83.77401,
      "municipio" : "bef",
      "nombre" : "Willin Cay 2"
    },
    {
      "lat" : 11.67381,
      "lng" : -83.83569,
      "municipio" : "bef",
      "nombre" : "Wiring Cay"
    },
    {
      "lat" : 11.77347,
      "lng" : -83.75752,
      "municipio" : "bef",
      "nombre" : "Yaladina"
    },
    {
      "lat" : 12.17582,
      "lng" : -83.05981,
      "municipio" : "cis",
      "nombre" : "Brig Bay I"
    },
    {
      "lat" : 12.16391,
      "lng" : -83.06921,
      "municipio" : "cis",
      "nombre" : "Brig Bay II"
    },
    {
      "lat" : 12.18371,
      "lng" : -83.0516,
      "municipio" : "cis",
      "nombre" : "North End"
    },
    {
      "lat" : 12.15156,
      "lng" : -83.06326,
      "municipio" : "cis",
      "nombre" : "Quinn Hill"
    },
    {
      "lat" : 12.1751508,
      "lng" : -83.037239,
      "municipio" : "cis",
      "nombre" : "Sally Peachie"
    },
    {
      "lat" : 12.17024,
      "lng" : -83.04074,
      "municipio" : "cis",
      "nombre" : "South End"
    },
    {
      "lat" : 12.28727,
      "lng" : -82.98111,
      "municipio" : "cis",
      "nombre" : "Little Corn Island"
    },
    {
      "lat" : 13.25529,
      "lng" : -83.98927,
      "municipio" : "drg",
      "nombre" : "Company Creek"
    },
    {
      "lat" : 13.2131,
      "lng" : -83.9256,
      "municipio" : "drg",
      "nombre" : "Guadalupe"
    },
    {
      "lat" : 12.89395,
      "lng" : -83.58325,
      "municipio" : "drg",
      "nombre" : "Kara"
    },
    {
      "lat" : 12.934549,
      "lng" : -83.577884,
      "municipio" : "drg",
      "nombre" : "Karawala"
    },
    {
      "lat" : 12.90642,
      "lng" : -83.52388,
      "municipio" : "drg",
      "nombre" : "La Barra"
    },
    {
      "lat" : 13.14645,
      "lng" : -83.90263,
      "municipio" : "drg",
      "nombre" : "La Esperanza"
    },
    {
      "lat" : 12.96295,
      "lng" : -83.53207,
      "municipio" : "drg",
      "nombre" : "Sandy Bay Sirpi"
    },
    {
      "lat" : 12.94016,
      "lng" : -83.53586,
      "municipio" : "drg",
      "nombre" : "Walpa"
    },
    {
      "lat" : 12.38561,
      "lng" : -84.17574,
      "municipio" : "rma",
      "nombre" : "Aguas Calientes"
    },
    {
      "lat" : 12.44731,
      "lng" : -84.48325,
      "municipio" : "rma",
      "nombre" : "Bella Vista"
    },
    {
      "lat" : 12.00045,
      "lng" : -84.35242,
      "municipio" : "rma",
      "nombre" : "Boca Azul"
    },
    {
      "lat" : 12.01909,
      "lng" : -84.33369,
      "municipio" : "rma",
      "nombre" : "Boca Azulita"
    },
    {
      "lat" : 11.83728,
      "lng" : -84.12391,
      "municipio" : "rma",
      "nombre" : "Boquita de Silva"
    },
    {
      "lat" : 11.80415,
      "lng" : -84.11945,
      "municipio" : "rma",
      "nombre" : "Boquita de Silva N°2"
    },
    {
      "lat" : 12.51081,
      "lng" : -84.2318,
      "municipio" : "rma",
      "nombre" : "Cabecera de Valentín"
    },
    {
      "lat" : 12.29759,
      "lng" : -84.25247,
      "municipio" : "rma",
      "nombre" : "Calderon"
    },
    {
      "lat" : 12.37513,
      "lng" : -84.28558,
      "municipio" : "rma",
      "nombre" : "Caño Adolfo"
    },
    {
      "lat" : 12.25412,
      "lng" : -84.49007,
      "municipio" : "rma",
      "nombre" : "Caño García"
    },
    {
      "lat" : 12.4606,
      "lng" : -84.27815,
      "municipio" : "rma",
      "nombre" : "Caño Valentín"
    },
    {
      "lat" : 12.34315,
      "lng" : -84.1582,
      "municipio" : "rma",
      "nombre" : "Caño Wilson"
    },
    {
      "lat" : 11.92323,
      "lng" : -84.23445,
      "municipio" : "rma",
      "nombre" : "Cedro Macho"
    },
    {
      "lat" : 12.38841,
      "lng" : -84.66748,
      "municipio" : "rma",
      "nombre" : "Cerro Grande"
    },
    {
      "lat" : 12.13961,
      "lng" : -84.09879,
      "municipio" : "rma",
      "nombre" : "Chalmeca Abajo"
    },
    {
      "lat" : 12.2151,
      "lng" : -84.09421,
      "municipio" : "rma",
      "nombre" : "Chalmeca Arriba"
    },
    {
      "lat" : 12.18837,
      "lng" : -84.09012,
      "municipio" : "rma",
      "nombre" : "Chalmeca Centro"
    },
    {
      "lat" : 12.41417,
      "lng" : -84.40584,
      "municipio" : "rma",
      "nombre" : "Correntada Larga"
    },
    {
      "lat" : 12.23937,
      "lng" : -84.25842,
      "municipio" : "rma",
      "nombre" : "Cuatro Esquina"
    },
    {
      "lat" : 12.1665,
      "lng" : -84.38118,
      "municipio" : "rma",
      "nombre" : "Diamante Rojo"
    },
    {
      "lat" : 12.14963,
      "lng" : -84.27087,
      "municipio" : "rma",
      "nombre" : "El Amparo"
    },
    {
      "lat" : 12.22715,
      "lng" : -84.23576,
      "municipio" : "rma",
      "nombre" : "El Areno"
    },
    {
      "lat" : 12.10202,
      "lng" : -84.11273,
      "municipio" : "rma",
      "nombre" : "El Banco"
    },
    {
      "lat" : 11.93884,
      "lng" : -84.08642,
      "municipio" : "rma",
      "nombre" : "El Carmen"
    },
    {
      "lat" : 12.06518,
      "lng" : -84.15485,
      "municipio" : "rma",
      "nombre" : "El Castillo"
    },
    {
      "lat" : 11.87625,
      "lng" : -84.08454,
      "municipio" : "rma",
      "nombre" : "El Coloradito"
    },
    {
      "lat" : 12.21537,
      "lng" : -84.17339,
      "municipio" : "rma",
      "nombre" : "El Colorado"
    },
    {
      "lat" : 12.05088,
      "lng" : -84.20193,
      "municipio" : "rma",
      "nombre" : "El Delirio"
    },
    {
      "lat" : 11.91273,
      "lng" : -84.10599,
      "municipio" : "rma",
      "nombre" : "El Diamante"
    },
    {
      "lat" : 12.05241,
      "lng" : -84.33897,
      "municipio" : "rma",
      "nombre" : "El Embudo"
    },
    {
      "lat" : 12.38711,
      "lng" : -84.39811,
      "municipio" : "rma",
      "nombre" : "El Garrobo"
    },
    {
      "lat" : 12.52971,
      "lng" : -84.48256,
      "municipio" : "rma",
      "nombre" : "El Guabo"
    },
    {
      "lat" : 12.49161,
      "lng" : -84.67401,
      "municipio" : "rma",
      "nombre" : "El Jobito"
    },
    {
      "lat" : 12.43193,
      "lng" : -84.6837,
      "municipio" : "rma",
      "nombre" : "El Jobo"
    },
    {
      "lat" : 12.28209,
      "lng" : -84.55045,
      "municipio" : "rma",
      "nombre" : "El Limón"
    },
    {
      "lat" : 12.11759,
      "lng" : -84.20261,
      "municipio" : "rma",
      "nombre" : "El Milan"
    },
    {
      "lat" : 11.98195,
      "lng" : -84.21226,
      "municipio" : "rma",
      "nombre" : "El Mobile"
    },
    {
      "lat" : 12.43688,
      "lng" : -84.34062,
      "municipio" : "rma",
      "nombre" : "El Molejón"
    },
    {
      "lat" : 12.0039,
      "lng" : -84.30398,
      "municipio" : "rma",
      "nombre" : "El Murciélago"
    },
    {
      "lat" : 12.03889,
      "lng" : -84.31083,
      "municipio" : "rma",
      "nombre" : "El Palmar"
    },
    {
      "lat" : 12.11776,
      "lng" : -84.06682,
      "municipio" : "rma",
      "nombre" : "El Paraíso"
    },
    {
      "lat" : 12.0185,
      "lng" : -84.14677,
      "municipio" : "rma",
      "nombre" : "El Pavón"
    },
    {
      "lat" : 12.03449,
      "lng" : -84.21628,
      "municipio" : "rma",
      "nombre" : "El Porvenir"
    },
    {
      "lat" : 12.17397,
      "lng" : -84.31682,
      "municipio" : "rma",
      "nombre" : "El Recreo"
    },
    {
      "lat" : 12.18194,
      "lng" : -84.25998,
      "municipio" : "rma",
      "nombre" : "El Silencio"
    },
    {
      "lat" : 12.51204,
      "lng" : -84.18969,
      "municipio" : "rma",
      "nombre" : "El Toro"
    },
    {
      "lat" : 11.90809,
      "lng" : -84.1459,
      "municipio" : "rma",
      "nombre" : "El Virgen"
    },
    {
      "lat" : 12.06345,
      "lng" : -84.12456,
      "municipio" : "rma",
      "nombre" : "Fruta de Pan"
    },
    {
      "lat" : 11.99145,
      "lng" : -84.23717,
      "municipio" : "rma",
      "nombre" : "Guadalupe"
    },
    {
      "lat" : 11.96273,
      "lng" : -84.06583,
      "municipio" : "rma",
      "nombre" : "Guana Kreek"
    },
    {
      "lat" : 12.43048,
      "lng" : -84.31818,
      "municipio" : "rma",
      "nombre" : "Ignacia"
    },
    {
      "lat" : 12.40027,
      "lng" : -84.60899,
      "municipio" : "rma",
      "nombre" : "Isla Grande"
    },
    {
      "lat" : 12.06601,
      "lng" : -84.23203,
      "municipio" : "rma",
      "nombre" : "Julio Buitrago"
    },
    {
      "lat" : 12.30458,
      "lng" : -84.75018,
      "municipio" : "rma",
      "nombre" : "Kilaika"
    },
    {
      "lat" : 12.25982,
      "lng" : -84.48967,
      "municipio" : "rma",
      "nombre" : "Kisilala"
    },
    {
      "lat" : 12.26096,
      "lng" : -84.47253,
      "municipio" : "rma",
      "nombre" : "Kisilala (Contiguo Kisilala N°2)"
    },
    {
      "lat" : 12.26589,
      "lng" : -84.35735,
      "municipio" : "rma",
      "nombre" : "Kisilala N°1"
    },
    {
      "lat" : 12.2655,
      "lng" : -84.42239,
      "municipio" : "rma",
      "nombre" : "Kisilala N°2"
    },
    {
      "lat" : 12.5995,
      "lng" : -84.64849,
      "municipio" : "rma",
      "nombre" : "Kurinwasito"
    },
    {
      "lat" : 12.08161,
      "lng" : -84.25311,
      "municipio" : "rma",
      "nombre" : "La Ceiba"
    },
    {
      "lat" : 12.09037,
      "lng" : -84.2204,
      "municipio" : "rma",
      "nombre" : "La Concha Río Rama"
    },
    {
      "lat" : 12.20885,
      "lng" : -84.42814,
      "municipio" : "rma",
      "nombre" : "La Concha Vía Carretera"
    },
    {
      "lat" : 12.17607,
      "lng" : -84.35504,
      "municipio" : "rma",
      "nombre" : "La Corona"
    },
    {
      "lat" : 12.54535,
      "lng" : -84.62154,
      "municipio" : "rma",
      "nombre" : "La Danta"
    },
    {
      "lat" : 12.20027,
      "lng" : -84.28955,
      "municipio" : "rma",
      "nombre" : "La Esperanza"
    },
    {
      "lat" : 12.06239,
      "lng" : -84.27113,
      "municipio" : "rma",
      "nombre" : "La Fortuna"
    },
    {
      "lat" : 12.13526,
      "lng" : -84.14431,
      "municipio" : "rma",
      "nombre" : "La Mosquitia"
    },
    {
      "lat" : 12.2585,
      "lng" : -84.10004,
      "municipio" : "rma",
      "nombre" : "La Palma"
    },
    {
      "lat" : 12.14316,
      "lng" : -84.25523,
      "municipio" : "rma",
      "nombre" : "La Palmera"
    },
    {
      "lat" : 12.4455,
      "lng" : -84.41982,
      "municipio" : "rma",
      "nombre" : "La Piñuela"
    },
    {
      "lat" : 12.30432,
      "lng" : -84.16497,
      "municipio" : "rma",
      "nombre" : "La Raicilla"
    },
    {
      "lat" : 11.95055,
      "lng" : -84.14638,
      "municipio" : "rma",
      "nombre" : "La Sardina"
    },
    {
      "lat" : 12.18707,
      "lng" : -84.01202,
      "municipio" : "rma",
      "nombre" : "La Sompopa"
    },
    {
      "lat" : 12.29405,
      "lng" : -84.38335,
      "municipio" : "rma",
      "nombre" : "La Tigra"
    },
    {
      "lat" : 12.59172,
      "lng" : -84.60918,
      "municipio" : "rma",
      "nombre" : "La Toalla"
    },
    {
      "lat" : 11.98735,
      "lng" : -84.14708,
      "municipio" : "rma",
      "nombre" : "La Virgen"
    },
    {
      "lat" : 12.03369,
      "lng" : -84.26026,
      "municipio" : "rma",
      "nombre" : "Las Iguanas"
    },
    {
      "lat" : 12.23769,
      "lng" : -84.1172,
      "municipio" : "rma",
      "nombre" : "Las Lapas"
    },
    {
      "lat" : 11.88806,
      "lng" : -84.19362,
      "municipio" : "rma",
      "nombre" : "Loma Linda"
    },
    {
      "lat" : 12.09735,
      "lng" : -84.05849,
      "municipio" : "rma",
      "nombre" : "Magnolia"
    },
    {
      "lat" : 12.10151,
      "lng" : -84.18355,
      "municipio" : "rma",
      "nombre" : "María Cristina"
    },
    {
      "lat" : 12.2999,
      "lng" : -84.3223,
      "municipio" : "rma",
      "nombre" : "Mataka"
    },
    {
      "lat" : 12.30448,
      "lng" : -84.41408,
      "municipio" : "rma",
      "nombre" : "Minas de Kisilala"
    },
    {
      "lat" : 12.4312,
      "lng" : -84.52476,
      "municipio" : "rma",
      "nombre" : "Mirasol"
    },
    {
      "lat" : 12.36382,
      "lng" : -84.25286,
      "municipio" : "rma",
      "nombre" : "Monte Rosa"
    },
    {
      "lat" : 12.31532,
      "lng" : -84.48534,
      "municipio" : "rma",
      "nombre" : "Montes de Oro"
    },
    {
      "lat" : 12.25136,
      "lng" : -84.30197,
      "municipio" : "rma",
      "nombre" : "Muelle  Real"
    },
    {
      "lat" : 12.35546,
      "lng" : -84.56232,
      "municipio" : "rma",
      "nombre" : "Musuwaka"
    },
    {
      "lat" : 12.46788,
      "lng" : -84.16502,
      "municipio" : "rma",
      "nombre" : "Nuevo Sauce"
    },
    {
      "lat" : 12.17831,
      "lng" : -84.23609,
      "municipio" : "rma",
      "nombre" : "Oscar Brenes"
    },
    {
      "lat" : 12.13791,
      "lng" : -84.21425,
      "municipio" : "rma",
      "nombre" : "Pablo Ubeda"
    },
    {
      "lat" : 12.13418,
      "lng" : -84.33255,
      "municipio" : "rma",
      "nombre" : "Pijibay (El Recreo)"
    },
    {
      "lat" : 12.42304,
      "lng" : -84.23533,
      "municipio" : "rma",
      "nombre" : "Pijibay (Wapi)"
    },
    {
      "lat" : 12.34619,
      "lng" : -84.77089,
      "municipio" : "rma",
      "nombre" : "Pilan"
    },
    {
      "lat" : 12.47642,
      "lng" : -84.50665,
      "municipio" : "rma",
      "nombre" : "Poza Redonda"
    },
    {
      "lat" : 11.95111,
      "lng" : -84.12202,
      "municipio" : "rma",
      "nombre" : "Pueblo Nuevo"
    },
    {
      "lat" : 12.44766,
      "lng" : -84.19532,
      "municipio" : "rma",
      "nombre" : "Salto de la Cruz"
    },
    {
      "lat" : 12.54164,
      "lng" : -84.59615,
      "municipio" : "rma",
      "nombre" : "Salto Grande"
    },
    {
      "lat" : 12.1566,
      "lng" : -84.21619,
      "municipio" : "rma",
      "nombre" : "San Agustín"
    },
    {
      "lat" : 11.91585,
      "lng" : -84.18131,
      "municipio" : "rma",
      "nombre" : "San Antonio del Pozol"
    },
    {
      "lat" : 12.18281,
      "lng" : -84.04536,
      "municipio" : "rma",
      "nombre" : "San Brown"
    },
    {
      "lat" : 12.4587,
      "lng" : -84.24866,
      "municipio" : "rma",
      "nombre" : "San Jerónimo"
    },
    {
      "lat" : 11.94538,
      "lng" : -84.25338,
      "municipio" : "rma",
      "nombre" : "San Jerónimo (Río Plata)"
    },
    {
      "lat" : 12.03167,
      "lng" : -84.10231,
      "municipio" : "rma",
      "nombre" : "San Luis"
    },
    {
      "lat" : 12.56282,
      "lng" : -84.50794,
      "municipio" : "rma",
      "nombre" : "San Rafael"
    },
    {
      "lat" : 12.22408,
      "lng" : -84.03303,
      "municipio" : "rma",
      "nombre" : "San Ramón"
    },
    {
      "lat" : 12.43132,
      "lng" : -84.15751,
      "municipio" : "rma",
      "nombre" : "Santa  Rita"
    },
    {
      "lat" : 11.83162,
      "lng" : -84.16634,
      "municipio" : "rma",
      "nombre" : "Santa Rita de Los Peñones"
    },
    {
      "lat" : 12.1753,
      "lng" : -84.19888,
      "municipio" : "rma",
      "nombre" : "Santa Rosa"
    },
    {
      "lat" : 12.24096,
      "lng" : -84.01808,
      "municipio" : "rma",
      "nombre" : "Son Cuan"
    },
    {
      "lat" : 12.12307,
      "lng" : -84.28824,
      "municipio" : "rma",
      "nombre" : "Tatumbla"
    },
    {
      "lat" : 12.37519,
      "lng" : -84.45959,
      "municipio" : "rma",
      "nombre" : "Tutuwaká"
    },
    {
      "lat" : 11.81968,
      "lng" : -84.0918,
      "municipio" : "rma",
      "nombre" : "Villa Nueva"
    },
    {
      "lat" : 12.38414,
      "lng" : -84.31851,
      "municipio" : "rma",
      "nombre" : "Wapi"
    },
    {
      "lat" : 12.22626,
      "lng" : -84.33961,
      "municipio" : "rma",
      "nombre" : "Zaragoza"
    },
    {
      "lat" : 12.795,
      "lng" : -84.035,
      "municipio" : "trtg",
      "nombre" : "Aguas Honda"
    },
    {
      "lat" : 12.529141,
      "lng" : -84.43631,
      "municipio" : "trtg",
      "nombre" : "Bambú Piñol"
    },
    {
      "lat" : 12.8171,
      "lng" : -84.31023,
      "municipio" : "trtg",
      "nombre" : "Caño Azul"
    },
    {
      "lat" : 12.68311,
      "lng" : -84.23645,
      "municipio" : "trtg",
      "nombre" : "Chili Kreek"
    },
    {
      "lat" : 12.64678,
      "lng" : -84.50786,
      "municipio" : "trtg",
      "nombre" : "Divino Niño"
    },
    {
      "lat" : 12.81924,
      "lng" : -84.14849,
      "municipio" : "trtg",
      "nombre" : "El Bambú"
    },
    {
      "lat" : 12.65615,
      "lng" : -84.56161,
      "municipio" : "trtg",
      "nombre" : "El Cedro"
    },
    {
      "lat" : 12.60388,
      "lng" : -84.15737,
      "municipio" : "trtg",
      "nombre" : "El Espavel"
    },
    {
      "lat" : 12.795,
      "lng" : -84.095,
      "municipio" : "trtg",
      "nombre" : "El Lajero"
    },
    {
      "lat" : 12.57686,
      "lng" : -84.23207,
      "municipio" : "trtg",
      "nombre" : "EL Marrón"
    },
    {
      "lat" : 12.64351,
      "lng" : -84.02631,
      "municipio" : "trtg",
      "nombre" : "El Papel"
    },
    {
      "lat" : 12.9157,
      "lng" : -84.14256,
      "municipio" : "trtg",
      "nombre" : "El Paraíso"
    },
    {
      "lat" : 12.93282,
      "lng" : -84.3338,
      "municipio" : "trtg",
      "nombre" : "El Pavón"
    },
    {
      "lat" : 12.52783,
      "lng" : -84.48264,
      "municipio" : "trtg",
      "nombre" : "El Wavo"
    },
    {
      "lat" : 12.85051,
      "lng" : -84.1063,
      "municipio" : "trtg",
      "nombre" : "Good Living"
    },
    {
      "lat" : 12.51207,
      "lng" : -84.2792,
      "municipio" : "trtg",
      "nombre" : "Hierba Buena"
    },
    {
      "lat" : 12.8402,
      "lng" : -84.37974,
      "municipio" : "trtg",
      "nombre" : "Karahola"
    },
    {
      "lat" : 12.7328,
      "lng" : -84.072,
      "municipio" : "trtg",
      "nombre" : "Kasmiting"
    },
    {
      "lat" : 12.92451,
      "lng" : -83.9552,
      "municipio" : "trtg",
      "nombre" : "Kun Kun"
    },
    {
      "lat" : 12.70923,
      "lng" : -84.51273,
      "municipio" : "trtg",
      "nombre" : "La Guitarra"
    },
    {
      "lat" : 12.71568,
      "lng" : -84.20365,
      "municipio" : "trtg",
      "nombre" : "La Isla Kukarawala"
    },
    {
      "lat" : 12.50992,
      "lng" : -84.35396,
      "municipio" : "trtg",
      "nombre" : "La Paila"
    },
    {
      "lat" : 12.61115,
      "lng" : -84.57199,
      "municipio" : "trtg",
      "nombre" : "La Toalla"
    },
    {
      "lat" : 12.75871,
      "lng" : -84.42257,
      "municipio" : "trtg",
      "nombre" : "Mata de Caña"
    },
    {
      "lat" : 12.7591,
      "lng" : -84.2424,
      "municipio" : "trtg",
      "nombre" : "Nuevo Belén"
    },
    {
      "lat" : 12.94573,
      "lng" : -84.23284,
      "municipio" : "trtg",
      "nombre" : "Paharatigni"
    },
    {
      "lat" : 12.76693,
      "lng" : -84.19696,
      "municipio" : "trtg",
      "nombre" : "Salto de Busaya"
    },
    {
      "lat" : 12.64943,
      "lng" : -84.44639,
      "municipio" : "trtg",
      "nombre" : "San Antonio de Kukarawala"
    },
    {
      "lat" : 12.69659,
      "lng" : -84.13728,
      "municipio" : "trtg",
      "nombre" : "San Francisco de Suslatigni"
    },
    {
      "lat" : 12.95513,
      "lng" : -84.03518,
      "municipio" : "trtg",
      "nombre" : "San Francisco de Wawalatigni"
    },
    {
      "lat" : 12.62146,
      "lng" : -84.23869,
      "municipio" : "trtg",
      "nombre" : "San Isidro"
    },
    {
      "lat" : 12.65338,
      "lng" : -84.3002,
      "municipio" : "trtg",
      "nombre" : "San José de Sawawas"
    },
    {
      "lat" : 12.87753,
      "lng" : -84.03963,
      "municipio" : "trtg",
      "nombre" : "San Jose Kurinwas"
    },
    {
      "lat" : 12.68505,
      "lng" : -84.02322,
      "municipio" : "trtg",
      "nombre" : "San Juan de Chaca Chaca"
    },
    {
      "lat" : 12.8695,
      "lng" : -84.32198,
      "municipio" : "trtg",
      "nombre" : "San Juan de Kurinwas"
    },
    {
      "lat" : 12.70079,
      "lng" : -84.599,
      "municipio" : "trtg",
      "nombre" : "San Miguel Calzon Quemado"
    },
    {
      "lat" : 12.76969,
      "lng" : -84.1406,
      "municipio" : "trtg",
      "nombre" : "San Miguel de los Olivos"
    },
    {
      "lat" : 12.71231,
      "lng" : -84.42599,
      "municipio" : "trtg",
      "nombre" : "San Miguelito"
    },
    {
      "lat" : 12.6002,
      "lng" : -84.49898,
      "municipio" : "trtg",
      "nombre" : "San Rafael"
    },
    {
      "lat" : 12.71984,
      "lng" : -84.15378,
      "municipio" : "trtg",
      "nombre" : "Santa Lucía"
    },
    {
      "lat" : 12.63759,
      "lng" : -84.39193,
      "municipio" : "trtg",
      "nombre" : "Santa Rita"
    },
    {
      "lat" : 12.7108,
      "lng" : -84.0483,
      "municipio" : "trtg",
      "nombre" : "Santa Teresa"
    },
    {
      "lat" : 12.58938,
      "lng" : -84.25812,
      "municipio" : "trtg",
      "nombre" : "Sawawas Central"
    },
    {
      "lat" : 12.6967,
      "lng" : -84.0822,
      "municipio" : "trtg",
      "nombre" : "Suslatigni"
    },
    {
      "lat" : 12.57411,
      "lng" : -84.41977,
      "municipio" : "trtg",
      "nombre" : "Tintas Verde"
    },
    {
      "lat" : 12.65219,
      "lng" : -84.19843,
      "municipio" : "trtg",
      "nombre" : "Walpapine"
    },
    {
      "lat" : 12.73539,
      "lng" : -84.5466,
      "municipio" : "trtg",
      "nombre" : "Wasmuka"
    },
    {
      "lat" : 12.73899,
      "lng" : -84.30753,
      "municipio" : "trtg",
      "nombre" : "Waspado"
    },
    {
      "lat" : 12.91795,
      "lng" : -84.0662,
      "municipio" : "trtg",
      "nombre" : "Wawalatigni"
    },
    {
      "lat" : 12.81895,
      "lng" : -84.20132,
      "municipio" : "trtg",
      "nombre" : "El Tortuguero"
    },
    {
      "lat" : 12.27628,
      "lng" : -83.84712,
      "municipio" : "khl",
      "nombre" : "Asentamiento Samuel Law"
    },
    {
      "lat" : 12.1128,
      "lng" : -83.9693,
      "municipio" : "khl",
      "nombre" : "Belén"
    },
    {
      "lat" : 12.241114,
      "lng" : -83.79478,
      "municipio" : "khl",
      "nombre" : "Big Lagoon"
    },
    {
      "lat" : 12.21516,
      "lng" : -84.09422,
      "municipio" : "khl",
      "nombre" : "Chalmeca"
    },
    {
      "lat" : 12.2443,
      "lng" : -83.82498,
      "municipio" : "khl",
      "nombre" : "El Campión"
    },
    {
      "lat" : 12.2715,
      "lng" : -83.793,
      "municipio" : "khl",
      "nombre" : "El Capricho"
    },
    {
      "lat" : 12.46028,
      "lng" : -83.98367,
      "municipio" : "khl",
      "nombre" : "El Diamante"
    },
    {
      "lat" : 12.2966,
      "lng" : -83.83165,
      "municipio" : "khl",
      "nombre" : "El Escobal"
    },
    {
      "lat" : 12.31649,
      "lng" : -83.86758,
      "municipio" : "khl",
      "nombre" : "El Panchón"
    },
    {
      "lat" : 12.49271,
      "lng" : -84.05645,
      "municipio" : "khl",
      "nombre" : "El Porvenir"
    },
    {
      "lat" : 12.37177,
      "lng" : -83.89191,
      "municipio" : "khl",
      "nombre" : "El Rosario"
    },
    {
      "lat" : 12.13861,
      "lng" : -83.93922,
      "municipio" : "khl",
      "nombre" : "El Sílico"
    },
    {
      "lat" : 12.44742,
      "lng" : -84.07662,
      "municipio" : "khl",
      "nombre" : "El Trapiche"
    },
    {
      "lat" : 12.2952,
      "lng" : -83.95985,
      "municipio" : "khl",
      "nombre" : "El Wary"
    },
    {
      "lat" : 12.27859,
      "lng" : -83.84188,
      "municipio" : "khl",
      "nombre" : "Flor de Pino"
    },
    {
      "lat" : 12.10412,
      "lng" : -83.99502,
      "municipio" : "khl",
      "nombre" : "Home Creek"
    },
    {
      "lat" : 12.31683,
      "lng" : -83.80845,
      "municipio" : "khl",
      "nombre" : "La Ceiba"
    },
    {
      "lat" : 12.2592,
      "lng" : -83.99119,
      "municipio" : "khl",
      "nombre" : "La Fonseca"
    },
    {
      "lat" : 12.36232,
      "lng" : -84.05808,
      "municipio" : "khl",
      "nombre" : "La Pichinga"
    },
    {
      "lat" : 12.51397,
      "lng" : -84.11086,
      "municipio" : "khl",
      "nombre" : "La Unión"
    },
    {
      "lat" : 12.17475,
      "lng" : -83.99194,
      "municipio" : "khl",
      "nombre" : "La Zompopa"
    },
    {
      "lat" : 12.29861,
      "lng" : -83.83572,
      "municipio" : "khl",
      "nombre" : "Las Lapas"
    },
    {
      "lat" : 12.24454,
      "lng" : -83.84481,
      "municipio" : "khl",
      "nombre" : "Las Limas"
    },
    {
      "lat" : 12.56266,
      "lng" : -84.08353,
      "municipio" : "khl",
      "nombre" : "Las Maravillas"
    },
    {
      "lat" : 12.18316,
      "lng" : -83.83157,
      "municipio" : "khl",
      "nombre" : "Loma de Mico"
    },
    {
      "lat" : 12.23565,
      "lng" : -83.7808,
      "municipio" : "khl",
      "nombre" : "Los Angeles"
    },
    {
      "lat" : 12.29612,
      "lng" : -83.75777,
      "municipio" : "khl",
      "nombre" : "Los Cinco"
    },
    {
      "lat" : 12.56606,
      "lng" : -84.11954,
      "municipio" : "khl",
      "nombre" : "Luz de San Marcos"
    },
    {
      "lat" : 12.27896,
      "lng" : -83.73625,
      "municipio" : "khl",
      "nombre" : "Manhattan"
    },
    {
      "lat" : 12.19993,
      "lng" : -83.97414,
      "municipio" : "khl",
      "nombre" : "Neysi Ríos"
    },
    {
      "lat" : 12.41128,
      "lng" : -83.92941,
      "municipio" : "khl",
      "nombre" : "Nueva Alianza"
    },
    {
      "lat" : 12.44155,
      "lng" : -84.03538,
      "municipio" : "khl",
      "nombre" : "Nuevo Chontales"
    },
    {
      "lat" : 12.18294,
      "lng" : -84.04536,
      "municipio" : "khl",
      "nombre" : "Salto Sam Brown"
    },
    {
      "lat" : 12.15528,
      "lng" : -83.97477,
      "municipio" : "khl",
      "nombre" : "Sam Brown"
    },
    {
      "lat" : 12.52381,
      "lng" : -84.0152,
      "municipio" : "khl",
      "nombre" : "San Pablo"
    },
    {
      "lat" : 12.23421,
      "lng" : -83.98717,
      "municipio" : "khl",
      "nombre" : "San Ramón Nuevo"
    },
    {
      "lat" : 12.22409,
      "lng" : -84.03307,
      "municipio" : "khl",
      "nombre" : "San Ramón Viejo"
    },
    {
      "lat" : 12.25607,
      "lng" : -83.8257,
      "municipio" : "khl",
      "nombre" : "Santa Isabel"
    },
    {
      "lat" : 12.24096,
      "lng" : -84.01805,
      "municipio" : "khl",
      "nombre" : "Son Cuan"
    },
    {
      "lat" : 13.02933,
      "lng" : -84.62172,
      "municipio" : "lcrg",
      "nombre" : "Aguas Calientes"
    },
    {
      "lat" : 13.21786,
      "lng" : -84.01696,
      "municipio" : "lcrg",
      "nombre" : "Anglo América"
    },
    {
      "lat" : 13.05084,
      "lng" : -84.47916,
      "municipio" : "lcrg",
      "nombre" : "Apawas"
    },
    {
      "lat" : 13.24005,
      "lng" : -84.3874,
      "municipio" : "lcrg",
      "nombre" : "Apawonta"
    },
    {
      "lat" : 13.06251,
      "lng" : -84.58569,
      "municipio" : "lcrg",
      "nombre" : "Batitán"
    },
    {
      "lat" : 13.20373,
      "lng" : -84.0503,
      "municipio" : "lcrg",
      "nombre" : "Betania"
    },
    {
      "lat" : 13.1415,
      "lng" : -84.7668,
      "municipio" : "lcrg",
      "nombre" : "Betanis"
    },
    {
      "lat" : 13.1993,
      "lng" : -84.3669,
      "municipio" : "lcrg",
      "nombre" : "Boca de Piedra"
    },
    {
      "lat" : 13.04351,
      "lng" : -84.30977,
      "municipio" : "lcrg",
      "nombre" : "El Cañal"
    },
    {
      "lat" : 13.10409,
      "lng" : -84.23101,
      "municipio" : "lcrg",
      "nombre" : "El Gallo"
    },
    {
      "lat" : 13.1769,
      "lng" : -84.7501,
      "municipio" : "lcrg",
      "nombre" : "El Gamalote"
    },
    {
      "lat" : 13.12043,
      "lng" : -84.16369,
      "municipio" : "lcrg",
      "nombre" : "El Guayabo"
    },
    {
      "lat" : 13.04704,
      "lng" : -84.72395,
      "municipio" : "lcrg",
      "nombre" : "Estrella de la Vega del Río"
    },
    {
      "lat" : 13.02707,
      "lng" : -84.70063,
      "municipio" : "lcrg",
      "nombre" : "Estrella Medalla Milagrosa"
    },
    {
      "lat" : 12.9464,
      "lng" : -84.64088,
      "municipio" : "lcrg",
      "nombre" : "Feliciano"
    },
    {
      "lat" : 13.0916,
      "lng" : -84.575,
      "municipio" : "lcrg",
      "nombre" : "Hachita"
    },
    {
      "lat" : 13.19772,
      "lng" : -84.08051,
      "municipio" : "lcrg",
      "nombre" : "Kansas City"
    },
    {
      "lat" : 13.11498,
      "lng" : -84.214209,
      "municipio" : "lcrg",
      "nombre" : "La Ceiba"
    },
    {
      "lat" : 12.96985,
      "lng" : -84.08048,
      "municipio" : "lcrg",
      "nombre" : "La Concepción"
    },
    {
      "lat" : 12.89775,
      "lng" : -84.45237,
      "municipio" : "lcrg",
      "nombre" : "La Palma"
    },
    {
      "lat" : 12.97337,
      "lng" : -84.18848,
      "municipio" : "lcrg",
      "nombre" : "La Trinidad"
    },
    {
      "lat" : 13.22754,
      "lng" : -84.06983,
      "municipio" : "lcrg",
      "nombre" : "Makantaka"
    },
    {
      "lat" : 13.24611,
      "lng" : -84.08692,
      "municipio" : "lcrg",
      "nombre" : "Makantakita"
    },
    {
      "lat" : 13.12039,
      "lng" : -84.13213,
      "municipio" : "lcrg",
      "nombre" : "Matagalpa"
    },
    {
      "lat" : 12.83111,
      "lng" : -84.58999,
      "municipio" : "lcrg",
      "nombre" : "Mayawas"
    },
    {
      "lat" : 13.09419,
      "lng" : -84.25026,
      "municipio" : "lcrg",
      "nombre" : "Muelle Real"
    },
    {
      "lat" : 13.07586,
      "lng" : -84.14623,
      "municipio" : "lcrg",
      "nombre" : "Nueva Estrella"
    },
    {
      "lat" : 12.9023,
      "lng" : -84.519,
      "municipio" : "lcrg",
      "nombre" : "Nuevo Amancecer"
    },
    {
      "lat" : 13.05292,
      "lng" : -84.2103,
      "municipio" : "lcrg",
      "nombre" : "Nuevo San Antonio"
    },
    {
      "lat" : 13.04641,
      "lng" : -84.51685,
      "municipio" : "lcrg",
      "nombre" : "Olea Olea"
    },
    {
      "lat" : 12.78077,
      "lng" : -84.60488,
      "municipio" : "lcrg",
      "nombre" : "Oliwas"
    },
    {
      "lat" : 13.1506,
      "lng" : -84.5954,
      "municipio" : "lcrg",
      "nombre" : "Poncaya"
    },
    {
      "lat" : 12.84741,
      "lng" : -84.49377,
      "municipio" : "lcrg",
      "nombre" : "Río Silva"
    },
    {
      "lat" : 12.95721,
      "lng" : -84.54183,
      "municipio" : "lcrg",
      "nombre" : "Sagrado Corazón"
    },
    {
      "lat" : 12.91372,
      "lng" : -84.68174,
      "municipio" : "lcrg",
      "nombre" : "San Antonio"
    },
    {
      "lat" : 12.92584,
      "lng" : -84.53901,
      "municipio" : "lcrg",
      "nombre" : "San Francisco Rancho Alegre"
    },
    {
      "lat" : 13.01593,
      "lng" : -84.13851,
      "municipio" : "lcrg",
      "nombre" : "San José"
    },
    {
      "lat" : 12.8273,
      "lng" : -84.57138,
      "municipio" : "lcrg",
      "nombre" : "San José del Arbolito"
    },
    {
      "lat" : 12.96057,
      "lng" : -84.47239,
      "municipio" : "lcrg",
      "nombre" : "San Miguel Casa de Alto"
    },
    {
      "lat" : 13.2326,
      "lng" : -84.45061,
      "municipio" : "lcrg",
      "nombre" : "San Miguel de la Esperanza"
    },
    {
      "lat" : 13.1897,
      "lng" : -84.5316,
      "municipio" : "lcrg",
      "nombre" : "San Pablo Río 22"
    },
    {
      "lat" : 13.17146,
      "lng" : -84.20029,
      "municipio" : "lcrg",
      "nombre" : "San Ramón"
    },
    {
      "lat" : 13.03166,
      "lng" : -84.19566,
      "municipio" : "lcrg",
      "nombre" : "Santa Rita"
    },
    {
      "lat" : 13.19361,
      "lng" : -84.43925,
      "municipio" : "lcrg",
      "nombre" : "Santo Domingo del Carmen"
    },
    {
      "lat" : 13.17525,
      "lng" : -84.13747,
      "municipio" : "lcrg",
      "nombre" : "Siawas"
    },
    {
      "lat" : 13.07703,
      "lng" : -84.29511,
      "municipio" : "lcrg",
      "nombre" : "Siksikwas"
    },
    {
      "lat" : 13.136,
      "lng" : -84.575,
      "municipio" : "lcrg",
      "nombre" : "Tres Esquinas"
    },
    {
      "lat" : 13.00947,
      "lng" : -84.35085,
      "municipio" : "lcrg",
      "nombre" : "Tumarin Indígena"
    },
    {
      "lat" : 12.98284,
      "lng" : -84.37826,
      "municipio" : "lcrg",
      "nombre" : "Tumarin Mestizo"
    },
    {
      "lat" : 13.201,
      "lng" : -84.6398,
      "municipio" : "lcrg",
      "nombre" : "Uliwas"
    },
    {
      "lat" : 13.1998,
      "lng" : -84.6585,
      "municipio" : "lcrg",
      "nombre" : "Uliwasito"
    },
    {
      "lat" : 13.1174,
      "lng" : -84.15356,
      "municipio" : "lcrg",
      "nombre" : "Walpa Daukra"
    },
    {
      "lat" : 13.11128,
      "lng" : -84.18681,
      "municipio" : "lcrg",
      "nombre" : "La Cruz de Río Grande"
    },
    {
      "lat" : 12.426361,
      "lng" : -83.815694,
      "municipio" : "lgp",
      "nombre" : "Arenita # 3"
    },
    {
      "lat" : 12.37212,
      "lng" : -83.82999,
      "municipio" : "lgp",
      "nombre" : "Arenita Land Creak"
    },
    {
      "lat" : 12.3383,
      "lng" : -83.68948,
      "municipio" : "lgp",
      "nombre" : "Awas"
    },
    {
      "lat" : 12.55496,
      "lng" : -83.9552,
      "municipio" : "lgp",
      "nombre" : "Blue Lagoon"
    },
    {
      "lat" : 12.44843,
      "lng" : -83.73132,
      "municipio" : "lgp",
      "nombre" : "Brown Bank"
    },
    {
      "lat" : 12.77816,
      "lng" : -83.87741,
      "municipio" : "lgp",
      "nombre" : "Caño Wilson"
    },
    {
      "lat" : 12.68667,
      "lng" : -83.80833,
      "municipio" : "lgp",
      "nombre" : "Dachinal"
    },
    {
      "lat" : 12.643017,
      "lng" : -83.966317,
      "municipio" : "lgp",
      "nombre" : "El Castaño"
    },
    {
      "lat" : 12.6514,
      "lng" : -83.7669,
      "municipio" : "lgp",
      "nombre" : "El Cedro 1"
    },
    {
      "lat" : 12.67508,
      "lng" : -83.87403,
      "municipio" : "lgp",
      "nombre" : "El Cedro 2"
    },
    {
      "lat" : 12.56571,
      "lng" : -83.99266,
      "municipio" : "lgp",
      "nombre" : "El Fosforo"
    },
    {
      "lat" : 12.78129,
      "lng" : -83.9237,
      "municipio" : "lgp",
      "nombre" : "El Limon"
    },
    {
      "lat" : 12.81325,
      "lng" : -83.9627,
      "municipio" : "lgp",
      "nombre" : "El Mango"
    },
    {
      "lat" : 12.614583,
      "lng" : -84.018033,
      "municipio" : "lgp",
      "nombre" : "El Papelito"
    },
    {
      "lat" : 12.34929,
      "lng" : -83.79965,
      "municipio" : "lgp",
      "nombre" : "El Paraiso"
    },
    {
      "lat" : 12.49631,
      "lng" : -83.93964,
      "municipio" : "lgp",
      "nombre" : "El Pedregal"
    },
    {
      "lat" : 12.67883,
      "lng" : -83.955383,
      "municipio" : "lgp",
      "nombre" : "El Zapote"
    },
    {
      "lat" : 12.67868,
      "lng" : -83.79069,
      "municipio" : "lgp",
      "nombre" : "Fruta de Pan"
    },
    {
      "lat" : 12.33003,
      "lng" : -83.67381,
      "municipio" : "lgp",
      "nombre" : "Haulover"
    },
    {
      "lat" : 12.67598,
      "lng" : -83.73258,
      "municipio" : "lgp",
      "nombre" : "Kahka Creek"
    },
    {
      "lat" : 12.39695,
      "lng" : -83.72556,
      "municipio" : "lgp",
      "nombre" : "Kahkabila"
    },
    {
      "lat" : 12.649944,
      "lng" : -83.683611,
      "municipio" : "lgp",
      "nombre" : "La Batata"
    },
    {
      "lat" : 12.62795,
      "lng" : -83.953067,
      "municipio" : "lgp",
      "nombre" : "La Chiripa"
    },
    {
      "lat" : 12.48117,
      "lng" : -83.75277,
      "municipio" : "lgp",
      "nombre" : "La Fe"
    },
    {
      "lat" : 12.52711,
      "lng" : -83.96708,
      "municipio" : "lgp",
      "nombre" : "La Pachona/El Toronjal"
    },
    {
      "lat" : 12.73215,
      "lng" : -83.79065,
      "municipio" : "lgp",
      "nombre" : "La Patriota"
    },
    {
      "lat" : 12.63908,
      "lng" : -83.77522,
      "municipio" : "lgp",
      "nombre" : "La Quinta"
    },
    {
      "lat" : 12.73067,
      "lng" : -83.94311,
      "municipio" : "lgp",
      "nombre" : "La Tortuguita"
    },
    {
      "lat" : 12.52777,
      "lng" : -84.00892,
      "municipio" : "lgp",
      "nombre" : "Los Duartes"
    },
    {
      "lat" : 12.62258,
      "lng" : -83.75404,
      "municipio" : "lgp",
      "nombre" : "Los Laurales"
    },
    {
      "lat" : 12.65065,
      "lng" : -83.79192,
      "municipio" : "lgp",
      "nombre" : "Mahagany"
    },
    {
      "lat" : 12.56121,
      "lng" : -83.69122,
      "municipio" : "lgp",
      "nombre" : "Marshall Point"
    },
    {
      "lat" : 12.41211,
      "lng" : -83.92924,
      "municipio" : "lgp",
      "nombre" : "Nueva Alianza"
    },
    {
      "lat" : 12.53463,
      "lng" : -83.83318,
      "municipio" : "lgp",
      "nombre" : "Nueva Esperanza"
    },
    {
      "lat" : 12.55704,
      "lng" : -83.7142,
      "municipio" : "lgp",
      "nombre" : "Orinoco"
    },
    {
      "lat" : 12.68292,
      "lng" : -83.75983,
      "municipio" : "lgp",
      "nombre" : "Pihtutigni"
    },
    {
      "lat" : 12.4576,
      "lng" : -83.85705,
      "municipio" : "lgp",
      "nombre" : "Pondler"
    },
    {
      "lat" : 12.65792,
      "lng" : -83.74238,
      "municipio" : "lgp",
      "nombre" : "Pueblo Nuevo"
    },
    {
      "lat" : 12.731789,
      "lng" : -83.723656,
      "municipio" : "lgp",
      "nombre" : "Punta Cañon"
    },
    {
      "lat" : 12.76332,
      "lng" : -83.682515,
      "municipio" : "lgp",
      "nombre" : "Punta Fusil"
    },
    {
      "lat" : 12.34064,
      "lng" : -83.68552,
      "municipio" : "lgp",
      "nombre" : "Raitipura"
    },
    {
      "lat" : 12.31217,
      "lng" : -83.72896,
      "municipio" : "lgp",
      "nombre" : "Rocky Point"
    },
    {
      "lat" : 12.45968,
      "lng" : -83.9322,
      "municipio" : "lgp",
      "nombre" : "San Jose"
    },
    {
      "lat" : 12.51717,
      "lng" : -83.78001,
      "municipio" : "lgp",
      "nombre" : "San Vicente"
    },
    {
      "lat" : 12.594,
      "lng" : -83.8069,
      "municipio" : "lgp",
      "nombre" : "Santa Rita"
    },
    {
      "lat" : 12.69743,
      "lng" : -83.84077,
      "municipio" : "lgp",
      "nombre" : "Sawawas"
    },
    {
      "lat" : 12.45619,
      "lng" : -83.48686,
      "municipio" : "lgp",
      "nombre" : "Set Net Point"
    },
    {
      "lat" : 12.75857,
      "lng" : -83.73854,
      "municipio" : "lgp",
      "nombre" : "Sumi Lagoon"
    },
    {
      "lat" : 12.67281,
      "lng" : -83.54485,
      "municipio" : "lgp",
      "nombre" : "Tasbapounie"
    },
    {
      "lat" : 12.339405,
      "lng" : -83.670971,
      "municipio" : "lgp",
      "nombre" : "Laguna de Perlas"
    },
    {
      "lat" : 13.0231,
      "lng" : -84.7905,
      "municipio" : "pwas",
      "nombre" : "Aguacate"
    },
    {
      "lat" : 13.03173,
      "lng" : -84.93627,
      "municipio" : "pwas",
      "nombre" : "Banderita"
    },
    {
      "lat" : 13.04687,
      "lng" : -84.88869,
      "municipio" : "pwas",
      "nombre" : "Barrio Pobre"
    },
    {
      "lat" : 13.03610359738,
      "lng" : -84.8562379473838,
      "municipio" : "pwas",
      "nombre" : "Belén"
    },
    {
      "lat" : 12.97205,
      "lng" : -84.94809,
      "municipio" : "pwas",
      "nombre" : "Betania"
    },
    {
      "lat" : 12.9628,
      "lng" : -85.00193,
      "municipio" : "pwas",
      "nombre" : "Bilampi"
    },
    {
      "lat" : 12.75273,
      "lng" : -84.75315,
      "municipio" : "pwas",
      "nombre" : "Calderón"
    },
    {
      "lat" : 12.92915,
      "lng" : -84.981,
      "municipio" : "pwas",
      "nombre" : "Caño de Agua"
    },
    {
      "lat" : 12.98935,
      "lng" : -84.13355,
      "municipio" : "pwas",
      "nombre" : "Chorro de Agua"
    },
    {
      "lat" : 12.9328658902996,
      "lng" : -84.917368715662,
      "municipio" : "pwas",
      "nombre" : "Cooperativa San José"
    },
    {
      "lat" : 13.01174,
      "lng" : -85.09236,
      "municipio" : "pwas",
      "nombre" : "Cuatro Esquinas Las Lomas"
    },
    {
      "lat" : 12.85495,
      "lng" : -85.18152,
      "municipio" : "pwas",
      "nombre" : "David Tejada"
    },
    {
      "lat" : 12.79839,
      "lng" : -84.90983,
      "municipio" : "pwas",
      "nombre" : "El Achote"
    },
    {
      "lat" : 12.79617,
      "lng" : -85.13694,
      "municipio" : "pwas",
      "nombre" : "El Campo"
    },
    {
      "lat" : 12.98851,
      "lng" : -84.77064,
      "municipio" : "pwas",
      "nombre" : "El Negro"
    },
    {
      "lat" : 12.8700011167215,
      "lng" : -85.1561452618067,
      "municipio" : "pwas",
      "nombre" : "El Pavón"
    },
    {
      "lat" : 12.92966,
      "lng" : -85.0701,
      "municipio" : "pwas",
      "nombre" : "El Toro"
    },
    {
      "lat" : 12.82246,
      "lng" : -84.68266,
      "municipio" : "pwas",
      "nombre" : "Jorgito"
    },
    {
      "lat" : 13.10181,
      "lng" : -84.80391,
      "municipio" : "pwas",
      "nombre" : "Kaskita"
    },
    {
      "lat" : 13.07714,
      "lng" : -84.86021,
      "municipio" : "pwas",
      "nombre" : "Kepi"
    },
    {
      "lat" : 12.85752,
      "lng" : -85.04312,
      "municipio" : "pwas",
      "nombre" : "La Hermosa Malakawas"
    },
    {
      "lat" : 13.06407,
      "lng" : -85.08183,
      "municipio" : "pwas",
      "nombre" : "La Paila"
    },
    {
      "lat" : 12.95228,
      "lng" : -85.17662,
      "municipio" : "pwas",
      "nombre" : "La Pedrera"
    },
    {
      "lat" : 12.93335,
      "lng" : -85.13606,
      "municipio" : "pwas",
      "nombre" : "La Placa"
    },
    {
      "lat" : 12.78304,
      "lng" : -84.96301,
      "municipio" : "pwas",
      "nombre" : "La Toboba"
    },
    {
      "lat" : 12.89264,
      "lng" : -84.84047,
      "municipio" : "pwas",
      "nombre" : "Las Martinas"
    },
    {
      "lat" : 12.76263,
      "lng" : -84.89256,
      "municipio" : "pwas",
      "nombre" : "Las Minas"
    },
    {
      "lat" : 12.94664,
      "lng" : -85.08643,
      "municipio" : "pwas",
      "nombre" : "Los Alcantaras"
    },
    {
      "lat" : 12.82655,
      "lng" : -85.01868,
      "municipio" : "pwas",
      "nombre" : "Malakawas (Sector El Diamante)"
    },
    {
      "lat" : 12.8349613910386,
      "lng" : -85.0994582076154,
      "municipio" : "pwas",
      "nombre" : "Malakawas Asentamiento"
    },
    {
      "lat" : 12.7962,
      "lng" : -85.13693,
      "municipio" : "pwas",
      "nombre" : "Nuevo Amanecer"
    },
    {
      "lat" : 12.84951,
      "lng" : -84.89165,
      "municipio" : "pwas",
      "nombre" : "Okawas"
    },
    {
      "lat" : 12.86876,
      "lng" : -84.00738,
      "municipio" : "pwas",
      "nombre" : "Palsawas"
    },
    {
      "lat" : 12.99778,
      "lng" : -84.8612,
      "municipio" : "pwas",
      "nombre" : "Pedro Baca"
    },
    {
      "lat" : 12.90134,
      "lng" : -84.92845,
      "municipio" : "pwas",
      "nombre" : "Perro Mocho"
    },
    {
      "lat" : 12.82613,
      "lng" : -84.7688,
      "municipio" : "pwas",
      "nombre" : "Pueblo Nuevo-Las Delicias"
    },
    {
      "lat" : 12.94813,
      "lng" : -84.77958,
      "municipio" : "pwas",
      "nombre" : "Salto Grande"
    },
    {
      "lat" : 13.05441,
      "lng" : -84.73943,
      "municipio" : "pwas",
      "nombre" : "San Pedro del Norte"
    },
    {
      "lat" : 12.75957,
      "lng" : -84.80997,
      "municipio" : "pwas",
      "nombre" : "Santa Rosa"
    },
    {
      "lat" : 12.95159,
      "lng" : -84.93517,
      "municipio" : "pwas",
      "nombre" : "Ubú Norte"
    },
    {
      "lat" : 12.7381749896272,
      "lng" : -85.0116183253495,
      "municipio" : "pwas",
      "nombre" : "Villa Siquia"
    },
    {
      "lat" : 12.95228,
      "lng" : -85.17662,
      "municipio" : "pwas",
      "nombre" : "Wanawana"
    },
    {
      "lat" : 13.06144,
      "lng" : -85.00832,
      "municipio" : "pwas",
      "nombre" : "Wasayamba"
    },
    {
      "lat" : 12.95986,
      "lng" : -85.10547,
      "municipio" : "pwas",
      "nombre" : "Wilike Arriba"
    },
    {
      "lat" : 13.01277,
      "lng" : -85.12192,
      "municipio" : "pwas",
      "nombre" : "Wilikito"
    },
    {
      "lat" : 12.78856,
      "lng" : -85.12322,
      "municipio" : "pwas",
      "nombre" : "Bocana de Paiwas"
    },
    {
      "lat" : 12.01369469,
      "lng" : -83.76528123,
      "municipio" : "bef",
      "nombre" : "Bluefields"
    },
    {
      "lat" : 12.16119206,
      "lng" : -84.21926208,
      "municipio" : "rma",
      "nombre" : "El Rama"
    },
    {
      "lat" : 12.23853304,
      "lng" : -83.74701898,
      "municipio" : "khl",
      "nombre" : "Kukra Hill"
    },
    {
      "lat" : 0,
      "lng" : 0,
      "municipio" : "bef",
      "nombre" : "Aguas Zarcas"
    }
]'''


municipios = json.loads(json_mun)

comunidades = json.loads(json_com)

mcount = 0

ccount = 0

overall_count = 0

print("Ingresando registros\n")
sys.stdout.write('['+' '*20+']  0%')
sys.stdout.flush()
for municipio in municipios:

  mun = Municipio()
  mun.nombre = municipio["nombre"].lower()
  mun.nombre_corto = municipio["nombre_corto"].lower()
  mun.area = municipio["area"]
  mun.poblacion = municipio["poblacion"]
  mun.save()
  mcount += 1
  num_com = 0

  for comunidad in comunidades:

    if comunidad["municipio"].lower() == municipio["nombre_corto"].lower():
      com = Comunidad()
      com.nombre = comunidad["nombre"].lower()
      com.municipio = mun
      com.lat = comunidad["lat"]
      com.lng = comunidad["lng"]
      com.save()
      num_com += 1

  ccount += num_com
  avance = (int)((num_com / len(comunidades)) * 20)
  overall_count += avance
  sys.stdout.write('\b'*25 + '=' * overall_count)
  if overall_count < 20:
    sys.stdout.write('>')
  sys.stdout.write(' '*(23-overall_count)+'] '+str(overall_count)+'%')
  sys.stdout.flush()
sys.stdout.write('\b'*25 + '=' * 20 + ']Hecho!\n' )
print("\n\n[OK]")
print("{0} de {1} municipios y {2} de {3} comunidades registrados.".format(mcount, len(municipios), ccount, len(comunidades)))

