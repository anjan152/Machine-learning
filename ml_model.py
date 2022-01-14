import tensorflow as tf
import numpy as np
from tensorflow import keras
img_height = 180
img_width = 180
flower_path ="test.jpg"
class_names = ["daisy", "dandelion", "roses", "sunflowers", "tulips"]
img = tf.keras.utils.load_img(
    flower_path, target_size=(img_height, img_width)
)
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch
model = keras.models.load_model('./model.h5')
predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)
