FROM dalloriam/python-dlib
ADD . /face_render
WORKDIR /face_render
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install -r requirements.txt
CMD ["flask", "run"]
