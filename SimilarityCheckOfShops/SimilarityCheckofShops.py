


import xlsxwriter
import pandas as pd


def find_similarity(id1, id2, magazas):
    num = .0
    den = .0
    for key in magazas[id1].keys():
        left, right = magazas[id1][key], magazas[id2][key]
        num += min(left, right)
        den += max(left, right)

    return num / den


def prepare_data(path):
    xlxs_file = pd.read_excel(path, )
    parsed_UrunID = xlxs_file["UrunID"][:]
    parsed_Magaza = xlxs_file["Mağaza"][:]
    parsed_Adet = xlxs_file["Adet"][:]

    magaza = {} #creating a dictionary for every magaza
    magaza_ids = list(set(parsed_Magaza))
    for id in magaza_ids:
        magaza[id] = {}

    urun_ids = list(set(parsed_UrunID))
    for id in urun_ids:
        for key in magaza_ids:
            magaza[key][id] = 0

    for i in range(len(parsed_UrunID)):
        magaza_id = parsed_Magaza[i]
        urun_id = parsed_UrunID[i]
        adet = parsed_Adet[i]
        magaza[magaza_id][urun_id] = adet

    return magaza


def interaction(magaza):
    id1 = int(input("Enter the magaza id 1: "))
    while id1 not in magaza.keys():
        print("Invalid id. Please enter a valid id")
        id1 = int(input("Enter the magaza id 1: "))

    id2 = int(input("Enter the magaza id 2: "))
    while id2 not in magaza.keys():
        print("Invalid id. Please enter a valid id")
        id2 = int(input("Enter the magaza id 2: "))

    print("Similarity between magaza {} and {} = {}".format(id1, id2, find_similarity(id1, id2, magaza)))


if __name__ == "__main__":
    magaza = prepare_data(r"C:\Users\baris\OneDrive\Masaüstü\2020 güz\aylin.xlsx")
    
"""
    matrix = []
    for key1 in magaza.keys():
        row = []
        for key2 in magaza.keys():
            row.append(find_similarity(key1, key2, magaza))
        matrix.append(row)
    print("matrix is {}".format(matrix))
    
    workbook = xlsxwriter.Workbook('denemeaylin.xlsx') 
    worksheet = workbook.add_worksheet()
    row = 0
    
    column = 0
    
    for module in matrix : 
  
        worksheet.write_row(row, column, module) 
        row += 1
      
    workbook.close() 
    """
    
    
    while True:
        interaction(magaza)
        check = input("To exit please write e, exit or quit: ")
        if check.lower() in ["e", "exit", "quit"]:
            break
        print("")
    
