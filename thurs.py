def sub_total(bill):
    subtot = 0

    for item in bill:
        subtot += (item['quantity']*item['item_cost'])

    return subtot



b = [{'quantity': 3, 'item_cost': 4.0, 'taxable': True}, {'quantity': 7, 'item_cost': 1.0, 'taxable': True}, {'quantity': 1, 'item_cost': 10.0, 'taxable': True}]

print(sub_total(b))




def taxable_items(bill):
    taxable =[]

    for item in bill:
        if item['taxable']:
            taxable.append(item)

    return taxable





c = [{'quantity': 3, 'item_cost': 4.0, 'taxable': False}, {'quantity': 7, 'item_cost': 1.0, 'taxable': False}, {'quantity': 4, 'item_cost': 10.0, 'taxable': True}, {'quantity': 1, 'item_cost': 10.0, 'taxable': False}]
print(taxable_items(c))



def taxable_sub_total(bill):
    subtot = 0
    for item in taxable_items(bill):
        subtot += (item['quantity']*item['item_cost'])

    return subtot

d = [{'quantity': 3, 'item_cost': 4.0, 'taxable': True}, {'quantity': 7, 'item_cost': 1.0, 'taxable': False}, {'quantity': 4, 'item_cost': 10.0, 'taxable': True}, {'quantity': 1, 'item_cost': 10.0, 'taxable': True}]

print(taxable_sub_total(d))



# def taxes(bill, tax_rate):
#     return taxable_sub_total(bill) * tax_rate








def taxes(bill, tax_rate):
    def g(bill):
        def f(bill):
            taxable =[]

            for item in bill:
                if item['taxable']:
                    taxable.append(item)

            return taxable

        subtot = 0
        for item in f(bill):
            subtot += (item['quantity']*item['item_cost'])

        return subtot

    return g(bill) * tax_rate

bill =[{'quantity': 3, 'item_cost': 4.0, 'taxable': True}, {'quantity': 7, 'item_cost': 1.0, 'taxable': False}, {'quantity': 3, 'item_cost': 10.0, 'taxable': True}, {'quantity': 1, 'item_cost': 10.0, 'taxable': True}]
tax_rate = 0.1

print(taxes(bill,tax_rate))



# return subtot*tax_rate


def bill_total(bill, tax_rate):
    def sub_total(bill):
        subtot = 0

        for item in bill:
            subtot += (item['quantity']*item['item_cost'])

        return subtot

    def taxes(bill, tax_rate):
        def g(bill):
            def f(bill):
                taxable =[]

                for item in bill:
                    if item['taxable']:
                        taxable.append(item)

                return taxable

            subtot = 0
            for item in f(bill):
                subtot += (item['quantity']*item['item_cost'])

            return subtot

        return g(bill) * tax_rate

    return sub_total(bill)+taxes(bill, tax_rate)


bill_total([{'quantity': 3, 'item_cost': 4.0, 'taxable': True}, {'quantity': 7, 'item_cost': 1.0, 'taxable': False}, {'quantity': 3, 'item_cost': 11.0, 'taxable': True}, {'quantity': 1, 'item_cost': 10.0, 'taxable': True}], 0.1)
