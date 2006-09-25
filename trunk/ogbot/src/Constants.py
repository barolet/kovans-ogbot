#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
#
#      Kovan's OGBot
#      Copyright (c) 2006 by kovan 
#
#      *************************************************************************
#      *                                                                       *
#      * This program is free software; you can redistribute it and/or modify  *
#      * it under the terms of the GNU General Public License as published by  *
#      * the Free Software Foundation; either version 2 of the License, or     *
#      * (at your option) any later version.                                   *
#      *                                                                       *
#      *************************************************************************
#
from GameEntities import Ship, Defense, Building, Research

FILE_PATHS = {
    'config' : 'config/config.ini', 
    'botstate' :  'botdata/bot.state.dat', 
    'webstate' : 'botdata/webadapter.state.dat', 
    'planetdb' :  'botdata/planets.db', 
    'planets' : 'botdata/simulations.dat', 
    'log' : 'log/ogbot.log', 
}

INGAME_TYPES = [
    Ship('smallCargo', _('Nave peque�a de carga'), 'ship202', 5000, 20), 
    Ship('largeCargo', _('Nave grande de carga'), 'ship203', 25000, 50), 
    Ship('lightFighter', _('Cazador ligero'), 'ship204', 50, 20), 
    Ship('heavyFighter', _('Cazador pesado'), 'ship205', 100, 75), 
    Ship('cruiser', _('Crucero'), 'ship206', 800, 300), 
    Ship('battleShip', _('Nave de batalla'), 'ship207', 1500, 500), 
    Ship('colonyShip', _('Colonizador'), 'ship208', 7500, 1000), 
    Ship('recycler', _('Reciclador'), 'ship209', 20000, 300), 
    Ship('espionageProbe', _('Sonda de espionaje'), 'ship210', 5, 1), 
    Ship('bomber', _('Bombardero'), 'ship211', 500, 1000), 
    Ship('solarSatellite', _('Sat�lite solar'), 'ship212', 0, 0), 
    Ship('destroyer', _('Destructor'), 'ship213', 2000, 1000), 
    Ship('deathStar', _('Estrella de la muerte'), 'ship214', 1000000, 1), 
    
    Building('metalMine', _("Mina de metal"), 1), 
    Building('crystalMine', _("Mina de cristal"), 2), 
    Building('deuteriumSynthesizer', _("Sintetizador de deuterio"), 3), 
    Building('solarPlant', _("Planta de energ�a solar"), 4), 
    Building('fusionReactor', _("Planta de fusi�n"), 12), 
    Building('roboticsFactory', _("F�brica de Robots"), 14), 
    Building('naniteFactory', _("F�brica de Nanobots"), 15), 
    Building('shipyard', _("Hangar"), 21), 
    Building('metalStorage', _("Almac�n de metal"), 22), 
    Building('crystalStorage', _("Almac�n de cristal"), 23), 
    Building('deuteriumTank', _("Contenedor de deuterio"), 24), 
    Building('researchLab', _("Laboratorio de investigaci�n"), 31), 
    Building('terraformer', _("Terraformer"), 33), 
    Building('allianceDepot', _("Dep�sito de la Alianza"), 34), 
    Building('lunarBase', _("Base lunar"), 41), 
    Building('sensorPhalanx', _("Sensor Phalanx"), 42), 
    Building('jumpGate', _("Salto cu�ntico"), 43), 
    Building('missileSilo', _("Silo"), 44), 
    
    Defense('rocketLauncher', _('Lanzamisiles'), 401), 
    Defense('lightLaser', _('L�ser peque�o'), 402), 
    Defense('heavyLaser', _('L�ser grande'), 403), 
    Defense('gaussCannon', _('Ca��n Gauss'), 404), 
    Defense('ionCannon', _('Ca��n i�nico'), 405), 
    Defense('plasmaTurret', _('Ca��n de plasma'), 406), 
    Defense('smallShieldDome', _('C�pula peque�a de protecci�n'), 407), 
    Defense('largeShieldDome', _('C�pula grande de protecci�n'), 408), 
    Defense('antiBallisticMissile', _('Misil de intercepci�n'), 502), 
    Defense('interplanetaryMissile', _('Misil interplanetario'), 503), 
    
    Research('espionageTechnology', _('Tecnolog�a de espionaje'), 106), 
    Research('computerTechnology', _('Tecnolog�a de computaci�n'), 108), 
    Research('weaponsTechnology', _('Tecnolog�a militar'), 109), 
    Research('shieldingTechnology', _('Tecnolog�a de defensa'), 110), 
    Research('armourTechnology', _('Tecnolog�a de blindaje'), 111), 
    Research('energyTechnology', _('Tecnolog�a de energ�a'), 113), 
    Research('hyperspaceTechnology', _('Tecnolog�a de hiperespacio'), 114), 
    Research('combustionDrive', _('Motor de combusti�n'), 115), 
    Research('impulseDrive', _('Motor de impulso'), 117), 
    Research('hyperspaceDrive', _('Propulsor hiperespacial'), 118), 
    Research('laserTechnology', _('Tecnolog�a l�ser'), 120), 
    Research('ionTechnology', _('Tecnolog�a i�nica'), 121), 
    Research('plasmaTechnology', _('Tecnolog�a de plasma'), 122), 
    Research('intergalacticResearchNetwork', _('Red de investigaci�n intergal�ctica'), 123), 
    Research('gravitonTechnology', _('Tecnolog�a de gravit�n'), 199), 
]

INGAME_TYPES_BY_NAME = dict([ (type.name, type) for type in INGAME_TYPES  ])
INGAME_TYPES_BY_CODE = dict([ (type.code, type) for type in INGAME_TYPES  ])
INGAME_TYPES_BY_FULLNAME = dict([ (type.fullName, type) for type in INGAME_TYPES  ])


