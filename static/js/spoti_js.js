window.onload = () => {
    // Llamada para obtener el access token desde el backend
    fetch('/home/get-token/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Error en la respuesta del servidor al obtener el access token');
            }
            return response.json();
        })
        .then(data => {
            if (data.access_token) {
                console.log('Access token recibido:', data.access_token);
                // Guardar el token en localStorage
                localStorage.setItem('access_token', data.access_token);

                // Inicializar el reproductor de Spotify
                initializeSpotifyPlayer(data.access_token);
            } else {
                console.error('Access token no disponible en la respuesta');
            }
        })
        .catch(error => {
            console.error('Error al obtener el access token:', error);
        });
};

// Función para inicializar el reproductor de Spotify
function initializeSpotifyPlayer(token) {
    const player = new Spotify.Player({
        name: 'Web Playback SDK Player',
        getOAuthToken: cb => { cb(token); },
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

    // Event listeners para los botones
    document.getElementById('prevTrack').addEventListener('click', () => {
        player.previousTrack().then(() => {
            console.log('Pista anterior reproducida');
        });
    });

    document.getElementById('togglePlay').addEventListener('click', () => {
        player.togglePlay().then(() => {
            console.log('Reproducción pausada/reanudada');
        });
    });

    document.getElementById('nextTrack').addEventListener('click', () => {
        player.nextTrack().then(() => {
            console.log('Siguiente pista reproducida');
        });
    });

    // Actualizar el nombre de la pista actual
    player.addListener('player_state_changed', state => {
        if (state) {
            const trackName = state.track_window.current_track.name;
            document.getElementById('trackName').textContent = trackName;
        }
    });
}
