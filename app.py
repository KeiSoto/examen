# -*- coding: utf-8 -*-
import web
import json

render = web.template.render("views/")

urls = (
    "/index(.*)", "index"
)

class index:
    data_list = []
    entidad = []
    numeroHombres = {}
    numeroMujeres = {}
    def GET(self, values):
        values = []
        with open('datos.json', 'r') as file:
            self.data_list = json.load(file)
        self.obtenerEntidades()
        values.append(self.numeroHombres)
        values.append(self.numeroMujeres)
        return render.index(values)
    
    def obtenerEntidades(self):
        for row in self.data_list['results']:
            if len(self.entidad) == 0:
                self.entidad.append(row['ENTIDAD'])
            else:
                if row['ENTIDAD'] in self.entidad:
                    continue
                else:
                    self.entidad.append(row['ENTIDAD'])
        
        for entidad in self.entidad:
            self.hombresPorEntidad(entidad)
            self.mujeresPorEntidad(entidad)
            
    def hombresPorEntidad(self,entidad): 
        contH = 0
        for row in self.data_list['results']:
            if row['ENTIDAD']== entidad:
                contH += row['HOMBRES']
        self.numeroHombres[entidad] = [contH]
            
    def mujeresPorEntidad(self,entidad):
        contM = 0
        for row in self.data_list['results']:
            if row['ENTIDAD'] == entidad:
                contM += row['MUJERES']
        self.numeroMujeres[entidad] = [contM]
            
if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = True
    app.run()
