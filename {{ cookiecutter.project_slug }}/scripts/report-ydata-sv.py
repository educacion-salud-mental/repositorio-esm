!pip install ydata-profiling
!pip install sweetviz


import pandas as pd
from ydata_profiling import ProfileReport
import sweetviz as sv
import os

ruta_input = [os.path.join('..', 'Data', 'interim', 'Adolescentes.csv'), os.path.join('..', 'Data', 'interim', 'Adultos.csv'), os.path.join('..', 'Data', 'processed', 'Ensanut-data-p.csv')]

ruta_output_y = [os.path.join('..', 'docs', 'docs', 'interim_salud_mental_adol.html'),os.path.join('..', 'docs', 'docs', 'interim_salud_mental_adul.html'),os.path.join('..', 'docs', 'docs', 'interim_salud_mental_adol_adul.html')]

ruta_output_sv = [os.path.join('..', 'docs', 'docs','interim_ensa_adol_sweetviz_report.html'), os.path.join('..', 'docs', 'docs','interim_ensa_adul_sweetviz_report.html'),os.path.join('..', 'docs', 'docs','interim_ensa_adol_adul_sweetviz_report.html')]

title = ["ENSANUT ADOLESCENTES YData Profiling Report","ENSANUT ADULTOS YData Profiling Report","ENSANUT ADOLESCENTES-ADULTOS YData Profiling Report"]
#Ydata

for i in range(3):
    df = pd.read_csv(ruta_input[i], low_memory=False) 
    profile_ensa_ydata = ProfileReport(df, title=title[i], explorative=True, minimal = True)
    profile_ensa_ydata.to_file(ruta_output[i])
    print(f"YData report para ENSANUT guardado en {ruta_output[i]}")
    profile_enco_sweetviz = sv.analyze(df)
    profile_enco_sweetviz.show_html(ruta_output_sv[i])
    print(f"Sweetviz report para ENSANUT guardado en {ruta_output_sv[i]}")
