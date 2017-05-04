#!/usr/bin/env python
# -*- coding: utf-8 -*-

excelOriginal = '../data/imd_student_blind.xlsx'
csvOriginal = '../data/imd-student-blind.csv'
csvWithNames = '../data/imd-student-blind-1.1.csv'

# Import pandas
import pandas as pd
#Import numpy
import numpy as np

imdBlindTestDf = pd.read_csv(csvOriginal)
imdBlindTestDf["full-name"] = ""
disciNames = ["INTRODUÇÃO ÀS TÉCNICAS DE PROGRAMAÇÃO",
    "PRÁTICAS DE LEITURA E ESCRITA EM PORTUGUÊS I",
    "RESOLUÇÃO DE PROBLEMAS MATEMÁTICOS PARA TI",
    "CÁLCULO DIFERENCIAL E INTEGRAL I",
    "PRÁTICAS DE LEITURA E ESCRITA EM PORTUGUÊS II",
    "FUNDAMENTOS MATEMÁTICOS DA COMPUTAÇÃO I",
    "VETORES E GEOMETRIA ANALÍTICA"]

for i in range(0, 6):
    discId = i
    disciName = disciNames[i]
    for label, row in imdBlindTestDf.iterrows():
        if(row['disciplina_ID'] == discId):
            imdBlindTestDf.set_value(label, 'full-name', disciName)
print(imdBlindTestDf.head())
imdBlindTestDf.to_csv(csvWithNames)
