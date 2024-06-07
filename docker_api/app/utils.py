from decimal import *
from .chem_data import atomic_masses, atomic_exact_masses
from pprint import pprint


def mol_mass_calc(brutto_part, masses_dict):
    if len(brutto_part) == 1 and brutto_part.isupper(): # тип A
        return brutto_part, masses_dict.get(brutto_part)
    elif len(brutto_part) == 2 and brutto_part[0].isupper() and brutto_part[1].islower(): # тип Aa
        return brutto_part, masses_dict.get(brutto_part)
    elif brutto_part[1:].isdigit() and brutto_part[0].isupper(): # тип A(2) A222222
        return brutto_part[0], int(brutto_part[1:]) * masses_dict.get(brutto_part[0])
    elif brutto_part[2:].isdigit() and brutto_part[0].isupper() and brutto_part[1].islower(): # тип Aa(2)
        return brutto_part[:2], int(brutto_part[2:]) * masses_dict.get(brutto_part[:2])


def result_calc(brutto, exact=False):
    masses_dict = atomic_exact_masses if exact else atomic_masses
    total_result = {
        'total_mass': 0,
        'elements': {}
    }
    result = {}
    while brutto:
        if (len(brutto) == 1) or (len(brutto) == 2 and not (brutto[0].isupper() and brutto[1].isupper())):
            b, p = mol_mass_calc(brutto, masses_dict)
            result[b] = result.get(b, 0) + p
            break
        elif (brutto[0].isupper() and brutto[1:].isdigit()) or (brutto[0].isupper() and brutto[1].islower() and brutto[2:].isdigit()):
            b, p = mol_mass_calc(brutto, masses_dict)
            result[b] = result.get(b, 0) + p
            break
        for i, x in enumerate(brutto[1:], 1):
            if x.isupper():
                brutto_part = brutto[:i]
                brutto = brutto[i:]
                break
        b, p = mol_mass_calc(brutto_part, masses_dict)
        result[b] = result.get(b, 0) + p


    total_result['total_mass'] = f'{round(sum(result.values()), 4):.4f}'
    for k, v in result.items():
        total_result['elements'][k] = {
                'mass': f'{round(v, 4):.4f}',
                'percent': f'{round(v / float(total_result['total_mass'])* 100, 2)}'
            }

    return total_result


