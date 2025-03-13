# Análise de Dados de Pacientes com Diabetes

Este projeto tem como objetivo a análise de um conjunto de dados sobre pacientes que desenvolveram ou não diabetes. Usando o **índice de massa corporal (BMI)**, identificamos e categorizamos pacientes com mais de 50 anos em duas categorias: **Normal** e **Obeso**, com base no valor do **BMI** (mantendo o padrão americano para representação de massa corporal). 

## Objetivo

O objetivo principal é gerar uma amostra de dados com pacientes com mais de 50 anos e para cada um deles, indicar em uma nova coluna se o paciente está com **índice de massa corporal (BMI)** normal (menor que 30) ou obeso (maior ou igual a 30). O resultado final será salvo em um novo arquivo CSV, pronto para ser analisado por um Cientista de Dados.

## Tecnologias Utilizadas

- **Python**: Para carregamento, processamento e manipulação de dados.
- **SQL**: Para consultas e transformações no banco de dados.
- **SQLite**: Banco de dados utilizado para armazenar os dados temporariamente.
- **Pandas**: Para manipulação e exportação dos dados para CSV.

## Passos Realizados

1. **Carregamento dos dados**: O conjunto de dados de pacientes foi carregado de um arquivo CSV.
2. **Armazenamento no Banco de Dados**: Os dados foram transferidos para um banco de dados SQLite.
3. **Transformações**: Utilizando SQL, os dados foram filtrados para incluir apenas pacientes com mais de 50 anos. Além disso, uma nova coluna foi adicionada para categorizar os pacientes como **Normal** ou **Obeso** com base no valor do BMI.
4. **Exportação dos Dados**: Após as transformações, os dados foram exportados para um arquivo CSV e também para um arquivo Excel formatado com bordas e cabeçalhos em negrito.

## Como Usar

1. Clone este repositório para o seu computador:

   ```bash
   git clone https://github.com/eudesdgsouza/dadosPacientesDiabetes
   cd dadosPacientesDiabetes
   ```

2. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

3. Baixe o conjunto de dados PIMA disponível [aqui](https://www.kaggle.com/uciml/pima-indians-diabetes-database) e coloque o arquivo `diabetes.csv` na pasta `dataset/`.

4. Execute o script principal:

   ```bash
   python pacientes_diabetes.py
   ```

5. O arquivo gerado será salvo na pasta `dataset/` como `pacientes.csv` (CSV).

## Arquivos

- `pacientes_diabetes.py`: Código principal que carrega os dados, faz as transformações e salva o arquivo resultante.
- `dataset/diabetes.csv`: Conjunto de dados PIMA original.
- `dataset/pacientes.csv`: Arquivo CSV gerado com os pacientes com mais de 50 anos e as categorias de BMI.

## Como Contribuir

Sinta-se à vontade para fazer um fork deste repositório e enviar pull requests. Para alterações significativas, por favor, abra uma issue primeiro para discutir o que você gostaria de mudar.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

### **Notas:**

1. **Link para o Dataset**: Incluir o link direto para o conjunto de dados PIMA, como feito acima.
2. **Requisitos**: Crie um arquivo `requirements.txt` com as dependências do projeto (por exemplo, pandas, sqlite3)
