atomic_masses = {
    'H': 1.0079,        # 1     Водород
    'He': 4.0026,       # 2     Гелий
    'Li': 6.9410,       # 3     Литий
    'Be': 9.0122,       # 4     Бериллий
    'B': 10.8110,       # 5     Бор
    'C': 12.0107,       # 6     Углерод
    'N': 14.0067,       # 7     Азот
    'O': 15.9994,       # 8     Кислород
    'F': 18.9984,       # 9     Фтор
    'Ne': 20.1797,      # 10    Неон
    'Na': 22.9898,      # 11    Натрий
    'Mg': 24.3050,      # 12    Магний
    'Al': 26.9815,      # 13    Алюминий
    'Si': 28.0855,      # 14    Кремний
    'P': 30.9738,       # 15    Фосфор
    'S': 32.0650,       # 16    Сера
    'Cl': 35.4530,      # 17    Хлор
    'Ar': 39.9480,      # 18    Аргон
    'K': 39.0983,       # 19    Калий
    'Ca': 40.0780,      # 20    Кальций
    'Sc': 44.9559,      # 21    Скандий
    'Ti': 47.8670,      # 22    Титан
    'V': 50.9415,       # 23    Ванадий
    'Cr': 51.9961,      # 24    Хром
    'Mn': 54.9380,      # 25    Марганец
    'Fe': 55.8450,      # 26    Железо
    'Co': 58.9332,      # 27    Кобальт
    'Ni': 58.6934,      # 28    Никель
    'Cu': 63.5460,      # 29    Медь
    'Zn': 65.3800,      # 30    Цинк
    'Ga': 69.7230,      # 31    Галлий
    'Ge': 72.6400,      # 32    Германий
    'As': 74.9216,      # 33    Мышьяк
    'Se': 78.9600,      # 34    Селен
    'Br': 79.9040,      # 35    Бром
    'Kr': 83.7980,      # 36    Криптон
    'Rb': 85.4678,      # 37    Рубидий
    'Sr': 87.6200,      # 38    Стронций
    'Y': 88.9059,       # 39    Иттрий
    'Zr': 91.2240,      # 40    Цирконий
    'Nb': 92.9064,      # 41    Ниобий
    'Mo': 95.9600,      # 42    Молибден
    'Tc': 98.9063,      # 43    Технеций
    'Ru': 101.0700,     # 44    Рутений
    'Rh': 102.9055,     # 45    Родий
    'Pd': 106.4200,     # 46    Палладий
    'Ag': 107.8682,     # 47    Серебро
    'Cd': 112.4110,     # 48    Кадмий
    'In': 114.8180,     # 49    Индий
    'Sn': 118.7100,     # 50    Олово
    'Sb': 121.7600,     # 51    Сурьма
    'Te': 127.6000,     # 52    Теллур
    'I': 126.9045,      # 53    Йод
    'Xe': 131.2930,     # 54    Ксенон
    'Cs': 132.9055,     # 55    Цезий
    'Ba': 137.3270,     # 56    Барий
    'La': 138.9055,     # 57    Лантан
    'Ce': 140.1160,     # 58    Церий
    'Pr': 140.9077,     # 59    Празеодим
    'Nd': 144.2420,     # 60    Неодим
    'Pm': 145.0000,     # 61    Прометий
    'Sm': 150.3600,     # 62    Самарий
    'Eu': 151.9640,     # 63    Европий
    'Gd': 157.2500,     # 64    Гадолиний
    'Tb': 158.9254,     # 65    Тербий
    'Dy': 162.5000,     # 66    Диспрозий
    'Ho': 164.9303,     # 67    Гольмий
    'Er': 167.2590,     # 68    Эрбий
    'Tm': 168.9342,     # 69    Тулий
    'Yb': 173.0540,     # 70    Иттербий
    'Lu': 174.9668,     # 71    Лютеций
    'Hf': 178.4900,     # 72    Гафний
    'Ta': 180.9479,     # 73    Тантал
    'W': 183.8400,      # 74    Вольфрам
    'Re': 186.2070,     # 75    Рений
    'Os': 190.2300,     # 76    Осмий
    'Ir': 192.2170,     # 77    Иридий
    'Pt': 195.0840,     # 78    Платина
    'Au': 196.9666,     # 79    Золото
    'Hg': 200.5900,     # 80    Ртуть
    'Tl': 204.3833,     # 81    Таллий
    'Pb': 207.2000,     # 82    Свинец
    'Bi': 208.9804,     # 83    Висмут
    'Po': 209.0000,     # 84    Полоний
    'At': 210.0000,     # 85    Астат
    'Rn': 222.0000,     # 86    Радон
    'Fr': 223.0000,     # 87    Франций
    'Ra': 226.0000,     # 88    Радий
    'Ac': 227.0000,     # 89    Актиний
    'Th': 232.0381,     # 90    Торий
    'Pa': 231.0359,     # 91    Протактиний
    'U': 238.0289       # 92    Уран
    }

atomic_exact_masses = {
    'H': 1.0078,        # 1     Водород
    'He': 4.0026,       # 2     Гелий
    'Li': 7.0160,       # 3     Литий
    'Be': 9.0122,       # 4     Бериллий
    'B': 11.0093,       # 5     Бор
    'C': 12.0000,       # 6     Углерод
    'N': 14.0031,       # 7     Азот
    'O': 15.9949,       # 8     Кислород
    'F': 18.9984,       # 9     Фтор
    'Ne': 19.9924,      # 10    Неон
    'Na': 22.9898,      # 11    Натрий
    'Mg': 23.9850,      # 12    Магний
    'Al': 26.9815,      # 13    Алюминий
    'Si': 27.9769,      # 14    Кремний
    'P': 30.9738,       # 15    Фосфор
    'S': 31.9721,       # 16    Сера
    'Cl': 34.9689,      # 17    Хлор
    'Ar': 39.9624,      # 18    Аргон
    'K': 38.9637,       # 19    Калий
    'Ca': 39.9626,      # 20    Кальций
    'Sc': 44.9559,      # 21    Скандий
    'Ti': 47.9479,      # 22    Титан
    'V': 50.9440,       # 23    Ванадий
    'Cr': 51.9405,      # 24    Хром
    'Mn': 54.9380,      # 25    Марганец
    'Fe': 55.9349,      # 26    Железо
    'Co': 58.9332,      # 27    Кобальт
    'Ni': 57.9353,      # 28    Никель
    'Cu': 62.9296,      # 29    Медь
    'Zn': 63.9291,      # 30    Цинк
    'Ga': 68.9256,      # 31    Галлий
    'Ge': 73.9212,      # 32    Германий
    'As': 74.9216,      # 33    Мышьяк
    'Se': 79.9165,      # 34    Селен
    'Br': 78.9183,      # 35    Бром
    'Kr': 83.9115,      # 36    Криптон
    'Rb': 84.9118,      # 37    Рубидий
    'Sr': 87.9056,      # 38    Стронций
    'Y': 88.9058,       # 39    Иттрий
    'Zr': 89.9047,      # 40    Цирконий
    'Nb': 92.9064,      # 41    Ниобий
    'Mo': 97.9054,      # 42    Молибден
    'Tc': 84.9489,      # 43    Технеций
    'Ru': 101.9043,     # 44    Рутений
    'Rh': 102.9055,     # 45    Родий
    'Pd': 105.9035,     # 46    Палладий
    'Ag': 106.9051,     # 47    Серебро
    'Cd': 113.9034,     # 48    Кадмий
    'In': 114.9039,     # 49    Индий
    'Sn': 119.9022,     # 50    Олово
    'Sb': 120.9038,     # 51    Сурьма
    'Te': 129.9062,     # 52    Теллур
    'I': 126.9045,      # 53    Йод
    'Xe': 131.9042,     # 54    Ксенон
    'Cs': 132.9054,     # 55    Цезий
    'Ba': 137.9052,     # 56    Барий
    'La': 138.9063,     # 57    Лантан
    'Ce': 139.9054,     # 58    Церий
    'Pr': 140.9077,     # 59    Празеодим
    'Nd': 141.9077,     # 60    Неодим
    'Pm': 127.9483,     # 61    Прометий
    'Sm': 151.9197,     # 62    Самарий
    'Eu': 152.9212,     # 63    Европий
    'Gd': 157.9241,     # 64    Гадолиний
    'Tb': 158.9253,     # 65    Тербий
    'Dy': 163.9292,     # 66    Диспрозий
    'Ho': 164.9303,     # 67    Гольмий
    'Er': 165.9303,     # 68    Эрбий
    'Tm': 168.9342,     # 69    Тулий
    'Yb': 173.9389,     # 70    Иттербий
    'Lu': 174.9408,     # 71    Лютеций
    'Hf': 179.9465,     # 72    Гафний
    'Ta': 180.9480,     # 73    Тантал
    'W': 183.9509,      # 74    Вольфрам
    'Re': 186.9558,     # 75    Рений
    'Os': 191.9615,     # 76    Осмий
    'Ir': 192.9629,     # 77    Иридий
    'Pt': 194.9648,     # 78    Платина
    'Au': 196.9666,     # 79    Золото
    'Hg': 201.9706,     # 80    Ртуть
    'Tl': 204.9744,     # 81    Таллий
    'Pb': 207.9766,     # 82    Свинец
    'Bi': 208.9804,     # 83    Висмут
    'Po': 189.9951,     # 84    Полоний
    'At': 193.0002,     # 85    Астат
    'Rn': 196.0023,     # 86    Радон
    'Fr': 200.0065,     # 87    Франций
    'Ra': 203.0092,     # 88    Радий
    'Ac': 227.0278,     # 89    Актиний
    'Th': 232.0381,     # 90    Торий
    'Pa': 231.0359,     # 91    Протактиний
    'U': 238.0508       # 92    Уран
    }

# atomic_masses = {k:v for k, v in atomic_masses_old.items()}