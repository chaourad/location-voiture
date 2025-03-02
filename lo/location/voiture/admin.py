from django.contrib import admin

from .models import Ville, Voiture, Reservation , Client


# Register your models here.




@admin.register(Ville)
class VilleAdmin(admin.ModelAdmin):
    list_display = ('nom' , )




@admin.register(Voiture)
class VoitureAdmin(admin.ModelAdmin):
    list_display = ('id','nom', 'prix_jour', 'nombre_siege', 'nbr_bagage', 'nbr_portes', 'climatise','manuelle','photourl' ,'ville',  )
    list_filter = ('id','nom', 'prix_jour', 'nombre_siege', 'nbr_bagage', 'nbr_portes', 'climatise','manuelle','photourl')
    search_fields = ( 'ville',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("date_debut" , "date_fin" , "voiture","client")
    list_filter = ("date_debut" , "date_fin" , "voiture","client")
    search_fields = ("voiture",)



@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("username" , "email" , "password" , "age", "date_permis", "ref_permis")
    search_fields = ("email",)
