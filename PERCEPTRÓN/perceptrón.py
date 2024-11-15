# -*- coding: utf-8 -*-
"""Perceptrón.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17u-vtqQfZr1srwAj6_au2R-x4lU_Rh-V

MAROCHO CAPA GABRIELA IRMA
"""

# Paso 1: Importar librerías
import numpy as np

# Paso 2: Definir la función de activación ReLU
def relu(x):
    return max(0, x)

class Perceptron:
    def __init__(self, input_size, learning_rate=0.01, epochs=100):
        # Inicializar pesos pequeños aleatorios y el umbral
        self.weights = np.random.uniform(-1, 1, input_size)
        self.bias = np.random.uniform(-1, 1)  # Umbral inicial
        self.learning_rate = learning_rate
        self.epochs = epochs

    def predict(self, X):
        # Calcular la salida Y usando los pesos y el umbral con ReLU
        linear_output = np.dot(X, self.weights) - self.bias
        return relu(linear_output)

    def predict_binary(self, X):
        # Predicción binaria utilizando un umbral de 0.5
        y = self.predict(X)
        return 1 if y >= 0.5 else 0

    def train(self, X, D):
        for epoch in range(self.epochs):
            print(f"Epoch {epoch+1}/{self.epochs}")
            for xi, di in zip(X, D):
                # Calcular salida predicha
                y = self.predict(xi)
                # Calcular el error
                error = di - y
                # Actualizar los pesos y el umbral
                self.weights += self.learning_rate * error * xi
                self.bias -= self.learning_rate * error

                print(f"Entrada: {xi}, Predicción continua: {y:.4f}, Deseada: {di}, Error: {error:.4f}")

# Paso 4: Preparar los datos de entrenamiento (Ejemplo: AND lógico)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
D = np.array([0, 0, 0, 1])  # Salidas deseadas para el AND

# Paso 5: Crear y entrenar el modelo
perceptron = Perceptron(input_size=2, learning_rate=0.1, epochs=10)
perceptron.train(X, D)

print("\nPredicciones finales (binarias):")
for xi in X:
    y_continua = perceptron.predict(xi)
    y_binaria = perceptron.predict_binary(xi)
    print(f"Entrada: {xi}, Predicción continua: {y_continua:.4f}, Predicción binaria: {y_binaria}")