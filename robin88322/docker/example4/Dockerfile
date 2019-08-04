FROM python:3 

WORKDIR /usr/src/app

COPY data.py /usr/src/app

COPY s_radiation_2018.nc  /usr/src/app

RUN pip install pandas && pip install xarray && pip install numpy && pip install netCDF4

CMD [ "python", "data.py" ]

