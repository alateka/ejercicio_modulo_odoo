# -*- coding: utf-8 -*-

from datetime import datetime
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api


class Chofer(models.Model):
    _name = "apf_sge.chofer"
    _description = "Modelo encargado de la gestion de los chofers"
    _order = "nombre"

    # Relacion uno a muchos entre la tabla chofer y camion
    chofer_ids = fields.One2many("apf_sge.camion", "camion_id", String = "Chofer")

    nombre = fields.Char(string = "Nombre del chofer", required = True)
    dni = fields.Char(string = "Documento DNI", required = True)
    apellidos = fields.Char(string = "Apellidos")
    fechaNacimiento = fields.Date(string = "Fecha de nacimiento")
    documentosCMR = fields.Char(string = "CMRs o Cartas de porte")
    edad = fields.Integer(string = "Edad del chofer", compute = "_get_edad")

    # A partir de la fecha de nacimiento del chofer, añadirá su edad actual.
    @api.depends('fechaNacimiento')
    def _get_edad(self):
        for chofer in self:
            edad = relativedelta(datetime.now(), chofer.fechaNacimiento)
            chofer.edad = edad.years
            



class Camion(models.Model):
    _name = "apf_sge.camion"
    _description = "Modelo encargado de la gestion de la flota de camiones"
    _order = "marca"

    modelo = fields.Char(string = "Modelo del camión", required = True)
    marca = fields.Char(string = "Marca", required = True)
    matricula = fields.Char(string = "Matrícula", required = True)
    tipoTrailer = fields.Char(string = "Tipo de Trailer")

    # Relacion muchos a uno entre la tabla camion y chofer 
    camion_id = fields.Many2one("apf_sge.chofer", String = "Vehículo de mercancias")

    # Relacion muchos a muchos entre la tabla camion y destino 
    destino_ids = fields.Many2many("apf_sge.destino", String = "Destinos de Ruta")



class Destino(models.Model):
    _name = "apf_sge.destino"
    _description = "Modelo encargado de la gestion de los viajes"
    _order = "pais"

    cp = fields.Char(string = "Código postal", required = True)
    pais = fields.Char(string = "Pais")
    direccion = fields.Char(string = "Dirección", required = True)
    provincia = fields.Char(string = "Provincia")

    # Relacion muchos a muchos entre la tabla camion y destino 
    camion_ids = fields.Many2many("apf_sge.camion", String = "Vehículos de mercancias")
