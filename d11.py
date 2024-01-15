import pandas as pd

def convert_people_cell(cell):
    if cell == "n.a.":
        return "Thuva"
    return cell

df = pd.read_excel("stock_data.xlsx","stock_data",converters={
    'people':convert_people_cell
})
print(df)

