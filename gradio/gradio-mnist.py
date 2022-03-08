import tensorflow as tf
import gradio as gr

# trained on code adapted from Chollet's Tensorflow Keras docs
# ~99% accuracy on the MNIST test set

# code below adapted from Gradio docs

model = tf.keras.models.load_model("models/mnist_convnet.h5")


def recognize_digit(image):
    image = image.reshape(1, 28, 28, 1)  # add batch and color dims
    prediction = model.predict(image).tolist()[0]
    print(prediction)
    return {str(i): prediction[i] for i in range(10)}


gr.Interface(
    fn=recognize_digit,
    inputs="sketchpad",
    outputs=gr.outputs.Label(num_top_classes=3),
    live=True,
    description="Draw a number 0 through 9 on the sketchpad and see a prediction in real time.",
).launch()
