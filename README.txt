Proyecto de Pelu-Query-A


La idea de este proyecto es una aplicacion web que nos permita cargar profesionales y servicios
Los profesionales se van a vincular a los servicios cargados, una vez vinculados se va a poder seleccionar un profesional luego un servicio, y vamos a poder elegir fechas, en la pagina fecha vamos a poder generar las fechas, luego horarios previamente cargados por el administrados, ya que esto solo lo debe manejar el dueño de la peluqueria.

Al momento de dar alta a un profesional se le puede dar de baja, pero este no va a ser borrado de forma permanente de la base si no que se se hace un borrado logico cambiando su estado a 'is_deleted = true' y no va a ser mostrado mas, lo mismo ocurre para los servicios pero el dueño va a tener la opcion de reactivar nuevamente los servicios.

Para confirmar permisos se requiere registrarse e inicar sesion, esto enviara un mail a la peluqueria y al cliente

la base de datos esta generada mendiante Postgree SQL, esta es su configuracion:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Peluqueria',
        'USER': 'postgres',
        'PASSWORD':'yourpass',
        'HOST': 'HostIP',
        'DATABASE_PORT': '5432'

    }
}

Aun faltan detalles y la gestion de permisos por usuarios ya que todos los usuarios pueden hacer el CRUD completo y modificar el css ya que esta muy basico 

Usuario admin:

#$!"#!" User: admin@test.com
!"#W%!"#% Password: Pass123$

