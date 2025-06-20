from PIL import Image
import pillow_heif
import os

def convert_heic_to_jpg(input_path, output_path=None, quality=75):
    """
    Converte uma imagem HEIC para JPG com opção de compressão.

    :param input_path: Caminho da imagem HEIC.
    :param output_path: Caminho de saída (opcional).
    :param quality: Qualidade da imagem JPG (1 a 95). Menor = mais compressão.
    """
    heif_file = pillow_heif.read_heif(input_path)
    image = Image.frombytes(
        heif_file.mode, heif_file.size, heif_file.data, "raw"
    )

    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".jpg"

    image.save(output_path, format="JPEG", quality=quality, optimize=True)
    print(f"Imagem convertida com sucesso: {output_path} (qualidade: {quality})")