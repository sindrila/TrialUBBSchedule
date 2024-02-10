from Domain.Professor import Professor
from Parsers.CadreDidacticeParser import CadreDidacticeParser

if __name__ == "__main__":
    test = CadreDidacticeParser('https://www.cs.ubbcluj.ro/files/orar/2023-1/cadre/index.html')
    print(test.get_tuple_text_website())
    # print(len(test))

