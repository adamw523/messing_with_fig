echo "*********** Creating database ***********"
gosu postgres postgres --single <<- EOSQL
    CREATE DATABASE flask_app;
EOSQL
