from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path='test.pdf', language='ru'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f'Original file name: {Path(file_path).name}')
        print('Work in progress...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages).replace('\n', '')
        audio = gTTS(text=text, lang=language)
        file_name = Path(file_path).stem
        audio.save(f'{file_name}.mp3')
        return f'{file_name}.mp3 created'

    else:
        return 'File not exist, check the file path'


if __name__ == '__main__':
    file_path = input('\nInput file path to .PDF file: ')
    language = input('Input language, "en" or "ru": ')
    tprint('PDF TO MP3', font='random')
    print(pdf_to_mp3(file_path=file_path, language=language))
