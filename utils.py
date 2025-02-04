import numpy as np

def aggiungi_velocita(gdf):
    """
    Aggiunge una colonna 'velocita' (in m/s) a un GeoDataFrame.
    La velocità viene calcolata considerando le distanze 3D e i tempi.
    
    Parametri:
        gdf (GeoDataFrame): Un GeoDataFrame con colonne 'geometry', 'altitudine', e 'unixtime'.
        
    Ritorna:
        GeoDataFrame: Il GeoDataFrame con la nuova colonna 'velocita'.
    """
    # Calcolo della distanza orizzontale in metri
    gdf['distanza_orizzontale'] = gdf.geometry.distance(gdf.geometry.shift())
    
    # Calcolo della variazione di altitudine (dislivello)
    gdf['delta_altitudine'] = gdf['altitudine'].diff()
    
    # Calcolo della distanza totale 3D usando il teorema di Pitagora
    gdf['distanza_totale'] = np.sqrt(
        gdf['distanza_orizzontale']**2 + gdf['delta_altitudine']**2
    )
    
    # Calcolo del delta tempo in secondi
    gdf['delta_tempo'] = gdf['unixtime'].diff()
    
    # Calcolo della velocità (m/s)
    gdf['velocita'] = gdf['distanza_totale'] / gdf['delta_tempo']
    
    # Riempimento valori NaN con 0 (es. per la prima riga)
    gdf['velocita'] = gdf['velocita'].fillna(0)
    
    # Rimozione delle colonne intermedie opzionale (se non servono)
    gdf.drop(columns=['distanza_orizzontale', 'delta_altitudine', 'distanza_totale', 'delta_tempo'], inplace=True)
    
    return gdf
