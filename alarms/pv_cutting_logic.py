# alarms/pv_cutting_logic.py
import pandas as pd

def detect_ecretage(data: pd.DataFrame, seuil_ecretage_kw=10):
    df = data.copy()
    df['Ecretage_PV'] = (df['PV_theorique'] - df['PV_reel']) > seuil_ecretage_kw
    df['Type_Ecretage'] = None

    for i in df.index:
        if df.loc[i, 'Ecretage_PV']:
            besoin = df.loc[i, 'Load'] - (df.loc[i, 'PV_reel'] + df.loc[i, 'Genset'])
            if df.loc[i, 'Load'] < df.loc[i, 'PV_theorique'] * 0.9:
                df.at[i, 'Type_Ecretage'] = 'Client'
            elif df.loc[i, 'Genset'] > 10 and besoin > seuil_ecretage_kw:
                df.at[i, 'Type_Ecretage'] = 'GE'
    return df