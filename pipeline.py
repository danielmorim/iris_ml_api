# -*- coding: utf-8 -*-
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
import joblib

def run_pipeline():
    # Carregar o dataset Iris
    iris = fetch_ucirepo(id=53)
    X = iris.data.features
    y = iris.data.targets

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Escalonamento dos dados
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.fit_transform(X_test)

    # Treinar o modelo de Regressão Logística
    model = LogisticRegression()
    model.fit(X_train, y_train.values.ravel())

    # Avaliação do modelo
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f'Acurácia do modelo: {accuracy:.2f}')

    cm = confusion_matrix(y_test, predictions)
    print(f'Matriz Confusão: \n{cm}')

    # Salvar o modelo e o scaler treinados
    joblib.dump(model, 'iris_model.pkl')
    joblib.dump(sc, 'iris_scaler.pkl')

if __name__ == '__main__':
    run_pipeline()