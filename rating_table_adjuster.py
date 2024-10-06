__author__ = 'Lukas Horst'

import csv

import openpyxl


def get_points(file_path):
    """Reads the given rating table and returns the total points"""
    wb = openpyxl.load_workbook(file_path, data_only=True)
    ws = wb['Sheet1']
    rows = ws.iter_rows(min_row=20, max_row=75, min_col=1, max_col=1)
    row_of_sum = -1
    for i in rows:  # searching the right row
        if i[0].value == 'Summe':
            row_of_sum = i[0].row
            break
    return ws[f'C{row_of_sum}'].value


def read_csv_file(file_path):
    """Function to read a csv file and returns a list with each row in a dic"""
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = []
        for row in reader:
            rows.append(row)
    return rows


def write_csv_file(file_path, data):
    """Function to (over)write a csv file with the given data"""
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = list(data[0].keys())
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def update_rating(overall_rating_path, student_rating_path, student_name):
    """Function to update the points of the given student"""
    csv_data = read_csv_file(overall_rating_path)
    for row in csv_data:
        if row['Vollständiger Name'] == student_name:
            points = str(get_points(student_rating_path)).replace('.', ',')
            row['Bewertung'] = points
            write_csv_file(overall_rating_path, csv_data)
            return


if __name__ == '__main__':
    print(*read_csv_file('Test.csv'), sep='\n')
