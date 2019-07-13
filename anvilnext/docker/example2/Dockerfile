FROM python:2.7 
RUN pip install Flask 
COPY . / 
ENV FLASK_APP=hello-world.py 
EXPOSE 5000 
CMD ["echo", "I'm your Python program running"] \ 
		flask run --host=0.0.0.0 
USER admin
