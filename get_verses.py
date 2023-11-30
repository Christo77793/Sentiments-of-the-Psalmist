import sqlite3
import csv

MAIN_DB_LOCATION = r"bible_database.db"  # Database location
csv_file_path = "psalm_text.csv"  # CSV file path


def show_verses(book_id, chapter_id, translation_filter):
    '''
    Function to show the verses from the provided book name, chapter number and the selected translation

    :parameter: book_id -> Contains the book name's index number
    :parameter: chapter_id -> Contains the chapter number
    :parameter: translation_filter -> Contains the translation's index
    '''
    conn = sqlite3.connect(MAIN_DB_LOCATION)

    cursor = conn.cursor()

    book_id += 1
    book_id = str(book_id)

    if type(chapter_id) is not str:
        chapter_id = str(chapter_id)  # converting to string

    if translation_filter == "KJV":
        selected_translation = "t_kjv"

    elif translation_filter == "ASV":
        selected_translation = "t_asv"

    elif translation_filter == "BBE":
        selected_translation = "t_bbe"

    elif translation_filter == "WBT":
        selected_translation = "t_wbt"

    elif translation_filter == "YLT":
        selected_translation = "t_ylt"

    else:  # DARBY
        selected_translation = "t_dby"

    cursor.execute(f'''SELECT * FROM {selected_translation}
                WHERE b = {book_id} AND c = {chapter_id}''')

    selected_verses = cursor.fetchall()

    conn.commit()
    conn.close()

    return selected_verses


psalmist_verses = []

# Code to add all of the verses to a single Python list
for chapters in range(1, 151):
    output = show_verses(18, chapters, "KJV")
    for x in range(0, len(output)):
        psalmist_verses.append(output[x][4])

# Write the Psalms data to the CSV file
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Psalm Text"])  # Writing the header
    writer.writerows([[verse] for verse in psalmist_verses])  # Write each verse to the CSV file

print(f"Psalm's data has been successfully stored in {csv_file_path}")
