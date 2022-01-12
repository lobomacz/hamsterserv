from django.contrib.auth.models import User, Group
from hamster.admin import *
from suir.admin import *


# Register your models here.

#  _   _                             _                      _                    
# | | | |   __ _   _ __ ___    ___  | |_    ___   _ __     / \     _ __    _ __  
# | |_| |  / _` | | '_ ` _ \  / __| | __|  / _ \ | '__|   / _ \   | '_ \  | '_ \ 
# |  _  | | (_| | | | | | | | \__ \ | |_  |  __/ | |     / ___ \  | |_) | | |_) |
# |_| |_|  \__,_| |_| |_| |_| |___/  \__|  \___| |_|    /_/   \_\ | .__/  | .__/ 
#                                                                 |_|     |_|    

# Admin de la aplicación hamster

hamster_admin = HamsterAdmin(name='hamsteradmin')

hamster_admin.register(Funcionario, FuncionarioAdmin)
hamster_admin.register(Beneficiario, BeneficiarioAdmin)
hamster_admin.register(User, UsuarioAdmin)
hamster_admin.register(Group)


#  ____    _   _   ___   ____  
# / ___|  | | | | |_ _| |  _ \ 
# \___ \  | | | |  | |  | |_) |
#  ___) | | |_| |  | |  |  _ < 
# |____/   \___/  |___| |_| \_\
                              

# Admin de la aplicación suir


suir_admin = SuirAdmin(name='suiradmin')

suir_admin.register(Anuncio, AnuncioAdmin)
suir_admin.register(Contacto)
suir_admin.register(Tabla, TablaAdmin)
suir_admin.register(DetalleTabla, DetalleTablaAdmin)
suir_admin.register(Entidad, EntidadAdmin)
suir_admin.register(Municipio, MunicipioAdmin)
suir_admin.register(Comunidad, ComunidadAdmin)
suir_admin.register(Indicador, IndicadorAdmin)
suir_admin.register(ValorIndicador, ValorAdmin)
suir_admin.register(Institucion)
suir_admin.register(LinkExterno)
suir_admin.register(LinkRed)
suir_admin.register(Publicacion, PublicacionAdmin)
suir_admin.register(Transmision, TransmisionAdmin)
suir_admin.register(Carrusel, CarruselAdmin)
suir_admin.register(User, SuirUserAdmin)
suir_admin.register(Group)
