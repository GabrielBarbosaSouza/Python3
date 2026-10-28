class Aluno:
    def __init__(
        self,
        nome: str,
        curso: str,
        serie: str
    ):
        self.nome = nome
        self.curso = curso
        self.serie = serie


class Usuario:
    def __init__(
        self,
        nome: str,
        email: str
    ):
        self.nome = nome
        self.email = email


class JSON:
    def exportar(self, dados: list):
        from json import dumps
        
        print(f"Exportando JSON dos dados enviados...")
        
        lista = [vars(item) for item in dados]
        return f"{dumps(lista, ensure_ascii=False, indent=4)}\n"


class XML:
    def exportar(self, dados: list):
        import xml.etree.ElementTree as ET
        
        print(f"Exportando XML dos dados enviados...")
        
        raiz = ET.Element("dados")

        for item in dados:
            tag_item = ET.SubElement(raiz, type(item).__name__.lower())
            for atributo, valor in vars(item).items():
                campo = ET.SubElement(tag_item, atributo)
                campo.text = str(valor)

        ET.indent(raiz, space="    ")
        
        return f"{ET.tostring(raiz, encoding='unicode', xml_declaration=True)}\n"

def exportar_dados(objeto, dados: list):
    print(objeto.exportar(dados))