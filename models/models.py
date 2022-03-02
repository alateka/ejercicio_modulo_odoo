# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Chofer(models.Model):
    _name = "apf_sge.chofer"
    _description = "Modelo encargado de la gestion de los chofers"
    _order = "nombre"

    # Relacion uno a muchos entre la tabla chofer y camion
    chofer_ids = fields.One2many("apf_sge.camion", "camion_id", String = "Chofer")

    nombre = fields.Char(String = "Nombre del chofer", required = True)
    dni = fields.Char(String = "Documento DNI", required = True)
    apellidos = fields.Char(String = "Apellidos")
    fechaNacimiento = fields.Date(String = "Edad")
    documentosCMR = fields.Char(String = "CMRs o Cartas de porte")



# TODO usar esto para calcular la edad a partir de la fecha de nacimiento del chofer
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class Camion(models.Model):
    _name = "apf_sge.camion"
    _description = "Modelo encargado de la gestion de la flota de camiones"
    _order = "marca"

    modelo = fields.Char(String = "Modelo del camión", required = True)
    marca = fields.Char(String = "Marca", required = True)
    matricula = fields.Char(String = "Matrícula")
    tipoTrailer = fields.Char(String = "Tipo de Trailer")

    # Relacion muchos a uno entre la tabla camion y chofer 
    camion_id = fields.Many2one("apf_sge.chofer", String = "Vehículo de mercancias")

    # Relacion muchos a muchos entre la tabla camion y destino 
    destino_ids = fields.Many2many("apf_sge.destino", String = "Destinos de Ruta")



class Destino(models.Model):
    _name = "apf_sge.destino"
    _description = "Modelo encargado de la gestion de los viajes"
    _order = "name"

    cp = fields.Char(String = "Código postal", required = True)
    pais = fields.Char(String = "Pais", required = True)
    direccion = fields.Char(String = "Dirección")
    provincia = fields.Char(String = "Provincia")

    # Relacion
    camion_ids = fields.Many2many("apf_sge.camion", String = "Vehículos de mercancias")
