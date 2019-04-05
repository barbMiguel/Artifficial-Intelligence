#####################################
# Autor: Miguel Angel Osorio Sanchez
# Autor: Juan Camilo Cubillos Ayala
# Universidad Icesi - Cali, Colombia
#####################################

#####################################
# Example of creating rules for an Expert System
#####################################
from pyknow import *


ACIDO ="Acido"
ALCALINO = "Alcalino"
BAJA = "Bajo"
NEUTRAL = "Neutro"
ALTA = "Alta"
LIGERAMENTE_ACIDO ="ligeramente acido"
LIGERAMENTE_ALCALINO ="ligeramente alcalino"

class AnalisisDeSuelo(Fact):
    arcilla = Field(float , default=0)
    arena = Field(float, default = 0)
    limo = Field(float, default=0)
    PH = Field(str,default="")
    conductividadElectrica = Field(str, default="")
    pass

class SistemaExperto(KnowledgeEngine):

    # Rule 0
    @Rule(AnalisisDeSuelo(PH=P(lambda x: x >= 7.2)))
    def rule0(self):
        print("\n\n\n")
        print("==> ph: ALCALINO")

    # Rule 1
    @Rule(AND(AnalisisDeSuelo(PH=P(lambda x: x > 6.8)),
               AnalisisDeSuelo(PH=P(lambda x: x < 7.2))))
    def rule1(self):
        print("\n\n\n")
        print("==> ph: LIGERAMENTE ALCALINO")

    # Rule 2
    @Rule(AND(AnalisisDeSuelo(PH=P(lambda x: x <= 6.8)), AnalisisDeSuelo(PH=P(lambda x: x >= 6.2))))
    def rule2(self):
        print("\n\n\n")
        print("==> ph: NEUTRO")

    # Rule 3
    @Rule(AND(AnalisisDeSuelo(PH=P(lambda x: x > 5.6)),
               AnalisisDeSuelo(PH=P(lambda x: x < 6.2))))
    def rule3(self):
        print("\n\n\n")
        print("==> ph: LIGERAMENTE ACIDO")

    # Rule 4
    @Rule(AnalisisDeSuelo(PH=P(lambda x: x < 5.6)))
    def rule4(self):
        print("\n\n\n")
        print("==> ph: ACIDO")

    # Rule 5
    @Rule(AnalisisDeSuelo(conductividadElectrica=P(lambda x: x < 0.8)))
    def rule5(self):
        print("\n\n\n")
        print("==> conductividadElectrica: BAJA")

    # Rule 6
    @Rule(AnalisisDeSuelo(conductividadElectrica=P(lambda x: x >= 0.8)))
    def rule6(self):
        print("\n\n\n")
        print("==> conductividadElectrica: ALTA")

    # Rule 7
    @Rule(AnalisisDeSuelo(PH=P(lambda x: x == ALCALINO)))
    def rule7(self):
        print("\n\n\n")
        print("==> ExtractoSoluble: True")

    # Rule 8
    @Rule(AnalisisDeSuelo(PH=P(lambda x: x == LIGERAMENTE_ALCALINO)))
    def rule8(self):
        print("\n\n\n")
        print("==> ExtractoSoluble: True")

    # Rule 9
    @Rule(AND(AnalisisDeSuelo(arcilla = P(lambda x: x >= 40.0)),
              AnalisisDeSuelo(PH = P(lambda x: x == ALCALINO)),
              AnalisisDeSuelo(conductividadElectrica = P(lambda x: x == ALTA))))
    def rule9(self):
        print("\n\n\n")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos")

    # Rule 10
    @Rule(AND(AnalisisDeSuelo(arena = P(lambda x: x >= 50.0)),
              AnalisisDeSuelo(PH = P(lambda x: x == ALCALINO)),
              AnalisisDeSuelo(conductividadElectrica = P(lambda x: x == ALTA))))
    def rule10(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")

    # Rule 11
    @Rule(AND(AnalisisDeSuelo(limo = P(lambda x: x >= 45.0)),
              AnalisisDeSuelo(PH = P(lambda x: x == ALCALINO)),
              AnalisisDeSuelo(conductividadElectrica = P(lambda x: x == ALTA))))
    def rule11(self):
        print("\n\n\n")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")

    # Rule 12
    @Rule(AND((AnalisisDeSuelo(limo = P(lambda x: x <= 40.0)),
               AnalisisDeSuelo(arena = P(lambda x: x <= 40.0)),
               AnalisisDeSuelo(arcilla = P(lambda x: x  <= 40.0)),
               AnalisisDeSuelo(PH = P(lambda x: x == ALCALINO)),
               AnalisisDeSuelo(conductividadElectrica = P(lambda x: x == ALTA)))))
    def rule12(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")

    # Rule 13
    @Rule(AND(AnalisisDeSuelo(arcilla = P(lambda x: x >= 40.0)),
          AnalisisDeSuelo(PH = P(lambda x: x == ALCALINO)),
          AnalisisDeSuelo(conductividadElectrica = P(lambda x: x == BAJA))))
    def rule13(self):
        print("\n\n\n")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Baja disponibilidad de elementos menores ")

    # Rule 14
    @Rule(AND(AnalisisDeSuelo(arena = P(lambda x: x >= 50.0)),
              AnalisisDeSuelo(PH = P(lambda x: x == ALCALINO)),
              AnalisisDeSuelo(conductividadElectrica = P(lambda x: x == BAJA))))
    def rule14(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")

    # Rule 15
    @Rule(AND(AnalisisDeSuelo(limo = P(lambda x: x >= 45.0)),
          AnalisisDeSuelo(PH = P(lambda x: x == ALCALINO)),
          AnalisisDeSuelo(conductividadElectrica = P(lambda x: x == BAJA))))
    def rule15(self):
        print("\n\n\n")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(5) Baja disponibilidad de elementos menores ")

    # Rule 16
    @Rule(AND(AnalisisDeSuelo(limo = P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(arena = P(lambda x: x<= 40.0)),
              AnalisisDeSuelo(arcilla = P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(PH = P(lambda x: x == ALCALINO)),
              AnalisisDeSuelo(conductividadElectrica = P(lambda x: x == ALTA))))
    def rule16(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        print("     |-(3) Baja disponibilidad de elementos menores ")

    # Rule 17
    @Rule(AND(AnalisisDeSuelo(arcilla = P(lambda x: x >= 40.0)),
              AnalisisDeSuelo(PH = P(lambda x: x== LIGERAMENTE_ALCALINO)),
              AnalisisDeSuelo(conductividadElectrica = P(lambda x: x == ALTA))))
    def rule17(self):
        print("\n\n\n")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Alta saturación de calcio")
        print("     |-(6) Salinidad en el suelo")
        print("     |-(7) Baja disponibilidad de Fosforo (Precipitación)")

    # Rule 18
    @Rule(AND(AnalisisDeSuelo(arena = P(lambda x: x >= 50.0)),
              AnalisisDeSuelo(PH = P(lambda x: x == LIGERAMENTE_ALCALINO)),
              AnalisisDeSuelo(conductividadElectrica = P(lambda x: x == ALTA))))
    def rule18(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")

    # Rule 19
    @Rule(AND(AnalisisDeSuelo(limo = P(lambda x: x >= 45.0)),
              AnalisisDeSuelo(PH = P(lambda x: x == LIGERAMENTE_ALCALINO)),
              AnalisisDeSuelo(conductividadElectrica = P(lambda x: x== ALTA))))
    def rule19(self):
        print("\n\n\n")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")

    # Rule 20
    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x <= 40.0)),
            AnalisisDeSuelo(arena=P(lambda x: x <= 40.0)),
            AnalisisDeSuelo(arcilla=P(lambda x: x <= 40.0)),
            AnalisisDeSuelo(PH=P(lambda x: x == LIGERAMENTE_ALCALINO)),
            AnalisisDeSuelo(conductividadElectrica = P(lambda x: x == ALTA))))
    def rule20(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")

    # Rule 21
    @Rule(AND(AnalisisDeSuelo(arcilla=P(lambda x: x >= 40.0)),
              AnalisisDeSuelo(PH=P(lambda x: x == LIGERAMENTE_ALCALINO)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x == BAJA))))
    def rule21(self):
        print("\n\n\n")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Baja disponibilidad de elementos menores ")

    # Rule 22
    @Rule(AND(AnalisisDeSuelo(arena=P(lambda x: x >= 50.0)),
              AnalisisDeSuelo(PH=P(lambda x: x == LIGERAMENTE_ALCALINO)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x == BAJA))))
    def rule22(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")

    # Rule 23
    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x >= 45.0)),
              AnalisisDeSuelo(PH=P(lambda x: x == LIGERAMENTE_ALCALINO)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x == BAJA))))
    def rule23(self):
        print("\n\n\n")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(5) Baja disponibilidad de elementos menores ")

    # Rule 24
    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(PH=P(lambda x: x == LIGERAMENTE_ALCALINO)),
              AnalisisDeSuelo(arena=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(arcilla=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x == ALTA))))
    def rule24(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        print("     |-(3) Baja disponibilidad de elementos menores")


    # Rule 25
    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(arcilla=P(lambda x: x >= 40.0)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x == ALTA))))
    def rule25(self):
        print("\n\n\n")
        print("     |-(1) Baja mineralizacion de MO (Baja actvidad microbiologica)	")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Salinidad en el suelo")


    # Rule 26
    @Rule(AND(AnalisisDeSuelo(PH=P(lambda x: x == NEUTRAL)),
              AnalisisDeSuelo(arena=P(lambda x: x >= 50.0)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x == ALTA))))
    def rule26(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        print("     |-(3) Baja disponibilidad de elementos menores")

    # Rule 27
    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x >= 45.0)),
              AnalisisDeSuelo(PH=P(lambda x: x == NEUTRAL)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x == ALTA))))
    def rule27(self):
        print("\n\n\n")
        print("     |-(1) Salinidad en el suelo")


    # Rule 28
    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(PH=P(lambda x: x == NEUTRAL)),
              AnalisisDeSuelo(arena=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(arcilla=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x == ALTA))))
    def rule28(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        print("     |-(3) Baja disponibilidad de elementos menores")

    # Rule 29
    @Rule(AND(AnalisisDeSuelo(arcilla=P(lambda x: x >= 40.0)),
              AnalisisDeSuelo(PH=P(lambda x: x == NEUTRAL)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x == BAJA))))
    def rule29(self):
        print("\n\n\n")
        print("     |-(1) Baja mineralizacion de MO (Baja actvidad microbiologica) ")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Limitaciones de movimiento de agua")

    # Rule 30
    @Rule(AND(AnalisisDeSuelo(PH=P(lambda x: x == NEUTRAL)),
              AnalisisDeSuelo(arena=P(lambda x: x >= 50.0)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x == BAJA))))
    def rule30(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")

    # Rule 31
    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x >= 45.0)),
              AnalisisDeSuelo(PH=P(lambda x: x == NEUTRAL)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x == BAJA))))
    def rule31(self):
        print("\n\n\n")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")

    # Rule 32
    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(PH=P(lambda x: x == NEUTRAL)),
              AnalisisDeSuelo(arena=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(arcilla=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x == ALTA))))
    def rule32(self):
        print("\n\n\n")

    # Rule 33
    @Rule(AND(AnalisisDeSuelo(PH=P(lambda x: x == LIGERAMENTE_ACIDO)),
              AnalisisDeSuelo(arcilla=P(lambda x: x >= 40.0)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x == ALTA))))
    def rule33(self):
        print("\n\n\n")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos")
        print("     |-(5) Alta saturación de calcio")
        print("     |-(6) Salinidad en el suelo")
        print("     |-(7) Baja disponibilidad de Fosforo (Precipitación)")

    # Rule 34
    @Rule(AND(AnalisisDeSuelo(PH=P(lambda x: x == LIGERAMENTE_ACIDO)),
              AnalisisDeSuelo(arena=P(lambda x: x >= 50.0)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x == ALTA))))
    def rule34(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")

    # Rule 35
    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x >= 45.0)),
              AnalisisDeSuelo(ph=P(lambda x: x < 6.2)),
              AnalisisDeSuelo(ph=P(lambda x: x > 5.6)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x >= 0.8))))
    def rule35(self):
        print("\n\n\n")
        print("     |-(1) Contenido de Aluminio")
        print("     |-(2) Sulfatos altos")
        print("     |-(3) Impedancia")

    # Rule 36
    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(arena=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(arcilla=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(ph=P(lambda x: x < 6.2)),
              AnalisisDeSuelo(ph=P(lambda x: x > 5.6)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x >= 0.8))))
    def rule36(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")

    # Rule 37
    @Rule(AND(AnalisisDeSuelo(arcilla=P(lambda x: x >= 40.0)),
              AnalisisDeSuelo(ph=P(lambda x: x < 6.2)),
              AnalisisDeSuelo(ph=P(lambda x: x > 5.6)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x < 0.8))))
    def rule37(self):
        print("\n\n\n")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Baja disponibilidad de elementos menores ")

    # Rule 38
    @Rule(AND(AnalisisDeSuelo(arena=P(lambda x: x >= 50.0)),
              AnalisisDeSuelo(ph=P(lambda x: x < 6.2)),
              AnalisisDeSuelo(ph=P(lambda x: x > 5.6)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x < 0.8))))
    def rule38(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")

    # Rule 39
    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x >= 45.0)),
              AnalisisDeSuelo(ph=P(lambda x: x < 6.2)),
              AnalisisDeSuelo(ph=P(lambda x: x > 5.6)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x < 0.8))))
    def rule39(self):
        print("\n\n\n")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(5) Baja disponibilidad de elementos menores ")

    # Rule 40
    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(arena=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(arcilla=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(ph=P(lambda x: x < 6.2)),
              AnalisisDeSuelo(ph=P(lambda x: x > 5.6)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x < 0.8))))
    def rule40(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        print("     |-(3) Baja disponibilidad de elementos menores ")

    # Rule 41
    @Rule(AND(AnalisisDeSuelo(arcilla=P(lambda x: x >= 40.0)),
              AnalisisDeSuelo(ph=P(lambda x: x <= 5.6)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x >= 0.8))))
    def rule41(self):
        print("\n\n\n")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Acumulacion de iones alcalinoterreos	")
        print("     |-(4) Salinidad en el suelo")
        print("     |-(5) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(6) Baja disponibilidad de Calcio")
        print("     |-(7) Contenido de Aluminio")

    # Rule 42
    @Rule(AND(AnalisisDeSuelo(arena=P(lambda x: x >= 50.0)),
              AnalisisDeSuelo(ph=P(lambda x: x <= 5.6)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x >= 0.8))))
    def rule42(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")

    # Rule 43
    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x >= 45.0)),
              AnalisisDeSuelo(ph=P(lambda x: x <= 5.6)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x >= 0.8))))
    def rule43(self):
        print("\n\n\n")
        print("     |-(1) Contenido de Aluminio")
        print("     |-(2) Sulfatos altos")
        print("     |-(3) Impedancia")

    # Rule 44
    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(arena=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(arcilla=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(ph=P(lambda x: x <= 5.6)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x >= 0.8))))
    def rule44(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")

        # Rule 45

    @Rule(AND(AnalisisDeSuelo(arcilla=P(lambda x: x >= 40.0)),
              AnalisisDeSuelo(ph=P(lambda x: x <= 5.6)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x < 0.8))))
    def rule45(self):
        print("\n\n\n")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica)")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Baja disponibilidad de elementos menores ")

    # Rule 46
    @Rule(AND(AnalisisDeSuelo(arena=P(lambda x: x >= 50.0)),
              AnalisisDeSuelo(ph=P(lambda x: x <= 5.6)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x < 0.8))))
    def rule46(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")

    # Rule 47
    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x >= 45.0)),
              AnalisisDeSuelo(ph=P(lambda x: x <= 5.6)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x < 0.8))))
    def rule47(self):
        print("\n\n\n")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(5) Baja disponibilidad de elementos menores ")

    # Rule 48
    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(arena=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(arcilla=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(ph=P(lambda x: x <= 5.6)),
              AnalisisDeSuelo(conductividadElectrica=P(lambda x: x < 0.8))))
    def rule48(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        print("     |-(3) Baja disponibilidad de elementos menores ")

