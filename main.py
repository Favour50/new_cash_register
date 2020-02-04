
def get_number_input(prompt):
    value = None
    while type(value) != float:

        try:
            value = float(input(prompt))
            return value

        except:
            pass


def main():
    while True:
        client_name = input('What is the customer\'s name?: ')
        if not client_name:
            break

        while True:
            product_name = input('what is the product name?: ')
            if not product_name:
                break
          
    
            product_qty = get_number_input(f'How many {product_name} purchased?: ')
            product_price = get_number_input(f'what is the {product_name}?: ')
            


if __name__ == '__main__':
    main()

