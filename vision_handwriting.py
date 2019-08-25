import argparse
import re

def detect_document_uri(uri):
    """Detects document features in the file located in Google Cloud
    Storage."""
    from google.cloud import vision
    from google.oauth2 import service_account
    credentials = service_account.Credentials. from_service_account_file('api_key.json')
    client = vision.ImageAnnotatorClient(credentials=credentials)
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.document_text_detection(image=image)
    word_list=[]

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))

                    for symbol in word.symbols:
                        print('\tSymbol: {} (confidence: {})'.format(
                            symbol.text, symbol.confidence))



def detect_document(path):
    """Detects document features in an image."""
    from google.cloud import vision
    from google.oauth2 import service_account
    import io
    credentials = service_account.Credentials. from_service_account_file('api_key.json')
    client = vision.ImageAnnotatorClient(credentials=credentials)
    client = vision.ImageAnnotatorClient()

    # [START vision_python_migration_document_text_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)
    word_list=[]
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    word_list.append(word_text)

                    # for symbol in word.symbols:
                    #     print('\tSymbol: {} (confidence: {})'.format(
                    #         symbol.text, symbol.confidence))

    print(' '.join(word_text))

if __name__ == '__main__':
    directory='./images'
    for filename in os.listdir(directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            detect_document(os.path.join(directory,filename))
