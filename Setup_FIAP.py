import pandas as pd
import numpy as np
import os
import warnings
from pathlib import Path

os.environ.setdefault('MPLCONFIGDIR', str(Path(__file__).with_name('.matplotlib')))

import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings('ignore')

sns.set_theme(style='whitegrid', palette='husl')
plt.rcParams['figure.dpi'] = 100

csv_path = Path(r'C:\Users\julho\Downloads\produtos_agricolas.csv.csv')
if not csv_path.exists():
    raise FileNotFoundError(f'Arquivo CSV nao encontrado: {csv_path}')

df = pd.read_csv(csv_path)

print(f"Dataset carregado: {df.shape[0]} linhas, {df['label'].nunique()} culturas")
print(df.head())

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

# TODO: Codificar o label (LabelEncoder), separar X e y,
# fazer train_test_split (80/20, stratify=y, random_state=42)
# e aplicar StandardScaler nos dados normalizados

le = LabelEncoder()
df['label_enc'] = le.fit_transform(df['label'])

X = df[features]
y = df['label_enc']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f'Treino: {X_train_scaled.shape[0]} linhas')
print(f'Teste: {X_test_scaled.shape[0]} linhas')

from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

modelos = {
    'Decision Tree': (DecisionTreeClassifier(random_state=42), X_train, X_test),
    'Random Forest': (RandomForestClassifier(random_state=42), X_train, X_test),
    'Gradient Boosting': (GradientBoostingClassifier(random_state=42), X_train, X_test),
    'KNN': (KNeighborsClassifier(n_neighbors=5), X_train_scaled, X_test_scaled),
    'Naive Bayes': (GaussianNB(), X_train_scaled, X_test_scaled),
}

resultados = {}

for nome, (modelo, X_tr, X_te) in modelos.items():
    modelo.fit(X_tr, y_train)
    y_pred = modelo.predict(X_te)

    resultados[nome] = {
        'accuracy': accuracy_score(y_test, y_pred),
        'f1_macro': f1_score(y_test, y_pred, average='macro')
    }

print('\nResultados:')
for nome, metricas in resultados.items():
    print(f"{nome}: accuracy={metricas['accuracy']:.4f} | f1_macro={metricas['f1_macro']:.4f}")

resultados_df = pd.DataFrame(resultados).T[['accuracy', 'f1_macro']]

fig1, ax1 = plt.subplots(figsize=(10, 5))
resultados_df.plot(kind='bar', ax=ax1, rot=35)
ax1.set_title('Comparacao de accuracy e f1_macro por modelo')
ax1.set_ylabel('Score')
ax1.set_ylim(0, 1.05)
ax1.legend(title='Metrica')
fig1.tight_layout()

melhor_modelo_nome = resultados_df['accuracy'].idxmax()
melhor_modelo, _, X_te_melhor = modelos[melhor_modelo_nome]
y_pred_melhor = melhor_modelo.predict(X_te_melhor)

cm = confusion_matrix(y_test, y_pred_melhor)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=le.classes_)
fig2, ax2 = plt.subplots(figsize=(12, 10))
disp.plot(ax=ax2, cmap='Blues', xticks_rotation=90, colorbar=False)
ax2.set_title(f'Matriz de confusao - {melhor_modelo_nome}')
fig2.tight_layout()

rf_modelo = modelos['Random Forest'][0]
importancias = pd.Series(rf_modelo.feature_importances_, index=features).sort_values()

fig3, ax3 = plt.subplots(figsize=(8, 5))
importancias.plot(kind='barh', ax=ax3)
ax3.set_title('Importancia das variaveis - Random Forest')
ax3.set_xlabel('Importancia')
fig3.tight_layout()

plt.show()
