from face_render import app
from flask import request, jsonify
import dlib
import os
from io import BytesIO
import numpy as np
from PIL import Image
import json

@app.route('/check_faces', methods=["POST"])
def check_faces():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  file_to_check = request.files["file_to_check"].read()
  image = Image.open(BytesIO(file_to_check))
  nparray_image = np.array(image)
  nparray_image.setflags(write=True)
  face_detector = dlib.get_frontal_face_detector()
  predictor = dlib.shape_predictor(os.path.normpath(dir_path + '/models/shape_predictor_5_face_landmarks.dat'))
  dets = face_detector(nparray_image, 1)
  array_of_faces = []
  
  for d in dets:
    face_info = {
      'boundingBox' : {
        'top': d.top(),
        'left': d.left(), 
        'bottom': d.bottom(),
        'right': d.right()
      },
      'facePoints' : []
    }

    shape = predictor(nparray_image, d)

    for i in range(shape.num_parts):
        p = shape.part(i)
        face_info['facePoints'].append({'coordX': p.x, 'coordY': p.y })
    array_of_faces.append(face_info)

  return jsonify(array_of_faces)