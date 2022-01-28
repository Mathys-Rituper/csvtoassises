from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF

regularFont = ImageFont.truetype("Nunito-Bold.ttf", size=280)
boldFont = ImageFont.truetype("Nunito-ExtraBold.ttf", size=270)


def create_badge(name='testname', pronouns='testpronouns', localgroup="testgl",
                 specialattribute=None):
    template = Image.open("empty_badge.png")
    w, h = (3400, 2155)
    draw = ImageDraw.Draw(template)

    line1 = name + ' (' + pronouns + ')'

    x1, y1 = draw.textsize(line1.upper(), boldFont)  # used for dynamic calculation to center text on page
    x2, y2 = draw.textsize(localgroup, regularFont)
    draw.text(((w - x1) / 2, 700), line1.upper(), font=boldFont, fill='black')
    draw.text(((w - x2) / 2, 1200), localgroup, font=regularFont, fill='black')
    # TODO : implement special attribute if needed
    return template


def generate_files_from_infolist(participantdata) -> [str]:
    i = 0  # used to name files since no unique attribute exists in given data
    created_files = []
    for participant in participantdata:
        print(f"Création du badge de {participant['pseudo']}")
        output_name = f"./output/{i}.jpg"
        create_badge(participant['pseudo'].strip(), participant['pronoms'].strip(), participant['groupe_local'].strip(),
                     None).convert('RGB').save(output_name, optimize=True, quality=1)
        created_files.append(output_name)
        i += 1
    return created_files


def filename_list_to_pdf(files, output_filename,num_items_per_page=10):
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
                    x, y = (15, (i // 2) * 57    + 5)
                else:
                    x, y = (106, (i // 2) * 57 + 5)
                print(f"Adding element {i + 1}/{len(page)} to page")
                pdf.image(page[i], x=x, y=y, w=90, h=57)

    pdf.output(f'./{output_filename}')
