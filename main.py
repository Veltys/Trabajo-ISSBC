#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Title         : main.py
# Description   : Lanzador del programa
# Author        : Julio Domingo Jiménez Ledesma
# Author        : Rafael Carlos Méndez Rodríguez
# Date          : 15-06-2018
# Version       : 1.0.1
# Usage         : python main.py
# Notes         : ...


DEBUG_REMOTO = False


import sys                                                  # Funcionalidades varias del sistema

if DEBUG_REMOTO:
    import pydevd                                           # Depuración remota

import controlador                                          # Módulo controlador

from PyQt4 import QtGui


def main(argv):
    if DEBUG_REMOTO:
        pydevd.settrace('127.0.0.1')

    aplicacion = QtGui.QApplication(argv)

    ventana = controlador.ventana_principal()

    if DEBUG_REMOTO == True:
        ventana.show()

    else:
        ventana.showMaximized()                             # Mejor maximizada

    sys.exit(aplicacion.exec_())


if __name__ == '__main__':
    main(sys.argv)
