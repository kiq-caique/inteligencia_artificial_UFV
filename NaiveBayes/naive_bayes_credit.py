
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score

credito = pd.read_csv("credit_customers.csv")

# Descobre os tipos de dados de cada coluna
col_types = credito.dtypes

# # CONFERÊNCIA DA LEITURA DAS COLUNAS DESSE DATASET
# # Exibe os resultados
# for col_name, dtype in col_types.items():
#     if pd.api.types.is_string_dtype(dtype):
#         print(f"A coluna '{col_name}' contém dados do tipo string.")
#     elif pd.api.types.is_numeric_dtype(dtype):
#         print(f"A coluna '{col_name}' contém dados do tipo numérico.")
        
# # credito.shape retorna uma tupla (num_linhas = 0, num_colunas = 1)
# num_colunas = credito.shape[1]
# print(f"O arquivo CSV possui {num_colunas} colunas.")

# # Inicializa uma lista para armazenar os índices das colunas que são strings
# string_columns_indices = []

# # Percorre as colunas e verifica se são do tipo string
# for idx, dtype in enumerate(col_types):
#     if pd.api.types.is_string_dtype(dtype):
#         string_columns_indices.append(idx)
        
# # Exibe os índices das colunas que são strings
# print("Índices das colunas que são strings:")
# print(string_columns_indices)

# # CONFERÊNCIA DA LEITURA DAS COLUNAS DESSE DATASET

previsores = credito.iloc[:, 0:20].values
classe = credito.iloc[:,20].values

# Converter os dados string para número
labelencoder = LabelEncoder()
previsores[:,0] = labelencoder.fit_transform(previsores[:,0])
previsores[:,2] = labelencoder.fit_transform(previsores[:,2])
previsores[:,3] = labelencoder.fit_transform(previsores[:,3])
previsores[:,5] = labelencoder.fit_transform(previsores[:,5])
previsores[:,6] = labelencoder.fit_transform(previsores[:,6])
previsores[:,8] = labelencoder.fit_transform(previsores[:,8])
previsores[:,9] = labelencoder.fit_transform(previsores[:,9])
previsores[:,11] = labelencoder.fit_transform(previsores[:,11])
previsores[:,13] = labelencoder.fit_transform(previsores[:,13])
previsores[:,14] = labelencoder.fit_transform(previsores[:,14])
previsores[:,16] = labelencoder.fit_transform(previsores[:,16])
previsores[:,18] = labelencoder.fit_transform(previsores[:,18])
previsores[:,19] = labelencoder.fit_transform(previsores[:,19])


x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(previsores, classe,test_size = 0.3, random_state=0)

# # CONFERINDO O DADOS DE TREINAMENTO E TESTES

# print("Conjunto de treinamento (features):")
# print(len(x_treinamento))

# print("\nConjunto de teste (features):")
# print(len(x_teste))

# print("\nConjunto de treinamento (labels):")
# print(len(y_treinamento))

# print("\nConjunto de teste (labels):")
# print(len(y_teste))

# # CONFERINDO O DADOS DE TREINAMENTO E TESTES

# # Para cada um dos registros de x_treinamento tem a resposta em y_treinamento para fazer a aprendizagem
naive_bayes = GaussianNB()
naive_bayes.fit(x_treinamento, y_treinamento)

previsoes = naive_bayes.predict(x_teste)
confusao = confusion_matrix(y_teste, previsoes)
taxa_acerto = accuracy_score(y_teste, previsoes)

print(confusao)
print(taxa_acerto)