import xmltodict
import xml.etree.ElementTree as xml


def get_dict(file):
    with open(file, "r") as hot:
        text = hot.read()
    d = xmltodict.parse(text)
    return d

def get_data(d):
    new = {}
    lst = []
    for i in d['Hotels']['Hotel']:
        if 'Hilton' in i['Name'] and 'new york' in i['Address']['State'].lower() or 'ny' in i['Address'][
            'State'].lower():
            new['Hotel'] = {}
            new['Hotel']['@Price'] = i['@Price']
            new['Hotel']['Name'] = i['Name']
            new['Hotel']['Address'] = i['Address'],
            d = dict(names=i['Name'], price=i['@Price'], adress=i['Address']['AddressLine'])
            lst.append(d)
    return lst

def createXML(filename, lst):
    root = xml.Element("Lists")

    appt = xml.Element("Names")
    root.append(appt)
    for i in lst:
        begin = xml.SubElement(appt, "Name")
        begin.text = i['names']

    appt = xml.Element("Prices")
    root.append(appt)
    for i in lst:
        begin = xml.SubElement(appt, "Price")
        begin.text = i['price']

    appt = xml.Element("Addresses")
    root.append(appt)
    for i in lst:
        begin = xml.SubElement(appt, "Address")
        begin.text = i['adress']

    tree = xml.ElementTree(root)

    with open(filename, "wb") as rez:
        tree.write(rez)


if __name__ == "__main__":
    input_file = 'Hotels.xml'
    output_file = 'Hilton.xml'
    dict_from_xml = get_dict(input_file)
    data_as_list = get_data(dict_from_xml)
    createXML(output_file, data_as_list)
