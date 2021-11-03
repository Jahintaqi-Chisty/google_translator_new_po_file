# import polib
# po = polib.pofile('/odoo/custom/syncoria/bambora-bank-to-bank-EFT/bambora_batch_payment/i18n/fr_CA.po')
# for value,entry in enumerate(po):
#     entry.msgstr = str(value)
#     print ("message_id:"+entry.msgid, "\n tran:"+entry.msgstr)
# from translate_po.main import run
#
# run(fro="en", to="fr", src="/odoo/custom/syncoria/bambora-bank-to-bank-EFT/bambora_batch_payment/i18n/", dest="/home/jahin/")


import polib
from google_trans_new import google_translator
from googletrans import Translator
import io
def read_lines(file: str) -> list:
    """ Read lines into memory. """
    # all_lines = []
    # with io.open(file, 'r', encoding='utf8') as infile:
    #     for line in infile:
    #         all_lines.append(line)
    # return all_lines
    return polib.pofile(file)

def translate(source: str, arguments) -> str:
    """ Translates a single string into target language. """
    translator = google_translator()
    # translator = Translator()
    return translator.translate(source, lang_tgt=arguments['to'], lang_src=arguments['fro'])
    # return translator.translate(source, dest=arguments['to'], src=arguments['fro']).text


def save_lines(file: str, lines: list):
    """ Save lines from memory into a file.
     :parameter file:
     :parameter lines:
     """
    with io.open(file, 'w', encoding='utf8') as infile:
        infile.write("""msgid "" msgstr """"")
        for keys, values in lines.metadata.items():
            infile.write(f'"{keys}:{values}"\n')
        infile.write('\n')
        for line in lines:
            infile.write(line.__unicode__())
    # polib.save(file)

lines = read_lines('/odoo/custom/syncoria/bambora-bank-to-bank-EFT/bambora_batch_payment/i18n/fr_CA.po')
arguments = {
    'dest': '/home/jahin/',
    'fro': 'en',
    'src': '/odoo/custom/syncoria/bambora-bank-to-bank-EFT/bambora_batch_payment/i18n/',
    'to': 'fr_CA'
}
list = []
for line in lines:

    try:
        line.msgstr = polib.unescape(translate(polib.escape(line.msgid), arguments))
        print(f"Translated {lines.percent_translated()}% of the lines.")
    except:
        list.append(line.msgid_with_context)
        continue

save_lines('/home/jahin/fr_CA.po', lines)
print(list)


# def solve(new_file: str, old_file: str, arguments):
#     """ Translates single file. """
#     lines = read_lines(old_file)
#     for line in lines:
#         line.msgstr = polib.unescape(translate(polib.escape(line.msgid), arguments))
#         print(f"Translated {lines.percent_translated()}% of the lines.")
#     save_lines(new_file, lines)