FROM postgres:11.3 AS postgres

LABEL Name="hinge_takehome"
LABEL Version="eric_meadows"

USER postgres

RUN /etc/init.d/postgresql start

EXPOSE 5432
