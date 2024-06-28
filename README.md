# Perceptrons Revisited

## Abstract:
This thesis investigates the capabilities of modern computer vision models in distinguishing between single connected spirals and disconnected double spirals on a two-dimensional plane. The study revisits the historical challenges posed by the spiral example, originally highlighted in the book "Perceptrons" by Minsky and Papert, which underscored the limitations of early neural network models like the perceptron. Utilizing a generated dataset inspired by a cellular automata-based method, the research implements Convolutional Neural Networks (CNNs) and Visual Transformers (ViT) to attempt to classify spiral patterns. The CNN achieved high accuracy, precision, recall, and F1-score, demonstrating significant advancements in neural network architectures. 

## Project structure:

### CCL
- **CCL_demo.ipynb** - notebook in which the CCL method is applied

### CNN
-   **CNN_best2.py** - the CNN code

-   **CNN_best2.h5** - the CNN model

-   **new_CNN_load.ipynb** - notebook in which the CNN model is loaded and tested

### Generate spirals
-   **one_spiral_function.py** - a function that creates a single connected spiral

-   **two_spirals_function.py** - a function that creates disconnected double spirals

-   **randomize_spirals.py** - a function that calls both of the spiral functions and creates a dataset of both kinds of spirals, including a JSON file of their labels

### Transformer
- **VisTransformer.ipynb** - notebook in which the transformer is trained

  

