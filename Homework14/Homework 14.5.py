import xml.etree.ElementTree as ET

# Чтение XML и вычисление общей стоимости
def calculate_total_cost(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    total_cost = 0
    for product in root.findall('product'):
        price = float(product.find('price').text)
        quantity = int(product.find('quantity').text)
        total_cost += price * quantity
    return total_cost

try:
    print(f"Общая стоимость товаров: {calculate_total_cost('products.xml')}")
except FileNotFoundError:
    print("Файл не найден!")
