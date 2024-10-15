// Función que se ejecuta cuando el SDK de Spotify está listo
window.onSpotifyWebPlaybackSDKReady = () => {
    // Recuperar el token almacenado
    const token = localStorage.getItem('access_token') || ''; // Asegúrate de que 'access_token' coincida con la clave utilizada para almacenarlo

    // Inicializar el reproductor
    const player = new Spotify.Player({
        name: 'Web Playback SDK Quick Start Player',
        getOAuthToken: cb => { cb(token); }, // Proporcionar el token cuando se necesite
        volume: 0.5
    });

    // Conectar el reproductor
    player.connect().then(success => {
        if (success) {
            console.log('Conectado al reproductor de Spotify');
        }
    }).catch(error => {
        console.error('Error al conectar con el reproductor:', error);
    });
};


