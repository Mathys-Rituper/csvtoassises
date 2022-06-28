from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF
from models.participant import Participant

regularFont = ImageFont.truetype("Nunito-Bold.ttf", size=280)
boldFont = ImageFont.truetype("Nunito-ExtraBold.ttf", size=270)
boldsmall = ImageFont.truetype("Nunito-ExtraBold.ttf", size=200)


def create_badge(participant:Participant) ->Image:
    """
    Creates a badge with the given name, pronouns and local group of the models
    :param participant: Participant object
    :return:
    """
    template = Image.open("empty_badge.png")
    w, h = (3400, 2155)
    draw = ImageDraw.Draw(template)

    line1 = participant.name.strip().upper()
    line2 = participant.pronouns.strip().lower()
    line3 = participant.localgroup.strip()

    x1, y1 = draw.textsize(line1, boldFont)  # used for dynamic calculation to center text on page
    x2, y2 = draw.textsize(line2, boldsmall)
    x3, y3 = draw.textsize(line3, regularFont)
    draw.text(((w - x1) / 2, 560), line1.upper(), font=boldFont, fill='black')
    draw.text(((w - x2) / 2, 1000), line2, font=boldsmall, fill='black')
    draw.text(((w - x3) / 2, 1350), line3, font=regularFont, fill='black')
    return template


def generate_files_from_infolist(participants) -> [str]:
    """
    Generates a list of badge from a list of participants
    :param participants: list of participants
    :return: list of badge image jpg files
    """
    i = 0  # used to name files since no unique attribute exists in given data
    created_files = []
    for participant in participants:
        print(f"Création du badge de {participant.name}")
        output_name = f"./output/{i}.jpg"
        create_badge(participant).convert('RGB').save(output_name, optimize=True, quality=1)
        created_files.append(output_name)
        i += 1
    return created_files


def filename_list_to_pdf(files, output_filename,num_items_per_page=10):
    """
    Creates a pdf from a list of badge image files

    :param files: list of badge image files
    :param output_filename: name of the output pdf file
    :param num_items_per_page: number of items per page
    :return:
    """
    final = [files[i * num_items_per_page:(i + 1) * num_items_per_page] for i in
             range((len(files) + num_items_per_page - 1) // num_items_per_page)]  # transforms files into a list of
    # num_items_per_page-sized lists
    print(f"{len(final)} pages will be needed to export this series of badges.")

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    for page in final:
        print(f"Page with {len(page)} elements")
        pdf.add_page()
        for i in range(0, num_items_per_page):
            if len(page) >= i + 1:  # to accomodate for not full pages
                if i % 2 == 0:  # smart positionning : values hardcoded for current badge size, to accomodate for printer margins
                    x, y = (15, (i // 2) * 57+ 5)
                else:
                    x, y = (106, (i // 2) * 57 + 5)
                print(f"Adding element {i + 1}/{len(page)} to page")
                pdf.image(page[i], x=x, y=y, w=90, h=57)

    pdf.output(f'./{output_filename}')
