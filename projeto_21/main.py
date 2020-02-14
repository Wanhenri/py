import requests
from xml.etree import ElementTree
import json

class prevInpe:
    def get_prevInpe(self,codigo):
        response_forecast = requests.get(
            'http://servicos.cptec.inpe.br/XML/cidade/7dias/' + str(codigo) + '/previsao.xml')
            

        prevCapitais = ElementTree.fromstring(response_forecast.content)
        content = []
        for tag in prevCapitais.findall("previsao"):
            metar = {}
            metar["dia"] = tag.find("dia").text
            metar["tempo"] = tag.find("tempo").text
            metar["maxima"] = tag.find("maxima").text
            metar["minima"] = tag.find("minima").text
            content.append(metar)
        return content     


inpe_reports = prevInpe()
codigo = 244
a = inpe_reports.get_prevInpe(codigo)
print(a)
