1. Pré-requisitos
Certifique-se de que você tem os seguintes itens instalados no seu sistema:

Python 3.10+
Docker e Docker Compose
Git

2. Clonar o Repositório
Baixe o projeto (ou crie um repositório Git para seu código).

git clone <URL_DO_REPOSITORIO>
cd poke-data-pipeline

3. Instalar Dependências Localmente
Se quiser rodar localmente (fora do Docker), instale as dependências Python:

python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt

4. Executar o Pipeline Localmente
Depois de instalar as dependências, execute o pipeline diretamente:

python main.py

5. Usando Docker
Para rodar tudo dentro de um container Docker:

1. Construir a imagem Docker:

docker build -t poke-data-pipeline.

2. Rodar o container:

docker run --rm -v $(pwd):/app poke-data-pipeline