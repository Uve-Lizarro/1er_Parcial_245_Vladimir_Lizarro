import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
#Vladimir Ariel Lizarro Velasquez
url='https://raw.githubusercontent.com/Uve-Lizarro/1er_Parcial_245_Vladimir_Lizarro/main/diabetes.csv'
datos=pd.read_csv(url)
x=datos.drop('Outcome', axis=1)
y=datos['Outcome']
arbol=DecisionTreeClassifier()
arbol.fit(x, y)
def modoGrafico():
    plt.figure(figsize=(12, 7))
    plot_tree(arbol, filled=True, feature_names=x.columns, class_names=['No Diabetes', 'Diabetes'])
    plt.show()
def modoEscrito():
    tree_text = export_text(arbol, feature_names=x.columns.tolist())
    with open("arbol_Decision_diabetes.txt", "w") as f:
        f.write(tree_text)

if __name__ == '__main__':
    modoEscrito()