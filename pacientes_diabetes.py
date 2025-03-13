import pandas as pd
import sqlite3
from typing import List


def load_data(filepath: str) -> pd.DataFrame:
    """Carrega o dataset de diabetes a partir de um arquivo CSV."""
    df = pd.read_csv(filepath)
    print(f"✔ Dataset carregado: {df.shape[0]} linhas, {df.shape[1]} colunas")
    return df


def create_database(connection: sqlite3.Connection) -> None:
    """Cria a tabela 'pacientes' no banco de dados, se não existir."""
    with connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS pacientes (
                Pregnancies INT,
                Glucose INT,
                BloodPressure INT,
                SkinThickness INT,
                Insulin INT,
                BMI DECIMAL(8, 2),
                DiabetesPedigreeFunction DECIMAL(8, 2),
                Age INT,
                Outcome INT,
                Perfil VARCHAR(10)
            )
        """)
    print("✔ Banco de dados inicializado.")


def insert_filtered_data(connection: sqlite3.Connection) -> None:
    """Insere pacientes com mais de 50 anos na tabela 'pacientes'."""
    with connection:
        connection.execute("""
            INSERT INTO pacientes (Pregnancies, Glucose, BloodPressure, SkinThickness, 
                                   Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome)
            SELECT Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, 
                   DiabetesPedigreeFunction, Age, Outcome 
            FROM diabetes WHERE Age > 50
        """)
    print("✔ Pacientes acima de 50 anos inseridos.")


def update_patient_profiles(connection: sqlite3.Connection) -> None:
    """Atualiza a coluna 'Perfil' na tabela 'pacientes' com base no IMC."""
    with connection:
        connection.execute("UPDATE pacientes SET Perfil = 'Normal' WHERE BMI < 30")
        connection.execute("UPDATE pacientes SET Perfil = 'Obeso' WHERE BMI >= 30")
    print("✔ Perfis dos pacientes atualizados com base no IMC.")


def fetch_data_as_dataframe(connection: sqlite3.Connection, query: str) -> pd.DataFrame:
    """Executa uma query SQL e retorna os resultados como um DataFrame do Pandas."""
    df = pd.read_sql_query(query, connection)
    print(f"✔ Consulta executada: {df.shape[0]} registros retornados")
    return df


def save_to_csv(df: pd.DataFrame, filepath: str) -> None:
    """Salva um DataFrame em formato CSV."""
    df.to_csv(filepath, index=False)
    print(f"✔ Arquivo salvo: {filepath}")


def main():
    dataset_path = "dataset/diabetes.csv"
    output_csv_path = "dataset/pacientes.csv"
    database_path = "dataset/diabetes.db"

    # Carregar dados
    df = load_data(dataset_path)

    # Criar conexão com o banco
    with sqlite3.connect(database_path) as connection:
        # Criar tabela e carregar dados
        create_database(connection)
        df.to_sql("diabetes", connection, if_exists="replace", index=False)
        print("✔ Dados carregados no banco de dados.")

        # Inserir e atualizar dados
        insert_filtered_data(connection)
        update_patient_profiles(connection)

        # Buscar os dados processados
        resultado = fetch_data_as_dataframe(connection, "SELECT * FROM pacientes")

        # Salvar em CSV
        save_to_csv(resultado, output_csv_path)

    print("🎯 Processo finalizado com sucesso!")


if __name__ == "__main__":
    main()
