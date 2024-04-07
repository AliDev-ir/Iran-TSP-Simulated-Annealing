from anneal import SimAnneal
import matplotlib.pyplot as plt
import random
import xlrd

loc = ("distances.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
number_of_cities = sheet.nrows - 1
cities = [sheet.cell_value(0, i) for i in range(1, number_of_cities + 1, 1)]
city_distance = [[sheet.cell_value(j, i) for i in range(1, number_of_cities + 1, 1)] for j in
                 range(1, number_of_cities + 1, 1)]
coords = []
coords = [[random.uniform(-100, 100), random.uniform(-100, 100),cities[i]] for i in range(number_of_cities)]

if __name__ == "__main__":
    sa = SimAnneal(coords, city_distance=city_distance,cities=cities, stopping_iter=100000)
    sa.anneal()
    sa.visualize_routes()
