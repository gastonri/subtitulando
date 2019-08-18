import os, sys

if sys.argv[1] == 'help':
    print('El script recibe 4 parámetros.\nEl primero es la ruta absoluta donde se encuentran los videos y subtitulos.\nEl segundo parámetro es el formato en el que se encuentra el video.\nEl tercer parámetro nomenclatura de temporada. Por ejemplo: "S01, 01 o Temporada1.".\nEl cuarto parametro es la nomenclatura por la que se define el episodio. Por ejemplo: Si el archivo fuese S01E09 el parámetro sería la letra E que designa el capitulo.\nEl último parámetro es igual que el anterior pero para los subtítulos. Esto permite mappear correctamente los nombres de videos y archivos.')
    
carpetaContenedora = sys.argv[1]
carpetaContenedora = r + carpetaContenedora
formatoVideo = sys.argv[2]
nomenclaturaTemporada = sys.argv[3]
capituloVideo = sys.argv[4]
capituloSubtitulo = sys.argv[5]

videos = []
subtitulos = []

def sanitizarParametros():
    if carpetaContenedora[-1:] != '\\':
        carpetaContenedora = carpetaContenedora + '\\'
    if formatoVideo[:1] != '.':
        formatoVideo = '.' + formatoVideo

def separarArchivos(carpetaContenedora):    
    for archivoVideo in os.listdir(carpetaContenedora):
        if archivoVideo.find('.srt') is not -1:
            subtitulos.append(archivoVideo)            
        if archivoVideo.find(formatoVideo)  is not -1:
            videos.append(archivoVideo)
        
def extraerCapitulo(nomenclaturaTemporada):
    formato = nomenclaturaTemporada
    for video in videos:        
        inicioNomenclaturaTemporada = video.find(nomenclaturaTemporada) + 3
        finNomenclaturaTemporada = inicioNomenclaturaTemporada + len(nomenclaturaTemporada)
        nomenclaturaEpisodio = video[inicioNomenclaturaTemporada:finNomenclaturaTemporada]
        cambiarNombre(video, nomenclaturaEpisodio)
        
def cambiarNombre(video, episodio):
    episodio = episodio.replace(capituloVideo, capituloSubtitulo)
    for subtitulo in subtitulos:
        if subtitulo.find(episodio) is not -1:
            video = video[:-4]
            os.rename(carpetaContenedora + subtitulo, carpetaContenedora + video + '.srt')

sanitizarParametros()
separarArchivos(carpetaContenedora)
extraerCapitulo(nomenclaturaTemporada)
