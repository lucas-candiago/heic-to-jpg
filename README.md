# HEIC to JPG Converter

Este script converte imagens no formato `.heic` para `.jpg` com opção de compressão, utilizando Python, `pillow` e `pillow-heif`.

## 🧰 Requisitos

- Python 3.13+

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/lucas-candiago/heic-to-jpg.git
cd heic-to-jpg
```

Crie e ative um ambiente virtual:

```bash
python3 -m venv env
source env/bin/activate  # no Windows use: env\Scripts\activate
pip install poetry
```

Instale as dependências com o Poetry:

```bash
poetry install
```

## 🖼️ Uso


### Parâmetros

| Parâmetro     | Tipo     | Descrição                                                                 |
|---------------|----------|---------------------------------------------------------------------------|
| `input_path`  | `str`    | Caminho para o arquivo `.heic`                                            |
| `output_path` | `str`    | (Opcional) Caminho de saída para o `.jpg`. Se não for passado, usa o nome original. |
| `quality`     | `int`    | Qualidade da imagem `.jpg` (1-95). Quanto menor, mais compressão.         |

---

## 🐍 Exemplo de conversão via script

```bash
python3
>>> from converter import convert_heic_to_jpg
>>> convert_heic_to_jpg("foto.heic", quality=95)
```

Lembre-se que a qualidade pode variar de 1 a 95

---

## Exemplo direto No arquivo main.py

Chame a função dentro do arquivo main.py

```bash
convert_heic_to_jpg("foto.heic", quality=95)
```

Rode o script dentro do ambiente virtual:

```bash
python main.py
```

## Resultado

A imagem será salva na mesma pasta do script
