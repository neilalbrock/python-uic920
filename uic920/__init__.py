# -*- coding: utf-8 -*-

import re
from numbers import Integral
from collections import namedtuple

__all__ = ["countries"]

Country = namedtuple('Country', 'name, iso, uic')

_records = [
    Country(u"Finland", "FI", "10"),
    Country(u"Russian Federation", "RU", "20"),
    Country(u"Belarus", "BY", "21"),
    Country(u"Ukraine", "UA", "22"),
    Country(u"Moldova, Republic of", "MD", "23"),
    Country(u"Lithuania", "LT", "24"),
    Country(u"Latvia", "LV", "25"),
    Country(u"Estonia", "EE", "26"),
    Country(u"Kazakhstan", "KZ", "27"),
    Country(u"Georgia", "GE", "28"),
    Country(u"Uzbekistan", "UZ", "29"),
    Country(u"Korea, Democratic People's Republic of", "KP", "30"),
    Country(u"Mongolia", "MN", "31"),
    Country(u"Viet nam", "VN", "32"),
    Country(u"China", "CN", "33"),
    Country(u"Cuba", "CU", "40"),
    Country(u"Albania", "AL", "41"),
    Country(u"Japan", "JP", "42"),
    Country(u"Bosnia and Herzegovina, Serb Republic of ", "BA", "44"),
    Country(u"Bosnia and Herzegovina, Muslim-Croat Federation of ", "BA", "50"),
    Country(u"Poland", "PL", "51"),
    Country(u"Bulgaria", "BG", "52"),
    Country(u"Romania", "RO", "53"),
    Country(u"Czech Republic", "CZ", "54"),
    Country(u"Hungary", "HU", "55"),
    Country(u"Slovakia", "SK", "56"),
    Country(u"Azerbaijan", "AZ", "57"),
    Country(u"Armenia", "AM", "58"),
    Country(u"Kyrgyzstan", "KG", "59"),
    Country(u"Ireland", "IE", "60"),
    Country(u"Korea, Republic of", "KR", "61"),
    Country(u"Montenegro", "ME", "62"),
    Country(u"Macedonia, The former Yugoslav Republic of", "MK", "65"),
    Country(u"Tajikistan", "TJ", "66"),
    Country(u"Turkmenistan", "TM", "67"),
    Country(u"United Kingdom of Great Britain and Northern Ireland", "GB", "70"),
    Country(u"Spain", "ES", "71"),
    Country(u"Serbia", "RS", "72"),
    Country(u"Greece", "GR", "73"),
    Country(u"Sweden", "SE", "74"),
    Country(u"Turkey", "TR", "75"),
    Country(u"Norway", "NO", "76"),
    Country(u"Croatia", "HR", "78"),
    Country(u"Slovenia", "SI", "79"),
    Country(u"Germany", "DE", "80"),
    Country(u"Austria", "AT", "81"),
    Country(u"Luxemburg", "LU", "82"),
    Country(u"Italy", "IT", "83"),
    Country(u"Netherlands", "NL", "84"),
    Country(u"Switzerland", "CH", "85"),
    Country(u"Denmark", "DK", "86"),
    Country(u"France", "FR", "87"),
    Country(u"Belgium", "BE", "88"),
    Country(u"Egypt", "EG", "90"),
    Country(u"Tunesia", "TN", "91"),
    Country(u"Algeria", "DZ", "92"),
    Country(u"Morocco", "MA", "93"),
    Country(u"Portugal", "PT", "94"),
    Country(u"Israel", "IL", "95"),
    Country(u"Iran, Islamic Republic of", "IR", "96"),
    Country(u"Syrian Arab Republic", "SY", "97"),
    Country(u"Lebanon", "LB", "98"),
    Country(u"Iraq", "IQ", "99")]

def _build_index(idx):
    return dict((r[idx], r) for r in _records)

_by_iso = _build_index(1)
_by_uic = _build_index(2)

class _CountryLookup(object):
    def get (self, key):
        if isinstance(key, Integral):
            return _by_uic["%d" % key]
        
        k = key.upper()
        if len(k) == 2 and re.match(r"[0-9]{2}", k):
            return _by_uic[k]
        elif len(k) == 2:
            return _by_iso[k]
        
        raise ValueError()
    
    def __iter__(self):
        return iter(_records)

countries = _CountryLookup()