// Suponiendo que tienes una función para manejar la respuesta del backend
function handleCallbackResponse(response) {
    if (response.access_token) {
        localStorage.setItem('access_token', response.access_token);
        
        // Inicializar el SDK de reproducción de Spotify
        window.onSpotifyWebPlaybackSDKReady = () => {
            const token = localStorage.getItem('access_token') || '';

            const player = new Spotify.Player({
                name: 'Web Playback SDK Quick Start Player',
                getOAuthToken: cb => { cb(token); },
                volume: 0.5
            });

            player.connect().then(success => {
                if (success) {
                    console.log('Conectado al reproductor de Spotify');
                }
            }).catch(error => {
                console.error('Error al conectar con el reproductor:', error);
            });
        };
    } else {
        console.error('No se obtuvo access token');
    }
}

// Suponiendo que haces una llamada AJAX para obtener el token
fetch('/your-callback-endpoint')
    .then(response => response.json())
    .then(handleCallbackResponse)
    .catch(error => console.error('Error en la llamada al callback:', error));
